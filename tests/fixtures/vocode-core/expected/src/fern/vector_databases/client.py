

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.pinecone_vector_database import PineconeVectorDatabase
from ..types.pinecone_vector_database_params_type import PineconeVectorDatabaseParamsType
from ..types.pinecone_vector_database_update_params_api_environment import (
    PineconeVectorDatabaseUpdateParamsApiEnvironment,
)
from ..types.pinecone_vector_database_update_params_api_key import PineconeVectorDatabaseUpdateParamsApiKey
from ..types.pinecone_vector_database_update_params_index import PineconeVectorDatabaseUpdateParamsIndex
from ..types.pinecone_vector_database_update_params_type import PineconeVectorDatabaseUpdateParamsType
from ..types.vector_database_page import VectorDatabasePage
from .raw_client import AsyncRawVectorDatabasesClient, RawVectorDatabasesClient


OMIT = typing.cast(typing.Any, ...)


class VectorDatabasesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVectorDatabasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVectorDatabasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVectorDatabasesClient
        """
        return self._raw_client

    def get_vector_database(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PineconeVectorDatabase:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PineconeVectorDatabase
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vector_databases.get_vector_database(
            id="id",
        )
        """
        _response = self._raw_client.get_vector_database(id=id, request_options=request_options)
        return _response.data

    def list_vector_databases(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VectorDatabasePage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VectorDatabasePage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vector_databases.list_vector_databases()
        """
        _response = self._raw_client.list_vector_databases(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    def create_vector_database(
        self,
        *,
        type: PineconeVectorDatabaseParamsType,
        index: str,
        api_key: str,
        api_environment: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PineconeVectorDatabase:
        """
        Parameters
        ----------
        type : PineconeVectorDatabaseParamsType

        index : str

        api_key : str

        api_environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PineconeVectorDatabase
            Successful Response

        Examples
        --------
        from fern import FernApi, PineconeVectorDatabaseParamsType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vector_databases.create_vector_database(
            type=PineconeVectorDatabaseParamsType.VECTOR_DATABASE_PINECONE,
            index="index",
            api_key="api_key",
            api_environment="api_environment",
        )
        """
        _response = self._raw_client.create_vector_database(
            type=type, index=index, api_key=api_key, api_environment=api_environment, request_options=request_options
        )
        return _response.data

    def update_vector_database(
        self,
        *,
        id: str,
        type: PineconeVectorDatabaseUpdateParamsType,
        index: typing.Optional[PineconeVectorDatabaseUpdateParamsIndex] = OMIT,
        api_key: typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey] = OMIT,
        api_environment: typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PineconeVectorDatabase:
        """
        Parameters
        ----------
        id : str

        type : PineconeVectorDatabaseUpdateParamsType

        index : typing.Optional[PineconeVectorDatabaseUpdateParamsIndex]

        api_key : typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey]

        api_environment : typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PineconeVectorDatabase
            Successful Response

        Examples
        --------
        from fern import FernApi, PineconeVectorDatabaseUpdateParamsType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vector_databases.update_vector_database(
            id="id",
            type=PineconeVectorDatabaseUpdateParamsType.VECTOR_DATABASE_PINECONE,
        )
        """
        _response = self._raw_client.update_vector_database(
            id=id,
            type=type,
            index=index,
            api_key=api_key,
            api_environment=api_environment,
            request_options=request_options,
        )
        return _response.data


class AsyncVectorDatabasesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVectorDatabasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVectorDatabasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVectorDatabasesClient
        """
        return self._raw_client

    async def get_vector_database(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PineconeVectorDatabase:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PineconeVectorDatabase
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vector_databases.get_vector_database(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_vector_database(id=id, request_options=request_options)
        return _response.data

    async def list_vector_databases(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VectorDatabasePage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VectorDatabasePage
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vector_databases.list_vector_databases()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_vector_databases(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    async def create_vector_database(
        self,
        *,
        type: PineconeVectorDatabaseParamsType,
        index: str,
        api_key: str,
        api_environment: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PineconeVectorDatabase:
        """
        Parameters
        ----------
        type : PineconeVectorDatabaseParamsType

        index : str

        api_key : str

        api_environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PineconeVectorDatabase
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PineconeVectorDatabaseParamsType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vector_databases.create_vector_database(
                type=PineconeVectorDatabaseParamsType.VECTOR_DATABASE_PINECONE,
                index="index",
                api_key="api_key",
                api_environment="api_environment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_vector_database(
            type=type, index=index, api_key=api_key, api_environment=api_environment, request_options=request_options
        )
        return _response.data

    async def update_vector_database(
        self,
        *,
        id: str,
        type: PineconeVectorDatabaseUpdateParamsType,
        index: typing.Optional[PineconeVectorDatabaseUpdateParamsIndex] = OMIT,
        api_key: typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey] = OMIT,
        api_environment: typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PineconeVectorDatabase:
        """
        Parameters
        ----------
        id : str

        type : PineconeVectorDatabaseUpdateParamsType

        index : typing.Optional[PineconeVectorDatabaseUpdateParamsIndex]

        api_key : typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey]

        api_environment : typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PineconeVectorDatabase
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PineconeVectorDatabaseUpdateParamsType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vector_databases.update_vector_database(
                id="id",
                type=PineconeVectorDatabaseUpdateParamsType.VECTOR_DATABASE_PINECONE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_vector_database(
            id=id,
            type=type,
            index=index,
            api_key=api_key,
            api_environment=api_environment,
            request_options=request_options,
        )
        return _response.data
