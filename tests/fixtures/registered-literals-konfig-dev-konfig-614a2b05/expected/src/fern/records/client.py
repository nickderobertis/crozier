

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.record_model import RecordModel
from ..types.record_property_link_model import RecordPropertyLinkModel
from .raw_client import AsyncRawRecordsClient, RawRecordsClient
from .types.create_a_record_request_parent import CreateARecordRequestParent
from .types.create_a_record_request_properties import CreateARecordRequestProperties
from .types.create_a_smart_import_record_response import CreateASmartImportRecordResponse
from .types.create_a_smart_import_record_to_import_response import CreateASmartImportRecordToImportResponse
from .types.create_an_attachment_on_a_record_request_metadata import CreateAnAttachmentOnARecordRequestMetadata
from .types.create_an_attachment_on_a_record_response import CreateAnAttachmentOnARecordResponse
from .types.delete_a_record_response import DeleteARecordResponse
from .types.list_all_records_metadata_response import ListAllRecordsMetadataResponse
from .types.list_all_records_request_sort_direction import ListAllRecordsRequestSortDirection
from .types.list_all_records_request_sort_field import ListAllRecordsRequestSortField
from .types.list_all_records_response import ListAllRecordsResponse
from .types.replace_a_record_request_parent import ReplaceARecordRequestParent
from .types.replace_a_record_request_properties import ReplaceARecordRequestProperties
from .types.retrieve_an_attachment_on_a_record_response import RetrieveAnAttachmentOnARecordResponse
from .types.retrieve_import_predictions_response import RetrieveImportPredictionsResponse
from .types.retrieve_xlsx_export_file_of_all_records_response import RetrieveXlsxExportFileOfAllRecordsResponse
from .types.update_record_metadata_request_add_properties import UpdateRecordMetadataRequestAddProperties
from .types.update_record_metadata_request_set_parent import UpdateRecordMetadataRequestSetParent


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

    def list_all_records(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        types: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        sort_field: typing.Optional[ListAllRecordsRequestSortField] = None,
        sort_direction: typing.Optional[ListAllRecordsRequestSortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAllRecordsResponse:
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

        sort_field : typing.Optional[ListAllRecordsRequestSortField]
            The field to sort Records. Only one field is supported in the sort operation.

        sort_direction : typing.Optional[ListAllRecordsRequestSortDirection]
            The direction the records are sorted by in correlation with the `sortField`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAllRecordsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.list_all_records(
            types="mutualNDA,consultingAgreement",
            last_updated="2018-03-10T00:00:00.000Z",
            filter="Equals([counterpartyName], 'Test LLC')",
        )
        """
        _response = self._raw_client.list_all_records(
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

    def create_a_record(
        self,
        *,
        type: str,
        name: str,
        properties: CreateARecordRequestProperties,
        links: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        parent: typing.Optional[CreateARecordRequestParent] = OMIT,
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

        properties : CreateARecordRequestProperties
            Object containing key/value pairs of metadata attached to the record. The key you specify must have a value with a supported type as outlined in the Supported Property Types section.

        links : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]

        parent : typing.Optional[CreateARecordRequestParent]
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
        from fern.records import CreateARecordRequestProperties

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.create_a_record(
            type="type",
            name="name",
            properties=CreateARecordRequestProperties(),
        )
        """
        _response = self._raw_client.create_a_record(
            type=type,
            name=name,
            properties=properties,
            links=links,
            parent=parent,
            children=children,
            request_options=request_options,
        )
        return _response.data

    def retrieve_import_predictions(
        self,
        *,
        record_id: typing.Optional[str] = None,
        import_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveImportPredictionsResponse:
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
        RetrieveImportPredictionsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.retrieve_import_predictions()
        """
        _response = self._raw_client.retrieve_import_predictions(
            record_id=record_id, import_id=import_id, request_options=request_options
        )
        return _response.data

    def create_a_smart_import_record(
        self,
        *,
        attachment: core.File,
        record_type: typing.Optional[str] = OMIT,
        new_record_type_id: typing.Optional[str] = OMIT,
        new_record_type_display_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateASmartImportRecordResponse:
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
        CreateASmartImportRecordResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.create_a_smart_import_record()
        """
        _response = self._raw_client.create_a_smart_import_record(
            attachment=attachment,
            record_type=record_type,
            new_record_type_id=new_record_type_id,
            new_record_type_display_name=new_record_type_display_name,
            request_options=request_options,
        )
        return _response.data

    def create_a_smart_import_record_to_import(
        self,
        import_id: str,
        *,
        attachment: core.File,
        record_type: str,
        new_record_type_id: typing.Optional[str] = OMIT,
        new_record_type_display_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateASmartImportRecordToImportResponse:
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
        CreateASmartImportRecordToImportResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.create_a_smart_import_record_to_import(
            import_id="importId",
            record_type="recordType",
        )
        """
        _response = self._raw_client.create_a_smart_import_record_to_import(
            import_id,
            attachment=attachment,
            record_type=record_type,
            new_record_type_id=new_record_type_id,
            new_record_type_display_name=new_record_type_display_name,
            request_options=request_options,
        )
        return _response.data

    def retrieve_a_record(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RecordModel:
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
        client.records.retrieve_a_record(
            id="id",
        )
        """
        _response = self._raw_client.retrieve_a_record(id, request_options=request_options)
        return _response.data

    def replace_a_record(
        self,
        id: str,
        *,
        type: str,
        name: str,
        properties: ReplaceARecordRequestProperties,
        parent: typing.Optional[ReplaceARecordRequestParent] = OMIT,
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

        properties : ReplaceARecordRequestProperties
            Object containing key/value pairs of metadata attached to the record. The key you specify must have a value with a supported type as outlined in the Supported Property Types section.

        parent : typing.Optional[ReplaceARecordRequestParent]
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
        from fern.records import ReplaceARecordRequestProperties

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.replace_a_record(
            id="id",
            type="type",
            name="name",
            properties=ReplaceARecordRequestProperties(),
        )
        """
        _response = self._raw_client.replace_a_record(
            id,
            type=type,
            name=name,
            properties=properties,
            parent=parent,
            children=children,
            request_options=request_options,
        )
        return _response.data

    def delete_a_record(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteARecordResponse:
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
        DeleteARecordResponse
            204

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.delete_a_record(
            id="id",
        )
        """
        _response = self._raw_client.delete_a_record(id, request_options=request_options)
        return _response.data

    def update_record_metadata(
        self,
        id: str,
        *,
        type: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        add_properties: typing.Optional[UpdateRecordMetadataRequestAddProperties] = OMIT,
        remove_properties: typing.Optional[typing.Sequence[str]] = OMIT,
        add_links: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        remove_links: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        set_parent: typing.Optional[UpdateRecordMetadataRequestSetParent] = OMIT,
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

        add_properties : typing.Optional[UpdateRecordMetadataRequestAddProperties]
            A key:value map of properties to add. The two below are examples.

        remove_properties : typing.Optional[typing.Sequence[str]]
            List of record property ids to be removed (e.g., ['counterpartyAddress', 'agreementExpirationDate'])

        add_links : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the records to link. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).

        remove_links : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the record links to remove. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).

        set_parent : typing.Optional[UpdateRecordMetadataRequestSetParent]
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
            UpdateRecordMetadataRequestAddProperties,
            UpdateRecordMetadataRequestAddPropertiesAgreementDate,
            UpdateRecordMetadataRequestAddPropertiesCounterpartyName,
        )

        from fern import FernApi, RecordPropertyLinkModel

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.update_record_metadata(
            id="id",
            type="consultingAgreement",
            name="Consulting Agreement with Jane Doe",
            add_properties=UpdateRecordMetadataRequestAddProperties(
                counterparty_name=UpdateRecordMetadataRequestAddPropertiesCounterpartyName(
                    type="string",
                    value="Jane Doe",
                ),
                agreement_date=UpdateRecordMetadataRequestAddPropertiesAgreementDate(
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
        _response = self._raw_client.update_record_metadata(
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

    def list_all_records_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAllRecordsMetadataResponse:
        """
        View the schema associated with contract records, including available record types and metadata properties.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAllRecordsMetadataResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.list_all_records_metadata()
        """
        _response = self._raw_client.list_all_records_metadata(request_options=request_options)
        return _response.data

    def retrieve_an_attachment_on_a_record(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveAnAttachmentOnARecordResponse:
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
        RetrieveAnAttachmentOnARecordResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.retrieve_an_attachment_on_a_record(
            id="id",
            key="key",
        )
        """
        _response = self._raw_client.retrieve_an_attachment_on_a_record(id, key, request_options=request_options)
        return _response.data

    def create_an_attachment_on_a_record(
        self,
        id: str,
        key: str,
        *,
        attachment: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[CreateAnAttachmentOnARecordRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAnAttachmentOnARecordResponse:
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

        metadata : typing.Optional[CreateAnAttachmentOnARecordRequestMetadata]
            The `metadata` property's value must be `{"filename": "[YOUR_FILE_NAME]"}`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAnAttachmentOnARecordResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.create_an_attachment_on_a_record(
            id="id",
            key="key",
        )
        """
        _response = self._raw_client.create_an_attachment_on_a_record(
            id, key, attachment=attachment, metadata=metadata, request_options=request_options
        )
        return _response.data

    def delete_an_attachment_on_a_record(
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
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.delete_an_attachment_on_a_record(
            id="id",
            key="key",
        )
        """
        _response = self._raw_client.delete_an_attachment_on_a_record(id, key, request_options=request_options)
        return _response.data

    def retrieve_xlsx_export_file_of_all_records(
        self,
        *,
        types: typing.Optional[str] = None,
        properties: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveXlsxExportFileOfAllRecordsResponse:
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
        RetrieveXlsxExportFileOfAllRecordsResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.records.retrieve_xlsx_export_file_of_all_records()
        """
        _response = self._raw_client.retrieve_xlsx_export_file_of_all_records(
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

    async def list_all_records(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        types: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        sort_field: typing.Optional[ListAllRecordsRequestSortField] = None,
        sort_direction: typing.Optional[ListAllRecordsRequestSortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAllRecordsResponse:
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

        sort_field : typing.Optional[ListAllRecordsRequestSortField]
            The field to sort Records. Only one field is supported in the sort operation.

        sort_direction : typing.Optional[ListAllRecordsRequestSortDirection]
            The direction the records are sorted by in correlation with the `sortField`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAllRecordsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.list_all_records(
                types="mutualNDA,consultingAgreement",
                last_updated="2018-03-10T00:00:00.000Z",
                filter="Equals([counterpartyName], 'Test LLC')",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_records(
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

    async def create_a_record(
        self,
        *,
        type: str,
        name: str,
        properties: CreateARecordRequestProperties,
        links: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        parent: typing.Optional[CreateARecordRequestParent] = OMIT,
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

        properties : CreateARecordRequestProperties
            Object containing key/value pairs of metadata attached to the record. The key you specify must have a value with a supported type as outlined in the Supported Property Types section.

        links : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]

        parent : typing.Optional[CreateARecordRequestParent]
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

        from fern.records import CreateARecordRequestProperties

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.create_a_record(
                type="type",
                name="name",
                properties=CreateARecordRequestProperties(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_record(
            type=type,
            name=name,
            properties=properties,
            links=links,
            parent=parent,
            children=children,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_import_predictions(
        self,
        *,
        record_id: typing.Optional[str] = None,
        import_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveImportPredictionsResponse:
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
        RetrieveImportPredictionsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.retrieve_import_predictions()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_import_predictions(
            record_id=record_id, import_id=import_id, request_options=request_options
        )
        return _response.data

    async def create_a_smart_import_record(
        self,
        *,
        attachment: core.File,
        record_type: typing.Optional[str] = OMIT,
        new_record_type_id: typing.Optional[str] = OMIT,
        new_record_type_display_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateASmartImportRecordResponse:
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
        CreateASmartImportRecordResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.create_a_smart_import_record()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_smart_import_record(
            attachment=attachment,
            record_type=record_type,
            new_record_type_id=new_record_type_id,
            new_record_type_display_name=new_record_type_display_name,
            request_options=request_options,
        )
        return _response.data

    async def create_a_smart_import_record_to_import(
        self,
        import_id: str,
        *,
        attachment: core.File,
        record_type: str,
        new_record_type_id: typing.Optional[str] = OMIT,
        new_record_type_display_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateASmartImportRecordToImportResponse:
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
        CreateASmartImportRecordToImportResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.create_a_smart_import_record_to_import(
                import_id="importId",
                record_type="recordType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_smart_import_record_to_import(
            import_id,
            attachment=attachment,
            record_type=record_type,
            new_record_type_id=new_record_type_id,
            new_record_type_display_name=new_record_type_display_name,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_a_record(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordModel:
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
            await client.records.retrieve_a_record(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_record(id, request_options=request_options)
        return _response.data

    async def replace_a_record(
        self,
        id: str,
        *,
        type: str,
        name: str,
        properties: ReplaceARecordRequestProperties,
        parent: typing.Optional[ReplaceARecordRequestParent] = OMIT,
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

        properties : ReplaceARecordRequestProperties
            Object containing key/value pairs of metadata attached to the record. The key you specify must have a value with a supported type as outlined in the Supported Property Types section.

        parent : typing.Optional[ReplaceARecordRequestParent]
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

        from fern.records import ReplaceARecordRequestProperties

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.replace_a_record(
                id="id",
                type="type",
                name="name",
                properties=ReplaceARecordRequestProperties(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_a_record(
            id,
            type=type,
            name=name,
            properties=properties,
            parent=parent,
            children=children,
            request_options=request_options,
        )
        return _response.data

    async def delete_a_record(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteARecordResponse:
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
        DeleteARecordResponse
            204

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.delete_a_record(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_record(id, request_options=request_options)
        return _response.data

    async def update_record_metadata(
        self,
        id: str,
        *,
        type: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        add_properties: typing.Optional[UpdateRecordMetadataRequestAddProperties] = OMIT,
        remove_properties: typing.Optional[typing.Sequence[str]] = OMIT,
        add_links: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        remove_links: typing.Optional[typing.Sequence[RecordPropertyLinkModel]] = OMIT,
        set_parent: typing.Optional[UpdateRecordMetadataRequestSetParent] = OMIT,
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

        add_properties : typing.Optional[UpdateRecordMetadataRequestAddProperties]
            A key:value map of properties to add. The two below are examples.

        remove_properties : typing.Optional[typing.Sequence[str]]
            List of record property ids to be removed (e.g., ['counterpartyAddress', 'agreementExpirationDate'])

        add_links : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the records to link. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).

        remove_links : typing.Optional[typing.Sequence[RecordPropertyLinkModel]]
            List of objects containing the Record IDs or Ironclad IDs of the record links to remove. For an explanation of Record IDs or Ironclad IDs and how to find them, see [Getting Started](https://developer.ironcladapp.com/reference/getting-started-api).

        set_parent : typing.Optional[UpdateRecordMetadataRequestSetParent]
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
            UpdateRecordMetadataRequestAddProperties,
            UpdateRecordMetadataRequestAddPropertiesAgreementDate,
            UpdateRecordMetadataRequestAddPropertiesCounterpartyName,
        )

        from fern import AsyncFernApi, RecordPropertyLinkModel

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.update_record_metadata(
                id="id",
                type="consultingAgreement",
                name="Consulting Agreement with Jane Doe",
                add_properties=UpdateRecordMetadataRequestAddProperties(
                    counterparty_name=UpdateRecordMetadataRequestAddPropertiesCounterpartyName(
                        type="string",
                        value="Jane Doe",
                    ),
                    agreement_date=UpdateRecordMetadataRequestAddPropertiesAgreementDate(
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
        _response = await self._raw_client.update_record_metadata(
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

    async def list_all_records_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAllRecordsMetadataResponse:
        """
        View the schema associated with contract records, including available record types and metadata properties.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAllRecordsMetadataResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.list_all_records_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_records_metadata(request_options=request_options)
        return _response.data

    async def retrieve_an_attachment_on_a_record(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveAnAttachmentOnARecordResponse:
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
        RetrieveAnAttachmentOnARecordResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.retrieve_an_attachment_on_a_record(
                id="id",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_an_attachment_on_a_record(id, key, request_options=request_options)
        return _response.data

    async def create_an_attachment_on_a_record(
        self,
        id: str,
        key: str,
        *,
        attachment: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[CreateAnAttachmentOnARecordRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAnAttachmentOnARecordResponse:
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

        metadata : typing.Optional[CreateAnAttachmentOnARecordRequestMetadata]
            The `metadata` property's value must be `{"filename": "[YOUR_FILE_NAME]"}`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAnAttachmentOnARecordResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.create_an_attachment_on_a_record(
                id="id",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_an_attachment_on_a_record(
            id, key, attachment=attachment, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def delete_an_attachment_on_a_record(
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
            await client.records.delete_an_attachment_on_a_record(
                id="id",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_an_attachment_on_a_record(id, key, request_options=request_options)
        return _response.data

    async def retrieve_xlsx_export_file_of_all_records(
        self,
        *,
        types: typing.Optional[str] = None,
        properties: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RetrieveXlsxExportFileOfAllRecordsResponse:
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
        RetrieveXlsxExportFileOfAllRecordsResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.records.retrieve_xlsx_export_file_of_all_records()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_xlsx_export_file_of_all_records(
            types=types, properties=properties, request_options=request_options
        )
        return _response.data
