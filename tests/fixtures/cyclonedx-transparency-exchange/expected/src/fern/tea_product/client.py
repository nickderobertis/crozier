

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.identifier_type import IdentifierType
from ..types.paginated_product_response import PaginatedProductResponse
from ..types.product import Product
from ..types.uuid_ import Uuid
from .raw_client import AsyncRawTeaProductClient, RawTeaProductClient
from .types.query_tea_products_request_sort_field import QueryTeaProductsRequestSortField
from .types.query_tea_products_request_sort_order import QueryTeaProductsRequestSortOrder


class TeaProductClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTeaProductClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTeaProductClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTeaProductClient
        """
        return self._raw_client

    def get_tea_product_by_uuid(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Product:
        """
        Get a TEA Product by UUID

        Parameters
        ----------
        uuid_ : Uuid
            UUID of the TEA product in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Product
            Requested TEA Product found and returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tea_product.get_tea_product_by_uuid(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_tea_product_by_uuid(uuid_, request_options=request_options)
        return _response.data

    def query_tea_products(
        self,
        *,
        id_type: typing.Optional[IdentifierType] = None,
        id_value: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[QueryTeaProductsRequestSortField] = None,
        sort_order: typing.Optional[QueryTeaProductsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedProductResponse:
        """
        Returns a list of TEA products. Note that multiple products may match.

        Parameters
        ----------
        id_type : typing.Optional[IdentifierType]
            Type of identifier specified in the `idValue` parameter

        id_value : typing.Optional[str]
            If present, only the objects with the given identifier value will be returned.

        page_size : typing.Optional[int]
            The maximum number of results to return.

        page_token : typing.Optional[str]
            An opaque continuation token produced by a previous response.
            This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
            Clients MUST NOT parse, construct, or modify this token.

            The token represents continuation state for the original query, including
            `sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
            and path parameters such as parent `uuid`.
            When `pageToken` is supplied, clients MUST NOT change those result-affecting query
            parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
            parameters conflict with the token state. To change any result-affecting parameter,
            clients MUST start a new pagination sequence without `pageToken`.

            A `pageToken` is only valid with the same request path and same path parameter values
            used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
            resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
            when a `pageToken` is used with a different path or different path parameter values.

            Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
            `pageToken` values.

        sort_field : typing.Optional[QueryTeaProductsRequestSortField]
            The field by which to sort the results.

            Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
            as a deterministic secondary tie-breaker.

        sort_order : typing.Optional[QueryTeaProductsRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedProductResponse
            A paginated response containing TEA Products

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tea_product.query_tea_products()
        """
        _response = self._raw_client.query_tea_products(
            id_type=id_type,
            id_value=id_value,
            page_size=page_size,
            page_token=page_token,
            sort_field=sort_field,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data


class AsyncTeaProductClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTeaProductClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTeaProductClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTeaProductClient
        """
        return self._raw_client

    async def get_tea_product_by_uuid(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Product:
        """
        Get a TEA Product by UUID

        Parameters
        ----------
        uuid_ : Uuid
            UUID of the TEA product in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Product
            Requested TEA Product found and returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tea_product.get_tea_product_by_uuid(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tea_product_by_uuid(uuid_, request_options=request_options)
        return _response.data

    async def query_tea_products(
        self,
        *,
        id_type: typing.Optional[IdentifierType] = None,
        id_value: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[QueryTeaProductsRequestSortField] = None,
        sort_order: typing.Optional[QueryTeaProductsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedProductResponse:
        """
        Returns a list of TEA products. Note that multiple products may match.

        Parameters
        ----------
        id_type : typing.Optional[IdentifierType]
            Type of identifier specified in the `idValue` parameter

        id_value : typing.Optional[str]
            If present, only the objects with the given identifier value will be returned.

        page_size : typing.Optional[int]
            The maximum number of results to return.

        page_token : typing.Optional[str]
            An opaque continuation token produced by a previous response.
            This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
            Clients MUST NOT parse, construct, or modify this token.

            The token represents continuation state for the original query, including
            `sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
            and path parameters such as parent `uuid`.
            When `pageToken` is supplied, clients MUST NOT change those result-affecting query
            parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
            parameters conflict with the token state. To change any result-affecting parameter,
            clients MUST start a new pagination sequence without `pageToken`.

            A `pageToken` is only valid with the same request path and same path parameter values
            used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
            resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
            when a `pageToken` is used with a different path or different path parameter values.

            Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
            `pageToken` values.

        sort_field : typing.Optional[QueryTeaProductsRequestSortField]
            The field by which to sort the results.

            Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
            as a deterministic secondary tie-breaker.

        sort_order : typing.Optional[QueryTeaProductsRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedProductResponse
            A paginated response containing TEA Products

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tea_product.query_tea_products()


        asyncio.run(main())
        """
        _response = await self._raw_client.query_tea_products(
            id_type=id_type,
            id_value=id_value,
            page_size=page_size,
            page_token=page_token,
            sort_field=sort_field,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data
