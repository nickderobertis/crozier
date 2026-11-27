

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.empty_object import EmptyObject
from ..types.entry_create import EntryCreate
from ..types.fields import Fields
from ..types.studies_archival_change import StudiesArchivalChange
from ..types.studies_bulk_create_response import StudiesBulkCreateResponse
from ..types.studies_bulk_update_response import StudiesBulkUpdateResponse
from ..types.studies_paginated_list import StudiesPaginatedList
from ..types.study import Study
from ..types.study_create import StudyCreate
from ..types.study_items import StudyItems
from ..types.study_items_create_response import StudyItemsCreateResponse
from ..types.study_update import StudyUpdate
from ..types.study_update_phase import StudyUpdatePhase
from .raw_client import AsyncRawStudiesClient, RawStudiesClient
from .types.list_studies_request_sort import ListStudiesRequestSort
from .types.studies_archive_reason import StudiesArchiveReason


OMIT = typing.cast(typing.Any, ...)


class StudiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStudiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStudiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStudiesClient
        """
        return self._raw_client

    def list_studies(
        self,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListStudiesRequestSort] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        modified_at_lt: typing.Optional[str] = None,
        modified_at_gt: typing.Optional[str] = None,
        modified_at_lte: typing.Optional[str] = None,
        modified_at_gte: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        name_includes: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        schema_id: typing.Optional[str] = None,
        archive_reason: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        names_any_of: typing.Optional[str] = None,
        names_any_of_case_sensitive: typing.Optional[str] = None,
        author_ids_any_of: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StudiesPaginatedList:
        """
        List Studies

        Parameters
        ----------
        page_size : typing.Optional[int]
            Number of results to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        sort : typing.Optional[ListStudiesRequestSort]
            Method by which to order search results. Valid sorts are modifiedAt (modified time, most recent first) and name (entity name, alphabetical). Optionally add :asc or :desc to specify ascending or descending order.

        created_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.

        created_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.

        created_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or before the specified time. e.g. <= 2017-04-30.

        created_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or after the specified time. e.g. >= 2017-04-30.

        modified_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.

        modified_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.

        modified_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.

        modified_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.

        name : typing.Optional[str]
            Name of a Study. Restricts results to those with the specified name, alias, or entity registry ID.

        name_includes : typing.Optional[str]
            Name substring of a Study. Restricts results to those with names that include the provided substring.

        folder_id : typing.Optional[str]
            ID of a folder. Restricts results to those in the folder.

        project_id : typing.Optional[str]
            ID of a project. Restricts results to those in the project.

        schema_id : typing.Optional[str]
            ID of a schema. Restricts results to those of the specified schema.

        archive_reason : typing.Optional[str]
            Archive reason. Restricts results to those with the specified archive reason. Use “NOT_ARCHIVED” to filter for unarchived Studies. Use "ANY_ARCHIVED" to filter for archived Molecules regardless of reason. Use "ANY_ARCHIVED_OR_NOT_ARCHIVED" to return items for both archived and unarchived.

        ids : typing.Optional[str]
            Comma-separated list of ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.

        names_any_of : typing.Optional[str]
            Comma-separated list of names. Maximum of 100. Restricts results to those that match any of the specified names.

        names_any_of_case_sensitive : typing.Optional[str]
            Comma-separated list of app names. Maximum of 100. Restricts results to those that match any of the specified names, case sensitive.

        author_ids_any_of : typing.Optional[str]
            Comma separated list of user or app IDs. Maximum of 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudiesPaginatedList
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.studies.list_studies(
            archive_reason="ANY_ARCHIVED",
            ids="stdy_yWs5X7lv,stdy_RhYGVnHF",
            names_any_of="MyName1,MyName2",
            names_any_of_case_sensitive="MyName1,MyName2",
            author_ids_any_of="ent_a0SApq3z,ent_b4AApz9b",
        )
        """
        _response = self._raw_client.list_studies(
            page_size=page_size,
            next_token=next_token,
            sort=sort,
            created_at_lt=created_at_lt,
            created_at_gt=created_at_gt,
            created_at_lte=created_at_lte,
            created_at_gte=created_at_gte,
            modified_at_lt=modified_at_lt,
            modified_at_gt=modified_at_gt,
            modified_at_lte=modified_at_lte,
            modified_at_gte=modified_at_gte,
            name=name,
            name_includes=name_includes,
            folder_id=folder_id,
            project_id=project_id,
            schema_id=schema_id,
            archive_reason=archive_reason,
            ids=ids,
            names_any_of=names_any_of,
            names_any_of_case_sensitive=names_any_of_case_sensitive,
            author_ids_any_of=author_ids_any_of,
            request_options=request_options,
        )
        return _response.data

    def create_study(
        self,
        *,
        entry_information: EntryCreate,
        fields: Fields,
        folder_id: str,
        name: str,
        study_schema_id: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Study:
        """
        Create a Study.

        Parameters
        ----------
        entry_information : EntryCreate

        fields : Fields

        folder_id : str
            ID of the folder that contains the Study.

        name : str
            Name of the Study.

        study_schema_id : str
            The ID of the Study's schema.

        description : typing.Optional[str]
            The description of the Study.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Study
            Created

        Examples
        --------
        from fern import EntryCreate, FernApi, Field

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.studies.create_study(
            entry_information=EntryCreate(
                folder_id="folderId",
                name="name",
            ),
            fields={"key": Field()},
            folder_id="folderId",
            name="name",
            study_schema_id="studySchemaId",
        )
        """
        _response = self._raw_client.create_study(
            entry_information=entry_information,
            fields=fields,
            folder_id=folder_id,
            name=name,
            study_schema_id=study_schema_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def get_study(self, study_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Study:
        """
        Get a Study

        Parameters
        ----------
        study_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Study
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.studies.get_study(
            study_id="study_id",
        )
        """
        _response = self._raw_client.get_study(study_id, request_options=request_options)
        return _response.data

    def update_study(
        self,
        study_id: str,
        *,
        archive_reason: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        fields: typing.Optional[Fields] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        phase: typing.Optional[StudyUpdatePhase] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Study:
        """
        Update a Study

        Parameters
        ----------
        study_id : str
            The ID of the study

        archive_reason : typing.Optional[str]

        description : typing.Optional[str]
            The description of the Study.

        fields : typing.Optional[Fields]

        folder_id : typing.Optional[str]
            ID of the folder that contains the Study.

        id : typing.Optional[str]

        is_archived : typing.Optional[bool]

        name : typing.Optional[str]
            Name of the Study.

        phase : typing.Optional[StudyUpdatePhase]
            The phase of the Study.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Study
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.studies.update_study(
            study_id="stdy_OnnsW08k",
        )
        """
        _response = self._raw_client.update_study(
            study_id,
            archive_reason=archive_reason,
            description=description,
            fields=fields,
            folder_id=folder_id,
            id=id,
            is_archived=is_archived,
            name=name,
            phase=phase,
            request_options=request_options,
        )
        return _response.data

    def get_study_items(self, study_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> StudyItems:
        """
        Get items for a Study

        Parameters
        ----------
        study_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudyItems
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.studies.get_study_items(
            study_id="study_id",
        )
        """
        _response = self._raw_client.get_study_items(study_id, request_options=request_options)
        return _response.data

    def add_study_items(
        self,
        study_id: str,
        *,
        item_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StudyItemsCreateResponse:
        """
        Add one or more items to a Study

        Parameters
        ----------
        study_id : str

        item_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudyItemsCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.studies.add_study_items(
            study_id="study_id",
        )
        """
        _response = self._raw_client.add_study_items(study_id, item_ids=item_ids, request_options=request_options)
        return _response.data

    def remove_study_items(
        self,
        study_id: str,
        *,
        item_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmptyObject:
        """
        Remove one or more items from a Study

        Parameters
        ----------
        study_id : str

        item_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.studies.remove_study_items(
            study_id="study_id",
        )
        """
        _response = self._raw_client.remove_study_items(study_id, item_ids=item_ids, request_options=request_options)
        return _response.data

    def archive_studies(
        self,
        *,
        reason: StudiesArchiveReason,
        study_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StudiesArchivalChange:
        """
        Archive Studies

        Parameters
        ----------
        reason : StudiesArchiveReason
            The reason for archiving the provided Studies. Accepted reasons may differ based on tenant configuration.

        study_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudiesArchivalChange
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.studies.archive_studies(
            reason="Made in error",
            study_ids=["studyIds"],
        )
        """
        _response = self._raw_client.archive_studies(
            reason=reason, study_ids=study_ids, request_options=request_options
        )
        return _response.data

    def bulk_create_studies(
        self,
        *,
        studies: typing.Optional[typing.Sequence[StudyCreate]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StudiesBulkCreateResponse:
        """
        Create one or more Studies

        Parameters
        ----------
        studies : typing.Optional[typing.Sequence[StudyCreate]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudiesBulkCreateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.studies.bulk_create_studies()
        """
        _response = self._raw_client.bulk_create_studies(studies=studies, request_options=request_options)
        return _response.data

    def bulk_update_studies(
        self,
        *,
        studies: typing.Optional[typing.Sequence[StudyUpdate]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StudiesBulkUpdateResponse:
        """
        Bulk Update Studies

        Parameters
        ----------
        studies : typing.Optional[typing.Sequence[StudyUpdate]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudiesBulkUpdateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.studies.bulk_update_studies()
        """
        _response = self._raw_client.bulk_update_studies(studies=studies, request_options=request_options)
        return _response.data

    def unarchive_studies(
        self, *, study_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> StudiesArchivalChange:
        """
        Unarchive Studies

        Parameters
        ----------
        study_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudiesArchivalChange
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.studies.unarchive_studies(
            study_ids=["studyIds"],
        )
        """
        _response = self._raw_client.unarchive_studies(study_ids=study_ids, request_options=request_options)
        return _response.data


class AsyncStudiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStudiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStudiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStudiesClient
        """
        return self._raw_client

    async def list_studies(
        self,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListStudiesRequestSort] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        modified_at_lt: typing.Optional[str] = None,
        modified_at_gt: typing.Optional[str] = None,
        modified_at_lte: typing.Optional[str] = None,
        modified_at_gte: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        name_includes: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        schema_id: typing.Optional[str] = None,
        archive_reason: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        names_any_of: typing.Optional[str] = None,
        names_any_of_case_sensitive: typing.Optional[str] = None,
        author_ids_any_of: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StudiesPaginatedList:
        """
        List Studies

        Parameters
        ----------
        page_size : typing.Optional[int]
            Number of results to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        sort : typing.Optional[ListStudiesRequestSort]
            Method by which to order search results. Valid sorts are modifiedAt (modified time, most recent first) and name (entity name, alphabetical). Optionally add :asc or :desc to specify ascending or descending order.

        created_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created before the specified time. e.g. < 2017-04-30.

        created_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created after the specified time. e.g. > 2017-04-30.

        created_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or before the specified time. e.g. <= 2017-04-30.

        created_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those created on or after the specified time. e.g. >= 2017-04-30.

        modified_at_lt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified before the specified time. e.g. < 2017-04-30.

        modified_at_gt : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified after the specified time. e.g. > 2017-04-30.

        modified_at_lte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or before the specified time. e.g. <= 2017-04-30.

        modified_at_gte : typing.Optional[str]
            Datetime, in RFC 3339 format. Time zone defaults to UTC. Restricts results to those modified on or after the specified time. e.g. >= 2017-04-30.

        name : typing.Optional[str]
            Name of a Study. Restricts results to those with the specified name, alias, or entity registry ID.

        name_includes : typing.Optional[str]
            Name substring of a Study. Restricts results to those with names that include the provided substring.

        folder_id : typing.Optional[str]
            ID of a folder. Restricts results to those in the folder.

        project_id : typing.Optional[str]
            ID of a project. Restricts results to those in the project.

        schema_id : typing.Optional[str]
            ID of a schema. Restricts results to those of the specified schema.

        archive_reason : typing.Optional[str]
            Archive reason. Restricts results to those with the specified archive reason. Use “NOT_ARCHIVED” to filter for unarchived Studies. Use "ANY_ARCHIVED" to filter for archived Molecules regardless of reason. Use "ANY_ARCHIVED_OR_NOT_ARCHIVED" to return items for both archived and unarchived.

        ids : typing.Optional[str]
            Comma-separated list of ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.

        names_any_of : typing.Optional[str]
            Comma-separated list of names. Maximum of 100. Restricts results to those that match any of the specified names.

        names_any_of_case_sensitive : typing.Optional[str]
            Comma-separated list of app names. Maximum of 100. Restricts results to those that match any of the specified names, case sensitive.

        author_ids_any_of : typing.Optional[str]
            Comma separated list of user or app IDs. Maximum of 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudiesPaginatedList
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.studies.list_studies(
                archive_reason="ANY_ARCHIVED",
                ids="stdy_yWs5X7lv,stdy_RhYGVnHF",
                names_any_of="MyName1,MyName2",
                names_any_of_case_sensitive="MyName1,MyName2",
                author_ids_any_of="ent_a0SApq3z,ent_b4AApz9b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_studies(
            page_size=page_size,
            next_token=next_token,
            sort=sort,
            created_at_lt=created_at_lt,
            created_at_gt=created_at_gt,
            created_at_lte=created_at_lte,
            created_at_gte=created_at_gte,
            modified_at_lt=modified_at_lt,
            modified_at_gt=modified_at_gt,
            modified_at_lte=modified_at_lte,
            modified_at_gte=modified_at_gte,
            name=name,
            name_includes=name_includes,
            folder_id=folder_id,
            project_id=project_id,
            schema_id=schema_id,
            archive_reason=archive_reason,
            ids=ids,
            names_any_of=names_any_of,
            names_any_of_case_sensitive=names_any_of_case_sensitive,
            author_ids_any_of=author_ids_any_of,
            request_options=request_options,
        )
        return _response.data

    async def create_study(
        self,
        *,
        entry_information: EntryCreate,
        fields: Fields,
        folder_id: str,
        name: str,
        study_schema_id: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Study:
        """
        Create a Study.

        Parameters
        ----------
        entry_information : EntryCreate

        fields : Fields

        folder_id : str
            ID of the folder that contains the Study.

        name : str
            Name of the Study.

        study_schema_id : str
            The ID of the Study's schema.

        description : typing.Optional[str]
            The description of the Study.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Study
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, EntryCreate, Field

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.studies.create_study(
                entry_information=EntryCreate(
                    folder_id="folderId",
                    name="name",
                ),
                fields={"key": Field()},
                folder_id="folderId",
                name="name",
                study_schema_id="studySchemaId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_study(
            entry_information=entry_information,
            fields=fields,
            folder_id=folder_id,
            name=name,
            study_schema_id=study_schema_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def get_study(self, study_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Study:
        """
        Get a Study

        Parameters
        ----------
        study_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Study
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.studies.get_study(
                study_id="study_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_study(study_id, request_options=request_options)
        return _response.data

    async def update_study(
        self,
        study_id: str,
        *,
        archive_reason: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        fields: typing.Optional[Fields] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        phase: typing.Optional[StudyUpdatePhase] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Study:
        """
        Update a Study

        Parameters
        ----------
        study_id : str
            The ID of the study

        archive_reason : typing.Optional[str]

        description : typing.Optional[str]
            The description of the Study.

        fields : typing.Optional[Fields]

        folder_id : typing.Optional[str]
            ID of the folder that contains the Study.

        id : typing.Optional[str]

        is_archived : typing.Optional[bool]

        name : typing.Optional[str]
            Name of the Study.

        phase : typing.Optional[StudyUpdatePhase]
            The phase of the Study.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Study
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.studies.update_study(
                study_id="stdy_OnnsW08k",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_study(
            study_id,
            archive_reason=archive_reason,
            description=description,
            fields=fields,
            folder_id=folder_id,
            id=id,
            is_archived=is_archived,
            name=name,
            phase=phase,
            request_options=request_options,
        )
        return _response.data

    async def get_study_items(
        self, study_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StudyItems:
        """
        Get items for a Study

        Parameters
        ----------
        study_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudyItems
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.studies.get_study_items(
                study_id="study_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_study_items(study_id, request_options=request_options)
        return _response.data

    async def add_study_items(
        self,
        study_id: str,
        *,
        item_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StudyItemsCreateResponse:
        """
        Add one or more items to a Study

        Parameters
        ----------
        study_id : str

        item_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudyItemsCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.studies.add_study_items(
                study_id="study_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_study_items(study_id, item_ids=item_ids, request_options=request_options)
        return _response.data

    async def remove_study_items(
        self,
        study_id: str,
        *,
        item_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmptyObject:
        """
        Remove one or more items from a Study

        Parameters
        ----------
        study_id : str

        item_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.studies.remove_study_items(
                study_id="study_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_study_items(
            study_id, item_ids=item_ids, request_options=request_options
        )
        return _response.data

    async def archive_studies(
        self,
        *,
        reason: StudiesArchiveReason,
        study_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StudiesArchivalChange:
        """
        Archive Studies

        Parameters
        ----------
        reason : StudiesArchiveReason
            The reason for archiving the provided Studies. Accepted reasons may differ based on tenant configuration.

        study_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudiesArchivalChange
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.studies.archive_studies(
                reason="Made in error",
                study_ids=["studyIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.archive_studies(
            reason=reason, study_ids=study_ids, request_options=request_options
        )
        return _response.data

    async def bulk_create_studies(
        self,
        *,
        studies: typing.Optional[typing.Sequence[StudyCreate]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StudiesBulkCreateResponse:
        """
        Create one or more Studies

        Parameters
        ----------
        studies : typing.Optional[typing.Sequence[StudyCreate]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudiesBulkCreateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.studies.bulk_create_studies()


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_create_studies(studies=studies, request_options=request_options)
        return _response.data

    async def bulk_update_studies(
        self,
        *,
        studies: typing.Optional[typing.Sequence[StudyUpdate]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StudiesBulkUpdateResponse:
        """
        Bulk Update Studies

        Parameters
        ----------
        studies : typing.Optional[typing.Sequence[StudyUpdate]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudiesBulkUpdateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.studies.bulk_update_studies()


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_update_studies(studies=studies, request_options=request_options)
        return _response.data

    async def unarchive_studies(
        self, *, study_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> StudiesArchivalChange:
        """
        Unarchive Studies

        Parameters
        ----------
        study_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StudiesArchivalChange
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.studies.unarchive_studies(
                study_ids=["studyIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unarchive_studies(study_ids=study_ids, request_options=request_options)
        return _response.data
