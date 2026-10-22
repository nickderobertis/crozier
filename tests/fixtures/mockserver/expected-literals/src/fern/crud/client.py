

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCrudClient, RawCrudClient
from .types.crud_expectations_definition_id_strategy import CrudExpectationsDefinitionIdStrategy
from .types.put_mockserver_crud_response import PutMockserverCrudResponse


OMIT = typing.cast(typing.Any, ...)


class CrudClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrudClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrudClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrudClient
        """
        return self._raw_client

    def register_a_generated_crud_data_store(
        self,
        *,
        base_path: str,
        id_field: typing.Optional[str] = OMIT,
        id_strategy: typing.Optional[CrudExpectationsDefinitionIdStrategy] = OMIT,
        initial_data: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverCrudResponse:
        """
        Registers a REST resource backed by an in-memory data store that automatically handles list, read, create, update and delete operations under the supplied base path.

        Parameters
        ----------
        base_path : str
            base path the CRUD resource is served under (e.g. /api/users)

        id_field : typing.Optional[str]
            name of the field used as the resource identifier

        id_strategy : typing.Optional[CrudExpectationsDefinitionIdStrategy]
            strategy used to generate identifiers for newly created resources

        initial_data : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            initial records to seed the data store with

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverCrudResponse
            CRUD resource registered

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crud.register_a_generated_crud_data_store(
            base_path="/api/users",
            id_field="id",
            id_strategy="AUTO_INCREMENT",
            initial_data=[
                {"id": 1, "name": "Alice", "email": "alice@example.com"},
                {"id": 2, "name": "Bob", "email": "bob@example.com"},
            ],
        )
        """
        _response = self._raw_client.register_a_generated_crud_data_store(
            base_path=base_path,
            id_field=id_field,
            id_strategy=id_strategy,
            initial_data=initial_data,
            request_options=request_options,
        )
        return _response.data


class AsyncCrudClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrudClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrudClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrudClient
        """
        return self._raw_client

    async def register_a_generated_crud_data_store(
        self,
        *,
        base_path: str,
        id_field: typing.Optional[str] = OMIT,
        id_strategy: typing.Optional[CrudExpectationsDefinitionIdStrategy] = OMIT,
        initial_data: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverCrudResponse:
        """
        Registers a REST resource backed by an in-memory data store that automatically handles list, read, create, update and delete operations under the supplied base path.

        Parameters
        ----------
        base_path : str
            base path the CRUD resource is served under (e.g. /api/users)

        id_field : typing.Optional[str]
            name of the field used as the resource identifier

        id_strategy : typing.Optional[CrudExpectationsDefinitionIdStrategy]
            strategy used to generate identifiers for newly created resources

        initial_data : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            initial records to seed the data store with

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverCrudResponse
            CRUD resource registered

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crud.register_a_generated_crud_data_store(
                base_path="/api/users",
                id_field="id",
                id_strategy="AUTO_INCREMENT",
                initial_data=[
                    {"id": 1, "name": "Alice", "email": "alice@example.com"},
                    {"id": 2, "name": "Bob", "email": "bob@example.com"},
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_a_generated_crud_data_store(
            base_path=base_path,
            id_field=id_field,
            id_strategy=id_strategy,
            initial_data=initial_data,
            request_options=request_options,
        )
        return _response.data
