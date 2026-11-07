

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.entity import Entity
from ..types.entity_type import EntityType
from ..types.id import Id
from ..types.order import Order
from .raw_client import AsyncRawEntitiesClient, RawEntitiesClient
from .types.list_entities_request_sort import ListEntitiesRequestSort
from .types.list_entities_response import ListEntitiesResponse


class EntitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEntitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEntitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEntitiesClient
        """
        return self._raw_client

    def list_entities(
        self,
        *,
        member_of: typing.Optional[str] = None,
        entity_type: typing.Optional[typing.Union[EntityType, typing.Sequence[EntityType]]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[ListEntitiesRequestSort] = None,
        order: typing.Optional[Order] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEntitiesResponse:
        """
        Retrieve and list the entities in a collection. This endpoint returns key metadata describing each entity (e.g., ID, name, description). The response can be filtered, paginated, and sorted, allowing clients to navigate large archives efficiently.

        Parameters
        ----------
        member_of : typing.Optional[str]
            Indicates that an entity is a member of another entity (e.g., a sub-collection). Use this parameter to filter results to only entities that belong to a certain parent.

        entity_type : typing.Optional[typing.Union[EntityType, typing.Sequence[EntityType]]]
            Restrict the types of entities that are returned by specifying which RO-Crate profiles they conform to. Any valid entity type URI may be used; if no entities match the given type, an empty list is returned.

        limit : typing.Optional[int]
            Maximum number of entities to return.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, useful for pagination.

        sort : typing.Optional[ListEntitiesRequestSort]
            Field to sort by, such as `name` or `createdAt`.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEntitiesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.entities.list_entities(
            member_of="https://catalog.paradisec.org.au/repository/NT1",
            entity_type=["http://pcdm.org/models#Collection"],
        )
        """
        _response = self._raw_client.list_entities(
            member_of=member_of,
            entity_type=entity_type,
            limit=limit,
            offset=offset,
            sort=sort,
            order=order,
            request_options=request_options,
        )
        return _response.data

    def get_entity(self, id: Id, *, request_options: typing.Optional[RequestOptions] = None) -> Entity:
        """
        Retrieve an entity in a collection. This endpoint returns key metadata describing each entity (e.g., ID, name, description).

        Parameters
        ----------
        id : Id
            The unique RO-Crate ID representing a specific entity in the repository.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Entity
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.entities.get_entity(
            id="https://catalog.paradisec.org.au/repository/NT1/001",
        )
        """
        _response = self._raw_client.get_entity(id, request_options=request_options)
        return _response.data

    def delete_entity(self, id: Id, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Delete an entity that no RO-Crate contributes to — its `roCrateIds` is empty. Such entities (for example an Organisation whose last contributing RO-Crate was deleted but which the implementation chose to retain) cannot be reached by any deposit-session operation, so this is the one entity-level write.

        An entity with contributing RO-Crates cannot be deleted directly — its lifecycle is governed by its RO-Crates — and the request is rejected with `409 Conflict`.

        After deletion the entity's URI follows the implementation's declared `tombstonePolicy`.

        Parameters
        ----------
        id : Id
            The unique RO-Crate ID representing a specific entity in the repository.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.entities.delete_entity(
            id="https://catalog.paradisec.org.au/repository/NT1/001",
        )
        """
        _response = self._raw_client.delete_entity(id, request_options=request_options)
        return _response.data

    def get_entity_metadata(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Retrieve the entity's RO-Crate Metadata Document: the complete JSON-LD conforming to the RO-Crate specification. This is the metadata document itself, not the summary `Entity` object returned by `GET /entity/{id}`.

        This endpoint works for any entity type: Collection, Object, or MediaObject.

        The returned document's provenance is implementation-defined: it may be a stored metadata document, or a view derived from the metadata documents of the entity's contributing RO-Crates. Either way it MUST be a valid RO-Crate whose root data entity describes this entity. To retrieve the original deposited metadata document verbatim, use `GET /ro-crate/{id}/metadata` (available where the implementation supports deposit).

        Parameters
        ----------
        id : Id
            The RO-Crate entity ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Returns the RO-Crate JSON-LD metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.entities.get_entity_metadata(
            id="https://catalog.paradisec.org.au/repository/NT1/001",
        )
        """
        _response = self._raw_client.get_entity_metadata(id, request_options=request_options)
        return _response.data

    def head_entity_metadata(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Retrieve RO-Crate metadata headers without downloading the metadata content. Returns the same headers as GET but with no response body, useful for checking metadata availability and caching information.

        Parameters
        ----------
        id : Id
            The RO-Crate entity ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.entities.head_entity_metadata(
            id="https://catalog.paradisec.org.au/repository/NT1/001",
        )
        """
        _response = self._raw_client.head_entity_metadata(id, request_options=request_options)
        return _response.headers


class AsyncEntitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEntitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEntitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEntitiesClient
        """
        return self._raw_client

    async def list_entities(
        self,
        *,
        member_of: typing.Optional[str] = None,
        entity_type: typing.Optional[typing.Union[EntityType, typing.Sequence[EntityType]]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[ListEntitiesRequestSort] = None,
        order: typing.Optional[Order] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEntitiesResponse:
        """
        Retrieve and list the entities in a collection. This endpoint returns key metadata describing each entity (e.g., ID, name, description). The response can be filtered, paginated, and sorted, allowing clients to navigate large archives efficiently.

        Parameters
        ----------
        member_of : typing.Optional[str]
            Indicates that an entity is a member of another entity (e.g., a sub-collection). Use this parameter to filter results to only entities that belong to a certain parent.

        entity_type : typing.Optional[typing.Union[EntityType, typing.Sequence[EntityType]]]
            Restrict the types of entities that are returned by specifying which RO-Crate profiles they conform to. Any valid entity type URI may be used; if no entities match the given type, an empty list is returned.

        limit : typing.Optional[int]
            Maximum number of entities to return.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, useful for pagination.

        sort : typing.Optional[ListEntitiesRequestSort]
            Field to sort by, such as `name` or `createdAt`.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEntitiesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.entities.list_entities(
                member_of="https://catalog.paradisec.org.au/repository/NT1",
                entity_type=["http://pcdm.org/models#Collection"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_entities(
            member_of=member_of,
            entity_type=entity_type,
            limit=limit,
            offset=offset,
            sort=sort,
            order=order,
            request_options=request_options,
        )
        return _response.data

    async def get_entity(self, id: Id, *, request_options: typing.Optional[RequestOptions] = None) -> Entity:
        """
        Retrieve an entity in a collection. This endpoint returns key metadata describing each entity (e.g., ID, name, description).

        Parameters
        ----------
        id : Id
            The unique RO-Crate ID representing a specific entity in the repository.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Entity
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.entities.get_entity(
                id="https://catalog.paradisec.org.au/repository/NT1/001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entity(id, request_options=request_options)
        return _response.data

    async def delete_entity(self, id: Id, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Delete an entity that no RO-Crate contributes to — its `roCrateIds` is empty. Such entities (for example an Organisation whose last contributing RO-Crate was deleted but which the implementation chose to retain) cannot be reached by any deposit-session operation, so this is the one entity-level write.

        An entity with contributing RO-Crates cannot be deleted directly — its lifecycle is governed by its RO-Crates — and the request is rejected with `409 Conflict`.

        After deletion the entity's URI follows the implementation's declared `tombstonePolicy`.

        Parameters
        ----------
        id : Id
            The unique RO-Crate ID representing a specific entity in the repository.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.entities.delete_entity(
                id="https://catalog.paradisec.org.au/repository/NT1/001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_entity(id, request_options=request_options)
        return _response.data

    async def get_entity_metadata(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Retrieve the entity's RO-Crate Metadata Document: the complete JSON-LD conforming to the RO-Crate specification. This is the metadata document itself, not the summary `Entity` object returned by `GET /entity/{id}`.

        This endpoint works for any entity type: Collection, Object, or MediaObject.

        The returned document's provenance is implementation-defined: it may be a stored metadata document, or a view derived from the metadata documents of the entity's contributing RO-Crates. Either way it MUST be a valid RO-Crate whose root data entity describes this entity. To retrieve the original deposited metadata document verbatim, use `GET /ro-crate/{id}/metadata` (available where the implementation supports deposit).

        Parameters
        ----------
        id : Id
            The RO-Crate entity ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Returns the RO-Crate JSON-LD metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.entities.get_entity_metadata(
                id="https://catalog.paradisec.org.au/repository/NT1/001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entity_metadata(id, request_options=request_options)
        return _response.data

    async def head_entity_metadata(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Retrieve RO-Crate metadata headers without downloading the metadata content. Returns the same headers as GET but with no response body, useful for checking metadata availability and caching information.

        Parameters
        ----------
        id : Id
            The RO-Crate entity ID.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.entities.head_entity_metadata(
                id="https://catalog.paradisec.org.au/repository/NT1/001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_entity_metadata(id, request_options=request_options)
        return _response.headers
