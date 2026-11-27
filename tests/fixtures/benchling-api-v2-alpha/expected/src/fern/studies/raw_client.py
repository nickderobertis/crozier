

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
from .types.list_studies_request_sort import ListStudiesRequestSort
from .types.studies_archive_reason import StudiesArchiveReason
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawStudiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[StudiesPaginatedList]:
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
        HttpResponse[StudiesPaginatedList]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "studies",
            method="GET",
            params={
                "pageSize": page_size,
                "nextToken": next_token,
                "sort": sort,
                "createdAt.lt": created_at_lt,
                "createdAt.gt": created_at_gt,
                "createdAt.lte": created_at_lte,
                "createdAt.gte": created_at_gte,
                "modifiedAt.lt": modified_at_lt,
                "modifiedAt.gt": modified_at_gt,
                "modifiedAt.lte": modified_at_lte,
                "modifiedAt.gte": modified_at_gte,
                "name": name,
                "nameIncludes": name_includes,
                "folderId": folder_id,
                "projectId": project_id,
                "schemaId": schema_id,
                "archiveReason": archive_reason,
                "ids": ids,
                "names.anyOf": names_any_of,
                "names.anyOf.caseSensitive": names_any_of_case_sensitive,
                "authorIds.anyOf": author_ids_any_of,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StudiesPaginatedList,
                    parse_obj_as(
                        type_=StudiesPaginatedList,
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
    ) -> HttpResponse[Study]:
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
        HttpResponse[Study]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "studies",
            method="POST",
            json={
                "description": description,
                "entryInformation": convert_and_respect_annotation_metadata(
                    object_=entry_information, annotation=EntryCreate, direction="write"
                ),
                "fields": convert_and_respect_annotation_metadata(object_=fields, annotation=Fields, direction="write"),
                "folderId": folder_id,
                "name": name,
                "studySchemaId": study_schema_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Study,
                    parse_obj_as(
                        type_=Study,
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

    def get_study(
        self, study_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Study]:
        """
        Get a Study

        Parameters
        ----------
        study_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Study]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"studies/{encode_path_param(study_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Study,
                    parse_obj_as(
                        type_=Study,
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
    ) -> HttpResponse[Study]:
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
        HttpResponse[Study]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"studies/{encode_path_param(study_id)}",
            method="PATCH",
            json={
                "archiveReason": archive_reason,
                "description": description,
                "fields": convert_and_respect_annotation_metadata(object_=fields, annotation=Fields, direction="write"),
                "folderId": folder_id,
                "id": id,
                "isArchived": is_archived,
                "name": name,
                "phase": phase,
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
                    Study,
                    parse_obj_as(
                        type_=Study,
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

    def get_study_items(
        self, study_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StudyItems]:
        """
        Get items for a Study

        Parameters
        ----------
        study_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StudyItems]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"studies/{encode_path_param(study_id)}/items",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StudyItems,
                    parse_obj_as(
                        type_=StudyItems,
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

    def add_study_items(
        self,
        study_id: str,
        *,
        item_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StudyItemsCreateResponse]:
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
        HttpResponse[StudyItemsCreateResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"studies/{encode_path_param(study_id)}/items:bulk-add",
            method="POST",
            json={
                "itemIds": item_ids,
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
                    StudyItemsCreateResponse,
                    parse_obj_as(
                        type_=StudyItemsCreateResponse,
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

    def remove_study_items(
        self,
        study_id: str,
        *,
        item_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmptyObject]:
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
        HttpResponse[EmptyObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"studies/{encode_path_param(study_id)}/items:bulk-remove",
            method="POST",
            json={
                "itemIds": item_ids,
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
                    EmptyObject,
                    parse_obj_as(
                        type_=EmptyObject,
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

    def archive_studies(
        self,
        *,
        reason: StudiesArchiveReason,
        study_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StudiesArchivalChange]:
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
        HttpResponse[StudiesArchivalChange]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "studies:archive",
            method="POST",
            json={
                "reason": reason,
                "studyIds": study_ids,
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
                    StudiesArchivalChange,
                    parse_obj_as(
                        type_=StudiesArchivalChange,
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

    def bulk_create_studies(
        self,
        *,
        studies: typing.Optional[typing.Sequence[StudyCreate]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StudiesBulkCreateResponse]:
        """
        Create one or more Studies

        Parameters
        ----------
        studies : typing.Optional[typing.Sequence[StudyCreate]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StudiesBulkCreateResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "studies:bulk-create",
            method="POST",
            json={
                "studies": convert_and_respect_annotation_metadata(
                    object_=studies, annotation=typing.Sequence[StudyCreate], direction="write"
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
                    StudiesBulkCreateResponse,
                    parse_obj_as(
                        type_=StudiesBulkCreateResponse,
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

    def bulk_update_studies(
        self,
        *,
        studies: typing.Optional[typing.Sequence[StudyUpdate]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StudiesBulkUpdateResponse]:
        """
        Bulk Update Studies

        Parameters
        ----------
        studies : typing.Optional[typing.Sequence[StudyUpdate]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StudiesBulkUpdateResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "studies:bulk-update",
            method="POST",
            json={
                "studies": convert_and_respect_annotation_metadata(
                    object_=studies, annotation=typing.Sequence[StudyUpdate], direction="write"
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
                    StudiesBulkUpdateResponse,
                    parse_obj_as(
                        type_=StudiesBulkUpdateResponse,
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

    def unarchive_studies(
        self, *, study_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StudiesArchivalChange]:
        """
        Unarchive Studies

        Parameters
        ----------
        study_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StudiesArchivalChange]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "studies:unarchive",
            method="POST",
            json={
                "studyIds": study_ids,
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
                    StudiesArchivalChange,
                    parse_obj_as(
                        type_=StudiesArchivalChange,
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


class AsyncRawStudiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[StudiesPaginatedList]:
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
        AsyncHttpResponse[StudiesPaginatedList]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "studies",
            method="GET",
            params={
                "pageSize": page_size,
                "nextToken": next_token,
                "sort": sort,
                "createdAt.lt": created_at_lt,
                "createdAt.gt": created_at_gt,
                "createdAt.lte": created_at_lte,
                "createdAt.gte": created_at_gte,
                "modifiedAt.lt": modified_at_lt,
                "modifiedAt.gt": modified_at_gt,
                "modifiedAt.lte": modified_at_lte,
                "modifiedAt.gte": modified_at_gte,
                "name": name,
                "nameIncludes": name_includes,
                "folderId": folder_id,
                "projectId": project_id,
                "schemaId": schema_id,
                "archiveReason": archive_reason,
                "ids": ids,
                "names.anyOf": names_any_of,
                "names.anyOf.caseSensitive": names_any_of_case_sensitive,
                "authorIds.anyOf": author_ids_any_of,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StudiesPaginatedList,
                    parse_obj_as(
                        type_=StudiesPaginatedList,
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
    ) -> AsyncHttpResponse[Study]:
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
        AsyncHttpResponse[Study]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "studies",
            method="POST",
            json={
                "description": description,
                "entryInformation": convert_and_respect_annotation_metadata(
                    object_=entry_information, annotation=EntryCreate, direction="write"
                ),
                "fields": convert_and_respect_annotation_metadata(object_=fields, annotation=Fields, direction="write"),
                "folderId": folder_id,
                "name": name,
                "studySchemaId": study_schema_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Study,
                    parse_obj_as(
                        type_=Study,
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

    async def get_study(
        self, study_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Study]:
        """
        Get a Study

        Parameters
        ----------
        study_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Study]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"studies/{encode_path_param(study_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Study,
                    parse_obj_as(
                        type_=Study,
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
    ) -> AsyncHttpResponse[Study]:
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
        AsyncHttpResponse[Study]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"studies/{encode_path_param(study_id)}",
            method="PATCH",
            json={
                "archiveReason": archive_reason,
                "description": description,
                "fields": convert_and_respect_annotation_metadata(object_=fields, annotation=Fields, direction="write"),
                "folderId": folder_id,
                "id": id,
                "isArchived": is_archived,
                "name": name,
                "phase": phase,
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
                    Study,
                    parse_obj_as(
                        type_=Study,
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

    async def get_study_items(
        self, study_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StudyItems]:
        """
        Get items for a Study

        Parameters
        ----------
        study_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StudyItems]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"studies/{encode_path_param(study_id)}/items",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StudyItems,
                    parse_obj_as(
                        type_=StudyItems,
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

    async def add_study_items(
        self,
        study_id: str,
        *,
        item_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StudyItemsCreateResponse]:
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
        AsyncHttpResponse[StudyItemsCreateResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"studies/{encode_path_param(study_id)}/items:bulk-add",
            method="POST",
            json={
                "itemIds": item_ids,
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
                    StudyItemsCreateResponse,
                    parse_obj_as(
                        type_=StudyItemsCreateResponse,
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

    async def remove_study_items(
        self,
        study_id: str,
        *,
        item_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmptyObject]:
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
        AsyncHttpResponse[EmptyObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"studies/{encode_path_param(study_id)}/items:bulk-remove",
            method="POST",
            json={
                "itemIds": item_ids,
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
                    EmptyObject,
                    parse_obj_as(
                        type_=EmptyObject,
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

    async def archive_studies(
        self,
        *,
        reason: StudiesArchiveReason,
        study_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StudiesArchivalChange]:
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
        AsyncHttpResponse[StudiesArchivalChange]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "studies:archive",
            method="POST",
            json={
                "reason": reason,
                "studyIds": study_ids,
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
                    StudiesArchivalChange,
                    parse_obj_as(
                        type_=StudiesArchivalChange,
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

    async def bulk_create_studies(
        self,
        *,
        studies: typing.Optional[typing.Sequence[StudyCreate]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StudiesBulkCreateResponse]:
        """
        Create one or more Studies

        Parameters
        ----------
        studies : typing.Optional[typing.Sequence[StudyCreate]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StudiesBulkCreateResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "studies:bulk-create",
            method="POST",
            json={
                "studies": convert_and_respect_annotation_metadata(
                    object_=studies, annotation=typing.Sequence[StudyCreate], direction="write"
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
                    StudiesBulkCreateResponse,
                    parse_obj_as(
                        type_=StudiesBulkCreateResponse,
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

    async def bulk_update_studies(
        self,
        *,
        studies: typing.Optional[typing.Sequence[StudyUpdate]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StudiesBulkUpdateResponse]:
        """
        Bulk Update Studies

        Parameters
        ----------
        studies : typing.Optional[typing.Sequence[StudyUpdate]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StudiesBulkUpdateResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "studies:bulk-update",
            method="POST",
            json={
                "studies": convert_and_respect_annotation_metadata(
                    object_=studies, annotation=typing.Sequence[StudyUpdate], direction="write"
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
                    StudiesBulkUpdateResponse,
                    parse_obj_as(
                        type_=StudiesBulkUpdateResponse,
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

    async def unarchive_studies(
        self, *, study_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StudiesArchivalChange]:
        """
        Unarchive Studies

        Parameters
        ----------
        study_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StudiesArchivalChange]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "studies:unarchive",
            method="POST",
            json={
                "studyIds": study_ids,
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
                    StudiesArchivalChange,
                    parse_obj_as(
                        type_=StudiesArchivalChange,
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
