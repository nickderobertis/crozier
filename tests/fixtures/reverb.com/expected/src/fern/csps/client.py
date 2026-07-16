

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCspsClient, RawCspsClient


class CspsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCspsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCspsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCspsClient
        """
        return self._raw_client

    def returns_a_set_of_comparison_shopping_pages_based_on_the_current_params(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns a set of comparison shopping pages based on the current params

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
        client.csps.returns_a_set_of_comparison_shopping_pages_based_on_the_current_params()
        """
        _response = self._raw_client.returns_a_set_of_comparison_shopping_pages_based_on_the_current_params(
            request_options=request_options
        )
        return _response.data

    def get_csps_categories(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.csps.get_csps_categories()
        """
        _response = self._raw_client.get_csps_categories(request_options=request_options)
        return _response.data

    def show_comparison_shopping_page(
        self,
        *,
        id: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Show comparison shopping page

        Parameters
        ----------
        id : typing.Optional[str]
            ID of the comparison shopping page

        slug : typing.Optional[str]
            Slug of the comparison shopping page

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
        client.csps.show_comparison_shopping_page()
        """
        _response = self._raw_client.show_comparison_shopping_page(id=id, slug=slug, request_options=request_options)
        return _response.data

    def get_csps_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
        client.csps.get_csps_id(
            id="id",
        )
        """
        _response = self._raw_client.get_csps_id(id, request_options=request_options)
        return _response.data


class AsyncCspsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCspsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCspsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCspsClient
        """
        return self._raw_client

    async def returns_a_set_of_comparison_shopping_pages_based_on_the_current_params(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns a set of comparison shopping pages based on the current params

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
            await client.csps.returns_a_set_of_comparison_shopping_pages_based_on_the_current_params()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_set_of_comparison_shopping_pages_based_on_the_current_params(
            request_options=request_options
        )
        return _response.data

    async def get_csps_categories(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.csps.get_csps_categories()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_csps_categories(request_options=request_options)
        return _response.data

    async def show_comparison_shopping_page(
        self,
        *,
        id: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Show comparison shopping page

        Parameters
        ----------
        id : typing.Optional[str]
            ID of the comparison shopping page

        slug : typing.Optional[str]
            Slug of the comparison shopping page

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
            await client.csps.show_comparison_shopping_page()


        asyncio.run(main())
        """
        _response = await self._raw_client.show_comparison_shopping_page(
            id=id, slug=slug, request_options=request_options
        )
        return _response.data

    async def get_csps_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            await client.csps.get_csps_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_csps_id(id, request_options=request_options)
        return _response.data
