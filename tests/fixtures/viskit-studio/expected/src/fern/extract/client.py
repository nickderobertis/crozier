

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.extract_response import ExtractResponse
from .raw_client import AsyncRawExtractClient, RawExtractClient


OMIT = typing.cast(typing.Any, ...)


class ExtractClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExtractClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExtractClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExtractClient
        """
        return self._raw_client

    def warmup_extract_api_kits_warmup_extract_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Prime the vision provider connection so the first /extract call is warm.

        Deliberately uses probe(timeout=5) — a 5s deviation from the 30s default
        because this is a best-effort fire-and-forget warmup; we swallow all
        failures and always return 204 so the frontend never sees an error.

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.extract.warmup_extract_api_kits_warmup_extract_get()
        """
        _response = self._raw_client.warmup_extract_api_kits_warmup_extract_get(request_options=request_options)
        return _response.data

    def extract(
        self,
        kit_id: str,
        *,
        image_url: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractResponse:
        """
        Extract per-field inferences from a product image.

        Uses the vision provider (registry role "vision"); falls back to "llm" if
        the vision role is unavailable (R2 mitigation).

        Reserved-prefix guard: POST to kit_id='_warmup' returns 404 — defensive
        against POST collision with the GET /_warmup/extract warmup endpoint.

        Parameters
        ----------
        kit_id : str

        image_url : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.extract.extract(
            kit_id="kit_id",
            image_url="image_url",
        )
        """
        _response = self._raw_client.extract(
            kit_id, image_url=image_url, description=description, request_options=request_options
        )
        return _response.data


class AsyncExtractClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExtractClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExtractClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExtractClient
        """
        return self._raw_client

    async def warmup_extract_api_kits_warmup_extract_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Prime the vision provider connection so the first /extract call is warm.

        Deliberately uses probe(timeout=5) — a 5s deviation from the 30s default
        because this is a best-effort fire-and-forget warmup; we swallow all
        failures and always return 204 so the frontend never sees an error.

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.extract.warmup_extract_api_kits_warmup_extract_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.warmup_extract_api_kits_warmup_extract_get(request_options=request_options)
        return _response.data

    async def extract(
        self,
        kit_id: str,
        *,
        image_url: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractResponse:
        """
        Extract per-field inferences from a product image.

        Uses the vision provider (registry role "vision"); falls back to "llm" if
        the vision role is unavailable (R2 mitigation).

        Reserved-prefix guard: POST to kit_id='_warmup' returns 404 — defensive
        against POST collision with the GET /_warmup/extract warmup endpoint.

        Parameters
        ----------
        kit_id : str

        image_url : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.extract.extract(
                kit_id="kit_id",
                image_url="image_url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.extract(
            kit_id, image_url=image_url, description=description, request_options=request_options
        )
        return _response.data
