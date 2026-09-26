

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.asset_delete_response import AssetDeleteResponse
from ..types.asset_edit_context import AssetEditContext
from ..types.asset_list_response import AssetListResponse
from .raw_client import AsyncRawAssetsClient, RawAssetsClient


class AssetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsClient
        """
        return self._raw_client

    def list_assets(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetListResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetListResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assets.list_assets()
        """
        _response = self._raw_client.list_assets(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def delete_asset(
        self, asset_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AssetDeleteResponse:
        """
        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetDeleteResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assets.delete_asset(
            asset_id="asset_id",
        )
        """
        _response = self._raw_client.delete_asset(asset_id, request_options=request_options)
        return _response.data

    def download_asset(self, asset_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assets.download_asset(
            asset_id="asset_id",
        )
        """
        _response = self._raw_client.download_asset(asset_id, request_options=request_options)
        return _response.data

    def get_asset_edit_context(
        self, asset_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AssetEditContext:
        """
        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetEditContext
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assets.get_asset_edit_context(
            asset_id="asset_id",
        )
        """
        _response = self._raw_client.get_asset_edit_context(asset_id, request_options=request_options)
        return _response.data

    def get_asset_image(self, asset_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assets.get_asset_image(
            asset_id="asset_id",
        )
        """
        _response = self._raw_client.get_asset_image(asset_id, request_options=request_options)
        return _response.data


class AsyncAssetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsClient
        """
        return self._raw_client

    async def list_assets(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssetListResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetListResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assets.list_assets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_assets(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    async def delete_asset(
        self, asset_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AssetDeleteResponse:
        """
        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetDeleteResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assets.delete_asset(
                asset_id="asset_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_asset(asset_id, request_options=request_options)
        return _response.data

    async def download_asset(
        self, asset_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assets.download_asset(
                asset_id="asset_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_asset(asset_id, request_options=request_options)
        return _response.data

    async def get_asset_edit_context(
        self, asset_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AssetEditContext:
        """
        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetEditContext
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assets.get_asset_edit_context(
                asset_id="asset_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_asset_edit_context(asset_id, request_options=request_options)
        return _response.data

    async def get_asset_image(
        self, asset_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assets.get_asset_image(
                asset_id="asset_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_asset_image(asset_id, request_options=request_options)
        return _response.data
