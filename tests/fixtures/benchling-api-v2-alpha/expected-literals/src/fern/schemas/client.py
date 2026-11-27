

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.constraint_create import ConstraintCreate
from ..types.entity_schema import EntitySchema
from ..types.entity_schemas_paginated_list import EntitySchemasPaginatedList
from ..types.field_create import FieldCreate
from ..types.naming_strategy import NamingStrategy
from ..types.schema_class import SchemaClass
from ..types.schema_classes_paginated_list import SchemaClassesPaginatedList
from .raw_client import AsyncRawSchemasClient, RawSchemasClient
from .types.entity_schema_create_auth_parent_option import EntitySchemaCreateAuthParentOption
from .types.entity_schema_create_containable_type import EntitySchemaCreateContainableType
from .types.entity_schema_create_type import EntitySchemaCreateType


OMIT = typing.cast(typing.Any, ...)


class SchemasClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSchemasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSchemasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSchemasClient
        """
        return self._raw_client

    def list_entity_schemas(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        modified_at: typing.Optional[str] = None,
        registry_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntitySchemasPaginatedList:
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
        EntitySchemasPaginatedList
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.schemas.list_entity_schemas(
            modified_at="> 2022-03-01 AND < 2022-04-01",
        )
        """
        _response = self._raw_client.list_entity_schemas(
            next_token=next_token,
            page_size=page_size,
            modified_at=modified_at,
            registry_id=registry_id,
            request_options=request_options,
        )
        return _response.data

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
    ) -> EntitySchema:
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
        EntitySchema
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.schemas.create_entity_schema(
            name="name",
            prefix="prefix",
            registry_id="registryId",
            type="custom_entity",
        )
        """
        _response = self._raw_client.create_entity_schema(
            name=name,
            prefix=prefix,
            registry_id=registry_id,
            type=type,
            auth_parent_option=auth_parent_option,
            constraint=constraint,
            containable_type=containable_type,
            fields=fields,
            include_registry_id_in_chips=include_registry_id_in_chips,
            is_containable=is_containable,
            labeling_strategies=labeling_strategies,
            mixture_schema_config=mixture_schema_config,
            result_schema_id=result_schema_id,
            sequence_type=sequence_type,
            should_create_as_oligo=should_create_as_oligo,
            should_order_name_parts_by_sequence=should_order_name_parts_by_sequence,
            show_residues=show_residues,
            use_organization_collection_alias_for_display_label=use_organization_collection_alias_for_display_label,
            request_options=request_options,
        )
        return _response.data

    def get_entity_schema(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntitySchema:
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
        EntitySchema
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.schemas.get_entity_schema(
            schema_id="schema_id",
        )
        """
        _response = self._raw_client.get_entity_schema(schema_id, request_options=request_options)
        return _response.data

    def list_schema_classes(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        modified_at: typing.Optional[str] = None,
        schema_ids_all_of: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchemaClassesPaginatedList:
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
        SchemaClassesPaginatedList
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.schemas.list_schema_classes(
            modified_at="> 2022-03-01 AND < 2022-04-01",
            schema_ids_all_of="bfi_ed1ef7,con_1c76c9",
        )
        """
        _response = self._raw_client.list_schema_classes(
            next_token=next_token,
            page_size=page_size,
            modified_at=modified_at,
            schema_ids_all_of=schema_ids_all_of,
            request_options=request_options,
        )
        return _response.data

    def get_schema_class(
        self, schema_class_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaClass:
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
        SchemaClass
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.schemas.get_schema_class(
            schema_class_id="schema_class_id",
        )
        """
        _response = self._raw_client.get_schema_class(schema_class_id, request_options=request_options)
        return _response.data


class AsyncSchemasClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSchemasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSchemasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSchemasClient
        """
        return self._raw_client

    async def list_entity_schemas(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        modified_at: typing.Optional[str] = None,
        registry_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntitySchemasPaginatedList:
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
        EntitySchemasPaginatedList
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
            await client.schemas.list_entity_schemas(
                modified_at="> 2022-03-01 AND < 2022-04-01",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_entity_schemas(
            next_token=next_token,
            page_size=page_size,
            modified_at=modified_at,
            registry_id=registry_id,
            request_options=request_options,
        )
        return _response.data

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
    ) -> EntitySchema:
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
        EntitySchema
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.schemas.create_entity_schema(
                name="name",
                prefix="prefix",
                registry_id="registryId",
                type="custom_entity",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_entity_schema(
            name=name,
            prefix=prefix,
            registry_id=registry_id,
            type=type,
            auth_parent_option=auth_parent_option,
            constraint=constraint,
            containable_type=containable_type,
            fields=fields,
            include_registry_id_in_chips=include_registry_id_in_chips,
            is_containable=is_containable,
            labeling_strategies=labeling_strategies,
            mixture_schema_config=mixture_schema_config,
            result_schema_id=result_schema_id,
            sequence_type=sequence_type,
            should_create_as_oligo=should_create_as_oligo,
            should_order_name_parts_by_sequence=should_order_name_parts_by_sequence,
            show_residues=show_residues,
            use_organization_collection_alias_for_display_label=use_organization_collection_alias_for_display_label,
            request_options=request_options,
        )
        return _response.data

    async def get_entity_schema(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntitySchema:
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
        EntitySchema
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
            await client.schemas.get_entity_schema(
                schema_id="schema_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entity_schema(schema_id, request_options=request_options)
        return _response.data

    async def list_schema_classes(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        modified_at: typing.Optional[str] = None,
        schema_ids_all_of: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchemaClassesPaginatedList:
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
        SchemaClassesPaginatedList
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
            await client.schemas.list_schema_classes(
                modified_at="> 2022-03-01 AND < 2022-04-01",
                schema_ids_all_of="bfi_ed1ef7,con_1c76c9",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_schema_classes(
            next_token=next_token,
            page_size=page_size,
            modified_at=modified_at,
            schema_ids_all_of=schema_ids_all_of,
            request_options=request_options,
        )
        return _response.data

    async def get_schema_class(
        self, schema_class_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaClass:
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
        SchemaClass
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
            await client.schemas.get_schema_class(
                schema_class_id="schema_class_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schema_class(schema_class_id, request_options=request_options)
        return _response.data
