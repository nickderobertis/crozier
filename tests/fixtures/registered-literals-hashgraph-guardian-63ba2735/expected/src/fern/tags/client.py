

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.schema import Schema
from ..types.schema_document import SchemaDocument
from ..types.tag import Tag
from ..types.tag_entity import TagEntity
from ..types.tag_map import TagMap
from ..types.tag_operation import TagOperation
from ..types.tag_status import TagStatus
from .raw_client import AsyncRawTagsClient, RawTagsClient
from .types.post_tags_search_request import PostTagsSearchRequest
from .types.post_tags_search_response import PostTagsSearchResponse
from .types.post_tags_synchronization_request_entity import PostTagsSynchronizationRequestEntity


OMIT = typing.cast(typing.Any, ...)


class TagsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTagsClient
        """
        return self._raw_client

    def tags_api_set_tags(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
        client.tags.tags_api_set_tags()
        """
        _response = self._raw_client.tags_api_set_tags(request_options=request_options)
        return _response.data

    def search_tags(
        self, *, request: PostTagsSearchRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostTagsSearchResponse:
        """
        Search tags.

        Parameters
        ----------
        request : PostTagsSearchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostTagsSearchResponse
            Successful operation.

        Examples
        --------
        from fern.tags import (
            PostTagsSearchRequestTarget,
            PostTagsSearchRequestTargetEntity,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.search_tags(
            request=PostTagsSearchRequestTarget(
                entity=PostTagsSearchRequestTargetEntity.POLICY_DOCUMENT,
                target="targetId1",
            ),
        )
        """
        _response = self._raw_client.search_tags(request=request, request_options=request_options)
        return _response.data

    def delete_tag(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Delete tag.

        Parameters
        ----------
        uuid_ : str
            Tag identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.delete_tag(
            uuid_="00000000-0000-0000-0000-000000000000",
        )
        """
        _response = self._raw_client.delete_tag(uuid_, request_options=request_options)
        return _response.data

    def synchronization(
        self,
        *,
        entity: PostTagsSynchronizationRequestEntity,
        target: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TagMap:
        """
        synchronization.

        Parameters
        ----------
        entity : PostTagsSynchronizationRequestEntity

        target : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagMap
            Successful operation.

        Examples
        --------
        from fern.tags import PostTagsSynchronizationRequestEntity

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.synchronization(
            entity=PostTagsSynchronizationRequestEntity.SCHEMA,
            target="targetId",
        )
        """
        _response = self._raw_client.synchronization(entity=entity, target=target, request_options=request_options)
        return _response.data

    def returns_all_schemas(
        self,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Returns all schema.

        Parameters
        ----------
        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.returns_all_schemas()
        """
        _response = self._raw_client.returns_all_schemas(
            page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    def creates_new_schema(
        self,
        *,
        id: str,
        name: str,
        description: str,
        entity: str,
        document: SchemaDocument,
        iri: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Schema:
        """
        Creates new schema. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str

        name : str

        description : str

        entity : str

        document : SchemaDocument

        iri : typing.Optional[str]

        uuid_ : typing.Optional[str]

        hash : typing.Optional[str]

        status : typing.Optional[str]

        topic_id : typing.Optional[str]

        version : typing.Optional[str]

        owner : typing.Optional[str]

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schema
            Created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.creates_new_schema(
            id="id",
            name="name",
            description="description",
            entity="entity",
            document="document",
        )
        """
        _response = self._raw_client.creates_new_schema(
            id=id,
            name=name,
            description=description,
            entity=entity,
            document=document,
            iri=iri,
            uuid_=uuid_,
            hash=hash,
            status=status,
            topic_id=topic_id,
            version=version,
            owner=owner,
            message_id=message_id,
            request_options=request_options,
        )
        return _response.data

    def updates_the_schema(
        self,
        schema_id: str,
        *,
        id: str,
        name: str,
        description: str,
        entity: str,
        document: SchemaDocument,
        iri: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Updates the schema with the provided schema ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        id : str

        name : str

        description : str

        entity : str

        document : SchemaDocument

        iri : typing.Optional[str]

        uuid_ : typing.Optional[str]

        hash : typing.Optional[str]

        status : typing.Optional[str]

        topic_id : typing.Optional[str]

        version : typing.Optional[str]

        owner : typing.Optional[str]

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.updates_the_schema(
            schema_id="schemaId",
            id="id",
            name="name",
            description="description",
            entity="entity",
            document="document",
        )
        """
        _response = self._raw_client.updates_the_schema(
            schema_id,
            id=id,
            name=name,
            description=description,
            entity=entity,
            document=document,
            iri=iri,
            uuid_=uuid_,
            hash=hash,
            status=status,
            topic_id=topic_id,
            version=version,
            owner=owner,
            message_id=message_id,
            request_options=request_options,
        )
        return _response.data

    def delete_the_schema(self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Deletes the schema with the provided schema ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.delete_the_schema(
            schema_id="schemaId",
        )
        """
        _response = self._raw_client.delete_the_schema(schema_id, request_options=request_options)
        return _response.data

    def publishes_the_schema(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Schema]:
        """
        Publishes the schema with the provided (internal) schema ID onto IPFS, sends a message featuring IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.publishes_the_schema(
            schema_id="schemaId",
        )
        """
        _response = self._raw_client.publishes_the_schema(schema_id, request_options=request_options)
        return _response.data

    def return_a_list_of_all_published_schemas(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Schema]:
        """
        Return a list of all published schemas.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.return_a_list_of_all_published_schemas()
        """
        _response = self._raw_client.return_a_list_of_all_published_schemas(request_options=request_options)
        return _response.data

    def creates_new_tag(
        self,
        *,
        name: str,
        entity: TagEntity,
        local_target: str,
        uuid_: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        target: typing.Optional[str] = OMIT,
        status: typing.Optional[TagStatus] = OMIT,
        operation: typing.Optional[TagOperation] = OMIT,
        date: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        policy_id: typing.Optional[str] = OMIT,
        uri: typing.Optional[str] = OMIT,
        document: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tag:
        """
        Creates new tag.

        Parameters
        ----------
        name : str

        entity : TagEntity

        local_target : str

        uuid_ : typing.Optional[str]

        description : typing.Optional[str]

        owner : typing.Optional[str]

        target : typing.Optional[str]

        status : typing.Optional[TagStatus]

        operation : typing.Optional[TagOperation]

        date : typing.Optional[str]

        topic_id : typing.Optional[str]

        message_id : typing.Optional[str]

        policy_id : typing.Optional[str]

        uri : typing.Optional[str]

        document : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Created.

        Examples
        --------
        from fern import FernApi, TagEntity

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tags.creates_new_tag(
            name="Tag label",
            entity=TagEntity.SCHEMA,
            local_target="db id",
        )
        """
        _response = self._raw_client.creates_new_tag(
            name=name,
            entity=entity,
            local_target=local_target,
            uuid_=uuid_,
            description=description,
            owner=owner,
            target=target,
            status=status,
            operation=operation,
            date=date,
            topic_id=topic_id,
            message_id=message_id,
            policy_id=policy_id,
            uri=uri,
            document=document,
            request_options=request_options,
        )
        return _response.data


class AsyncTagsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTagsClient
        """
        return self._raw_client

    async def tags_api_set_tags(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            await client.tags.tags_api_set_tags()


        asyncio.run(main())
        """
        _response = await self._raw_client.tags_api_set_tags(request_options=request_options)
        return _response.data

    async def search_tags(
        self, *, request: PostTagsSearchRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostTagsSearchResponse:
        """
        Search tags.

        Parameters
        ----------
        request : PostTagsSearchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostTagsSearchResponse
            Successful operation.

        Examples
        --------
        import asyncio

        from fern.tags import (
            PostTagsSearchRequestTarget,
            PostTagsSearchRequestTargetEntity,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.search_tags(
                request=PostTagsSearchRequestTarget(
                    entity=PostTagsSearchRequestTargetEntity.POLICY_DOCUMENT,
                    target="targetId1",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_tags(request=request, request_options=request_options)
        return _response.data

    async def delete_tag(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Delete tag.

        Parameters
        ----------
        uuid_ : str
            Tag identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.delete_tag(
                uuid_="00000000-0000-0000-0000-000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_tag(uuid_, request_options=request_options)
        return _response.data

    async def synchronization(
        self,
        *,
        entity: PostTagsSynchronizationRequestEntity,
        target: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TagMap:
        """
        synchronization.

        Parameters
        ----------
        entity : PostTagsSynchronizationRequestEntity

        target : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TagMap
            Successful operation.

        Examples
        --------
        import asyncio

        from fern.tags import PostTagsSynchronizationRequestEntity

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.synchronization(
                entity=PostTagsSynchronizationRequestEntity.SCHEMA,
                target="targetId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.synchronization(
            entity=entity, target=target, request_options=request_options
        )
        return _response.data

    async def returns_all_schemas(
        self,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Returns all schema.

        Parameters
        ----------
        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.returns_all_schemas()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_schemas(
            page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def creates_new_schema(
        self,
        *,
        id: str,
        name: str,
        description: str,
        entity: str,
        document: SchemaDocument,
        iri: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Schema:
        """
        Creates new schema. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str

        name : str

        description : str

        entity : str

        document : SchemaDocument

        iri : typing.Optional[str]

        uuid_ : typing.Optional[str]

        hash : typing.Optional[str]

        status : typing.Optional[str]

        topic_id : typing.Optional[str]

        version : typing.Optional[str]

        owner : typing.Optional[str]

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Schema
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.creates_new_schema(
                id="id",
                name="name",
                description="description",
                entity="entity",
                document="document",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_new_schema(
            id=id,
            name=name,
            description=description,
            entity=entity,
            document=document,
            iri=iri,
            uuid_=uuid_,
            hash=hash,
            status=status,
            topic_id=topic_id,
            version=version,
            owner=owner,
            message_id=message_id,
            request_options=request_options,
        )
        return _response.data

    async def updates_the_schema(
        self,
        schema_id: str,
        *,
        id: str,
        name: str,
        description: str,
        entity: str,
        document: SchemaDocument,
        iri: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Schema]:
        """
        Updates the schema with the provided schema ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        id : str

        name : str

        description : str

        entity : str

        document : SchemaDocument

        iri : typing.Optional[str]

        uuid_ : typing.Optional[str]

        hash : typing.Optional[str]

        status : typing.Optional[str]

        topic_id : typing.Optional[str]

        version : typing.Optional[str]

        owner : typing.Optional[str]

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.updates_the_schema(
                schema_id="schemaId",
                id="id",
                name="name",
                description="description",
                entity="entity",
                document="document",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_the_schema(
            schema_id,
            id=id,
            name=name,
            description=description,
            entity=entity,
            document=document,
            iri=iri,
            uuid_=uuid_,
            hash=hash,
            status=status,
            topic_id=topic_id,
            version=version,
            owner=owner,
            message_id=message_id,
            request_options=request_options,
        )
        return _response.data

    async def delete_the_schema(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Deletes the schema with the provided schema ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.delete_the_schema(
                schema_id="schemaId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_the_schema(schema_id, request_options=request_options)
        return _response.data

    async def publishes_the_schema(
        self, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Schema]:
        """
        Publishes the schema with the provided (internal) schema ID onto IPFS, sends a message featuring IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        schema_id : str
            Schema ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.publishes_the_schema(
                schema_id="schemaId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publishes_the_schema(schema_id, request_options=request_options)
        return _response.data

    async def return_a_list_of_all_published_schemas(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Schema]:
        """
        Return a list of all published schemas.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Schema]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.return_a_list_of_all_published_schemas()


        asyncio.run(main())
        """
        _response = await self._raw_client.return_a_list_of_all_published_schemas(request_options=request_options)
        return _response.data

    async def creates_new_tag(
        self,
        *,
        name: str,
        entity: TagEntity,
        local_target: str,
        uuid_: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        target: typing.Optional[str] = OMIT,
        status: typing.Optional[TagStatus] = OMIT,
        operation: typing.Optional[TagOperation] = OMIT,
        date: typing.Optional[str] = OMIT,
        topic_id: typing.Optional[str] = OMIT,
        message_id: typing.Optional[str] = OMIT,
        policy_id: typing.Optional[str] = OMIT,
        uri: typing.Optional[str] = OMIT,
        document: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tag:
        """
        Creates new tag.

        Parameters
        ----------
        name : str

        entity : TagEntity

        local_target : str

        uuid_ : typing.Optional[str]

        description : typing.Optional[str]

        owner : typing.Optional[str]

        target : typing.Optional[str]

        status : typing.Optional[TagStatus]

        operation : typing.Optional[TagOperation]

        date : typing.Optional[str]

        topic_id : typing.Optional[str]

        message_id : typing.Optional[str]

        policy_id : typing.Optional[str]

        uri : typing.Optional[str]

        document : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tag
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TagEntity

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tags.creates_new_tag(
                name="Tag label",
                entity=TagEntity.SCHEMA,
                local_target="db id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_new_tag(
            name=name,
            entity=entity,
            local_target=local_target,
            uuid_=uuid_,
            description=description,
            owner=owner,
            target=target,
            status=status,
            operation=operation,
            date=date,
            topic_id=topic_id,
            message_id=message_id,
            policy_id=policy_id,
            uri=uri,
            document=document,
            request_options=request_options,
        )
        return _response.data
