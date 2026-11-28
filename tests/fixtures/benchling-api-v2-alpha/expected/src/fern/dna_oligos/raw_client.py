

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
from ..types.async_task_link import AsyncTaskLink
from ..types.custom_fields import CustomFields
from ..types.dna_oligo_helm import DnaOligoHelm
from ..types.dna_oligos_paginated_list_helm import DnaOligosPaginatedListHelm
from ..types.fields import Fields
from ..types.naming_strategy import NamingStrategy
from ..types.oligo_create_helm import OligoCreateHelm
from ..types.schema_fields_query_param import SchemaFieldsQueryParam
from .types.list_dna_oligos_helm_request_sort import ListDnaOligosHelmRequestSort
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDnaOligosClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_dna_oligos_helm(
        self,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListDnaOligosHelmRequestSort] = None,
        modified_at: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        name_includes: typing.Optional[str] = None,
        bases: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        mentioned_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        project_id: typing.Optional[str] = None,
        registry_id: typing.Optional[str] = None,
        schema_id: typing.Optional[str] = None,
        schema_fields: typing.Optional[SchemaFieldsQueryParam] = None,
        archive_reason: typing.Optional[str] = None,
        mentions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ids: typing.Optional[str] = None,
        entity_registry_ids_any_of: typing.Optional[str] = None,
        names_any_of: typing.Optional[str] = None,
        names_any_of_case_sensitive: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DnaOligosPaginatedListHelm]:
        """
        List DNA Oligos with HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        page_size : typing.Optional[int]
            Number of results to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        sort : typing.Optional[ListDnaOligosHelmRequestSort]
            Method by which to order search results. Valid sorts are modifiedAt (modified time, most recent first) and name (entity name, alphabetical). Optionally add :asc or :desc to specify ascending or descending order.

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        name : typing.Optional[str]
            Name of a DNA Oligo. Restricts results to those with the specified name, alias, or entity registry ID.

        name_includes : typing.Optional[str]
            Name substring of a DNA Oligo. Restricts results to those with names, aliases, or entity registry IDs that include the provided substring.

        bases : typing.Optional[str]
            Full bases of the DNA Oligo. Restricts results to those with the specified bases, case-insensitive, allowing for circular or reverse complement matches. Does not allow partial matching or loose matching via degenerate bases.

        folder_id : typing.Optional[str]
            ID of a folder. Restricts results to those in the folder.

        mentioned_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of entry IDs. Restricts results to DNA Oligos mentioned in those entries.

        project_id : typing.Optional[str]
            ID of a project. Restricts results to those in the project.

        registry_id : typing.Optional[str]
            ID of a registry. Restricts results to those registered in this registry. Specifying "null" returns unregistered items.

        schema_id : typing.Optional[str]
            ID of a schema. Restricts results to those of the specified schema.

        schema_fields : typing.Optional[SchemaFieldsQueryParam]
            Schema field value. For Integer, Float, and Date type fields, supports the >= and <= operators. If present, the schemaId param must also be present. Restricts results to those with a field of whose value matches the filter.

        archive_reason : typing.Optional[str]
            Archive reason. Restricts results to those with the specified archive reason. Use “NOT_ARCHIVED” to filter for unarchived DNA Oligos.

        mentions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of item IDs. Restricts results to those that mention the given items in the description.

        ids : typing.Optional[str]
            Comma-separated list of ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.

        entity_registry_ids_any_of : typing.Optional[str]
            Comma-separated list of entity registry IDs. Restricts results to those that match any of the specified registry IDs.

        names_any_of : typing.Optional[str]
            Comma-separated list of names. Restricts results to those that match any of the specified names, aliases, or entity registry IDs, case insensitive.  Warning - this filter can be non-performant due to case insensitivity.

        names_any_of_case_sensitive : typing.Optional[str]
            Comma-separated list of names. Restricts results to those that match any of the specified names, aliases, or entity registry IDs, case sensitive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DnaOligosPaginatedListHelm]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "dna-oligos",
            method="GET",
            params={
                "pageSize": page_size,
                "nextToken": next_token,
                "sort": sort,
                "modifiedAt": modified_at,
                "name": name,
                "nameIncludes": name_includes,
                "bases": bases,
                "folderId": folder_id,
                "mentionedIn": ",".join(map(str, mentioned_in))
                if isinstance(mentioned_in, (list, tuple, set))
                else mentioned_in,
                "projectId": project_id,
                "registryId": registry_id,
                "schemaId": schema_id,
                "schemaFields": schema_fields,
                "archiveReason": archive_reason,
                "mentions": ",".join(map(str, mentions)) if isinstance(mentions, (list, tuple, set)) else mentions,
                "ids": ids,
                "entityRegistryIds.anyOf": entity_registry_ids_any_of,
                "names.anyOf": names_any_of,
                "names.anyOf.caseSensitive": names_any_of_case_sensitive,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DnaOligosPaginatedListHelm,
                    parse_obj_as(
                        type_=DnaOligosPaginatedListHelm,
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

    def create_dna_oligo_with_helm(
        self,
        *,
        name: str,
        helm: typing.Optional[str] = OMIT,
        aliases: typing.Optional[typing.Sequence[str]] = OMIT,
        author_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bases: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[CustomFields] = OMIT,
        fields: typing.Optional[Fields] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        schema_id: typing.Optional[str] = OMIT,
        entity_registry_id: typing.Optional[str] = OMIT,
        naming_strategy: typing.Optional[NamingStrategy] = OMIT,
        registry_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DnaOligoHelm]:
        """
        Create a DNA Oligo with optional HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        name : str
            Name of the Oligo.

        helm : typing.Optional[str]
            Representation of the oligo in HELM syntax, including any chemical modifications

        aliases : typing.Optional[typing.Sequence[str]]
            Aliases to add to the Oligo

        author_ids : typing.Optional[typing.Sequence[str]]
            IDs of users to set as the Oligo's authors.

        bases : typing.Optional[str]
            Base pairs of the oligo.

        custom_fields : typing.Optional[CustomFields]
            Custom fields to add to the Oligo. Every field should have its name as a key, mapping to an object with information about the value of the field.

        fields : typing.Optional[Fields]
            Fields to set on the Oligo. Must correspond with the schema's field definitions. Every field should have its name as a key, mapping to an object with information about the value of the field.

        folder_id : typing.Optional[str]
            ID of the folder containing the Oligo.

        schema_id : typing.Optional[str]
            ID of the oligo's schema.

        entity_registry_id : typing.Optional[str]
            Entity registry ID to set for the registered entity. Cannot specify both entityRegistryId and namingStrategy at the same time.

        naming_strategy : typing.Optional[NamingStrategy]

        registry_id : typing.Optional[str]
            Registry ID into which entity should be registered. this is the ID of the registry which was configured for a particular organization
            To get available registryIds, use the [/registries endpoint](#/Registry/listRegistries)

            Required in order for entities to be created directly in the registry.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DnaOligoHelm]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "dna-oligos",
            method="POST",
            json={
                "helm": helm,
                "aliases": aliases,
                "authorIds": author_ids,
                "bases": bases,
                "customFields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=CustomFields, direction="write"
                ),
                "fields": convert_and_respect_annotation_metadata(object_=fields, annotation=Fields, direction="write"),
                "folderId": folder_id,
                "name": name,
                "schemaId": schema_id,
                "entityRegistryId": entity_registry_id,
                "namingStrategy": naming_strategy,
                "registryId": registry_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DnaOligoHelm,
                    parse_obj_as(
                        type_=DnaOligoHelm,
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

    def get_dna_oligo_helm(
        self, oligo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DnaOligoHelm]:
        """
        Get a DNA Oligo with HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        oligo_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DnaOligoHelm]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dna-oligos/{encode_path_param(oligo_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DnaOligoHelm,
                    parse_obj_as(
                        type_=DnaOligoHelm,
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

    def update_dna_oligo_helm(
        self,
        oligo_id: str,
        *,
        helm: typing.Optional[str] = OMIT,
        aliases: typing.Optional[typing.Sequence[str]] = OMIT,
        author_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bases: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[CustomFields] = OMIT,
        fields: typing.Optional[Fields] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        schema_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DnaOligoHelm]:
        """
        Update a DNA Oligo with optional HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        oligo_id : str

        helm : typing.Optional[str]
            Representation of the oligo in HELM syntax, including any chemical modifications

        aliases : typing.Optional[typing.Sequence[str]]
            Aliases to add to the Oligo

        author_ids : typing.Optional[typing.Sequence[str]]
            IDs of users to set as the Oligo's authors.

        bases : typing.Optional[str]
            Base pairs of the oligo.

        custom_fields : typing.Optional[CustomFields]
            Custom fields to add to the Oligo. Every field should have its name as a key, mapping to an object with information about the value of the field.

        fields : typing.Optional[Fields]
            Fields to set on the Oligo. Must correspond with the schema's field definitions. Every field should have its name as a key, mapping to an object with information about the value of the field.

        folder_id : typing.Optional[str]
            ID of the folder containing the Oligo.

        name : typing.Optional[str]
            Name of the Oligo.

        schema_id : typing.Optional[str]
            ID of the oligo's schema.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DnaOligoHelm]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dna-oligos/{encode_path_param(oligo_id)}",
            method="PATCH",
            json={
                "helm": helm,
                "aliases": aliases,
                "authorIds": author_ids,
                "bases": bases,
                "customFields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=CustomFields, direction="write"
                ),
                "fields": convert_and_respect_annotation_metadata(object_=fields, annotation=Fields, direction="write"),
                "folderId": folder_id,
                "name": name,
                "schemaId": schema_id,
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
                    DnaOligoHelm,
                    parse_obj_as(
                        type_=DnaOligoHelm,
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

    def bulk_create_dna_oligos_helm(
        self,
        *,
        dna_oligos: typing.Optional[typing.Sequence[OligoCreateHelm]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncTaskLink]:
        """
        Bulk Create DNA Oligos with optional HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        dna_oligos : typing.Optional[typing.Sequence[OligoCreateHelm]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AsyncTaskLink]
            Accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            "dna-oligos:bulk-create",
            method="POST",
            json={
                "dnaOligos": convert_and_respect_annotation_metadata(
                    object_=dna_oligos, annotation=typing.Sequence[OligoCreateHelm], direction="write"
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


class AsyncRawDnaOligosClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_dna_oligos_helm(
        self,
        *,
        page_size: typing.Optional[int] = None,
        next_token: typing.Optional[str] = None,
        sort: typing.Optional[ListDnaOligosHelmRequestSort] = None,
        modified_at: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        name_includes: typing.Optional[str] = None,
        bases: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        mentioned_in: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        project_id: typing.Optional[str] = None,
        registry_id: typing.Optional[str] = None,
        schema_id: typing.Optional[str] = None,
        schema_fields: typing.Optional[SchemaFieldsQueryParam] = None,
        archive_reason: typing.Optional[str] = None,
        mentions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ids: typing.Optional[str] = None,
        entity_registry_ids_any_of: typing.Optional[str] = None,
        names_any_of: typing.Optional[str] = None,
        names_any_of_case_sensitive: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DnaOligosPaginatedListHelm]:
        """
        List DNA Oligos with HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        page_size : typing.Optional[int]
            Number of results to return. Defaults to 50, maximum of 100.

        next_token : typing.Optional[str]
            Token for pagination

        sort : typing.Optional[ListDnaOligosHelmRequestSort]
            Method by which to order search results. Valid sorts are modifiedAt (modified time, most recent first) and name (entity name, alphabetical). Optionally add :asc or :desc to specify ascending or descending order.

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        name : typing.Optional[str]
            Name of a DNA Oligo. Restricts results to those with the specified name, alias, or entity registry ID.

        name_includes : typing.Optional[str]
            Name substring of a DNA Oligo. Restricts results to those with names, aliases, or entity registry IDs that include the provided substring.

        bases : typing.Optional[str]
            Full bases of the DNA Oligo. Restricts results to those with the specified bases, case-insensitive, allowing for circular or reverse complement matches. Does not allow partial matching or loose matching via degenerate bases.

        folder_id : typing.Optional[str]
            ID of a folder. Restricts results to those in the folder.

        mentioned_in : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of entry IDs. Restricts results to DNA Oligos mentioned in those entries.

        project_id : typing.Optional[str]
            ID of a project. Restricts results to those in the project.

        registry_id : typing.Optional[str]
            ID of a registry. Restricts results to those registered in this registry. Specifying "null" returns unregistered items.

        schema_id : typing.Optional[str]
            ID of a schema. Restricts results to those of the specified schema.

        schema_fields : typing.Optional[SchemaFieldsQueryParam]
            Schema field value. For Integer, Float, and Date type fields, supports the >= and <= operators. If present, the schemaId param must also be present. Restricts results to those with a field of whose value matches the filter.

        archive_reason : typing.Optional[str]
            Archive reason. Restricts results to those with the specified archive reason. Use “NOT_ARCHIVED” to filter for unarchived DNA Oligos.

        mentions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Comma-separated list of item IDs. Restricts results to those that mention the given items in the description.

        ids : typing.Optional[str]
            Comma-separated list of ids. Matches all of the provided IDs, or returns a 400 error that includes a list of which IDs are invalid.

        entity_registry_ids_any_of : typing.Optional[str]
            Comma-separated list of entity registry IDs. Restricts results to those that match any of the specified registry IDs.

        names_any_of : typing.Optional[str]
            Comma-separated list of names. Restricts results to those that match any of the specified names, aliases, or entity registry IDs, case insensitive.  Warning - this filter can be non-performant due to case insensitivity.

        names_any_of_case_sensitive : typing.Optional[str]
            Comma-separated list of names. Restricts results to those that match any of the specified names, aliases, or entity registry IDs, case sensitive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DnaOligosPaginatedListHelm]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "dna-oligos",
            method="GET",
            params={
                "pageSize": page_size,
                "nextToken": next_token,
                "sort": sort,
                "modifiedAt": modified_at,
                "name": name,
                "nameIncludes": name_includes,
                "bases": bases,
                "folderId": folder_id,
                "mentionedIn": ",".join(map(str, mentioned_in))
                if isinstance(mentioned_in, (list, tuple, set))
                else mentioned_in,
                "projectId": project_id,
                "registryId": registry_id,
                "schemaId": schema_id,
                "schemaFields": schema_fields,
                "archiveReason": archive_reason,
                "mentions": ",".join(map(str, mentions)) if isinstance(mentions, (list, tuple, set)) else mentions,
                "ids": ids,
                "entityRegistryIds.anyOf": entity_registry_ids_any_of,
                "names.anyOf": names_any_of,
                "names.anyOf.caseSensitive": names_any_of_case_sensitive,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DnaOligosPaginatedListHelm,
                    parse_obj_as(
                        type_=DnaOligosPaginatedListHelm,
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

    async def create_dna_oligo_with_helm(
        self,
        *,
        name: str,
        helm: typing.Optional[str] = OMIT,
        aliases: typing.Optional[typing.Sequence[str]] = OMIT,
        author_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bases: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[CustomFields] = OMIT,
        fields: typing.Optional[Fields] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        schema_id: typing.Optional[str] = OMIT,
        entity_registry_id: typing.Optional[str] = OMIT,
        naming_strategy: typing.Optional[NamingStrategy] = OMIT,
        registry_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DnaOligoHelm]:
        """
        Create a DNA Oligo with optional HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        name : str
            Name of the Oligo.

        helm : typing.Optional[str]
            Representation of the oligo in HELM syntax, including any chemical modifications

        aliases : typing.Optional[typing.Sequence[str]]
            Aliases to add to the Oligo

        author_ids : typing.Optional[typing.Sequence[str]]
            IDs of users to set as the Oligo's authors.

        bases : typing.Optional[str]
            Base pairs of the oligo.

        custom_fields : typing.Optional[CustomFields]
            Custom fields to add to the Oligo. Every field should have its name as a key, mapping to an object with information about the value of the field.

        fields : typing.Optional[Fields]
            Fields to set on the Oligo. Must correspond with the schema's field definitions. Every field should have its name as a key, mapping to an object with information about the value of the field.

        folder_id : typing.Optional[str]
            ID of the folder containing the Oligo.

        schema_id : typing.Optional[str]
            ID of the oligo's schema.

        entity_registry_id : typing.Optional[str]
            Entity registry ID to set for the registered entity. Cannot specify both entityRegistryId and namingStrategy at the same time.

        naming_strategy : typing.Optional[NamingStrategy]

        registry_id : typing.Optional[str]
            Registry ID into which entity should be registered. this is the ID of the registry which was configured for a particular organization
            To get available registryIds, use the [/registries endpoint](#/Registry/listRegistries)

            Required in order for entities to be created directly in the registry.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DnaOligoHelm]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "dna-oligos",
            method="POST",
            json={
                "helm": helm,
                "aliases": aliases,
                "authorIds": author_ids,
                "bases": bases,
                "customFields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=CustomFields, direction="write"
                ),
                "fields": convert_and_respect_annotation_metadata(object_=fields, annotation=Fields, direction="write"),
                "folderId": folder_id,
                "name": name,
                "schemaId": schema_id,
                "entityRegistryId": entity_registry_id,
                "namingStrategy": naming_strategy,
                "registryId": registry_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DnaOligoHelm,
                    parse_obj_as(
                        type_=DnaOligoHelm,
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

    async def get_dna_oligo_helm(
        self, oligo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DnaOligoHelm]:
        """
        Get a DNA Oligo with HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        oligo_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DnaOligoHelm]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dna-oligos/{encode_path_param(oligo_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DnaOligoHelm,
                    parse_obj_as(
                        type_=DnaOligoHelm,
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

    async def update_dna_oligo_helm(
        self,
        oligo_id: str,
        *,
        helm: typing.Optional[str] = OMIT,
        aliases: typing.Optional[typing.Sequence[str]] = OMIT,
        author_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bases: typing.Optional[str] = OMIT,
        custom_fields: typing.Optional[CustomFields] = OMIT,
        fields: typing.Optional[Fields] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        schema_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DnaOligoHelm]:
        """
        Update a DNA Oligo with optional HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        oligo_id : str

        helm : typing.Optional[str]
            Representation of the oligo in HELM syntax, including any chemical modifications

        aliases : typing.Optional[typing.Sequence[str]]
            Aliases to add to the Oligo

        author_ids : typing.Optional[typing.Sequence[str]]
            IDs of users to set as the Oligo's authors.

        bases : typing.Optional[str]
            Base pairs of the oligo.

        custom_fields : typing.Optional[CustomFields]
            Custom fields to add to the Oligo. Every field should have its name as a key, mapping to an object with information about the value of the field.

        fields : typing.Optional[Fields]
            Fields to set on the Oligo. Must correspond with the schema's field definitions. Every field should have its name as a key, mapping to an object with information about the value of the field.

        folder_id : typing.Optional[str]
            ID of the folder containing the Oligo.

        name : typing.Optional[str]
            Name of the Oligo.

        schema_id : typing.Optional[str]
            ID of the oligo's schema.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DnaOligoHelm]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dna-oligos/{encode_path_param(oligo_id)}",
            method="PATCH",
            json={
                "helm": helm,
                "aliases": aliases,
                "authorIds": author_ids,
                "bases": bases,
                "customFields": convert_and_respect_annotation_metadata(
                    object_=custom_fields, annotation=CustomFields, direction="write"
                ),
                "fields": convert_and_respect_annotation_metadata(object_=fields, annotation=Fields, direction="write"),
                "folderId": folder_id,
                "name": name,
                "schemaId": schema_id,
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
                    DnaOligoHelm,
                    parse_obj_as(
                        type_=DnaOligoHelm,
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

    async def bulk_create_dna_oligos_helm(
        self,
        *,
        dna_oligos: typing.Optional[typing.Sequence[OligoCreateHelm]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AsyncTaskLink]:
        """
        Bulk Create DNA Oligos with optional HELM Deprecated as HELM support is now in stable.

        Parameters
        ----------
        dna_oligos : typing.Optional[typing.Sequence[OligoCreateHelm]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AsyncTaskLink]
            Accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            "dna-oligos:bulk-create",
            method="POST",
            json={
                "dnaOligos": convert_and_respect_annotation_metadata(
                    object_=dna_oligos, annotation=typing.Sequence[OligoCreateHelm], direction="write"
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
