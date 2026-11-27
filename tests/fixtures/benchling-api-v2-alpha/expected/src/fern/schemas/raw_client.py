

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
from ..types.constraint_create import ConstraintCreate
from ..types.entity_schema import EntitySchema
from ..types.entity_schemas_paginated_list import EntitySchemasPaginatedList
from ..types.field_create import FieldCreate
from ..types.naming_strategy import NamingStrategy
from ..types.schema_class import SchemaClass
from ..types.schema_classes_paginated_list import SchemaClassesPaginatedList
from .types.entity_schema_create_auth_parent_option import EntitySchemaCreateAuthParentOption
from .types.entity_schema_create_containable_type import EntitySchemaCreateContainableType
from .types.entity_schema_create_type import EntitySchemaCreateType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSchemasClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_entity_schemas(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        modified_at: typing.Optional[str] = None,
        registry_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntitySchemasPaginatedList]:
        """
        List entity schemas

        Parameters
        ----------
        next_token : typing.Optional[str]

        page_size : typing.Optional[int]

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        registry_id : typing.Optional[str]
            ID of a registry. Restricts results to schemas in this registry.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntitySchemasPaginatedList]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "entity-schemas",
            method="GET",
            params={
                "nextToken": next_token,
                "pageSize": page_size,
                "modifiedAt": modified_at,
                "registryId": registry_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntitySchemasPaginatedList,
                    parse_obj_as(
                        type_=EntitySchemasPaginatedList,
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

    def create_entity_schema(
        self,
        *,
        name: str,
        prefix: str,
        registry_id: str,
        type: EntitySchemaCreateType,
        auth_parent_option: typing.Optional[EntitySchemaCreateAuthParentOption] = OMIT,
        constraint: typing.Optional[ConstraintCreate] = OMIT,
        containable_type: typing.Optional[EntitySchemaCreateContainableType] = OMIT,
        fields: typing.Optional[typing.Sequence[FieldCreate]] = OMIT,
        include_registry_id_in_chips: typing.Optional[bool] = OMIT,
        is_containable: typing.Optional[bool] = OMIT,
        labeling_strategies: typing.Optional[typing.Sequence[NamingStrategy]] = OMIT,
        mixture_schema_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        result_schema_id: typing.Optional[str] = OMIT,
        sequence_type: typing.Optional[str] = OMIT,
        should_create_as_oligo: typing.Optional[bool] = OMIT,
        should_order_name_parts_by_sequence: typing.Optional[bool] = OMIT,
        show_residues: typing.Optional[bool] = OMIT,
        use_organization_collection_alias_for_display_label: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntitySchema]:
        """
        Create an entity schema

        Parameters
        ----------
        name : str

        prefix : str

        registry_id : str

        type : EntitySchemaCreateType

        auth_parent_option : typing.Optional[EntitySchemaCreateAuthParentOption]

        constraint : typing.Optional[ConstraintCreate]

        containable_type : typing.Optional[EntitySchemaCreateContainableType]

        fields : typing.Optional[typing.Sequence[FieldCreate]]

        include_registry_id_in_chips : typing.Optional[bool]

        is_containable : typing.Optional[bool]

        labeling_strategies : typing.Optional[typing.Sequence[NamingStrategy]]

        mixture_schema_config : typing.Optional[typing.Dict[str, typing.Any]]

        result_schema_id : typing.Optional[str]

        sequence_type : typing.Optional[str]

        should_create_as_oligo : typing.Optional[bool]

        should_order_name_parts_by_sequence : typing.Optional[bool]

        show_residues : typing.Optional[bool]

        use_organization_collection_alias_for_display_label : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntitySchema]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "entity-schemas",
            method="POST",
            json={
                "authParentOption": auth_parent_option,
                "constraint": convert_and_respect_annotation_metadata(
                    object_=constraint, annotation=typing.Optional[ConstraintCreate], direction="write"
                ),
                "containableType": containable_type,
                "fields": convert_and_respect_annotation_metadata(
                    object_=fields, annotation=typing.Optional[typing.Sequence[FieldCreate]], direction="write"
                ),
                "includeRegistryIdInChips": include_registry_id_in_chips,
                "isContainable": is_containable,
                "labelingStrategies": labeling_strategies,
                "mixtureSchemaConfig": mixture_schema_config,
                "name": name,
                "prefix": prefix,
                "registryId": registry_id,
                "resultSchemaId": result_schema_id,
                "sequenceType": sequence_type,
                "shouldCreateAsOligo": should_create_as_oligo,
                "shouldOrderNamePartsBySequence": should_order_name_parts_by_sequence,
                "showResidues": show_residues,
                "type": type,
                "useOrganizationCollectionAliasForDisplayLabel": use_organization_collection_alias_for_display_label,
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
                    EntitySchema,
                    parse_obj_as(
                        type_=EntitySchema,
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

    def get_entity_schema(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EntitySchema]:
        """
        Get an entity schema by ID

        Parameters
        ----------
        schema_id : str
            ID of schema to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntitySchema]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"entity-schemas/{encode_path_param(schema_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntitySchema,
                    parse_obj_as(
                        type_=EntitySchema,
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

    def list_schema_classes(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        modified_at: typing.Optional[str] = None,
        schema_ids_all_of: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SchemaClassesPaginatedList]:
        """
        List schema classes

        Parameters
        ----------
        next_token : typing.Optional[str]

        page_size : typing.Optional[int]

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        schema_ids_all_of : typing.Optional[str]
            Comma separated list of bioentity IDs. Returns schema classes where the schema class is implemented by all of the provided items.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchemaClassesPaginatedList]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "schema-classes",
            method="GET",
            params={
                "nextToken": next_token,
                "pageSize": page_size,
                "modifiedAt": modified_at,
                "SchemaIds.allOf": schema_ids_all_of,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchemaClassesPaginatedList,
                    parse_obj_as(
                        type_=SchemaClassesPaginatedList,
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

    def get_schema_class(
        self, schema_class_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SchemaClass]:
        """
        Get a schema class by ID

        Parameters
        ----------
        schema_class_id : str
            ID of schema class to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchemaClass]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"schemas-classes/{encode_path_param(schema_class_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchemaClass,
                    parse_obj_as(
                        type_=SchemaClass,
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


class AsyncRawSchemasClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_entity_schemas(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        modified_at: typing.Optional[str] = None,
        registry_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntitySchemasPaginatedList]:
        """
        List entity schemas

        Parameters
        ----------
        next_token : typing.Optional[str]

        page_size : typing.Optional[int]

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        registry_id : typing.Optional[str]
            ID of a registry. Restricts results to schemas in this registry.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntitySchemasPaginatedList]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "entity-schemas",
            method="GET",
            params={
                "nextToken": next_token,
                "pageSize": page_size,
                "modifiedAt": modified_at,
                "registryId": registry_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntitySchemasPaginatedList,
                    parse_obj_as(
                        type_=EntitySchemasPaginatedList,
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

    async def create_entity_schema(
        self,
        *,
        name: str,
        prefix: str,
        registry_id: str,
        type: EntitySchemaCreateType,
        auth_parent_option: typing.Optional[EntitySchemaCreateAuthParentOption] = OMIT,
        constraint: typing.Optional[ConstraintCreate] = OMIT,
        containable_type: typing.Optional[EntitySchemaCreateContainableType] = OMIT,
        fields: typing.Optional[typing.Sequence[FieldCreate]] = OMIT,
        include_registry_id_in_chips: typing.Optional[bool] = OMIT,
        is_containable: typing.Optional[bool] = OMIT,
        labeling_strategies: typing.Optional[typing.Sequence[NamingStrategy]] = OMIT,
        mixture_schema_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        result_schema_id: typing.Optional[str] = OMIT,
        sequence_type: typing.Optional[str] = OMIT,
        should_create_as_oligo: typing.Optional[bool] = OMIT,
        should_order_name_parts_by_sequence: typing.Optional[bool] = OMIT,
        show_residues: typing.Optional[bool] = OMIT,
        use_organization_collection_alias_for_display_label: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntitySchema]:
        """
        Create an entity schema

        Parameters
        ----------
        name : str

        prefix : str

        registry_id : str

        type : EntitySchemaCreateType

        auth_parent_option : typing.Optional[EntitySchemaCreateAuthParentOption]

        constraint : typing.Optional[ConstraintCreate]

        containable_type : typing.Optional[EntitySchemaCreateContainableType]

        fields : typing.Optional[typing.Sequence[FieldCreate]]

        include_registry_id_in_chips : typing.Optional[bool]

        is_containable : typing.Optional[bool]

        labeling_strategies : typing.Optional[typing.Sequence[NamingStrategy]]

        mixture_schema_config : typing.Optional[typing.Dict[str, typing.Any]]

        result_schema_id : typing.Optional[str]

        sequence_type : typing.Optional[str]

        should_create_as_oligo : typing.Optional[bool]

        should_order_name_parts_by_sequence : typing.Optional[bool]

        show_residues : typing.Optional[bool]

        use_organization_collection_alias_for_display_label : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntitySchema]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "entity-schemas",
            method="POST",
            json={
                "authParentOption": auth_parent_option,
                "constraint": convert_and_respect_annotation_metadata(
                    object_=constraint, annotation=typing.Optional[ConstraintCreate], direction="write"
                ),
                "containableType": containable_type,
                "fields": convert_and_respect_annotation_metadata(
                    object_=fields, annotation=typing.Optional[typing.Sequence[FieldCreate]], direction="write"
                ),
                "includeRegistryIdInChips": include_registry_id_in_chips,
                "isContainable": is_containable,
                "labelingStrategies": labeling_strategies,
                "mixtureSchemaConfig": mixture_schema_config,
                "name": name,
                "prefix": prefix,
                "registryId": registry_id,
                "resultSchemaId": result_schema_id,
                "sequenceType": sequence_type,
                "shouldCreateAsOligo": should_create_as_oligo,
                "shouldOrderNamePartsBySequence": should_order_name_parts_by_sequence,
                "showResidues": show_residues,
                "type": type,
                "useOrganizationCollectionAliasForDisplayLabel": use_organization_collection_alias_for_display_label,
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
                    EntitySchema,
                    parse_obj_as(
                        type_=EntitySchema,
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

    async def get_entity_schema(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EntitySchema]:
        """
        Get an entity schema by ID

        Parameters
        ----------
        schema_id : str
            ID of schema to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntitySchema]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"entity-schemas/{encode_path_param(schema_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntitySchema,
                    parse_obj_as(
                        type_=EntitySchema,
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

    async def list_schema_classes(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        modified_at: typing.Optional[str] = None,
        schema_ids_all_of: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SchemaClassesPaginatedList]:
        """
        List schema classes

        Parameters
        ----------
        next_token : typing.Optional[str]

        page_size : typing.Optional[int]

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        schema_ids_all_of : typing.Optional[str]
            Comma separated list of bioentity IDs. Returns schema classes where the schema class is implemented by all of the provided items.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchemaClassesPaginatedList]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "schema-classes",
            method="GET",
            params={
                "nextToken": next_token,
                "pageSize": page_size,
                "modifiedAt": modified_at,
                "SchemaIds.allOf": schema_ids_all_of,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchemaClassesPaginatedList,
                    parse_obj_as(
                        type_=SchemaClassesPaginatedList,
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

    async def get_schema_class(
        self, schema_class_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SchemaClass]:
        """
        Get a schema class by ID

        Parameters
        ----------
        schema_class_id : str
            ID of schema class to get

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchemaClass]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"schemas-classes/{encode_path_param(schema_class_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchemaClass,
                    parse_obj_as(
                        type_=SchemaClass,
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
