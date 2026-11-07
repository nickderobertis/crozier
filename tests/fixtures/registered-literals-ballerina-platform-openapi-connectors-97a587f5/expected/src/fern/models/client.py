

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.model import Model
from ..types.model_list import ModelList
from .raw_client import AsyncRawModelsClient, RawModelsClient


class ModelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawModelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawModelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawModelsClient
        """
        return self._raw_client

    def list(self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None) -> ModelList:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelList
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.models.list(
            api_version="api-version",
        )
        """
        _response = self._raw_client.list(api_version=api_version, request_options=request_options)
        return _response.data

    def get(self, model_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None) -> Model:
        """
        Parameters
        ----------
        model_id : str
            The identifier of the model.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.models.get(
            model_id="model-id",
            api_version="api-version",
        )
        """
        _response = self._raw_client.get(model_id, api_version=api_version, request_options=request_options)
        return _response.data


class AsyncModelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawModelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawModelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawModelsClient
        """
        return self._raw_client

    async def list(self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None) -> ModelList:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelList
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.models.list(
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(api_version=api_version, request_options=request_options)
        return _response.data

    async def get(
        self, model_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Model:
        """
        Parameters
        ----------
        model_id : str
            The identifier of the model.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.models.get(
                model_id="model-id",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(model_id, api_version=api_version, request_options=request_options)
        return _response.data
