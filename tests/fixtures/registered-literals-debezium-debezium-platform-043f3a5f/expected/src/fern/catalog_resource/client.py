

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCatalogResourceClient, RawCatalogResourceClient


class CatalogResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCatalogResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCatalogResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCatalogResourceClient
        """
        return self._raw_client

    def returns_all_available_components_for_the_current_application_version(
        self, *, type: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.catalog_resource.returns_all_available_components_for_the_current_application_version()
        """
        _response = self._raw_client.returns_all_available_components_for_the_current_application_version(
            type=type, request_options=request_options
        )
        return _response.data

    def returns_descriptors_for_a_specific_component_using_current_application_version(
        self, type: str, class_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        type : str

        class_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.catalog_resource.returns_descriptors_for_a_specific_component_using_current_application_version(
            type="type",
            class_="class",
        )
        """
        _response = self._raw_client.returns_descriptors_for_a_specific_component_using_current_application_version(
            type, class_, request_options=request_options
        )
        return _response.data

    def returns_all_available_components_for_a_specific_version(
        self,
        version: str,
        *,
        type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        version : str

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.catalog_resource.returns_all_available_components_for_a_specific_version(
            version="version",
        )
        """
        _response = self._raw_client.returns_all_available_components_for_a_specific_version(
            version, type=type, request_options=request_options
        )
        return _response.data

    def returns_descriptors_for_a_specific_component(
        self, version: str, type: str, class_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        version : str

        type : str

        class_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.catalog_resource.returns_descriptors_for_a_specific_component(
            version="version",
            type="type",
            class_="class",
        )
        """
        _response = self._raw_client.returns_descriptors_for_a_specific_component(
            version, type, class_, request_options=request_options
        )
        return _response.data


class AsyncCatalogResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCatalogResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCatalogResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCatalogResourceClient
        """
        return self._raw_client

    async def returns_all_available_components_for_the_current_application_version(
        self, *, type: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog_resource.returns_all_available_components_for_the_current_application_version()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_available_components_for_the_current_application_version(
            type=type, request_options=request_options
        )
        return _response.data

    async def returns_descriptors_for_a_specific_component_using_current_application_version(
        self, type: str, class_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        type : str

        class_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog_resource.returns_descriptors_for_a_specific_component_using_current_application_version(
                type="type",
                class_="class",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.returns_descriptors_for_a_specific_component_using_current_application_version(
                type, class_, request_options=request_options
            )
        )
        return _response.data

    async def returns_all_available_components_for_a_specific_version(
        self,
        version: str,
        *,
        type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        version : str

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog_resource.returns_all_available_components_for_a_specific_version(
                version="version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_available_components_for_a_specific_version(
            version, type=type, request_options=request_options
        )
        return _response.data

    async def returns_descriptors_for_a_specific_component(
        self, version: str, type: str, class_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        version : str

        type : str

        class_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.catalog_resource.returns_descriptors_for_a_specific_component(
                version="version",
                type="type",
                class_="class",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_descriptors_for_a_specific_component(
            version, type, class_, request_options=request_options
        )
        return _response.data
