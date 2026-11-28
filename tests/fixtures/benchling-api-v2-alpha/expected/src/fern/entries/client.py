

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawEntriesClient, RawEntriesClient
from .types.list_entries_request_review_status import ListEntriesRequestReviewStatus
from .types.list_entries_request_sort import ListEntriesRequestSort


OMIT = typing.cast(typing.Any, ...)


class EntriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEntriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEntriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEntriesClient
        """
        return self._raw_client

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
    ) -> EntriesPaginatedList:
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
        EntriesPaginatedList
            Returns a list of entries. Entries are notes that users can take. They're organized by "days" (which are user-configurable) and modeled within each day as a list of "notes." Each note has a type - the simplest is a "text" type, but lists, tables, and external files are also supported.

            *Note:* the current Entry resource has a few limitations:
            - Formatting information is not yet supported. Header formatting, bolding, and other stylistic information is not presented.
            - Data in tables is presented as text always - numeric values will need to be parsed into floats or integers, as appropriate.

            Note: Data in Results tables are not accessible through this API call. Results table data can be called through the Results API calls.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.entries.list_entries(
            modified_at="> 2022-03-01 AND < 2022-04-01",
            archive_reason="NOT_ARCHIVED",
            names_any_of="MyName1,MyName2",
            names_any_of_case_sensitive="MyName1,MyName2",
            assigned_reviewer_ids_any_of="ent_a0SApq3z,ent_SdUvia1v",
            creator_ids="ent_a0SApq3z",
            author_ids_any_of="ent_a0SApq3z,ent_b4AApz9b",
            display_ids="VPR001,VPR002",
            returning="entries.id, entries.name, entries.modifiedAt",
        )
        """
        _response = self._raw_client.list_entries(
            page_size=page_size,
            next_token=next_token,
            sort=sort,
            modified_at=modified_at,
            name=name,
            project_id=project_id,
            archive_reason=archive_reason,
            review_status=review_status,
            mentioned_in=mentioned_in,
            mentions=mentions,
            ids=ids,
            schema_id=schema_id,
            names_any_of=names_any_of,
            names_any_of_case_sensitive=names_any_of_case_sensitive,
            assigned_reviewer_ids_any_of=assigned_reviewer_ids_any_of,
            creator_ids=creator_ids,
            author_ids_any_of=author_ids_any_of,
            display_ids=display_ids,
            returning=returning,
            request_options=request_options,
        )
        return _response.data

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
    ) -> AsyncTaskLink:
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
        AsyncTaskLink
            Accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.entries.create_entry_with_attachments(
            folder_id="folderId",
            name="name",
        )
        """
        _response = self._raw_client.create_entry_with_attachments(
            folder_id=folder_id,
            name=name,
            review_record=review_record,
            author_ids=author_ids,
            custom_fields=custom_fields,
            entry_template_id=entry_template_id,
            fields=fields,
            initial_tables=initial_tables,
            schema_id=schema_id,
            attachment_text=attachment_text,
            attachments=attachments,
            request_options=request_options,
        )
        return _response.data

    def get_entry(
        self,
        entry_id: str,
        *,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntryById:
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
        EntryById
            Returns a single entry. Entries are notes that users can take. They're organized by "days" (which are user-configurable) and modeled within each day as a list of "notes." Each note has a type - the simplest is a "text" type, but lists, tables, and external files are also supported.

            *Note:* the current Entry resource has a few limitations:
            - Formatting information is not yet supported. Header formatting, bolding, and other stylistic information is not presented.
            - Data in tables is presented as text always - numeric values will need to be parsed into floats or integers, as appropriate.

            Note: Data in Results tables are not accessible through this API call. Results table data can be called through the Results API calls.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.entries.get_entry(
            entry_id="entry_id",
            returning="id, name, modifiedAt",
        )
        """
        _response = self._raw_client.get_entry(entry_id, returning=returning, request_options=request_options)
        return _response.data

    def bulk_create_entries(
        self,
        *,
        entry_datas: typing.Optional[typing.Sequence[EntryCreateAttachments]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncTaskLink:
        """
        Bulk create notebook entries with optional attachments. Limit of 100 Entries per request. Attachments will be placed into the entry body in the order they are specified.

        Parameters
        ----------
        entry_datas : typing.Optional[typing.Sequence[EntryCreateAttachments]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncTaskLink
            Accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.entries.bulk_create_entries()
        """
        _response = self._raw_client.bulk_create_entries(entry_datas=entry_datas, request_options=request_options)
        return _response.data

    def get_template_entry(
        self, entry_template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntryTemplate:
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
        EntryTemplate
            Returns a single entry template. Entry templates are templates that users can base new notebook entries off of.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.entries.get_template_entry(
            entry_template_id="entry_template_id",
        )
        """
        _response = self._raw_client.get_template_entry(entry_template_id, request_options=request_options)
        return _response.data


class AsyncEntriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEntriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEntriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEntriesClient
        """
        return self._raw_client

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
    ) -> EntriesPaginatedList:
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
        EntriesPaginatedList
            Returns a list of entries. Entries are notes that users can take. They're organized by "days" (which are user-configurable) and modeled within each day as a list of "notes." Each note has a type - the simplest is a "text" type, but lists, tables, and external files are also supported.

            *Note:* the current Entry resource has a few limitations:
            - Formatting information is not yet supported. Header formatting, bolding, and other stylistic information is not presented.
            - Data in tables is presented as text always - numeric values will need to be parsed into floats or integers, as appropriate.

            Note: Data in Results tables are not accessible through this API call. Results table data can be called through the Results API calls.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.entries.list_entries(
                modified_at="> 2022-03-01 AND < 2022-04-01",
                archive_reason="NOT_ARCHIVED",
                names_any_of="MyName1,MyName2",
                names_any_of_case_sensitive="MyName1,MyName2",
                assigned_reviewer_ids_any_of="ent_a0SApq3z,ent_SdUvia1v",
                creator_ids="ent_a0SApq3z",
                author_ids_any_of="ent_a0SApq3z,ent_b4AApz9b",
                display_ids="VPR001,VPR002",
                returning="entries.id, entries.name, entries.modifiedAt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_entries(
            page_size=page_size,
            next_token=next_token,
            sort=sort,
            modified_at=modified_at,
            name=name,
            project_id=project_id,
            archive_reason=archive_reason,
            review_status=review_status,
            mentioned_in=mentioned_in,
            mentions=mentions,
            ids=ids,
            schema_id=schema_id,
            names_any_of=names_any_of,
            names_any_of_case_sensitive=names_any_of_case_sensitive,
            assigned_reviewer_ids_any_of=assigned_reviewer_ids_any_of,
            creator_ids=creator_ids,
            author_ids_any_of=author_ids_any_of,
            display_ids=display_ids,
            returning=returning,
            request_options=request_options,
        )
        return _response.data

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
    ) -> AsyncTaskLink:
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
        AsyncTaskLink
            Accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.entries.create_entry_with_attachments(
                folder_id="folderId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_entry_with_attachments(
            folder_id=folder_id,
            name=name,
            review_record=review_record,
            author_ids=author_ids,
            custom_fields=custom_fields,
            entry_template_id=entry_template_id,
            fields=fields,
            initial_tables=initial_tables,
            schema_id=schema_id,
            attachment_text=attachment_text,
            attachments=attachments,
            request_options=request_options,
        )
        return _response.data

    async def get_entry(
        self,
        entry_id: str,
        *,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntryById:
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
        EntryById
            Returns a single entry. Entries are notes that users can take. They're organized by "days" (which are user-configurable) and modeled within each day as a list of "notes." Each note has a type - the simplest is a "text" type, but lists, tables, and external files are also supported.

            *Note:* the current Entry resource has a few limitations:
            - Formatting information is not yet supported. Header formatting, bolding, and other stylistic information is not presented.
            - Data in tables is presented as text always - numeric values will need to be parsed into floats or integers, as appropriate.

            Note: Data in Results tables are not accessible through this API call. Results table data can be called through the Results API calls.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.entries.get_entry(
                entry_id="entry_id",
                returning="id, name, modifiedAt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entry(entry_id, returning=returning, request_options=request_options)
        return _response.data

    async def bulk_create_entries(
        self,
        *,
        entry_datas: typing.Optional[typing.Sequence[EntryCreateAttachments]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncTaskLink:
        """
        Bulk create notebook entries with optional attachments. Limit of 100 Entries per request. Attachments will be placed into the entry body in the order they are specified.

        Parameters
        ----------
        entry_datas : typing.Optional[typing.Sequence[EntryCreateAttachments]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncTaskLink
            Accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.entries.bulk_create_entries()


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_create_entries(entry_datas=entry_datas, request_options=request_options)
        return _response.data

    async def get_template_entry(
        self, entry_template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntryTemplate:
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
        EntryTemplate
            Returns a single entry template. Entry templates are templates that users can base new notebook entries off of.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.entries.get_template_entry(
                entry_template_id="entry_template_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_template_entry(entry_template_id, request_options=request_options)
        return _response.data
