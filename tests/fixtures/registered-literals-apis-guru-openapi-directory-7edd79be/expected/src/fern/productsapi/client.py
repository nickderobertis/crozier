

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_key import ApiKey
from ..types.count_of import CountOf
from ..types.find_credentials import FindCredentials
from ..types.product_create_modify import ProductCreateModify
from ..types.product_view import ProductView
from .raw_client import AsyncRawProductsapiClient, RawProductsapiClient


OMIT = typing.cast(typing.Any, ...)


class ProductsapiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProductsapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProductsapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProductsapiClient
        """
        return self._raw_client

    def patchproduct2(
        self,
        *,
        request: typing.Optional[ProductCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[ProductCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, ProductCreateModify

        client = FernApi()
        client.productsapi.patchproduct2(
            request=ProductCreateModify(),
        )
        """
        _response = self._raw_client.patchproduct2(request=request, request_options=request_options)
        return _response.data

    def patchproduct(
        self,
        *,
        request: typing.Optional[ProductCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[ProductCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, ProductCreateModify

        client = FernApi()
        client.productsapi.patchproduct(
            request=ProductCreateModify(),
        )
        """
        _response = self._raw_client.patchproduct(request=request, request_options=request_options)
        return _response.data

    def count(
        self, *, request: typing.Optional[ApiKey] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CountOf]:
        """
        Parameters
        ----------
        request : typing.Optional[ApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CountOf]


        Examples
        --------
        from fern import ApiKey, FernApi

        client = FernApi()
        client.productsapi.count(
            request=ApiKey(),
        )
        """
        _response = self._raw_client.count(request=request, request_options=request_options)
        return _response.data

    def find(
        self,
        *,
        page: typing.Optional[int] = None,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[ProductView]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ProductView]


        Examples
        --------
        from fern import FernApi, FindCredentials

        client = FernApi()
        client.productsapi.find(
            request=FindCredentials(),
        )
        """
        _response = self._raw_client.find(page=page, request=request, request_options=request_options)
        return _response.data

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        request: typing.Optional[ApiKey] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ProductView]]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request : typing.Optional[ApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ProductView]]


        Examples
        --------
        from fern import ApiKey, FernApi

        client = FernApi()
        client.productsapi.list(
            request=ApiKey(),
        )
        """
        _response = self._raw_client.list(page=page, request=request, request_options=request_options)
        return _response.data

    def save(
        self,
        *,
        request: typing.Optional[ProductCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[ProductView]:
        """
        Parameters
        ----------
        request : typing.Optional[ProductCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ProductView]


        Examples
        --------
        from fern import FernApi, ProductCreateModify

        client = FernApi()
        client.productsapi.save(
            request=ProductCreateModify(),
        )
        """
        _response = self._raw_client.save(request=request, request_options=request_options)
        return _response.data

    def deleteproduct2(
        self, serial: str, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        serial : str

        api_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.productsapi.deleteproduct2(
            serial="serial",
            api_key="X-Api-Key",
        )
        """
        _response = self._raw_client.deleteproduct2(serial, api_key=api_key, request_options=request_options)
        return _response.data

    def deleteproduct(
        self, serial: str, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        serial : str

        api_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.productsapi.deleteproduct(
            serial="serial",
            api_key="X-Api-Key",
        )
        """
        _response = self._raw_client.deleteproduct(serial, api_key=api_key, request_options=request_options)
        return _response.data


class AsyncProductsapiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProductsapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProductsapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProductsapiClient
        """
        return self._raw_client

    async def patchproduct2(
        self,
        *,
        request: typing.Optional[ProductCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[ProductCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProductCreateModify

        client = AsyncFernApi()


        async def main() -> None:
            await client.productsapi.patchproduct2(
                request=ProductCreateModify(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patchproduct2(request=request, request_options=request_options)
        return _response.data

    async def patchproduct(
        self,
        *,
        request: typing.Optional[ProductCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request : typing.Optional[ProductCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProductCreateModify

        client = AsyncFernApi()


        async def main() -> None:
            await client.productsapi.patchproduct(
                request=ProductCreateModify(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patchproduct(request=request, request_options=request_options)
        return _response.data

    async def count(
        self, *, request: typing.Optional[ApiKey] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CountOf]:
        """
        Parameters
        ----------
        request : typing.Optional[ApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CountOf]


        Examples
        --------
        import asyncio

        from fern import ApiKey, AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.productsapi.count(
                request=ApiKey(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.count(request=request, request_options=request_options)
        return _response.data

    async def find(
        self,
        *,
        page: typing.Optional[int] = None,
        request: typing.Optional[FindCredentials] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[ProductView]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request : typing.Optional[FindCredentials]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ProductView]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FindCredentials

        client = AsyncFernApi()


        async def main() -> None:
            await client.productsapi.find(
                request=FindCredentials(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find(page=page, request=request, request_options=request_options)
        return _response.data

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        request: typing.Optional[ApiKey] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ProductView]]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request : typing.Optional[ApiKey]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ProductView]]


        Examples
        --------
        import asyncio

        from fern import ApiKey, AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.productsapi.list(
                request=ApiKey(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(page=page, request=request, request_options=request_options)
        return _response.data

    async def save(
        self,
        *,
        request: typing.Optional[ProductCreateModify] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[ProductView]:
        """
        Parameters
        ----------
        request : typing.Optional[ProductCreateModify]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ProductView]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProductCreateModify

        client = AsyncFernApi()


        async def main() -> None:
            await client.productsapi.save(
                request=ProductCreateModify(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save(request=request, request_options=request_options)
        return _response.data

    async def deleteproduct2(
        self, serial: str, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        serial : str

        api_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.productsapi.deleteproduct2(
                serial="serial",
                api_key="X-Api-Key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteproduct2(serial, api_key=api_key, request_options=request_options)
        return _response.data

    async def deleteproduct(
        self, serial: str, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        serial : str

        api_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.productsapi.deleteproduct(
                serial="serial",
                api_key="X-Api-Key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteproduct(serial, api_key=api_key, request_options=request_options)
        return _response.data
