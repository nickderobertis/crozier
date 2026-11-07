

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.schema_config_dto import SchemaConfigDto
from ..types.table_config_dto import TableConfigDto
from .raw_client import AsyncRawSqlSchemaClient, RawSqlSchemaClient


OMIT = typing.cast(typing.Any, ...)


class SqlSchemaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSqlSchemaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSqlSchemaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSqlSchemaClient
        """
        return self._raw_client

    def get_schema_by_name(
        self, *, schema_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaConfigDto:
        """
        Retrieves a schema configuration using its name

        Parameters
        ----------
        schema_name : str
            Name of the schema to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaConfigDto
            Schema found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sql_schema.get_schema_by_name(
            schema_name="schemaName",
        )
        """
        _response = self._raw_client.get_schema_by_name(schema_name=schema_name, request_options=request_options)
        return _response.data

    def save_schema(
        self,
        *,
        schema_name: str,
        tables: typing.Sequence[TableConfigDto],
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Saves a new or updates an existing schema configuration

        Parameters
        ----------
        schema_name : str

        tables : typing.Sequence[TableConfigDto]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Schema saved successfully

        Examples
        --------
        from fern import FernApi, FieldConfigDto, TableConfigDto

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sql_schema.save_schema(
            schema_name="NOBEL_PRIZES",
            tables=[
                TableConfigDto(
                    table_name="nobel-prize",
                    metadata_class_id="1dba8c8a-77bb-11f0-822a-ae468cd3ed16",
                    uniformed_path="$",
                    fields=[
                        FieldConfigDto(
                            field_name="entity_id",
                            field_key="ENTITY_ID",
                            field_category="SPECIAL",
                            data_type="UUID_TYPE",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="point_time",
                            field_key="POINT_TIME",
                            field_category="SPECIAL",
                            data_type="DATE",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="creation_date",
                            field_key="creationDate",
                            field_category="ROOT",
                            data_type="DATE",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="last_update_date",
                            field_key="lastUpdateTime",
                            field_category="ROOT",
                            data_type="DATE",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="state",
                            field_key="state",
                            field_category="ROOT",
                            data_type="STRING",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="category",
                            field_key=".category",
                            field_category="DATA",
                            data_type="STRING",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="year",
                            field_key=".year",
                            field_category="DATA",
                            data_type="STRING",
                            is_array=True,
                            hidden=True,
                        ),
                    ],
                    hidden=False,
                ),
                TableConfigDto(
                    table_name="nobel-prize_laureates",
                    metadata_class_id="1dba8c8a-77bb-11f0-822a-ae468cd3ed16",
                    uniformed_path="$.laureates[*]",
                    fields=[
                        FieldConfigDto(
                            field_name="entity_id",
                            field_key="ENTITY_ID",
                            field_category="SPECIAL",
                            data_type="UUID_TYPE",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="point_time",
                            field_key="POINT_TIME",
                            field_category="SPECIAL",
                            data_type="DATE",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="creation_date",
                            field_key="creationDate",
                            field_category="ROOT",
                            data_type="DATE",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="last_update_date",
                            field_key="lastUpdateTime",
                            field_category="ROOT",
                            data_type="DATE",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="state",
                            field_key="state",
                            field_category="ROOT",
                            data_type="STRING",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="index",
                            field_key="",
                            field_category="INDEX",
                            data_type="INTEGER",
                            is_array=True,
                            hidden=True,
                            flatten=True,
                        ),
                        FieldConfigDto(
                            field_name="firstname",
                            field_key=".firstname",
                            field_category="DATA",
                            data_type="STRING",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="surname",
                            field_key=".surname",
                            field_category="DATA",
                            data_type="STRING",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="id",
                            field_key=".id",
                            field_category="DATA",
                            data_type="STRING",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="motivation",
                            field_key=".motivation",
                            field_category="DATA",
                            data_type="STRING",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="share",
                            field_key=".share",
                            field_category="DATA",
                            data_type="STRING",
                            is_array=True,
                            hidden=True,
                        ),
                    ],
                    hidden=False,
                ),
                TableConfigDto(
                    table_name="nobel-prize_json",
                    metadata_class_id="1dba8c8a-77bb-11f0-822a-ae468cd3ed16",
                    uniformed_path="json",
                    fields=[
                        FieldConfigDto(
                            field_name="entity_id",
                            field_key="ENTITY_ID",
                            field_category="SPECIAL",
                            data_type="UUID_TYPE",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="point_time",
                            field_key="POINT_TIME",
                            field_category="SPECIAL",
                            data_type="DATE",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="creation_date",
                            field_key="creationDate",
                            field_category="ROOT",
                            data_type="DATE",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="last_update_date",
                            field_key="lastUpdateTime",
                            field_category="ROOT",
                            data_type="DATE",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="state",
                            field_key="state",
                            field_category="ROOT",
                            data_type="STRING",
                            is_array=True,
                            hidden=True,
                        ),
                        FieldConfigDto(
                            field_name="entity",
                            field_key="JSON",
                            field_category="SPECIAL",
                            data_type="STRING",
                            is_array=True,
                            hidden=True,
                        ),
                    ],
                    hidden=False,
                ),
            ],
        )
        """
        _response = self._raw_client.save_schema(
            schema_name=schema_name, tables=tables, id=id, request_options=request_options
        )
        return _response.data

    def delete_schema_by_name(
        self, *, schema_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Deletes an existing schema configuration using its name

        Parameters
        ----------
        schema_name : str
            Name of the schema to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Schema deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sql_schema.delete_schema_by_name(
            schema_name="schemaName",
        )
        """
        _response = self._raw_client.delete_schema_by_name(schema_name=schema_name, request_options=request_options)
        return _response.data

    def gen_tables(
        self, entity_model_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TableConfigDto:
        """
        Generates table configurations based on entity model ID

        Parameters
        ----------
        entity_model_id : str
            The entity model id to generate tables from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TableConfigDto
            Tables generated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sql_schema.gen_tables(
            entity_model_id="entityModelId",
        )
        """
        _response = self._raw_client.gen_tables(entity_model_id, request_options=request_options)
        return _response.data

    def get_schemas(self, *, request_options: typing.Optional[RequestOptions] = None) -> SchemaConfigDto:
        """
        Retrieves all available schema configurations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaConfigDto
            List of schemas retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sql_schema.get_schemas()
        """
        _response = self._raw_client.get_schemas(request_options=request_options)
        return _response.data

    def put_schema(
        self, schema_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaConfigDto:
        """
        Creates a new schema configuration that includes all available entity models with their complete field structures

        Parameters
        ----------
        schema_name : str
            Name for the new schema. The name can have a maximum of 1024 characters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaConfigDto
            Schema created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sql_schema.put_schema(
            schema_name="schemaName",
        )
        """
        _response = self._raw_client.put_schema(schema_name, request_options=request_options)
        return _response.data

    def update_tables(
        self, entity_model_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TableConfigDto:
        """
        Synchronizes given table configurations with the current entity model structure, preserving custom settings while incorporating any model changes

        Parameters
        ----------
        entity_model_id : str
            The entity model ID to update tables from

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TableConfigDto
            Tables updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sql_schema.update_tables(
            entity_model_id="entityModelId",
            request="string",
        )
        """
        _response = self._raw_client.update_tables(entity_model_id, request=request, request_options=request_options)
        return _response.data

    def get_schema(self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SchemaConfigDto:
        """
        Retrieves a schema configuration using its UUID

        Parameters
        ----------
        schema_id : str
            UUID of the schema to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaConfigDto
            Schema found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sql_schema.get_schema(
            schema_id="schemaId",
        )
        """
        _response = self._raw_client.get_schema(schema_id, request_options=request_options)
        return _response.data

    def delete_schema(self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Deletes a schema configuration using its UUID

        Parameters
        ----------
        schema_id : str
            UUID of the schema to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Schema deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sql_schema.delete_schema(
            schema_id="schemaId",
        )
        """
        _response = self._raw_client.delete_schema(schema_id, request_options=request_options)
        return _response.data


class AsyncSqlSchemaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSqlSchemaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSqlSchemaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSqlSchemaClient
        """
        return self._raw_client

    async def get_schema_by_name(
        self, *, schema_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaConfigDto:
        """
        Retrieves a schema configuration using its name

        Parameters
        ----------
        schema_name : str
            Name of the schema to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaConfigDto
            Schema found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sql_schema.get_schema_by_name(
                schema_name="schemaName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schema_by_name(schema_name=schema_name, request_options=request_options)
        return _response.data

    async def save_schema(
        self,
        *,
        schema_name: str,
        tables: typing.Sequence[TableConfigDto],
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Saves a new or updates an existing schema configuration

        Parameters
        ----------
        schema_name : str

        tables : typing.Sequence[TableConfigDto]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Schema saved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FieldConfigDto, TableConfigDto

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sql_schema.save_schema(
                schema_name="NOBEL_PRIZES",
                tables=[
                    TableConfigDto(
                        table_name="nobel-prize",
                        metadata_class_id="1dba8c8a-77bb-11f0-822a-ae468cd3ed16",
                        uniformed_path="$",
                        fields=[
                            FieldConfigDto(
                                field_name="entity_id",
                                field_key="ENTITY_ID",
                                field_category="SPECIAL",
                                data_type="UUID_TYPE",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="point_time",
                                field_key="POINT_TIME",
                                field_category="SPECIAL",
                                data_type="DATE",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="creation_date",
                                field_key="creationDate",
                                field_category="ROOT",
                                data_type="DATE",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="last_update_date",
                                field_key="lastUpdateTime",
                                field_category="ROOT",
                                data_type="DATE",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="state",
                                field_key="state",
                                field_category="ROOT",
                                data_type="STRING",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="category",
                                field_key=".category",
                                field_category="DATA",
                                data_type="STRING",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="year",
                                field_key=".year",
                                field_category="DATA",
                                data_type="STRING",
                                is_array=True,
                                hidden=True,
                            ),
                        ],
                        hidden=False,
                    ),
                    TableConfigDto(
                        table_name="nobel-prize_laureates",
                        metadata_class_id="1dba8c8a-77bb-11f0-822a-ae468cd3ed16",
                        uniformed_path="$.laureates[*]",
                        fields=[
                            FieldConfigDto(
                                field_name="entity_id",
                                field_key="ENTITY_ID",
                                field_category="SPECIAL",
                                data_type="UUID_TYPE",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="point_time",
                                field_key="POINT_TIME",
                                field_category="SPECIAL",
                                data_type="DATE",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="creation_date",
                                field_key="creationDate",
                                field_category="ROOT",
                                data_type="DATE",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="last_update_date",
                                field_key="lastUpdateTime",
                                field_category="ROOT",
                                data_type="DATE",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="state",
                                field_key="state",
                                field_category="ROOT",
                                data_type="STRING",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="index",
                                field_key="",
                                field_category="INDEX",
                                data_type="INTEGER",
                                is_array=True,
                                hidden=True,
                                flatten=True,
                            ),
                            FieldConfigDto(
                                field_name="firstname",
                                field_key=".firstname",
                                field_category="DATA",
                                data_type="STRING",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="surname",
                                field_key=".surname",
                                field_category="DATA",
                                data_type="STRING",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="id",
                                field_key=".id",
                                field_category="DATA",
                                data_type="STRING",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="motivation",
                                field_key=".motivation",
                                field_category="DATA",
                                data_type="STRING",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="share",
                                field_key=".share",
                                field_category="DATA",
                                data_type="STRING",
                                is_array=True,
                                hidden=True,
                            ),
                        ],
                        hidden=False,
                    ),
                    TableConfigDto(
                        table_name="nobel-prize_json",
                        metadata_class_id="1dba8c8a-77bb-11f0-822a-ae468cd3ed16",
                        uniformed_path="json",
                        fields=[
                            FieldConfigDto(
                                field_name="entity_id",
                                field_key="ENTITY_ID",
                                field_category="SPECIAL",
                                data_type="UUID_TYPE",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="point_time",
                                field_key="POINT_TIME",
                                field_category="SPECIAL",
                                data_type="DATE",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="creation_date",
                                field_key="creationDate",
                                field_category="ROOT",
                                data_type="DATE",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="last_update_date",
                                field_key="lastUpdateTime",
                                field_category="ROOT",
                                data_type="DATE",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="state",
                                field_key="state",
                                field_category="ROOT",
                                data_type="STRING",
                                is_array=True,
                                hidden=True,
                            ),
                            FieldConfigDto(
                                field_name="entity",
                                field_key="JSON",
                                field_category="SPECIAL",
                                data_type="STRING",
                                is_array=True,
                                hidden=True,
                            ),
                        ],
                        hidden=False,
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_schema(
            schema_name=schema_name, tables=tables, id=id, request_options=request_options
        )
        return _response.data

    async def delete_schema_by_name(
        self, *, schema_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Deletes an existing schema configuration using its name

        Parameters
        ----------
        schema_name : str
            Name of the schema to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Schema deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sql_schema.delete_schema_by_name(
                schema_name="schemaName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_schema_by_name(
            schema_name=schema_name, request_options=request_options
        )
        return _response.data

    async def gen_tables(
        self, entity_model_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TableConfigDto:
        """
        Generates table configurations based on entity model ID

        Parameters
        ----------
        entity_model_id : str
            The entity model id to generate tables from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TableConfigDto
            Tables generated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sql_schema.gen_tables(
                entity_model_id="entityModelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gen_tables(entity_model_id, request_options=request_options)
        return _response.data

    async def get_schemas(self, *, request_options: typing.Optional[RequestOptions] = None) -> SchemaConfigDto:
        """
        Retrieves all available schema configurations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaConfigDto
            List of schemas retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sql_schema.get_schemas()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schemas(request_options=request_options)
        return _response.data

    async def put_schema(
        self, schema_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaConfigDto:
        """
        Creates a new schema configuration that includes all available entity models with their complete field structures

        Parameters
        ----------
        schema_name : str
            Name for the new schema. The name can have a maximum of 1024 characters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaConfigDto
            Schema created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sql_schema.put_schema(
                schema_name="schemaName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_schema(schema_name, request_options=request_options)
        return _response.data

    async def update_tables(
        self, entity_model_id: str, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TableConfigDto:
        """
        Synchronizes given table configurations with the current entity model structure, preserving custom settings while incorporating any model changes

        Parameters
        ----------
        entity_model_id : str
            The entity model ID to update tables from

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TableConfigDto
            Tables updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sql_schema.update_tables(
                entity_model_id="entityModelId",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_tables(
            entity_model_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_schema(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SchemaConfigDto:
        """
        Retrieves a schema configuration using its UUID

        Parameters
        ----------
        schema_id : str
            UUID of the schema to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemaConfigDto
            Schema found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sql_schema.get_schema(
                schema_id="schemaId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schema(schema_id, request_options=request_options)
        return _response.data

    async def delete_schema(self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Deletes a schema configuration using its UUID

        Parameters
        ----------
        schema_id : str
            UUID of the schema to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Schema deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sql_schema.delete_schema(
                schema_id="schemaId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_schema(schema_id, request_options=request_options)
        return _response.data
