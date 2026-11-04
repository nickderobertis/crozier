

import json
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param, jsonable_encoder
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
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
from .types.records_create_attachment_request_metadata import RecordsCreateAttachmentRequestMetadata
from .types.records_create_record_request_parent import RecordsCreateRecordRequestParent
from .types.records_create_record_request_properties import RecordsCreateRecordRequestProperties
from .types.records_list_all_request_sort_direction import RecordsListAllRequestSortDirection
from .types.records_list_all_request_sort_field import RecordsListAllRequestSortField
from .types.records_replace_metadata_request_parent import RecordsReplaceMetadataRequestParent
from .types.records_replace_metadata_request_properties import RecordsReplaceMetadataRequestProperties
from .types.records_update_metadata_request_add_properties import RecordsUpdateMetadataRequestAddProperties
from .types.records_update_metadata_request_set_parent import RecordsUpdateMetadataRequestSetParent
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRecordsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[RecordsListAllResponse]:
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
        HttpResponse[RecordsListAllResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "records",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "types": types,
                "lastUpdated": last_updated,
                "filter": filter,
                "sortField": sort_field,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsListAllResponse,
                    parse_obj_as(
                        type_=RecordsListAllResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[RecordModel]:
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
        HttpResponse[RecordModel]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "records",
            method="POST",
            json={
                "type": type,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=RecordsCreateRecordRequestProperties, direction="write"
                ),
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=RecordsCreateRecordRequestParent, direction="write"
                ),
                "children": convert_and_respect_annotation_metadata(
                    object_=children, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordModel,
                    parse_obj_as(
                        type_=RecordModel,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getpredictions(
        self,
        *,
        record_id: typing.Optional[str] = None,
        import_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RecordsGetPredictionsResponse]:
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
        HttpResponse[RecordsGetPredictionsResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "records/smart-import",
            method="GET",
            params={
                "recordId": record_id,
                "importId": import_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsGetPredictionsResponse,
                    parse_obj_as(
                        type_=RecordsGetPredictionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def uploadsmartimportrecord(
        self,
        *,
        attachment: core.File,
        record_type: typing.Optional[str] = OMIT,
        new_record_type_id: typing.Optional[str] = OMIT,
        new_record_type_display_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RecordsUploadSmartImportRecordResponse]:
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
        HttpResponse[RecordsUploadSmartImportRecordResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "records/smart-import",
            method="POST",
            data={
                "recordType": record_type,
                "newRecordTypeId": new_record_type_id,
                "newRecordTypeDisplayName": new_record_type_display_name,
            },
            files={
                "attachment": attachment,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsUploadSmartImportRecordResponse,
                    parse_obj_as(
                        type_=RecordsUploadSmartImportRecordResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def uploadsmartimportrecordwithpredictions(
        self,
        import_id: str,
        *,
        attachment: core.File,
        record_type: str,
        new_record_type_id: typing.Optional[str] = OMIT,
        new_record_type_display_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RecordsUploadSmartImportRecordWithPredictionsResponse]:
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
        HttpResponse[RecordsUploadSmartImportRecordWithPredictionsResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"records/smart-import/{encode_path_param(import_id)}",
            method="POST",
            data={
                "recordType": record_type,
                "newRecordTypeId": new_record_type_id,
                "newRecordTypeDisplayName": new_record_type_display_name,
            },
            files={
                "attachment": attachment,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsUploadSmartImportRecordWithPredictionsResponse,
                    parse_obj_as(
                        type_=RecordsUploadSmartImportRecordWithPredictionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getrecorddata(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RecordModel]:
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
        HttpResponse[RecordModel]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordModel,
                    parse_obj_as(
                        type_=RecordModel,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[RecordModel]:
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
        HttpResponse[RecordModel]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}",
            method="PUT",
            json={
                "type": type,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=RecordsReplaceMetadataRequestProperties, direction="write"
                ),
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=RecordsReplaceMetadataRequestParent, direction="write"
                ),
                "children": convert_and_respect_annotation_metadata(
                    object_=children, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordModel,
                    parse_obj_as(
                        type_=RecordModel,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deleterecord(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RecordsDeleteRecordResponse]:
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
        HttpResponse[RecordsDeleteRecordResponse]
            204
        """
        _response = self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsDeleteRecordResponse,
                    parse_obj_as(
                        type_=RecordsDeleteRecordResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[RecordModel]:
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
        HttpResponse[RecordModel]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}",
            method="PATCH",
            json={
                "type": type,
                "name": name,
                "addProperties": convert_and_respect_annotation_metadata(
                    object_=add_properties, annotation=RecordsUpdateMetadataRequestAddProperties, direction="write"
                ),
                "removeProperties": remove_properties,
                "addLinks": convert_and_respect_annotation_metadata(
                    object_=add_links, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
                "removeLinks": convert_and_respect_annotation_metadata(
                    object_=remove_links, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
                "setParent": convert_and_respect_annotation_metadata(
                    object_=set_parent, annotation=RecordsUpdateMetadataRequestSetParent, direction="write"
                ),
                "addChildren": convert_and_respect_annotation_metadata(
                    object_=add_children, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
                "removeParent": remove_parent,
                "removeChildren": convert_and_respect_annotation_metadata(
                    object_=remove_children, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordModel,
                    parse_obj_as(
                        type_=RecordModel,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getschema(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RecordsGetSchemaResponse]:
        """
        View the schema associated with contract records, including available record types and metadata properties.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RecordsGetSchemaResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "records/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsGetSchemaResponse,
                    parse_obj_as(
                        type_=RecordsGetSchemaResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getattachment(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RecordsGetAttachmentResponse]:
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
        HttpResponse[RecordsGetAttachmentResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}/attachments/{encode_path_param(key)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsGetAttachmentResponse,
                    parse_obj_as(
                        type_=RecordsGetAttachmentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def createattachment(
        self,
        id: str,
        key: str,
        *,
        attachment: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[RecordsCreateAttachmentRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RecordsCreateAttachmentResponse]:
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
        HttpResponse[RecordsCreateAttachmentResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}/attachments/{encode_path_param(key)}",
            method="POST",
            data={
                "metadata": json.dumps(jsonable_encoder(metadata)) if metadata is not OMIT else OMIT,
            },
            files={
                **({"attachment": attachment} if attachment is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsCreateAttachmentResponse,
                    parse_obj_as(
                        type_=RecordsCreateAttachmentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def removeattachment(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}/attachments/{encode_path_param(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getxlsxexportfile(
        self,
        *,
        types: typing.Optional[str] = None,
        properties: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RecordsGetXlsxExportFileResponse]:
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
        HttpResponse[RecordsGetXlsxExportFileResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "records/export",
            method="GET",
            params={
                "types": types,
                "properties": properties,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsGetXlsxExportFileResponse,
                    parse_obj_as(
                        type_=RecordsGetXlsxExportFileResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawRecordsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[RecordsListAllResponse]:
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
        AsyncHttpResponse[RecordsListAllResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "records",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "types": types,
                "lastUpdated": last_updated,
                "filter": filter,
                "sortField": sort_field,
                "sortDirection": sort_direction,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsListAllResponse,
                    parse_obj_as(
                        type_=RecordsListAllResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[RecordModel]:
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
        AsyncHttpResponse[RecordModel]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "records",
            method="POST",
            json={
                "type": type,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=RecordsCreateRecordRequestProperties, direction="write"
                ),
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=RecordsCreateRecordRequestParent, direction="write"
                ),
                "children": convert_and_respect_annotation_metadata(
                    object_=children, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordModel,
                    parse_obj_as(
                        type_=RecordModel,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getpredictions(
        self,
        *,
        record_id: typing.Optional[str] = None,
        import_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RecordsGetPredictionsResponse]:
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
        AsyncHttpResponse[RecordsGetPredictionsResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "records/smart-import",
            method="GET",
            params={
                "recordId": record_id,
                "importId": import_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsGetPredictionsResponse,
                    parse_obj_as(
                        type_=RecordsGetPredictionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def uploadsmartimportrecord(
        self,
        *,
        attachment: core.File,
        record_type: typing.Optional[str] = OMIT,
        new_record_type_id: typing.Optional[str] = OMIT,
        new_record_type_display_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RecordsUploadSmartImportRecordResponse]:
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
        AsyncHttpResponse[RecordsUploadSmartImportRecordResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "records/smart-import",
            method="POST",
            data={
                "recordType": record_type,
                "newRecordTypeId": new_record_type_id,
                "newRecordTypeDisplayName": new_record_type_display_name,
            },
            files={
                "attachment": attachment,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsUploadSmartImportRecordResponse,
                    parse_obj_as(
                        type_=RecordsUploadSmartImportRecordResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def uploadsmartimportrecordwithpredictions(
        self,
        import_id: str,
        *,
        attachment: core.File,
        record_type: str,
        new_record_type_id: typing.Optional[str] = OMIT,
        new_record_type_display_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RecordsUploadSmartImportRecordWithPredictionsResponse]:
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
        AsyncHttpResponse[RecordsUploadSmartImportRecordWithPredictionsResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"records/smart-import/{encode_path_param(import_id)}",
            method="POST",
            data={
                "recordType": record_type,
                "newRecordTypeId": new_record_type_id,
                "newRecordTypeDisplayName": new_record_type_display_name,
            },
            files={
                "attachment": attachment,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsUploadSmartImportRecordWithPredictionsResponse,
                    parse_obj_as(
                        type_=RecordsUploadSmartImportRecordWithPredictionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getrecorddata(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RecordModel]:
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
        AsyncHttpResponse[RecordModel]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordModel,
                    parse_obj_as(
                        type_=RecordModel,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[RecordModel]:
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
        AsyncHttpResponse[RecordModel]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}",
            method="PUT",
            json={
                "type": type,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=RecordsReplaceMetadataRequestProperties, direction="write"
                ),
                "parent": convert_and_respect_annotation_metadata(
                    object_=parent, annotation=RecordsReplaceMetadataRequestParent, direction="write"
                ),
                "children": convert_and_respect_annotation_metadata(
                    object_=children, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordModel,
                    parse_obj_as(
                        type_=RecordModel,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deleterecord(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RecordsDeleteRecordResponse]:
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
        AsyncHttpResponse[RecordsDeleteRecordResponse]
            204
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsDeleteRecordResponse,
                    parse_obj_as(
                        type_=RecordsDeleteRecordResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[RecordModel]:
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
        AsyncHttpResponse[RecordModel]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}",
            method="PATCH",
            json={
                "type": type,
                "name": name,
                "addProperties": convert_and_respect_annotation_metadata(
                    object_=add_properties, annotation=RecordsUpdateMetadataRequestAddProperties, direction="write"
                ),
                "removeProperties": remove_properties,
                "addLinks": convert_and_respect_annotation_metadata(
                    object_=add_links, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
                "removeLinks": convert_and_respect_annotation_metadata(
                    object_=remove_links, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
                "setParent": convert_and_respect_annotation_metadata(
                    object_=set_parent, annotation=RecordsUpdateMetadataRequestSetParent, direction="write"
                ),
                "addChildren": convert_and_respect_annotation_metadata(
                    object_=add_children, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
                "removeParent": remove_parent,
                "removeChildren": convert_and_respect_annotation_metadata(
                    object_=remove_children, annotation=typing.Sequence[RecordPropertyLinkModel], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordModel,
                    parse_obj_as(
                        type_=RecordModel,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getschema(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RecordsGetSchemaResponse]:
        """
        View the schema associated with contract records, including available record types and metadata properties.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RecordsGetSchemaResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "records/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsGetSchemaResponse,
                    parse_obj_as(
                        type_=RecordsGetSchemaResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getattachment(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RecordsGetAttachmentResponse]:
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
        AsyncHttpResponse[RecordsGetAttachmentResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}/attachments/{encode_path_param(key)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsGetAttachmentResponse,
                    parse_obj_as(
                        type_=RecordsGetAttachmentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def createattachment(
        self,
        id: str,
        key: str,
        *,
        attachment: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[RecordsCreateAttachmentRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RecordsCreateAttachmentResponse]:
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
        AsyncHttpResponse[RecordsCreateAttachmentResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}/attachments/{encode_path_param(key)}",
            method="POST",
            data={
                "metadata": json.dumps(jsonable_encoder(metadata)) if metadata is not OMIT else OMIT,
            },
            files={
                **({"attachment": attachment} if attachment is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsCreateAttachmentResponse,
                    parse_obj_as(
                        type_=RecordsCreateAttachmentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def removeattachment(
        self, id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"records/{encode_path_param(id)}/attachments/{encode_path_param(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getxlsxexportfile(
        self,
        *,
        types: typing.Optional[str] = None,
        properties: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RecordsGetXlsxExportFileResponse]:
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
        AsyncHttpResponse[RecordsGetXlsxExportFileResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "records/export",
            method="GET",
            params={
                "types": types,
                "properties": properties,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordsGetXlsxExportFileResponse,
                    parse_obj_as(
                        type_=RecordsGetXlsxExportFileResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
