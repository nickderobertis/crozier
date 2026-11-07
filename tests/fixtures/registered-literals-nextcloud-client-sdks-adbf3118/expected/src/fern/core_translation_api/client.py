

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_translation_api_languages200response import CoreTranslationApiLanguages200Response
from ..types.core_translation_api_translate200response import CoreTranslationApiTranslate200Response
from .raw_client import AsyncRawCoreTranslationApiClient, RawCoreTranslationApiClient


class CoreTranslationApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreTranslationApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreTranslationApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreTranslationApiClient
        """
        return self._raw_client

    def languages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreTranslationApiLanguages200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreTranslationApiLanguages200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_translation_api.languages()
        """
        _response = self._raw_client.languages(request_options=request_options)
        return _response.data

    def translate(
        self,
        *,
        text: str,
        to_language: str,
        from_language: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreTranslationApiTranslate200Response:
        """
        Parameters
        ----------
        text : str
            Text to be translated

        to_language : str
            Language to translate to

        from_language : typing.Optional[str]
            Language to translate from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreTranslationApiTranslate200Response
            Translated text returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_translation_api.translate(
            text="text",
            to_language="toLanguage",
        )
        """
        _response = self._raw_client.translate(
            text=text, to_language=to_language, from_language=from_language, request_options=request_options
        )
        return _response.data


class AsyncCoreTranslationApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreTranslationApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreTranslationApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreTranslationApiClient
        """
        return self._raw_client

    async def languages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreTranslationApiLanguages200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreTranslationApiLanguages200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_translation_api.languages()


        asyncio.run(main())
        """
        _response = await self._raw_client.languages(request_options=request_options)
        return _response.data

    async def translate(
        self,
        *,
        text: str,
        to_language: str,
        from_language: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreTranslationApiTranslate200Response:
        """
        Parameters
        ----------
        text : str
            Text to be translated

        to_language : str
            Language to translate to

        from_language : typing.Optional[str]
            Language to translate from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreTranslationApiTranslate200Response
            Translated text returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_translation_api.translate(
                text="text",
                to_language="toLanguage",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.translate(
            text=text, to_language=to_language, from_language=from_language, request_options=request_options
        )
        return _response.data
