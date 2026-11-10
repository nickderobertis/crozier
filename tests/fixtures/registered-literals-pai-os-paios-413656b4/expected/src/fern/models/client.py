

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delete_model_response import DeleteModelResponse
from ..types.list_models_response import ListModelsResponse
from ..types.model import Model
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

    def list_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListModelsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListModelsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.models.list_models()
        """
        _response = self._raw_client.list_models(request_options=request_options)
        return _response.data

    def retrieve_model(self, model: str, *, request_options: typing.Optional[RequestOptions] = None) -> Model:
        """
        Parameters
        ----------
        model : str
            The ID of the model to use for this request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.models.retrieve_model(
            model="gpt-3.5-turbo",
        )
        """
        _response = self._raw_client.retrieve_model(model, request_options=request_options)
        return _response.data

    def delete_model(
        self, model: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteModelResponse:
        """
        Parameters
        ----------
        model : str
            The model to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteModelResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.models.delete_model(
            model="ft:gpt-3.5-turbo:acemeco:suffix:abc123",
        )
        """
        _response = self._raw_client.delete_model(model, request_options=request_options)
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

    async def list_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListModelsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListModelsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.models.list_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_models(request_options=request_options)
        return _response.data

    async def retrieve_model(self, model: str, *, request_options: typing.Optional[RequestOptions] = None) -> Model:
        """
        Parameters
        ----------
        model : str
            The ID of the model to use for this request

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.models.retrieve_model(
                model="gpt-3.5-turbo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_model(model, request_options=request_options)
        return _response.data

    async def delete_model(
        self, model: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteModelResponse:
        """
        Parameters
        ----------
        model : str
            The model to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteModelResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.models.delete_model(
                model="ft:gpt-3.5-turbo:acemeco:suffix:abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_model(model, request_options=request_options)
        return _response.data
