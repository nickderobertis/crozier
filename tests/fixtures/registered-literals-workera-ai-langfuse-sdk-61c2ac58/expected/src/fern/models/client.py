

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.model import Model
from ..types.model_usage_unit import ModelUsageUnit
from ..types.paginated_models import PaginatedModels
from .raw_client import AsyncRawModelsClient, RawModelsClient


OMIT = typing.cast(typing.Any, ...)


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

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedModels:
        """
        Get all models

        Parameters
        ----------
        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedModels


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.models.list()
        """
        _response = self._raw_client.list(page=page, limit=limit, request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        model_name: str,
        match_pattern: str,
        start_date: typing.Optional[dt.datetime] = OMIT,
        unit: typing.Optional[ModelUsageUnit] = OMIT,
        input_price: typing.Optional[float] = OMIT,
        output_price: typing.Optional[float] = OMIT,
        total_price: typing.Optional[float] = OMIT,
        tokenizer_id: typing.Optional[str] = OMIT,
        tokenizer_config: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Model:
        """
        Create a model

        Parameters
        ----------
        model_name : str
            Name of the model definition. If multiple with the same name exist, they are applied in the following order: (1) custom over built-in, (2) newest according to startTime where model.startTime<observation.startTime

        match_pattern : str
            Regex pattern which matches this model definition to generation.model. Useful in case of fine-tuned models. If you want to exact match, use `(?i)^modelname$`

        start_date : typing.Optional[dt.datetime]
            Apply only to generations which are newer than this ISO date.

        unit : typing.Optional[ModelUsageUnit]
            Unit used by this model.

        input_price : typing.Optional[float]
            Price (USD) per input unit

        output_price : typing.Optional[float]
            Price (USD) per output unit

        total_price : typing.Optional[float]
            Price (USD) per total units. Cannot be set if input or output price is set.

        tokenizer_id : typing.Optional[str]
            Optional. Tokenizer to be applied to observations which match to this model. See docs for more details.

        tokenizer_config : typing.Optional[typing.Any]
            Optional. Configuration for the selected tokenizer. Needs to be JSON. See docs for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.models.create(
            model_name="modelName",
            match_pattern="matchPattern",
        )
        """
        _response = self._raw_client.create(
            model_name=model_name,
            match_pattern=match_pattern,
            start_date=start_date,
            unit=unit,
            input_price=input_price,
            output_price=output_price,
            total_price=total_price,
            tokenizer_id=tokenizer_id,
            tokenizer_config=tokenizer_config,
            request_options=request_options,
        )
        return _response.data

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Model:
        """
        Get a model

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.models.get(
            id="id",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a model. Cannot delete models managed by Langfuse. You can create your own definition with the same modelName to override the definition though.

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.models.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
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

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedModels:
        """
        Get all models

        Parameters
        ----------
        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedModels


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.models.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(page=page, limit=limit, request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        model_name: str,
        match_pattern: str,
        start_date: typing.Optional[dt.datetime] = OMIT,
        unit: typing.Optional[ModelUsageUnit] = OMIT,
        input_price: typing.Optional[float] = OMIT,
        output_price: typing.Optional[float] = OMIT,
        total_price: typing.Optional[float] = OMIT,
        tokenizer_id: typing.Optional[str] = OMIT,
        tokenizer_config: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Model:
        """
        Create a model

        Parameters
        ----------
        model_name : str
            Name of the model definition. If multiple with the same name exist, they are applied in the following order: (1) custom over built-in, (2) newest according to startTime where model.startTime<observation.startTime

        match_pattern : str
            Regex pattern which matches this model definition to generation.model. Useful in case of fine-tuned models. If you want to exact match, use `(?i)^modelname$`

        start_date : typing.Optional[dt.datetime]
            Apply only to generations which are newer than this ISO date.

        unit : typing.Optional[ModelUsageUnit]
            Unit used by this model.

        input_price : typing.Optional[float]
            Price (USD) per input unit

        output_price : typing.Optional[float]
            Price (USD) per output unit

        total_price : typing.Optional[float]
            Price (USD) per total units. Cannot be set if input or output price is set.

        tokenizer_id : typing.Optional[str]
            Optional. Tokenizer to be applied to observations which match to this model. See docs for more details.

        tokenizer_config : typing.Optional[typing.Any]
            Optional. Configuration for the selected tokenizer. Needs to be JSON. See docs for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.models.create(
                model_name="modelName",
                match_pattern="matchPattern",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            model_name=model_name,
            match_pattern=match_pattern,
            start_date=start_date,
            unit=unit,
            input_price=input_price,
            output_price=output_price,
            total_price=total_price,
            tokenizer_id=tokenizer_id,
            tokenizer_config=tokenizer_config,
            request_options=request_options,
        )
        return _response.data

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Model:
        """
        Get a model

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Model


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.models.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a model. Cannot delete models managed by Langfuse. You can create your own definition with the same modelName to override the definition though.

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.models.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data
