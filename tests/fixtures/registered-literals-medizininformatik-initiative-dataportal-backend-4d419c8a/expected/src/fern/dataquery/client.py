

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ccdl import Ccdl
from ..types.crtdl import Crtdl
from ..types.data_extraction_query import DataExtractionQuery
from ..types.data_query_list_entry import DataQueryListEntry
from ..types.data_query_slots import DataQuerySlots
from ..types.dataquery import Dataquery
from .raw_client import AsyncRawDataqueryClient, RawDataqueryClient
from .types.get_data_query_crtdl_by_id_request_accept import GetDataQueryCrtdlByIdRequestAccept


OMIT = typing.cast(typing.Any, ...)


class DataqueryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDataqueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDataqueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDataqueryClient
        """
        return self._raw_client

    def get_data_query_list(
        self,
        *,
        include_temporary: typing.Optional[bool] = None,
        skip_validation: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[DataQueryListEntry]:
        """
        This returns a list with basic information about the queries. Id, label (if present) and creation date. Basically for all parameters I'm not sure if we need them (at least right away)

        Parameters
        ----------
        include_temporary : typing.Optional[bool]
            if set to true, queries spawned from other users are contained

        skip_validation : typing.Optional[bool]
            If true, do not validate the query and do not include a list of invalid terms.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DataQueryListEntry]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.dataquery.get_data_query_list()
        """
        _response = self._raw_client.get_data_query_list(
            include_temporary=include_temporary, skip_validation=skip_validation, request_options=request_options
        )
        return _response.data

    def store_data_query(
        self,
        *,
        content: Crtdl,
        label: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        total_number_of_results: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The query will only be stored, nothing will be dispatched. Does not have to pass any validation and may be incomplete. May or may not contain result.

        Parameters
        ----------
        content : Crtdl

        label : typing.Optional[str]

        comment : typing.Optional[str]

        total_number_of_results : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import Crtdl, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.dataquery.store_data_query(
            content=Crtdl(),
        )
        """
        _response = self._raw_client.store_data_query(
            content=content,
            label=label,
            comment=comment,
            total_number_of_results=total_number_of_results,
            request_options=request_options,
        )
        return _response.data

    def find_data_queries_by_user(
        self,
        user_id: str,
        *,
        include_temporary: typing.Optional[bool] = None,
        skip_validation: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[DataQueryListEntry]:
        """
        Parameters
        ----------
        user_id : str
            User to filter by (keycloak id)

        include_temporary : typing.Optional[bool]
            if set to true, queries spawned from other users are contained

        skip_validation : typing.Optional[bool]
            If true, do not validate the query and do not include a list of invalid terms.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DataQueryListEntry]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.dataquery.find_data_queries_by_user(
            user_id="userId",
        )
        """
        _response = self._raw_client.find_data_queries_by_user(
            user_id,
            include_temporary=include_temporary,
            skip_validation=skip_validation,
            request_options=request_options,
        )
        return _response.data

    def create_dataquery_for_user(
        self,
        user_id: str,
        *,
        ttl: str,
        content: Crtdl,
        label: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        total_number_of_results: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        user_id : str
            ID of the user for whom to spawn the query

        ttl : str
            How long until the query gets deleted (ISO 8601 Duration)

        content : Crtdl

        label : typing.Optional[str]

        comment : typing.Optional[str]

        total_number_of_results : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import Crtdl, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.dataquery.create_dataquery_for_user(
            user_id="userId",
            ttl="ttl",
            content=Crtdl(),
        )
        """
        _response = self._raw_client.create_dataquery_for_user(
            user_id,
            ttl=ttl,
            content=content,
            label=label,
            comment=comment,
            total_number_of_results=total_number_of_results,
            request_options=request_options,
        )
        return _response.data

    def get_data_query_by_id(
        self,
        query_id: int,
        *,
        skip_validation: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataquery:
        """
        Returns a single dataquery.

        Parameters
        ----------
        query_id : int
            ID of query to return

        skip_validation : typing.Optional[bool]
            If true, do not validate the query and do not include a list of invalid terms

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataquery
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.dataquery.get_data_query_by_id(
            query_id=1000000,
        )
        """
        _response = self._raw_client.get_data_query_by_id(
            query_id, skip_validation=skip_validation, request_options=request_options
        )
        return _response.data

    def update_data_query(
        self,
        query_id: int,
        *,
        content: Crtdl,
        label: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        total_number_of_results: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The query will be updated. It must be provided completely, there are no partial updates.

        Parameters
        ----------
        query_id : int

        content : Crtdl

        label : typing.Optional[str]

        comment : typing.Optional[str]

        total_number_of_results : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import Crtdl, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.dataquery.update_data_query(
            query_id=1000000,
            content=Crtdl(),
        )
        """
        _response = self._raw_client.update_data_query(
            query_id,
            content=content,
            label=label,
            comment=comment,
            total_number_of_results=total_number_of_results,
            request_options=request_options,
        )
        return _response.data

    def delete_data_query(self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        query_id : int

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.dataquery.delete_data_query(
            query_id=1000000,
        )
        """
        _response = self._raw_client.delete_data_query(query_id, request_options=request_options)
        return _response.data

    def get_data_query_crtdl_by_id(
        self,
        query_id: int,
        *,
        skip_validation: typing.Optional[bool] = None,
        accept: typing.Optional[GetDataQueryCrtdlByIdRequestAccept] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Returns only the CRTDL part of a dataquery or alternatively a zip file containing the crtdl json and csv files

        Parameters
        ----------
        query_id : int
            ID of query to return

        skip_validation : typing.Optional[bool]
            If true, do not validate the query and do not include a list of invalid terms

        accept : typing.Optional[GetDataQueryCrtdlByIdRequestAccept]
            Specify the desired format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.dataquery.get_data_query_crtdl_by_id(
            query_id=1000000,
        )
        """
        with self._raw_client.get_data_query_crtdl_by_id(
            query_id, skip_validation=skip_validation, accept=accept, request_options=request_options
        ) as r:
            yield from r.data

    def convert_crtdl_to_csv(
        self,
        *,
        display: typing.Optional[str] = OMIT,
        cohort_definition: typing.Optional[Ccdl] = OMIT,
        data_extraction: typing.Optional[DataExtractionQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Nothing will be stored, only a zip file will be generated

        Parameters
        ----------
        display : typing.Optional[str]

        cohort_definition : typing.Optional[Ccdl]

        data_extraction : typing.Optional[DataExtractionQuery]

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.dataquery.convert_crtdl_to_csv()
        """
        _response = self._raw_client.convert_crtdl_to_csv(
            display=display,
            cohort_definition=cohort_definition,
            data_extraction=data_extraction,
            request_options=request_options,
        )
        return _response.data

    def get_data_query_slots(self, *, request_options: typing.Optional[RequestOptions] = None) -> DataQuerySlots:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataQuerySlots
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.dataquery.get_data_query_slots()
        """
        _response = self._raw_client.get_data_query_slots(request_options=request_options)
        return _response.data


class AsyncDataqueryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDataqueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDataqueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDataqueryClient
        """
        return self._raw_client

    async def get_data_query_list(
        self,
        *,
        include_temporary: typing.Optional[bool] = None,
        skip_validation: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[DataQueryListEntry]:
        """
        This returns a list with basic information about the queries. Id, label (if present) and creation date. Basically for all parameters I'm not sure if we need them (at least right away)

        Parameters
        ----------
        include_temporary : typing.Optional[bool]
            if set to true, queries spawned from other users are contained

        skip_validation : typing.Optional[bool]
            If true, do not validate the query and do not include a list of invalid terms.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DataQueryListEntry]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dataquery.get_data_query_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_data_query_list(
            include_temporary=include_temporary, skip_validation=skip_validation, request_options=request_options
        )
        return _response.data

    async def store_data_query(
        self,
        *,
        content: Crtdl,
        label: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        total_number_of_results: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The query will only be stored, nothing will be dispatched. Does not have to pass any validation and may be incomplete. May or may not contain result.

        Parameters
        ----------
        content : Crtdl

        label : typing.Optional[str]

        comment : typing.Optional[str]

        total_number_of_results : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Crtdl

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dataquery.store_data_query(
                content=Crtdl(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_data_query(
            content=content,
            label=label,
            comment=comment,
            total_number_of_results=total_number_of_results,
            request_options=request_options,
        )
        return _response.data

    async def find_data_queries_by_user(
        self,
        user_id: str,
        *,
        include_temporary: typing.Optional[bool] = None,
        skip_validation: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[DataQueryListEntry]:
        """
        Parameters
        ----------
        user_id : str
            User to filter by (keycloak id)

        include_temporary : typing.Optional[bool]
            if set to true, queries spawned from other users are contained

        skip_validation : typing.Optional[bool]
            If true, do not validate the query and do not include a list of invalid terms.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DataQueryListEntry]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dataquery.find_data_queries_by_user(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_data_queries_by_user(
            user_id,
            include_temporary=include_temporary,
            skip_validation=skip_validation,
            request_options=request_options,
        )
        return _response.data

    async def create_dataquery_for_user(
        self,
        user_id: str,
        *,
        ttl: str,
        content: Crtdl,
        label: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        total_number_of_results: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        user_id : str
            ID of the user for whom to spawn the query

        ttl : str
            How long until the query gets deleted (ISO 8601 Duration)

        content : Crtdl

        label : typing.Optional[str]

        comment : typing.Optional[str]

        total_number_of_results : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Crtdl

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dataquery.create_dataquery_for_user(
                user_id="userId",
                ttl="ttl",
                content=Crtdl(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_dataquery_for_user(
            user_id,
            ttl=ttl,
            content=content,
            label=label,
            comment=comment,
            total_number_of_results=total_number_of_results,
            request_options=request_options,
        )
        return _response.data

    async def get_data_query_by_id(
        self,
        query_id: int,
        *,
        skip_validation: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataquery:
        """
        Returns a single dataquery.

        Parameters
        ----------
        query_id : int
            ID of query to return

        skip_validation : typing.Optional[bool]
            If true, do not validate the query and do not include a list of invalid terms

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataquery
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dataquery.get_data_query_by_id(
                query_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_data_query_by_id(
            query_id, skip_validation=skip_validation, request_options=request_options
        )
        return _response.data

    async def update_data_query(
        self,
        query_id: int,
        *,
        content: Crtdl,
        label: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        total_number_of_results: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The query will be updated. It must be provided completely, there are no partial updates.

        Parameters
        ----------
        query_id : int

        content : Crtdl

        label : typing.Optional[str]

        comment : typing.Optional[str]

        total_number_of_results : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Crtdl

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dataquery.update_data_query(
                query_id=1000000,
                content=Crtdl(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_data_query(
            query_id,
            content=content,
            label=label,
            comment=comment,
            total_number_of_results=total_number_of_results,
            request_options=request_options,
        )
        return _response.data

    async def delete_data_query(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        query_id : int

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dataquery.delete_data_query(
                query_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_data_query(query_id, request_options=request_options)
        return _response.data

    async def get_data_query_crtdl_by_id(
        self,
        query_id: int,
        *,
        skip_validation: typing.Optional[bool] = None,
        accept: typing.Optional[GetDataQueryCrtdlByIdRequestAccept] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns only the CRTDL part of a dataquery or alternatively a zip file containing the crtdl json and csv files

        Parameters
        ----------
        query_id : int
            ID of query to return

        skip_validation : typing.Optional[bool]
            If true, do not validate the query and do not include a list of invalid terms

        accept : typing.Optional[GetDataQueryCrtdlByIdRequestAccept]
            Specify the desired format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dataquery.get_data_query_crtdl_by_id(
                query_id=1000000,
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_data_query_crtdl_by_id(
            query_id, skip_validation=skip_validation, accept=accept, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def convert_crtdl_to_csv(
        self,
        *,
        display: typing.Optional[str] = OMIT,
        cohort_definition: typing.Optional[Ccdl] = OMIT,
        data_extraction: typing.Optional[DataExtractionQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Nothing will be stored, only a zip file will be generated

        Parameters
        ----------
        display : typing.Optional[str]

        cohort_definition : typing.Optional[Ccdl]

        data_extraction : typing.Optional[DataExtractionQuery]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dataquery.convert_crtdl_to_csv()


        asyncio.run(main())
        """
        _response = await self._raw_client.convert_crtdl_to_csv(
            display=display,
            cohort_definition=cohort_definition,
            data_extraction=data_extraction,
            request_options=request_options,
        )
        return _response.data

    async def get_data_query_slots(self, *, request_options: typing.Optional[RequestOptions] = None) -> DataQuerySlots:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataQuerySlots
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dataquery.get_data_query_slots()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_data_query_slots(request_options=request_options)
        return _response.data
