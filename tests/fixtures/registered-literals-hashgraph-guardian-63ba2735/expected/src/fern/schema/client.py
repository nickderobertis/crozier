

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.schema import Schema
from ..types.schema_dto import SchemaDto
from .raw_client import AsyncRawSchemaClient, RawSchemaClient
from .types.single_schema_api_get_schema_tree_response import SingleSchemaApiGetSchemaTreeResponse


class SchemaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSchemaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSchemaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSchemaClient
        """
        return self._raw_client

    def returns_schema_by_schema_id(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Schema:
        """
        Returns schema by schema ID.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schema
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schema.returns_schema_by_schema_id(
            schema_id="schemaId",
        )
        """
        _response = self._raw_client.returns_schema_by_schema_id(schema_id, request_options=request_options)
        return _response.data

    def single_schema_api_get_schema_parents(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SchemaDto]:
        """
        Returns all parent schemas.

        Parameters
        ----------
        schema_id : str
            Schema identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SchemaDto]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schema.single_schema_api_get_schema_parents(
            schema_id="schemaId",
        )
        """
        _response = self._raw_client.single_schema_api_get_schema_parents(schema_id, request_options=request_options)
        return _response.data

    def single_schema_api_get_schema_tree(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SingleSchemaApiGetSchemaTreeResponse:
        """
        Returns schema tree.

        Parameters
        ----------
        schema_id : str
            Schema identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SingleSchemaApiGetSchemaTreeResponse
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.schema.single_schema_api_get_schema_tree(
            schema_id="schemaId",
        )
        """
        _response = self._raw_client.single_schema_api_get_schema_tree(schema_id, request_options=request_options)
        return _response.data


class AsyncSchemaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSchemaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSchemaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSchemaClient
        """
        return self._raw_client

    async def returns_schema_by_schema_id(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Schema:
        """
        Returns schema by schema ID.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schema
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schema.returns_schema_by_schema_id(
                schema_id="schemaId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_schema_by_schema_id(schema_id, request_options=request_options)
        return _response.data

    async def single_schema_api_get_schema_parents(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SchemaDto]:
        """
        Returns all parent schemas.

        Parameters
        ----------
        schema_id : str
            Schema identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SchemaDto]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schema.single_schema_api_get_schema_parents(
                schema_id="schemaId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.single_schema_api_get_schema_parents(
            schema_id, request_options=request_options
        )
        return _response.data

    async def single_schema_api_get_schema_tree(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SingleSchemaApiGetSchemaTreeResponse:
        """
        Returns schema tree.

        Parameters
        ----------
        schema_id : str
            Schema identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SingleSchemaApiGetSchemaTreeResponse
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.schema.single_schema_api_get_schema_tree(
                schema_id="schemaId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.single_schema_api_get_schema_tree(schema_id, request_options=request_options)
        return _response.data
