

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.connection_response import ConnectionResponse
from ..types.type import Type
from .raw_client import AsyncRawConnectionsClient, RawConnectionsClient
from .types.get_api_connections_id_collections_response import GetApiConnectionsIdCollectionsResponse
from .types.post_api_connections_validate_response import PostApiConnectionsValidateResponse


OMIT = typing.cast(typing.Any, ...)


class ConnectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConnectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConnectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConnectionsClient
        """
        return self._raw_client

    def returns_all_available_connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ConnectionResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ConnectionResponse]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connections.returns_all_available_connections()
        """
        _response = self._raw_client.returns_all_available_connections(request_options=request_options)
        return _response.data

    def creates_new_connection(
        self,
        *,
        name: str,
        type: Type,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        name : str

        type : Type

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        from fern import FernApi, Type

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connections.creates_new_connection(
            name="name",
            type=Type.ORACLE,
        )
        """
        _response = self._raw_client.creates_new_connection(
            name=name, type=type, description=description, config=config, request_options=request_options
        )
        return _response.data

    def returns_a_list_of_json_schema_describing_the_required_field_for_a_connection(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connections.returns_a_list_of_json_schema_describing_the_required_field_for_a_connection()
        """
        _response = self._raw_client.returns_a_list_of_json_schema_describing_the_required_field_for_a_connection(
            request_options=request_options
        )
        return _response.data

    def verify_that_the_connection_is_valid(
        self,
        *,
        name: str,
        type: Type,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiConnectionsValidateResponse:
        """
        Parameters
        ----------
        name : str

        type : Type

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiConnectionsValidateResponse
            OK

        Examples
        --------
        from fern import FernApi, Type

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connections.verify_that_the_connection_is_valid(
            name="name",
            type=Type.ORACLE,
        )
        """
        _response = self._raw_client.verify_that_the_connection_is_valid(
            name=name, type=type, description=description, config=config, request_options=request_options
        )
        return _response.data

    def returns_a_connection_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connections.returns_a_connection_with_given_id(
            id=1000000,
        )
        """
        _response = self._raw_client.returns_a_connection_with_given_id(id, request_options=request_options)
        return _response.data

    def updates_an_existing_connection(
        self,
        id: int,
        *,
        name: str,
        type: Type,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        type : Type

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionResponse
            OK

        Examples
        --------
        from fern import FernApi, Type

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connections.updates_an_existing_connection(
            id=1000000,
            name="name",
            type=Type.ORACLE,
        )
        """
        _response = self._raw_client.updates_an_existing_connection(
            id, name=name, type=type, description=description, config=config, request_options=request_options
        )
        return _response.data

    def deletes_an_existing_connection(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connections.deletes_an_existing_connection(
            id=1000000,
        )
        """
        _response = self._raw_client.deletes_an_existing_connection(id, request_options=request_options)
        return _response.data

    def returns_a_list_of_collection_names_available_on_the_source(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiConnectionsIdCollectionsResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiConnectionsIdCollectionsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connections.returns_a_list_of_collection_names_available_on_the_source(
            id=1000000,
        )
        """
        _response = self._raw_client.returns_a_list_of_collection_names_available_on_the_source(
            id, request_options=request_options
        )
        return _response.data


class AsyncConnectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConnectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConnectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConnectionsClient
        """
        return self._raw_client

    async def returns_all_available_connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ConnectionResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ConnectionResponse]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connections.returns_all_available_connections()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_available_connections(request_options=request_options)
        return _response.data

    async def creates_new_connection(
        self,
        *,
        name: str,
        type: Type,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        name : str

        type : Type

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Type

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connections.creates_new_connection(
                name="name",
                type=Type.ORACLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_new_connection(
            name=name, type=type, description=description, config=config, request_options=request_options
        )
        return _response.data

    async def returns_a_list_of_json_schema_describing_the_required_field_for_a_connection(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connections.returns_a_list_of_json_schema_describing_the_required_field_for_a_connection()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_json_schema_describing_the_required_field_for_a_connection(
            request_options=request_options
        )
        return _response.data

    async def verify_that_the_connection_is_valid(
        self,
        *,
        name: str,
        type: Type,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostApiConnectionsValidateResponse:
        """
        Parameters
        ----------
        name : str

        type : Type

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiConnectionsValidateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Type

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connections.verify_that_the_connection_is_valid(
                name="name",
                type=Type.ORACLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_that_the_connection_is_valid(
            name=name, type=type, description=description, config=config, request_options=request_options
        )
        return _response.data

    async def returns_a_connection_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connections.returns_a_connection_with_given_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_connection_with_given_id(id, request_options=request_options)
        return _response.data

    async def updates_an_existing_connection(
        self,
        id: int,
        *,
        name: str,
        type: Type,
        description: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        type : Type

        description : typing.Optional[str]

        config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Type

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connections.updates_an_existing_connection(
                id=1000000,
                name="name",
                type=Type.ORACLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_an_existing_connection(
            id, name=name, type=type, description=description, config=config, request_options=request_options
        )
        return _response.data

    async def deletes_an_existing_connection(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connections.deletes_an_existing_connection(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_an_existing_connection(id, request_options=request_options)
        return _response.data

    async def returns_a_list_of_collection_names_available_on_the_source(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiConnectionsIdCollectionsResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiConnectionsIdCollectionsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connections.returns_a_list_of_collection_names_available_on_the_source(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_collection_names_available_on_the_source(
            id, request_options=request_options
        )
        return _response.data
