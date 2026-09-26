

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAliasOperationsV2Client, RawAliasOperationsV2Client
from .types.post_v2vectordb_aliases_alter_response import PostV2VectordbAliasesAlterResponse
from .types.post_v2vectordb_aliases_create_response import PostV2VectordbAliasesCreateResponse
from .types.post_v2vectordb_aliases_describe_response import PostV2VectordbAliasesDescribeResponse
from .types.post_v2vectordb_aliases_drop_response import PostV2VectordbAliasesDropResponse
from .types.post_v2vectordb_aliases_list_response import PostV2VectordbAliasesListResponse


OMIT = typing.cast(typing.Any, ...)


class AliasOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAliasOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAliasOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAliasOperationsV2Client
        """
        return self._raw_client

    def list_aliases(
        self, *, db_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbAliasesListResponse:
        """
        This operation lists all existing collection aliases.

        Parameters
        ----------
        db_name : str
            The name of an existing database. The value defaults to __default__.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbAliasesListResponse
            A list of collection aliases.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.alias_operations_v2.list_aliases(
            db_name="dbName",
        )
        """
        _response = self._raw_client.list_aliases(db_name=db_name, request_options=request_options)
        return _response.data

    def describe_alias(
        self, *, db_name: str, alias_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbAliasesDescribeResponse:
        """
        This operation describes the details of a specific alias.

        Parameters
        ----------
        db_name : str
            The name of the database to which the collection belongs.

        alias_name : str
            The name of the alias whose details are to be listed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbAliasesDescribeResponse
            An alias object that contains the detailed description of an alias.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.alias_operations_v2.describe_alias(
            db_name="dbName",
            alias_name="aliasName",
        )
        """
        _response = self._raw_client.describe_alias(
            db_name=db_name, alias_name=alias_name, request_options=request_options
        )
        return _response.data

    def alter_alias(
        self,
        *,
        collection_name: str,
        alias_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbAliasesAlterResponse:
        """
        This operation reassigns the alias of one collection to another.

        Parameters
        ----------
        collection_name : str
            The name of the target collection to reassign an alias to.

        alias_name : str
            The alias of the collection.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbAliasesAlterResponse
            None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.alias_operations_v2.alter_alias(
            collection_name="collectionName",
            alias_name="aliasName",
        )
        """
        _response = self._raw_client.alter_alias(
            collection_name=collection_name, alias_name=alias_name, db_name=db_name, request_options=request_options
        )
        return _response.data

    def drop_alias(
        self,
        *,
        collection_name: str,
        alias_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbAliasesDropResponse:
        """
        This operation drops a specified alias.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which the alias is assigned to.

        alias_name : str
            The alias to drop.
            When dropping an alias, you do not need to provide the collection name because one alias can only be assigned to exactly one collection. Therefore, the server knows which collection the specified alias belongs to.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbAliasesDropResponse
            None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.alias_operations_v2.drop_alias(
            collection_name="collectionName",
            alias_name="aliasName",
        )
        """
        _response = self._raw_client.drop_alias(
            collection_name=collection_name, alias_name=alias_name, db_name=db_name, request_options=request_options
        )
        return _response.data

    def create_alias(
        self,
        *,
        collection_name: str,
        alias_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbAliasesCreateResponse:
        """
        This operation creates an alias for an existing collection.

        Parameters
        ----------
        collection_name : str
            The name of the target collection to reassign an alias to.

        alias_name : str
            The alias of the collection.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbAliasesCreateResponse
            None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.alias_operations_v2.create_alias(
            collection_name="collectionName",
            alias_name="aliasName",
        )
        """
        _response = self._raw_client.create_alias(
            collection_name=collection_name, alias_name=alias_name, db_name=db_name, request_options=request_options
        )
        return _response.data


class AsyncAliasOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAliasOperationsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAliasOperationsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAliasOperationsV2Client
        """
        return self._raw_client

    async def list_aliases(
        self, *, db_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbAliasesListResponse:
        """
        This operation lists all existing collection aliases.

        Parameters
        ----------
        db_name : str
            The name of an existing database. The value defaults to __default__.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbAliasesListResponse
            A list of collection aliases.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.alias_operations_v2.list_aliases(
                db_name="dbName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_aliases(db_name=db_name, request_options=request_options)
        return _response.data

    async def describe_alias(
        self, *, db_name: str, alias_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV2VectordbAliasesDescribeResponse:
        """
        This operation describes the details of a specific alias.

        Parameters
        ----------
        db_name : str
            The name of the database to which the collection belongs.

        alias_name : str
            The name of the alias whose details are to be listed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbAliasesDescribeResponse
            An alias object that contains the detailed description of an alias.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.alias_operations_v2.describe_alias(
                db_name="dbName",
                alias_name="aliasName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.describe_alias(
            db_name=db_name, alias_name=alias_name, request_options=request_options
        )
        return _response.data

    async def alter_alias(
        self,
        *,
        collection_name: str,
        alias_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbAliasesAlterResponse:
        """
        This operation reassigns the alias of one collection to another.

        Parameters
        ----------
        collection_name : str
            The name of the target collection to reassign an alias to.

        alias_name : str
            The alias of the collection.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbAliasesAlterResponse
            None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.alias_operations_v2.alter_alias(
                collection_name="collectionName",
                alias_name="aliasName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.alter_alias(
            collection_name=collection_name, alias_name=alias_name, db_name=db_name, request_options=request_options
        )
        return _response.data

    async def drop_alias(
        self,
        *,
        collection_name: str,
        alias_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbAliasesDropResponse:
        """
        This operation drops a specified alias.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which the alias is assigned to.

        alias_name : str
            The alias to drop.
            When dropping an alias, you do not need to provide the collection name because one alias can only be assigned to exactly one collection. Therefore, the server knows which collection the specified alias belongs to.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbAliasesDropResponse
            None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.alias_operations_v2.drop_alias(
                collection_name="collectionName",
                alias_name="aliasName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.drop_alias(
            collection_name=collection_name, alias_name=alias_name, db_name=db_name, request_options=request_options
        )
        return _response.data

    async def create_alias(
        self,
        *,
        collection_name: str,
        alias_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV2VectordbAliasesCreateResponse:
        """
        This operation creates an alias for an existing collection.

        Parameters
        ----------
        collection_name : str
            The name of the target collection to reassign an alias to.

        alias_name : str
            The alias of the collection.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV2VectordbAliasesCreateResponse
            None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            request_timeout="YOUR_REQUEST_TIMEOUT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.alias_operations_v2.create_alias(
                collection_name="collectionName",
                alias_name="aliasName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_alias(
            collection_name=collection_name, alias_name=alias_name, db_name=db_name, request_options=request_options
        )
        return _response.data
