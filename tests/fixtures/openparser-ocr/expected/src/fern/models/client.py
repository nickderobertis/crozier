

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ocr_llm_models_response import OcrLlmModelsResponse
from ..types.ocr_models_response import OcrModelsResponse
from .raw_client import AsyncRawModelsClient, RawModelsClient
from .types.list_llm_models_request_mode import ListLlmModelsRequestMode


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

    def list_ocr_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> OcrModelsResponse:
        """
        Returns the hosted OCR model registry with current capabilities, option defaults,
        retail page prices, and availability. Clients should discover this endpoint instead of
        hard-coding model IDs or provider-specific options.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcrModelsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.models.list_ocr_models()
        """
        _response = self._raw_client.list_ocr_models(request_options=request_options)
        return _response.data

    def list_llm_models(
        self,
        *,
        mode: typing.Optional[ListLlmModelsRequestMode] = None,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OcrLlmModelsResponse:
        """
        Returns a cached, normalized OpenRouter catalog filtered to models that advertise
        strict structured output (`structured_outputs` + `response_format`), have valid finite
        provider-list cost (internally) that is converted to customer retail rates, produce text, and are not expired.

        Default `mode=suggested` returns a short recommended subset. `mode=search` discovers the
        full compatible catalog with optional `q` / pagination. Field grounding and schema
        suggestion remain restricted to certified models.

        Parameters
        ----------
        mode : typing.Optional[ListLlmModelsRequestMode]
            `suggested` (default): short recommended subset.
            `search`: full compatible catalog filtered by `q`.

        q : typing.Optional[str]
            Case-insensitive substring match against id, label, or provider. Used with `mode=search`.

        page : typing.Optional[int]
            1-based page index when paginating search results.

        limit : typing.Optional[int]
            Page size for search; ignored for suggested mode (bounded server-side).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcrLlmModelsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.models.list_llm_models()
        """
        _response = self._raw_client.list_llm_models(
            mode=mode, q=q, page=page, limit=limit, request_options=request_options
        )
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

    async def list_ocr_models(self, *, request_options: typing.Optional[RequestOptions] = None) -> OcrModelsResponse:
        """
        Returns the hosted OCR model registry with current capabilities, option defaults,
        retail page prices, and availability. Clients should discover this endpoint instead of
        hard-coding model IDs or provider-specific options.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcrModelsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.models.list_ocr_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_ocr_models(request_options=request_options)
        return _response.data

    async def list_llm_models(
        self,
        *,
        mode: typing.Optional[ListLlmModelsRequestMode] = None,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OcrLlmModelsResponse:
        """
        Returns a cached, normalized OpenRouter catalog filtered to models that advertise
        strict structured output (`structured_outputs` + `response_format`), have valid finite
        provider-list cost (internally) that is converted to customer retail rates, produce text, and are not expired.

        Default `mode=suggested` returns a short recommended subset. `mode=search` discovers the
        full compatible catalog with optional `q` / pagination. Field grounding and schema
        suggestion remain restricted to certified models.

        Parameters
        ----------
        mode : typing.Optional[ListLlmModelsRequestMode]
            `suggested` (default): short recommended subset.
            `search`: full compatible catalog filtered by `q`.

        q : typing.Optional[str]
            Case-insensitive substring match against id, label, or provider. Used with `mode=search`.

        page : typing.Optional[int]
            1-based page index when paginating search results.

        limit : typing.Optional[int]
            Page size for search; ignored for suggested mode (bounded server-side).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcrLlmModelsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.models.list_llm_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_llm_models(
            mode=mode, q=q, page=page, limit=limit, request_options=request_options
        )
        return _response.data
