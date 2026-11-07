

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.record_model import RecordModel
from ..types.record_property_link_model import RecordPropertyLinkModel
from ..types.records_create_attachment_response import RecordsCreateAttachmentResponse
from ..types.records_delete_record_response import RecordsDeleteRecordResponse
from ..types.records_get_attachment_response import RecordsGetAttachmentResponse
from ..types.records_get_predictions_response import RecordsGetPredictionsResponse
from ..types.records_get_schema_response import RecordsGetSchemaResponse
from ..types.records_get_xlsx_export_file_response import RecordsGetXlsxExportFileResponse
from ..types.records_list_all_response import RecordsListAllResponse
from ..types.records_upload_smart_import_record_response import RecordsUploadSmartImportRecordResponse
from ..types.records_upload_smart_import_record_with_predictions_response import (
    RecordsUploadSmartImportRecordWithPredictionsResponse,
)
from .raw_client import AsyncRawRecordsClient, RawRecordsClient
from .types.records_create_attachment_request_metadata import RecordsCreateAttachmentRequestMetadata
from .types.records_create_record_request_parent import RecordsCreateRecordRequestParent
from .types.records_create_record_request_properties import RecordsCreateRecordRequestProperties
from .types.records_list_all_request_sort_direction import RecordsListAllRequestSortDirection
from .types.records_list_all_request_sort_field import RecordsListAllRequestSortField
from .types.records_replace_metadata_request_parent import RecordsReplaceMetadataRequestParent
from .types.records_replace_metadata_request_properties import RecordsReplaceMetadataRequestProperties
from .types.records_update_metadata_request_add_properties import RecordsUpdateMetadataRequestAddProperties
from .types.records_update_metadata_request_set_parent import RecordsUpdateMetadataRequestSetParent


OMIT = typing.cast(typing.Any, ...)


class RecordsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRecordsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRecordsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRecordsClient
        """
        return self._raw_client

    def listall(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        types: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        sort_field: typing.Optional[RecordsListAllRequestSortField] = None,
        sort_direction: typing.Optional[RecordsListAllRequestSortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordsListAllResponse:
        """
        View all records in the company, with filtering available via query parameters

        Parameters
        ----------
        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        types : typing.Optional[str]
            Comma separated (no spaces) record types to export. Use the [Retrieve Records Schema](https://developer.ironcladapp.com/reference/list-all-records-metadata) endpoint to retrieve a list of types.

        last_updated : typing.Optional[str]
            Get records updated since (UTC)

        filter : typing.Optional[str]
            Filter records for those that contain (1) the specified property with (2) the specified value. The record property ID should be enclosed in brackets `[ ]` and the value should be enclosed in single quotes `' '`.

        sort_field : typing.Optional[RecordsListAllRequestSortField]
            The field to sort Records. Only one field is supported in the sort operation.

        sort_direction : typing.Optional[RecordsListAllRequestSortDirection]
            The direction the records are sorted by in correlation with the `sortField`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsListAllResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.listall(
            types="mutualNDA,consultingAgreement",
            last_updated="2018-03-10T00:00:00.000Z",
            filter="Equals([counterpartyName], 'Test LLC')",
        )
        """
        _response = self._raw_client.listall(
            page=page,
            page_size=page_size,
            types=types,
            last_updated=last_updated,
            filter=filter,
            sort_field=sort_field,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    def createrecord(
        self,
        *,
        type: str,
        name: str,
        properties: RecordsCreateRecordRequestProperties,
        links: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        parent: typing.Optional[RecordsCreateRecordRequestParent] = OMIT,
        children: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordModel:
        """
        Create a contract record by specifying its intended metadata properties

        Parameters
        ----------
        type : str
            The type of record to be created. You can view available record types by retrieving records metadata.

        name : str
            The name of the record.

        properties : RecordsCreateRecordRequestProperties
            Object containing key/value pairs of metadata attached to the record. The key you specify must have a value with a supported type as outlined in the Supported Property Types section.

        links : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]

        parent : typing.Optional[RecordsCreateRecordRequestParent]
            Object containing Record IDs or Ironclad IDs to be set as the parent of the current record.

        children : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the records to be set as child records of the current record.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordModel
            200

        Examples
        --------
        from fern.records import RecordsCreateRecordRequestProperties

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.createrecord(
            type="type",
            name="name",
            properties=RecordsCreateRecordRequestProperties(),
        )
        """
        _response = self._raw_client.createrecord(
            type=type,
            name=name,
            properties=properties,
            links=links,
            parent=parent,
            children=children,
            request_options=request_options,
        )
        return _response.data

    def getpredictions(
        self,
        *,
        record_id: typing.Optional[str] = None,
        import_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordsGetPredictionsResponse:
        """
        Retrieve status of predictions of specific smart import record or all records in an import, one of Record Id or Import Id is required.

        Parameters
        ----------
        record_id : typing.Optional[str]
            The ID of the Record for prediction status.

        import_id : typing.Optional[str]
            The ID of the Import for prediction statuses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsGetPredictionsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.getpredictions()
        """
        _response = self._raw_client.getpredictions(
            record_id=record_id, import_id=import_id, request_options=request_options
        )
        return _response.data

    def uploadsmartimportrecord(
        self,
        *,
        attachment: core.File,
        record_type: typing.Optional[str] = OMIT,
        new_record_type_id: typing.Optional[str] = OMIT,
        new_record_type_display_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordsUploadSmartImportRecordResponse:
        """
        Upload a file to create a record with smart import and predictions.  Provide none of recordType, newRecordTypeId, or newRecordTypeDisplayName to default to Imported type.

        Parameters
        ----------
        attachment : core.File
            See core.File for more documentation

        record_type : typing.Optional[str]
            Upload a smart import record as an existing record type.  Cannot provide alongside newRecordTypeId and newRecordTypeDisplayName. Defaults to Imported.

        new_record_type_id : typing.Optional[str]
            The record type ID for a not-yet-existing record type.  Must be provided along with a newRecordTypeDisplayName

        new_record_type_display_name : typing.Optional[str]
            The display name of the new record type to create.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsUploadSmartImportRecordResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.uploadsmartimportrecord()
        """
        _response = self._raw_client.uploadsmartimportrecord(
            attachment=attachment,
            record_type=record_type,
            new_record_type_id=new_record_type_id,
            new_record_type_display_name=new_record_type_display_name,
            request_options=request_options,
        )
        return _response.data

    def uploadsmartimportrecordwithpredictions(
        self,
        import_id: str,
        *,
        attachment: core.File,
        record_type: str,
        new_record_type_id: typing.Optional[str] = OMIT,
        new_record_type_display_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordsUploadSmartImportRecordWithPredictionsResponse:
        """
        Upload a file to an existing import and create a record with smart import and predictions.  Provide none of recordType, newRecordTypeId, or newRecordTypeDisplayName to default to Imported type.

        Parameters
        ----------
        import_id : str
            The Import Id. You can upload a record to an existing import in the repository.

        attachment : core.File
            See core.File for more documentation

        record_type : str
            Upload a smart import record as an existing record type.  Cannot provide alongside newRecordTypeId and newRecordTypeDisplayName. Defaults to Imported.

        new_record_type_id : typing.Optional[str]
            The record type ID for a not-yet-existing record type.  Must be provided along with a newRecordTypeDisplayName

        new_record_type_display_name : typing.Optional[str]
            The display name of the new record type to create.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsUploadSmartImportRecordWithPredictionsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.uploadsmartimportrecordwithpredictions(
            import_id="importId",
            record_type="recordType",
        )
        """
        _response = self._raw_client.uploadsmartimportrecordwithpredictions(
            import_id,
            attachment=attachment,
            record_type=record_type,
            new_record_type_id=new_record_type_id,
            new_record_type_display_name=new_record_type_display_name,
            request_options=request_options,
        )
        return _response.data

    def getrecorddata(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RecordModel:
        """
        View a specific record and its associated data

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordModel
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.getrecorddata(
            id="id",
        )
        """
        _response = self._raw_client.getrecorddata(id, request_options=request_options)
        return _response.data

    def replacemetadata(
        self,
        id: str,
        *,
        type: str,
        name: str,
        properties: RecordsReplaceMetadataRequestProperties,
        parent: typing.Optional[RecordsReplaceMetadataRequestParent] = OMIT,
        children: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordModel:
        """
        Update an existing record with a new set of metadata

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record.

        type : str
            The type of record to be created. You can view available record types by retrieving records metadata.

        name : str
            The name of the record.

        properties : RecordsReplaceMetadataRequestProperties
            Object containing key/value pairs of metadata attached to the record. The key you specify must have a value with a supported type as outlined in the Supported Property Types section.

        parent : typing.Optional[RecordsReplaceMetadataRequestParent]
            Object containing Record IDs or Ironclad IDs to be set as the parent of the current record.

        children : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the records to be set as child records of the current record.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordModel
            200

        Examples
        --------
        from fern.records import RecordsReplaceMetadataRequestProperties

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.replacemetadata(
            id="id",
            type="type",
            name="name",
            properties=RecordsReplaceMetadataRequestProperties(),
        )
        """
        _response = self._raw_client.replacemetadata(
            id,
            type=type,
            name=name,
            properties=properties,
            parent=parent,
            children=children,
            request_options=request_options,
        )
        return _response.data

    def deleterecord(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordsDeleteRecordResponse:
        """
        Delete an existing record

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsDeleteRecordResponse
            204

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.deleterecord(
            id="id",
        )
        """
        _response = self._raw_client.deleterecord(id, request_options=request_options)
        return _response.data

    def updatemetadata(
        self,
        id: str,
        *,
        type: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        add_properties: typing.Optional[RecordsUpdateMetadataRequestAddProperties] = OMIT,
        remove_properties: typing.Optional[typing.Sequence[str]] = OMIT,
        add_links: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        remove_links: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        set_parent: typing.Optional[RecordsUpdateMetadataRequestSetParent] = OMIT,
        add_children: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        remove_parent: typing.Optional[bool] = OMIT,
        remove_children: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordModel:
        """
        Update specific fields on a record

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record.

        type : typing.Optional[str]
            The type of Record.

        name : typing.Optional[str]
            The name of the Record.

        add_properties : typing.Optional[RecordsUpdateMetadataRequestAddProperties]
            A key:value map of properties to add. The two below are examples.

        remove_properties : typing.Optional[typing.Sequence[str]]
            List of record property ids to be removed (e.g., ['counterpartyAddress', 'agreementExpirationDate'])

        add_links : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the records to link. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).

        remove_links : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the record links to remove. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).

        set_parent : typing.Optional[RecordsUpdateMetadataRequestSetParent]
            Object containing Record IDs or Ironclad IDs to be set as the parent of the current record.

        add_children : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the records to be set as child records of the current record.

        remove_parent : typing.Optional[bool]
            Boolean flag to indicate if the parent id should be removed for the current record.

        remove_children : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the child records to be removed from the current record.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordModel
            200

        Examples
        --------
        from fern.records import (
            RecordsUpdateMetadataRequestAddProperties,
            RecordsUpdateMetadataRequestAddPropertiesAgreementDate,
            RecordsUpdateMetadataRequestAddPropertiesCounterpartyName,
        )

        from fern import FernApi, RecordPropertyLinkModel

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.updatemetadata(
            id="id",
            type="consultingAgreement",
            name="Consulting Agreement with Jane Doe",
            add_properties=RecordsUpdateMetadataRequestAddProperties(
                counterparty_name=RecordsUpdateMetadataRequestAddPropertiesCounterpartyName(
                    type="string",
                    value="Jane Doe",
                ),
                agreement_date=RecordsUpdateMetadataRequestAddPropertiesAgreementDate(
                    type="date",
                    value="2018-05-08T00:00:00-07:00",
                ),
            ),
            remove_properties=["counterpartySigner"],
            add_links=[
                RecordPropertyLinkModel(
                    record_id="df1c2805-f5a3-4a14-9386-c28d950dff49",
                )
            ],
            remove_links=[
                RecordPropertyLinkModel(
                    record_id="df1c2805-f5a3-4a14-9386-c28d950dff49",
                )
            ],
        )
        """
        _response = self._raw_client.updatemetadata(
            id,
            type=type,
            name=name,
            add_properties=add_properties,
            remove_properties=remove_properties,
            add_links=add_links,
            remove_links=remove_links,
            set_parent=set_parent,
            add_children=add_children,
            remove_parent=remove_parent,
            remove_children=remove_children,
            request_options=request_options,
        )
        return _response.data

    def getschema(self, *, request_options: typing.Optional[RequestOptions] = None) -> RecordsGetSchemaResponse:
        """
        View the schema associated with contract records, including available record types and metadata properties.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsGetSchemaResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.getschema()
        """
        _response = self._raw_client.getschema(request_options=request_options)
        return _response.data

    def getattachment(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordsGetAttachmentResponse:
        """
        View an attachment associated with a specific record

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record.

        key : str
            The attachment key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsGetAttachmentResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.getattachment(
            id="id",
            key="key",
        )
        """
        _response = self._raw_client.getattachment(id, key, request_options=request_options)
        return _response.data

    def createattachment(
        self,
        id: str,
        key: str,
        *,
        attachment: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[RecordsCreateAttachmentRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordsCreateAttachmentResponse:
        """
        Create an attachment on a specified record at the specified attachment key.

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).

        key : str
            The attachment key. You can retrieve a list of available attachment keys with the [Retrieve Records Schema](https://developer.ironcladapp.com/reference/list-all-records-metadata) endpoint.

        attachment : typing.Optional[core.File]
            See core.File for more documentation

        metadata : typing.Optional[RecordsCreateAttachmentRequestMetadata]
            The `metadata` property's value must be `{"filename": "[YOUR_FILE_NAME]"}`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsCreateAttachmentResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.createattachment(
            id="id",
            key="key",
        )
        """
        _response = self._raw_client.createattachment(
            id, key, attachment=attachment, metadata=metadata, request_options=request_options
        )
        return _response.data

    def removeattachment(self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Remove an attachment associated with a specific record

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record.

        key : str
            The attachment key.

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
        client.records.removeattachment(
            id="id",
            key="key",
        )
        """
        _response = self._raw_client.removeattachment(id, key, request_options=request_options)
        return _response.data

    def getxlsxexportfile(
        self,
        *,
        types: typing.Optional[str] = None,
        properties: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordsGetXlsxExportFileResponse:
        """
        Export a records report with filtering available via query parameters

        Parameters
        ----------
        types : typing.Optional[str]
            Comma separated list of record types to export. Example: `mutualNDA,NDA`

        properties : typing.Optional[str]
            IDs of properties to export, comma separated. Example: `counterpartyName,agreementDate`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsGetXlsxExportFileResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.getxlsxexportfile()
        """
        _response = self._raw_client.getxlsxexportfile(
            types=types, properties=properties, request_options=request_options
        )
        return _response.data


class AsyncRecordsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRecordsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRecordsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRecordsClient
        """
        return self._raw_client

    async def listall(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        types: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        sort_field: typing.Optional[RecordsListAllRequestSortField] = None,
        sort_direction: typing.Optional[RecordsListAllRequestSortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordsListAllResponse:
        """
        View all records in the company, with filtering available via query parameters

        Parameters
        ----------
        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        types : typing.Optional[str]
            Comma separated (no spaces) record types to export. Use the [Retrieve Records Schema](https://developer.ironcladapp.com/reference/list-all-records-metadata) endpoint to retrieve a list of types.

        last_updated : typing.Optional[str]
            Get records updated since (UTC)

        filter : typing.Optional[str]
            Filter records for those that contain (1) the specified property with (2) the specified value. The record property ID should be enclosed in brackets `[ ]` and the value should be enclosed in single quotes `' '`.

        sort_field : typing.Optional[RecordsListAllRequestSortField]
            The field to sort Records. Only one field is supported in the sort operation.

        sort_direction : typing.Optional[RecordsListAllRequestSortDirection]
            The direction the records are sorted by in correlation with the `sortField`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsListAllResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.listall(
                types="mutualNDA,consultingAgreement",
                last_updated="2018-03-10T00:00:00.000Z",
                filter="Equals([counterpartyName], 'Test LLC')",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listall(
            page=page,
            page_size=page_size,
            types=types,
            last_updated=last_updated,
            filter=filter,
            sort_field=sort_field,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    async def createrecord(
        self,
        *,
        type: str,
        name: str,
        properties: RecordsCreateRecordRequestProperties,
        links: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        parent: typing.Optional[RecordsCreateRecordRequestParent] = OMIT,
        children: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordModel:
        """
        Create a contract record by specifying its intended metadata properties

        Parameters
        ----------
        type : str
            The type of record to be created. You can view available record types by retrieving records metadata.

        name : str
            The name of the record.

        properties : RecordsCreateRecordRequestProperties
            Object containing key/value pairs of metadata attached to the record. The key you specify must have a value with a supported type as outlined in the Supported Property Types section.

        links : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]

        parent : typing.Optional[RecordsCreateRecordRequestParent]
            Object containing Record IDs or Ironclad IDs to be set as the parent of the current record.

        children : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the records to be set as child records of the current record.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordModel
            200

        Examples
        --------
        import asyncio

        from fern.records import RecordsCreateRecordRequestProperties

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.createrecord(
                type="type",
                name="name",
                properties=RecordsCreateRecordRequestProperties(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createrecord(
            type=type,
            name=name,
            properties=properties,
            links=links,
            parent=parent,
            children=children,
            request_options=request_options,
        )
        return _response.data

    async def getpredictions(
        self,
        *,
        record_id: typing.Optional[str] = None,
        import_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordsGetPredictionsResponse:
        """
        Retrieve status of predictions of specific smart import record or all records in an import, one of Record Id or Import Id is required.

        Parameters
        ----------
        record_id : typing.Optional[str]
            The ID of the Record for prediction status.

        import_id : typing.Optional[str]
            The ID of the Import for prediction statuses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsGetPredictionsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.getpredictions()


        asyncio.run(main())
        """
        _response = await self._raw_client.getpredictions(
            record_id=record_id, import_id=import_id, request_options=request_options
        )
        return _response.data

    async def uploadsmartimportrecord(
        self,
        *,
        attachment: core.File,
        record_type: typing.Optional[str] = OMIT,
        new_record_type_id: typing.Optional[str] = OMIT,
        new_record_type_display_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordsUploadSmartImportRecordResponse:
        """
        Upload a file to create a record with smart import and predictions.  Provide none of recordType, newRecordTypeId, or newRecordTypeDisplayName to default to Imported type.

        Parameters
        ----------
        attachment : core.File
            See core.File for more documentation

        record_type : typing.Optional[str]
            Upload a smart import record as an existing record type.  Cannot provide alongside newRecordTypeId and newRecordTypeDisplayName. Defaults to Imported.

        new_record_type_id : typing.Optional[str]
            The record type ID for a not-yet-existing record type.  Must be provided along with a newRecordTypeDisplayName

        new_record_type_display_name : typing.Optional[str]
            The display name of the new record type to create.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsUploadSmartImportRecordResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.uploadsmartimportrecord()


        asyncio.run(main())
        """
        _response = await self._raw_client.uploadsmartimportrecord(
            attachment=attachment,
            record_type=record_type,
            new_record_type_id=new_record_type_id,
            new_record_type_display_name=new_record_type_display_name,
            request_options=request_options,
        )
        return _response.data

    async def uploadsmartimportrecordwithpredictions(
        self,
        import_id: str,
        *,
        attachment: core.File,
        record_type: str,
        new_record_type_id: typing.Optional[str] = OMIT,
        new_record_type_display_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordsUploadSmartImportRecordWithPredictionsResponse:
        """
        Upload a file to an existing import and create a record with smart import and predictions.  Provide none of recordType, newRecordTypeId, or newRecordTypeDisplayName to default to Imported type.

        Parameters
        ----------
        import_id : str
            The Import Id. You can upload a record to an existing import in the repository.

        attachment : core.File
            See core.File for more documentation

        record_type : str
            Upload a smart import record as an existing record type.  Cannot provide alongside newRecordTypeId and newRecordTypeDisplayName. Defaults to Imported.

        new_record_type_id : typing.Optional[str]
            The record type ID for a not-yet-existing record type.  Must be provided along with a newRecordTypeDisplayName

        new_record_type_display_name : typing.Optional[str]
            The display name of the new record type to create.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsUploadSmartImportRecordWithPredictionsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.uploadsmartimportrecordwithpredictions(
                import_id="importId",
                record_type="recordType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.uploadsmartimportrecordwithpredictions(
            import_id,
            attachment=attachment,
            record_type=record_type,
            new_record_type_id=new_record_type_id,
            new_record_type_display_name=new_record_type_display_name,
            request_options=request_options,
        )
        return _response.data

    async def getrecorddata(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RecordModel:
        """
        View a specific record and its associated data

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordModel
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.getrecorddata(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getrecorddata(id, request_options=request_options)
        return _response.data

    async def replacemetadata(
        self,
        id: str,
        *,
        type: str,
        name: str,
        properties: RecordsReplaceMetadataRequestProperties,
        parent: typing.Optional[RecordsReplaceMetadataRequestParent] = OMIT,
        children: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordModel:
        """
        Update an existing record with a new set of metadata

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record.

        type : str
            The type of record to be created. You can view available record types by retrieving records metadata.

        name : str
            The name of the record.

        properties : RecordsReplaceMetadataRequestProperties
            Object containing key/value pairs of metadata attached to the record. The key you specify must have a value with a supported type as outlined in the Supported Property Types section.

        parent : typing.Optional[RecordsReplaceMetadataRequestParent]
            Object containing Record IDs or Ironclad IDs to be set as the parent of the current record.

        children : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the records to be set as child records of the current record.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordModel
            200

        Examples
        --------
        import asyncio

        from fern.records import RecordsReplaceMetadataRequestProperties

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.replacemetadata(
                id="id",
                type="type",
                name="name",
                properties=RecordsReplaceMetadataRequestProperties(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replacemetadata(
            id,
            type=type,
            name=name,
            properties=properties,
            parent=parent,
            children=children,
            request_options=request_options,
        )
        return _response.data

    async def deleterecord(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordsDeleteRecordResponse:
        """
        Delete an existing record

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsDeleteRecordResponse
            204

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.deleterecord(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleterecord(id, request_options=request_options)
        return _response.data

    async def updatemetadata(
        self,
        id: str,
        *,
        type: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        add_properties: typing.Optional[RecordsUpdateMetadataRequestAddProperties] = OMIT,
        remove_properties: typing.Optional[typing.Sequence[str]] = OMIT,
        add_links: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        remove_links: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        set_parent: typing.Optional[RecordsUpdateMetadataRequestSetParent] = OMIT,
        add_children: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        remove_parent: typing.Optional[bool] = OMIT,
        remove_children: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordModel:
        """
        Update specific fields on a record

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record.

        type : typing.Optional[str]
            The type of Record.

        name : typing.Optional[str]
            The name of the Record.

        add_properties : typing.Optional[RecordsUpdateMetadataRequestAddProperties]
            A key:value map of properties to add. The two below are examples.

        remove_properties : typing.Optional[typing.Sequence[str]]
            List of record property ids to be removed (e.g., ['counterpartyAddress', 'agreementExpirationDate'])

        add_links : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the records to link. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).

        remove_links : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the record links to remove. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).

        set_parent : typing.Optional[RecordsUpdateMetadataRequestSetParent]
            Object containing Record IDs or Ironclad IDs to be set as the parent of the current record.

        add_children : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the records to be set as child records of the current record.

        remove_parent : typing.Optional[bool]
            Boolean flag to indicate if the parent id should be removed for the current record.

        remove_children : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the child records to be removed from the current record.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordModel
            200

        Examples
        --------
        import asyncio

        from fern.records import (
            RecordsUpdateMetadataRequestAddProperties,
            RecordsUpdateMetadataRequestAddPropertiesAgreementDate,
            RecordsUpdateMetadataRequestAddPropertiesCounterpartyName,
        )

        from fern import AsyncFernApi, RecordPropertyLinkModel

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.updatemetadata(
                id="id",
                type="consultingAgreement",
                name="Consulting Agreement with Jane Doe",
                add_properties=RecordsUpdateMetadataRequestAddProperties(
                    counterparty_name=RecordsUpdateMetadataRequestAddPropertiesCounterpartyName(
                        type="string",
                        value="Jane Doe",
                    ),
                    agreement_date=RecordsUpdateMetadataRequestAddPropertiesAgreementDate(
                        type="date",
                        value="2018-05-08T00:00:00-07:00",
                    ),
                ),
                remove_properties=["counterpartySigner"],
                add_links=[
                    RecordPropertyLinkModel(
                        record_id="df1c2805-f5a3-4a14-9386-c28d950dff49",
                    )
                ],
                remove_links=[
                    RecordPropertyLinkModel(
                        record_id="df1c2805-f5a3-4a14-9386-c28d950dff49",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatemetadata(
            id,
            type=type,
            name=name,
            add_properties=add_properties,
            remove_properties=remove_properties,
            add_links=add_links,
            remove_links=remove_links,
            set_parent=set_parent,
            add_children=add_children,
            remove_parent=remove_parent,
            remove_children=remove_children,
            request_options=request_options,
        )
        return _response.data

    async def getschema(self, *, request_options: typing.Optional[RequestOptions] = None) -> RecordsGetSchemaResponse:
        """
        View the schema associated with contract records, including available record types and metadata properties.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsGetSchemaResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.getschema()


        asyncio.run(main())
        """
        _response = await self._raw_client.getschema(request_options=request_options)
        return _response.data

    async def getattachment(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordsGetAttachmentResponse:
        """
        View an attachment associated with a specific record

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record.

        key : str
            The attachment key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsGetAttachmentResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.getattachment(
                id="id",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getattachment(id, key, request_options=request_options)
        return _response.data

    async def createattachment(
        self,
        id: str,
        key: str,
        *,
        attachment: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[RecordsCreateAttachmentRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordsCreateAttachmentResponse:
        """
        Create an attachment on a specified record at the specified attachment key.

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).

        key : str
            The attachment key. You can retrieve a list of available attachment keys with the [Retrieve Records Schema](https://developer.ironcladapp.com/reference/list-all-records-metadata) endpoint.

        attachment : typing.Optional[core.File]
            See core.File for more documentation

        metadata : typing.Optional[RecordsCreateAttachmentRequestMetadata]
            The `metadata` property's value must be `{"filename": "[YOUR_FILE_NAME]"}`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsCreateAttachmentResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.createattachment(
                id="id",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createattachment(
            id, key, attachment=attachment, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def removeattachment(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove an attachment associated with a specific record

        Parameters
        ----------
        id : str
            The ID or Ironclad ID of the Record.

        key : str
            The attachment key.

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
            await client.records.removeattachment(
                id="id",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.removeattachment(id, key, request_options=request_options)
        return _response.data

    async def getxlsxexportfile(
        self,
        *,
        types: typing.Optional[str] = None,
        properties: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordsGetXlsxExportFileResponse:
        """
        Export a records report with filtering available via query parameters

        Parameters
        ----------
        types : typing.Optional[str]
            Comma separated list of record types to export. Example: `mutualNDA,NDA`

        properties : typing.Optional[str]
            IDs of properties to export, comma separated. Example: `counterpartyName,agreementDate`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordsGetXlsxExportFileResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.getxlsxexportfile()


        asyncio.run(main())
        """
        _response = await self._raw_client.getxlsxexportfile(
            types=types, properties=properties, request_options=request_options
        )
        return _response.data
