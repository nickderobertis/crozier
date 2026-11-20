

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawQueryParametersClient, RawQueryParametersClient
from .types.get_params_default_object_query_request_filter import GetParamsDefaultObjectQueryRequestFilter
from .types.get_params_default_object_query_response import GetParamsDefaultObjectQueryResponse
from .types.get_params_mixed_query_request_statuses_item import GetParamsMixedQueryRequestStatusesItem
from .types.get_params_mixed_query_response import GetParamsMixedQueryResponse
from .types.get_params_simple_query_request_order_by import GetParamsSimpleQueryRequestOrderBy
from .types.get_params_simple_query_response import GetParamsSimpleQueryResponse
from .types.get_params_unexploded_object_query_request_filter import GetParamsUnexplodedObjectQueryRequestFilter
from .types.get_params_unexploded_object_query_response import GetParamsUnexplodedObjectQueryResponse


class QueryParametersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQueryParametersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQueryParametersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQueryParametersClient
        """
        return self._raw_client

    def get_params_simple_query(
        self,
        *,
        order_by: GetParamsSimpleQueryRequestOrderBy,
        limit: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetParamsSimpleQueryResponse:
        """
        Parameters
        ----------
        order_by : GetParamsSimpleQueryRequestOrderBy

        limit : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetParamsSimpleQueryResponse
            success

        Examples
        --------
        from fern.query_parameters import GetParamsSimpleQueryRequestOrderBy

        from fern import FernApi

        client = FernApi()
        client.query_parameters.get_params_simple_query(
            order_by=GetParamsSimpleQueryRequestOrderBy.ASC,
            limit=1.1,
        )
        """
        _response = self._raw_client.get_params_simple_query(
            order_by=order_by, limit=limit, request_options=request_options
        )
        return _response.data

    def get_params_default_object_query(
        self,
        *,
        filter: GetParamsDefaultObjectQueryRequestFilter,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetParamsDefaultObjectQueryResponse:
        """
        Parameters
        ----------
        filter : GetParamsDefaultObjectQueryRequestFilter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetParamsDefaultObjectQueryResponse
            success

        Examples
        --------
        from fern.query_parameters import GetParamsDefaultObjectQueryRequestFilter

        from fern import FernApi

        client = FernApi()
        client.query_parameters.get_params_default_object_query(
            filter=GetParamsDefaultObjectQueryRequestFilter(
                name="name",
                age=1.1,
            ),
        )
        """
        _response = self._raw_client.get_params_default_object_query(filter=filter, request_options=request_options)
        return _response.data

    def get_params_unexploded_object_query(
        self,
        *,
        filter: GetParamsUnexplodedObjectQueryRequestFilter,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetParamsUnexplodedObjectQueryResponse:
        """
        Parameters
        ----------
        filter : GetParamsUnexplodedObjectQueryRequestFilter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetParamsUnexplodedObjectQueryResponse
            success

        Examples
        --------
        from fern.query_parameters import GetParamsUnexplodedObjectQueryRequestFilter

        from fern import FernApi

        client = FernApi()
        client.query_parameters.get_params_unexploded_object_query(
            filter=GetParamsUnexplodedObjectQueryRequestFilter(
                name="name",
                age=1.1,
            ),
        )
        """
        _response = self._raw_client.get_params_unexploded_object_query(filter=filter, request_options=request_options)
        return _response.data

    def get_params_mixed_query(
        self,
        *,
        limit: float,
        kebab_case: str,
        author_ids: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        statuses: typing.Optional[
            typing.Union[
                GetParamsMixedQueryRequestStatusesItem, typing.Sequence[GetParamsMixedQueryRequestStatusesItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetParamsMixedQueryResponse:
        """
        Parameters
        ----------
        limit : float

        kebab_case : str

        author_ids : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        statuses : typing.Optional[typing.Union[GetParamsMixedQueryRequestStatusesItem, typing.Sequence[GetParamsMixedQueryRequestStatusesItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetParamsMixedQueryResponse
            success

        Examples
        --------
        from fern.query_parameters import GetParamsMixedQueryRequestStatusesItem

        from fern import FernApi

        client = FernApi()
        client.query_parameters.get_params_mixed_query(
            limit=1.1,
            author_ids=[1],
            kebab_case="kebab-case",
            statuses=[GetParamsMixedQueryRequestStatusesItem.OPEN],
        )
        """
        _response = self._raw_client.get_params_mixed_query(
            limit=limit,
            kebab_case=kebab_case,
            author_ids=author_ids,
            statuses=statuses,
            request_options=request_options,
        )
        return _response.data


class AsyncQueryParametersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQueryParametersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQueryParametersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQueryParametersClient
        """
        return self._raw_client

    async def get_params_simple_query(
        self,
        *,
        order_by: GetParamsSimpleQueryRequestOrderBy,
        limit: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetParamsSimpleQueryResponse:
        """
        Parameters
        ----------
        order_by : GetParamsSimpleQueryRequestOrderBy

        limit : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetParamsSimpleQueryResponse
            success

        Examples
        --------
        import asyncio

        from fern.query_parameters import GetParamsSimpleQueryRequestOrderBy

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.query_parameters.get_params_simple_query(
                order_by=GetParamsSimpleQueryRequestOrderBy.ASC,
                limit=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_params_simple_query(
            order_by=order_by, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_params_default_object_query(
        self,
        *,
        filter: GetParamsDefaultObjectQueryRequestFilter,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetParamsDefaultObjectQueryResponse:
        """
        Parameters
        ----------
        filter : GetParamsDefaultObjectQueryRequestFilter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetParamsDefaultObjectQueryResponse
            success

        Examples
        --------
        import asyncio

        from fern.query_parameters import GetParamsDefaultObjectQueryRequestFilter

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.query_parameters.get_params_default_object_query(
                filter=GetParamsDefaultObjectQueryRequestFilter(
                    name="name",
                    age=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_params_default_object_query(
            filter=filter, request_options=request_options
        )
        return _response.data

    async def get_params_unexploded_object_query(
        self,
        *,
        filter: GetParamsUnexplodedObjectQueryRequestFilter,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetParamsUnexplodedObjectQueryResponse:
        """
        Parameters
        ----------
        filter : GetParamsUnexplodedObjectQueryRequestFilter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetParamsUnexplodedObjectQueryResponse
            success

        Examples
        --------
        import asyncio

        from fern.query_parameters import GetParamsUnexplodedObjectQueryRequestFilter

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.query_parameters.get_params_unexploded_object_query(
                filter=GetParamsUnexplodedObjectQueryRequestFilter(
                    name="name",
                    age=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_params_unexploded_object_query(
            filter=filter, request_options=request_options
        )
        return _response.data

    async def get_params_mixed_query(
        self,
        *,
        limit: float,
        kebab_case: str,
        author_ids: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        statuses: typing.Optional[
            typing.Union[
                GetParamsMixedQueryRequestStatusesItem, typing.Sequence[GetParamsMixedQueryRequestStatusesItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetParamsMixedQueryResponse:
        """
        Parameters
        ----------
        limit : float

        kebab_case : str

        author_ids : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        statuses : typing.Optional[typing.Union[GetParamsMixedQueryRequestStatusesItem, typing.Sequence[GetParamsMixedQueryRequestStatusesItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetParamsMixedQueryResponse
            success

        Examples
        --------
        import asyncio

        from fern.query_parameters import GetParamsMixedQueryRequestStatusesItem

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.query_parameters.get_params_mixed_query(
                limit=1.1,
                author_ids=[1],
                kebab_case="kebab-case",
                statuses=[GetParamsMixedQueryRequestStatusesItem.OPEN],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_params_mixed_query(
            limit=limit,
            kebab_case=kebab_case,
            author_ids=author_ids,
            statuses=statuses,
            request_options=request_options,
        )
        return _response.data
