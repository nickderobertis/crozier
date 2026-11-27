

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.async_task_link import AsyncTaskLink
from ..types.custom_fields import CustomFields
from ..types.entries_paginated_list import EntriesPaginatedList
from ..types.entry_by_id import EntryById
from ..types.entry_create_attachments import EntryCreateAttachments
from ..types.entry_create_attachments_review_record import EntryCreateAttachmentsReviewRecord
from ..types.entry_create_author_ids import EntryCreateAuthorIds
from ..types.entry_template import EntryTemplate
from ..types.fields import Fields
from ..types.initial_table import InitialTable
from .types.list_entries_request_review_status import ListEntriesRequestReviewStatus
from .types.list_entries_request_sort import ListEntriesRequestSort
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEntriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_entries(
        self,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListEntriesRequestSort] = None,
        modified_at: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        archive_reason: typing.Optional[str] = None,
        review_status: typing.Optional[ListEntriesRequestReviewStatus] = None,
        mentioned_in: typing.Optional[str] = None,
        mentions: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        schema_id: typing.Optional[str] = None,
        names_any_of: typing.Optional[str] = None,
        names_any_of_case_sensitive: typing.Optional[str] = None,
        assigned_reviewer_ids_any_of: typing.Optional[str] = None,
        creator_ids: typing.Optional[str] = None,
        author_ids_any_of: typing.Optional[str] = None,
        display_ids: typing.Optional[str] = None,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntriesPaginatedList]:
        """
        List notebook entries

        Parameters
        ----------
        page_size : typing.Optional[int]
            Number of results to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        sort : typing.Optional[ListEntriesRequestSort]
            Method by which to order search results. Valid sorts are modifiedAt (modified time, most recent first) and name (entity name, alphabetical). Optionally add :asc or :desc to specify ascending or descending order.

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        name : typing.Optional[str]
            Name of an Entry. Restricts results to those with the specified name.

        project_id : typing.Optional[str]
            ID of a project. Restricts results to those in the project.

        archive_reason : typing.Optional[str]
            Archive reason. Restricts items to those with the specified archive reason. Use "NOT_ARCHIVED" to filter for unarchived entries. Use "ANY_ARCHIVED" to filter for archived entries regardless of reason. Use "ANY_ARCHIVED_OR_NOT_ARCHIVED" to return items for both archived and unarchived.

        review_status : typing.Optional[ListEntriesRequestReviewStatus]
            Restrict results to those with the given review status. Supported statuses: IN_PROGRESS, ACCEPTED, REJECTED, NEEDS_REVIEW, RETRACTED

        mentioned_in : typing.Optional[str]
            Comma-separated list of entry IDs. Restricts results to those mentioned within the entries in this list.

        mentions : typing.Optional[str]
            Comma-separated list of resource IDs. Restricts results to entries that mention the given items.

        ids : typing.Optional[str]
            Comma-separated list of ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.

        schema_id : typing.Optional[str]
            ID of a schema. Restricts results to those of the specified schema.

        names_any_of : typing.Optional[str]
            Comma-separated list of names. Restricts results to those that match any of the specified names, case insensitive.  Warning - this filter can be non-performant due to case insensitivity.

        names_any_of_case_sensitive : typing.Optional[str]
            Comma-separated list of names. Restricts results to those that match any of the specified names, case sensitive.

        assigned_reviewer_ids_any_of : typing.Optional[str]
            Comma-separated list of ids. Restricts results to entries that have assignees of any of the specified ids.

        creator_ids : typing.Optional[str]
            Comma separated list of users IDs

        author_ids_any_of : typing.Optional[str]
            Comma separated list of user or app IDs

        display_ids : typing.Optional[str]
            Comma-separated list of Entry Display IDs.

        returning : typing.Optional[str]
            Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

            **Note:** "entries.days.notes" cannot be introspected with the returning parameter, and any sub fields will be ignored. E.g., "entries.days.notes.text" will return the same model as "entries.days.notes".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntriesPaginatedList]
            Returns a list of entries. Entries are notes that users can take. They're organized by "days" (which are user-configurable) and modeled within each day as a list of "notes." Each note has a type - the simplest is a "text" type, but lists, tables, and external files are also supported.

            *Note:* the current Entry resource has a few limitations:
            - Formatting information is not yet supported. Header formatting, bolding, and other stylistic information is not presented.
            - Data in tables is presented as text always - numeric values will need to be parsed into floats or integers, as appropriate.

            Note: Data in Results tables are not accessible through this API call. Results table data can be called through the Results API calls.
        """
        _response = self._client_wrapper.httpx_client.request(
            "entries",
            method="GET",
            params={
                "pageSize": page_size,
                "nextToken": next_token,
                "sort": sort,
                "modifiedAt": modified_at,
                "name": name,
                "projectId": project_id,
                "archiveReason": archive_reason,
                "reviewStatus": review_status,
                "mentionedIn": mentioned_in,
                "mentions": mentions,
                "ids": ids,
                "schemaId": schema_id,
                "names.anyOf": names_any_of,
                "names.anyOf.caseSensitive": names_any_of_case_sensitive,
                "assignedReviewerIds.anyOf": assigned_reviewer_ids_any_of,
                "creatorIds": creator_ids,
                "authorIds.anyOf": author_ids_any_of,
                "displayIds": display_ids,
                "returning": returning,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntriesPaginatedList,
                    parse_obj_as(
                        type_=EntriesPaginatedList,
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

    def create_entry_with_attachments(
        self,
        *,
        folder_id: str,
        name: str,
        review_record: typing.Optional[EntryCreateAttachmentsReviewRecord] = OMIT,
        author_ids: typing.Optional[EntryCreateAuthorIds] = OMIT,
        custom_fields: typing.Optional[CustomFields] = OMIT,
        entry_template_id: typing.Optional[str] = OMIT,
        fields: typing.Optional[Fields] = OMIT,
        initial_tables: typing.Optional[typing.Sequence[InitialTable]] = OMIT,
        schema_id: typing.Optional[str] = OMIT,
        attachment_text: typing.Optional[typing.Any] = OMIT,
        attachments: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncTaskLink]:
        """
        Create a notebook entry with optional attachments. Attachments will be placed into the entry body in the order they are specified.

        Parameters
        ----------
        folder_id : str
            ID of the folder that will contain the entry

        name : str
            Name of the entry

        review_record : typing.Optional[EntryCreateAttachmentsReviewRecord]

        author_ids : typing.Optional[EntryCreateAuthorIds]

        custom_fields : typing.Optional[CustomFields]
            Custom fields to add to the entry

        entry_template_id : typing.Optional[str]
            ID of the template to clone the entry from

        fields : typing.Optional[Fields]
            Fields to set on the entry. Must correspond with the schema's field definitions.

        initial_tables : typing.Optional[typing.Sequence[InitialTable]]
            An array of table API IDs and blob id pairs to seed tables from the template while creating the entry. The entryTemplateId parameter must be set to use this parameter. The table API IDs should be the API Identifiers of the tables in the given template.
            - If a template table has one row, the values in that row act as default values for cloned entries.
            - If a template table has multiple rows, there is no default value and those rows are added to the cloned entry along with the provided csv data.
            - If a table has default values, they will be populated in any respective undefined columns in the csv data.
            - If a table has no default values, undefined columns from csv data will be empty.
            - If no csv data is provided for a table, the table in the entry will be populated with whatever values are in the respective template table.

        schema_id : typing.Optional[str]
            ID of the entry's schema

        attachment_text : typing.Optional[typing.Any]
            Text to include in the entry before the attachments. If not provided, the text will be "File attachments are listed below:"

        attachments : typing.Optional[typing.Sequence[str]]
            An array of IDs representing Blob objects in Benchling to be attached to the entry.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AsyncTaskLink]
            Accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            "entries",
            method="POST",
            json={
                "reviewRecord": convert_and_respect_annotation_metadata(
                    object_=review_record, annotation=EntryCreateAttachmentsReviewRecord, direction="write"
                ),
                "authorIds": convert_and_respect_annotation_metadata(
                    object_=author_ids, annotation=EntryCreateAuthorIds, direction="write"
                ),
                "customFields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=CustomFields, direction="write"
                ),
                "entryTemplateId": entry_template_id,
                "fields": convert_and_respect_annotation_metadata(object_=fields, annotation=Fields, direction="write"),
                "folderId": folder_id,
                "initialTables": convert_and_respect_annotation_metadata(
                    object_=initial_tables, annotation=typing.Sequence[InitialTable], direction="write"
                ),
                "name": name,
                "schemaId": schema_id,
                "attachmentText": attachment_text,
                "attachments": attachments,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AsyncTaskLink,
                    parse_obj_as(
                        type_=AsyncTaskLink,
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

    def get_entry(
        self,
        entry_id: str,
        *,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntryById]:
        """
        Get a notebook entry by ID

        Parameters
        ----------
        entry_id : str
            ID of the entry

        returning : typing.Optional[str]
            Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

            **Note:** "days.notes" cannot be introspected with the returning parameter, and any sub fields will be ignored. E.g., "days.notes.text" will return the same model as "days.notes".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntryById]
            Returns a single entry. Entries are notes that users can take. They're organized by "days" (which are user-configurable) and modeled within each day as a list of "notes." Each note has a type - the simplest is a "text" type, but lists, tables, and external files are also supported.

            *Note:* the current Entry resource has a few limitations:
            - Formatting information is not yet supported. Header formatting, bolding, and other stylistic information is not presented.
            - Data in tables is presented as text always - numeric values will need to be parsed into floats or integers, as appropriate.

            Note: Data in Results tables are not accessible through this API call. Results table data can be called through the Results API calls.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entries/{encode_path_param(entry_id)}",
            method="GET",
            params={
                "returning": returning,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntryById,
                    parse_obj_as(
                        type_=EntryById,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def bulk_create_entries(
        self,
        *,
        entry_datas: typing.Optional[typing.Sequence[EntryCreateAttachments]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncTaskLink]:
        """
        Bulk create notebook entries with optional attachments. Limit of 100 Entries per request. Attachments will be placed into the entry body in the order they are specified.

        Parameters
        ----------
        entry_datas : typing.Optional[typing.Sequence[EntryCreateAttachments]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AsyncTaskLink]
            Accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            "entries:bulk-create",
            method="POST",
            json={
                "entryDatas": convert_and_respect_annotation_metadata(
                    object_=entry_datas, annotation=typing.Sequence[EntryCreateAttachments], direction="write"
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
                    AsyncTaskLink,
                    parse_obj_as(
                        type_=AsyncTaskLink,
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

    def get_template_entry(
        self, entry_template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EntryTemplate]:
        """
        Get a notebook template entry by ID

        Parameters
        ----------
        entry_template_id : str
            ID of the entry template

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntryTemplate]
            Returns a single entry template. Entry templates are templates that users can base new notebook entries off of.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entry-templates/{encode_path_param(entry_template_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntryTemplate,
                    parse_obj_as(
                        type_=EntryTemplate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawEntriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_entries(
        self,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListEntriesRequestSort] = None,
        modified_at: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        archive_reason: typing.Optional[str] = None,
        review_status: typing.Optional[ListEntriesRequestReviewStatus] = None,
        mentioned_in: typing.Optional[str] = None,
        mentions: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        schema_id: typing.Optional[str] = None,
        names_any_of: typing.Optional[str] = None,
        names_any_of_case_sensitive: typing.Optional[str] = None,
        assigned_reviewer_ids_any_of: typing.Optional[str] = None,
        creator_ids: typing.Optional[str] = None,
        author_ids_any_of: typing.Optional[str] = None,
        display_ids: typing.Optional[str] = None,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntriesPaginatedList]:
        """
        List notebook entries

        Parameters
        ----------
        page_size : typing.Optional[int]
            Number of results to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        sort : typing.Optional[ListEntriesRequestSort]
            Method by which to order search results. Valid sorts are modifiedAt (modified time, most recent first) and name (entity name, alphabetical). Optionally add :asc or :desc to specify ascending or descending order.

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        name : typing.Optional[str]
            Name of an Entry. Restricts results to those with the specified name.

        project_id : typing.Optional[str]
            ID of a project. Restricts results to those in the project.

        archive_reason : typing.Optional[str]
            Archive reason. Restricts items to those with the specified archive reason. Use "NOT_ARCHIVED" to filter for unarchived entries. Use "ANY_ARCHIVED" to filter for archived entries regardless of reason. Use "ANY_ARCHIVED_OR_NOT_ARCHIVED" to return items for both archived and unarchived.

        review_status : typing.Optional[ListEntriesRequestReviewStatus]
            Restrict results to those with the given review status. Supported statuses: IN_PROGRESS, ACCEPTED, REJECTED, NEEDS_REVIEW, RETRACTED

        mentioned_in : typing.Optional[str]
            Comma-separated list of entry IDs. Restricts results to those mentioned within the entries in this list.

        mentions : typing.Optional[str]
            Comma-separated list of resource IDs. Restricts results to entries that mention the given items.

        ids : typing.Optional[str]
            Comma-separated list of ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.

        schema_id : typing.Optional[str]
            ID of a schema. Restricts results to those of the specified schema.

        names_any_of : typing.Optional[str]
            Comma-separated list of names. Restricts results to those that match any of the specified names, case insensitive.  Warning - this filter can be non-performant due to case insensitivity.

        names_any_of_case_sensitive : typing.Optional[str]
            Comma-separated list of names. Restricts results to those that match any of the specified names, case sensitive.

        assigned_reviewer_ids_any_of : typing.Optional[str]
            Comma-separated list of ids. Restricts results to entries that have assignees of any of the specified ids.

        creator_ids : typing.Optional[str]
            Comma separated list of users IDs

        author_ids_any_of : typing.Optional[str]
            Comma separated list of user or app IDs

        display_ids : typing.Optional[str]
            Comma-separated list of Entry Display IDs.

        returning : typing.Optional[str]
            Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

            **Note:** "entries.days.notes" cannot be introspected with the returning parameter, and any sub fields will be ignored. E.g., "entries.days.notes.text" will return the same model as "entries.days.notes".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntriesPaginatedList]
            Returns a list of entries. Entries are notes that users can take. They're organized by "days" (which are user-configurable) and modeled within each day as a list of "notes." Each note has a type - the simplest is a "text" type, but lists, tables, and external files are also supported.

            *Note:* the current Entry resource has a few limitations:
            - Formatting information is not yet supported. Header formatting, bolding, and other stylistic information is not presented.
            - Data in tables is presented as text always - numeric values will need to be parsed into floats or integers, as appropriate.

            Note: Data in Results tables are not accessible through this API call. Results table data can be called through the Results API calls.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "entries",
            method="GET",
            params={
                "pageSize": page_size,
                "nextToken": next_token,
                "sort": sort,
                "modifiedAt": modified_at,
                "name": name,
                "projectId": project_id,
                "archiveReason": archive_reason,
                "reviewStatus": review_status,
                "mentionedIn": mentioned_in,
                "mentions": mentions,
                "ids": ids,
                "schemaId": schema_id,
                "names.anyOf": names_any_of,
                "names.anyOf.caseSensitive": names_any_of_case_sensitive,
                "assignedReviewerIds.anyOf": assigned_reviewer_ids_any_of,
                "creatorIds": creator_ids,
                "authorIds.anyOf": author_ids_any_of,
                "displayIds": display_ids,
                "returning": returning,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntriesPaginatedList,
                    parse_obj_as(
                        type_=EntriesPaginatedList,
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

    async def create_entry_with_attachments(
        self,
        *,
        folder_id: str,
        name: str,
        review_record: typing.Optional[EntryCreateAttachmentsReviewRecord] = OMIT,
        author_ids: typing.Optional[EntryCreateAuthorIds] = OMIT,
        custom_fields: typing.Optional[CustomFields] = OMIT,
        entry_template_id: typing.Optional[str] = OMIT,
        fields: typing.Optional[Fields] = OMIT,
        initial_tables: typing.Optional[typing.Sequence[InitialTable]] = OMIT,
        schema_id: typing.Optional[str] = OMIT,
        attachment_text: typing.Optional[typing.Any] = OMIT,
        attachments: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AsyncTaskLink]:
        """
        Create a notebook entry with optional attachments. Attachments will be placed into the entry body in the order they are specified.

        Parameters
        ----------
        folder_id : str
            ID of the folder that will contain the entry

        name : str
            Name of the entry

        review_record : typing.Optional[EntryCreateAttachmentsReviewRecord]

        author_ids : typing.Optional[EntryCreateAuthorIds]

        custom_fields : typing.Optional[CustomFields]
            Custom fields to add to the entry

        entry_template_id : typing.Optional[str]
            ID of the template to clone the entry from

        fields : typing.Optional[Fields]
            Fields to set on the entry. Must correspond with the schema's field definitions.

        initial_tables : typing.Optional[typing.Sequence[InitialTable]]
            An array of table API IDs and blob id pairs to seed tables from the template while creating the entry. The entryTemplateId parameter must be set to use this parameter. The table API IDs should be the API Identifiers of the tables in the given template.
            - If a template table has one row, the values in that row act as default values for cloned entries.
            - If a template table has multiple rows, there is no default value and those rows are added to the cloned entry along with the provided csv data.
            - If a table has default values, they will be populated in any respective undefined columns in the csv data.
            - If a table has no default values, undefined columns from csv data will be empty.
            - If no csv data is provided for a table, the table in the entry will be populated with whatever values are in the respective template table.

        schema_id : typing.Optional[str]
            ID of the entry's schema

        attachment_text : typing.Optional[typing.Any]
            Text to include in the entry before the attachments. If not provided, the text will be "File attachments are listed below:"

        attachments : typing.Optional[typing.Sequence[str]]
            An array of IDs representing Blob objects in Benchling to be attached to the entry.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AsyncTaskLink]
            Accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            "entries",
            method="POST",
            json={
                "reviewRecord": convert_and_respect_annotation_metadata(
                    object_=review_record, annotation=EntryCreateAttachmentsReviewRecord, direction="write"
                ),
                "authorIds": convert_and_respect_annotation_metadata(
                    object_=author_ids, annotation=EntryCreateAuthorIds, direction="write"
                ),
                "customFields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=CustomFields, direction="write"
                ),
                "entryTemplateId": entry_template_id,
                "fields": convert_and_respect_annotation_metadata(object_=fields, annotation=Fields, direction="write"),
                "folderId": folder_id,
                "initialTables": convert_and_respect_annotation_metadata(
                    object_=initial_tables, annotation=typing.Sequence[InitialTable], direction="write"
                ),
                "name": name,
                "schemaId": schema_id,
                "attachmentText": attachment_text,
                "attachments": attachments,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AsyncTaskLink,
                    parse_obj_as(
                        type_=AsyncTaskLink,
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

    async def get_entry(
        self,
        entry_id: str,
        *,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntryById]:
        """
        Get a notebook entry by ID

        Parameters
        ----------
        entry_id : str
            ID of the entry

        returning : typing.Optional[str]
            Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

            **Note:** "days.notes" cannot be introspected with the returning parameter, and any sub fields will be ignored. E.g., "days.notes.text" will return the same model as "days.notes".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntryById]
            Returns a single entry. Entries are notes that users can take. They're organized by "days" (which are user-configurable) and modeled within each day as a list of "notes." Each note has a type - the simplest is a "text" type, but lists, tables, and external files are also supported.

            *Note:* the current Entry resource has a few limitations:
            - Formatting information is not yet supported. Header formatting, bolding, and other stylistic information is not presented.
            - Data in tables is presented as text always - numeric values will need to be parsed into floats or integers, as appropriate.

            Note: Data in Results tables are not accessible through this API call. Results table data can be called through the Results API calls.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entries/{encode_path_param(entry_id)}",
            method="GET",
            params={
                "returning": returning,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntryById,
                    parse_obj_as(
                        type_=EntryById,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def bulk_create_entries(
        self,
        *,
        entry_datas: typing.Optional[typing.Sequence[EntryCreateAttachments]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AsyncTaskLink]:
        """
        Bulk create notebook entries with optional attachments. Limit of 100 Entries per request. Attachments will be placed into the entry body in the order they are specified.

        Parameters
        ----------
        entry_datas : typing.Optional[typing.Sequence[EntryCreateAttachments]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AsyncTaskLink]
            Accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            "entries:bulk-create",
            method="POST",
            json={
                "entryDatas": convert_and_respect_annotation_metadata(
                    object_=entry_datas, annotation=typing.Sequence[EntryCreateAttachments], direction="write"
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
                    AsyncTaskLink,
                    parse_obj_as(
                        type_=AsyncTaskLink,
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

    async def get_template_entry(
        self, entry_template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EntryTemplate]:
        """
        Get a notebook template entry by ID

        Parameters
        ----------
        entry_template_id : str
            ID of the entry template

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntryTemplate]
            Returns a single entry template. Entry templates are templates that users can base new notebook entries off of.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entry-templates/{encode_path_param(entry_template_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntryTemplate,
                    parse_obj_as(
                        type_=EntryTemplate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
