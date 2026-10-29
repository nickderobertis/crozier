

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dataset_id import DatasetId
from ..types.entity_preview_config import EntityPreviewConfig
from ..types.frontend_config import FrontendConfig
from ..types.frontend_dataset_id import FrontendDatasetId
from ..types.me import Me
from .raw_client import AsyncRawFrontendClient, RawFrontendClient


class FrontendClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFrontendClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFrontendClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFrontendClient
        """
        return self._raw_client

    def get_frontend_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> FrontendConfig:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FrontendConfig
            The Configuration for the Frontend

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.frontend.get_frontend_config()
        """
        _response = self._raw_client.get_frontend_config(request_options=request_options)
        return _response.data

    def get_entity_preview_config(
        self, dataset: DatasetId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntityPreviewConfig:
        """
        Parameters
        ----------
        dataset : DatasetId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityPreviewConfig
            The config.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.frontend.get_entity_preview_config(
            dataset="dataset",
        )
        """
        _response = self._raw_client.get_entity_preview_config(dataset, request_options=request_options)
        return _response.data

    def get_me(self, *, request_options: typing.Optional[RequestOptions] = None) -> Me:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Me
            Description of the user

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.frontend.get_me()
        """
        _response = self._raw_client.get_me(request_options=request_options)
        return _response.data

    def list_datasets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FrontendDatasetId]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FrontendDatasetId]
            The available datasets.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.frontend.list_datasets()
        """
        _response = self._raw_client.list_datasets(request_options=request_options)
        return _response.data


class AsyncFrontendClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFrontendClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFrontendClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFrontendClient
        """
        return self._raw_client

    async def get_frontend_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> FrontendConfig:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FrontendConfig
            The Configuration for the Frontend

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.frontend.get_frontend_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_frontend_config(request_options=request_options)
        return _response.data

    async def get_entity_preview_config(
        self, dataset: DatasetId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntityPreviewConfig:
        """
        Parameters
        ----------
        dataset : DatasetId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityPreviewConfig
            The config.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.frontend.get_entity_preview_config(
                dataset="dataset",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entity_preview_config(dataset, request_options=request_options)
        return _response.data

    async def get_me(self, *, request_options: typing.Optional[RequestOptions] = None) -> Me:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Me
            Description of the user

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.frontend.get_me()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_me(request_options=request_options)
        return _response.data

    async def list_datasets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FrontendDatasetId]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FrontendDatasetId]
            The available datasets.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.frontend.list_datasets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_datasets(request_options=request_options)
        return _response.data
