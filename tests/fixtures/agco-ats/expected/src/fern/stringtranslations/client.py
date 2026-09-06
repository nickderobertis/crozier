

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_global_resources_shared_models_string_translation import (
    ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation,
)
from ..types.global_resources_shared_models_string_translation import GlobalResourcesSharedModelsStringTranslation
from ..types.global_resources_shared_models_string_translation_state import (
    GlobalResourcesSharedModelsStringTranslationState,
)
from .raw_client import AsyncRawStringtranslationsClient, RawStringtranslationsClient


OMIT = typing.cast(typing.Any, ...)


class StringtranslationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStringtranslationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStringtranslationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStringtranslationsClient
        """
        return self._raw_client

    def gettranslations(
        self,
        *,
        limit: typing.Optional[int] = None,
        modified_after_timestamp: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        modified_after_timestamp : typing.Optional[str]
            Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.stringtranslations.gettranslations()
        """
        _response = self._raw_client.gettranslations(
            limit=limit, modified_after_timestamp=modified_after_timestamp, request_options=request_options
        )
        return _response.data

    def updatetranslations(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsStringTranslation],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsStringTranslation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, GlobalResourcesSharedModelsStringTranslation

        client = FernApi()
        client.stringtranslations.updatetranslations(
            request=[
                GlobalResourcesSharedModelsStringTranslation(
                    string_value="StringValue",
                )
            ],
        )
        """
        _response = self._raw_client.updatetranslations(request=request, request_options=request_options)
        return _response.data

    def gettranslation(
        self, string_id: str, language_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsStringTranslation:
        """
        No Documentation Found.

        Parameters
        ----------
        string_id : str


        language_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsStringTranslation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.stringtranslations.gettranslation(
            string_id="stringId",
            language_id=1,
        )
        """
        _response = self._raw_client.gettranslation(string_id, language_id, request_options=request_options)
        return _response.data

    def updatetranslation(
        self,
        string_id_: str,
        language_id_: int,
        *,
        string_value: str,
        author_id: typing.Optional[int] = OMIT,
        language_id: typing.Optional[int] = OMIT,
        state: typing.Optional[GlobalResourcesSharedModelsStringTranslationState] = OMIT,
        string_id: typing.Optional[str] = OMIT,
        timestamp: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        string_id_ : str


        language_id_ : int


        string_value : str
            The translated string

        author_id : typing.Optional[int]
            The id of the user to last edit thie translation

        language_id : typing.Optional[int]
            The id of the language of the translation

        state : typing.Optional[GlobalResourcesSharedModelsStringTranslationState]
            The state of the translation

        string_id : typing.Optional[str]
            The id of the string that is translated

        timestamp : typing.Optional[str]
            A value indicating the last modification of this translation. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.stringtranslations.updatetranslation(
            string_id_="stringId",
            language_id_=1,
            string_value="StringValue",
        )
        """
        _response = self._raw_client.updatetranslation(
            string_id_,
            language_id_,
            string_value=string_value,
            author_id=author_id,
            language_id=language_id,
            state=state,
            string_id=string_id,
            timestamp=timestamp,
            request_options=request_options,
        )
        return _response.data


class AsyncStringtranslationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStringtranslationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStringtranslationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStringtranslationsClient
        """
        return self._raw_client

    async def gettranslations(
        self,
        *,
        limit: typing.Optional[int] = None,
        modified_after_timestamp: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        modified_after_timestamp : typing.Optional[str]
            Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsStringTranslation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.stringtranslations.gettranslations()


        asyncio.run(main())
        """
        _response = await self._raw_client.gettranslations(
            limit=limit, modified_after_timestamp=modified_after_timestamp, request_options=request_options
        )
        return _response.data

    async def updatetranslations(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsStringTranslation],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsStringTranslation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GlobalResourcesSharedModelsStringTranslation

        client = AsyncFernApi()


        async def main() -> None:
            await client.stringtranslations.updatetranslations(
                request=[
                    GlobalResourcesSharedModelsStringTranslation(
                        string_value="StringValue",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatetranslations(request=request, request_options=request_options)
        return _response.data

    async def gettranslation(
        self, string_id: str, language_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsStringTranslation:
        """
        No Documentation Found.

        Parameters
        ----------
        string_id : str


        language_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsStringTranslation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.stringtranslations.gettranslation(
                string_id="stringId",
                language_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gettranslation(string_id, language_id, request_options=request_options)
        return _response.data

    async def updatetranslation(
        self,
        string_id_: str,
        language_id_: int,
        *,
        string_value: str,
        author_id: typing.Optional[int] = OMIT,
        language_id: typing.Optional[int] = OMIT,
        state: typing.Optional[GlobalResourcesSharedModelsStringTranslationState] = OMIT,
        string_id: typing.Optional[str] = OMIT,
        timestamp: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        string_id_ : str


        language_id_ : int


        string_value : str
            The translated string

        author_id : typing.Optional[int]
            The id of the user to last edit thie translation

        language_id : typing.Optional[int]
            The id of the language of the translation

        state : typing.Optional[GlobalResourcesSharedModelsStringTranslationState]
            The state of the translation

        string_id : typing.Optional[str]
            The id of the string that is translated

        timestamp : typing.Optional[str]
            A value indicating the last modification of this translation. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.stringtranslations.updatetranslation(
                string_id_="stringId",
                language_id_=1,
                string_value="StringValue",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatetranslation(
            string_id_,
            language_id_,
            string_value=string_value,
            author_id=author_id,
            language_id=language_id,
            state=state,
            string_id=string_id,
            timestamp=timestamp,
            request_options=request_options,
        )
        return _response.data
