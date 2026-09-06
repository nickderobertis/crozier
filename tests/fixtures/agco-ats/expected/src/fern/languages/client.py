

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_global_resources_shared_models_language import (
    ApiIPagedResponseGlobalResourcesSharedModelsLanguage,
)
from ..types.global_resources_shared_models_language import GlobalResourcesSharedModelsLanguage
from .raw_client import AsyncRawLanguagesClient, RawLanguagesClient


OMIT = typing.cast(typing.Any, ...)


class LanguagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLanguagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLanguagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLanguagesClient
        """
        return self._raw_client

    def getlanguages(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsLanguage:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            limit the number of Language objects returned. Optional (defaults to 10).

        offset : typing.Optional[int]
            the number of Language objects to skip. Optional (defaults to 0).

        include_deleted : typing.Optional[bool]
            whether to include languages marked as deleted. Defaults to false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsLanguage
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.languages.getlanguages()
        """
        _response = self._raw_client.getlanguages(
            limit=limit, offset=offset, include_deleted=include_deleted, request_options=request_options
        )
        return _response.data

    def createlanguage(
        self,
        *,
        description: str,
        locale_id: int,
        is_deleted: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            The description of the language (e.g. “English – United States”).

        locale_id : int
            The Locale Id of the language.

        is_deleted : typing.Optional[bool]
            Indicates whether the API supports the language. Must be false when created. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.languages.createlanguage(
            description="Description",
            locale_id=1,
        )
        """
        _response = self._raw_client.createlanguage(
            description=description, locale_id=locale_id, is_deleted=is_deleted, request_options=request_options
        )
        return _response.data

    def getlanguage(
        self, locale_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsLanguage:
        """
        No Documentation Found.

        Parameters
        ----------
        locale_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsLanguage
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.languages.getlanguage(
            locale_id=1,
        )
        """
        _response = self._raw_client.getlanguage(locale_id, request_options=request_options)
        return _response.data

    def updatelanguage(
        self,
        locale_id_: int,
        *,
        description: str,
        locale_id: int,
        is_deleted: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        locale_id_ : int


        description : str
            The description of the language (e.g. “English – United States”).

        locale_id : int
            The Locale Id of the language.

        is_deleted : typing.Optional[bool]
            Indicates whether the API supports the language. Must be false when created. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.languages.updatelanguage(
            locale_id_=1,
            description="Description",
            locale_id=1,
        )
        """
        _response = self._raw_client.updatelanguage(
            locale_id_,
            description=description,
            locale_id=locale_id,
            is_deleted=is_deleted,
            request_options=request_options,
        )
        return _response.data

    def deletelanguage(self, locale_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        locale_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.languages.deletelanguage(
            locale_id=1,
        )
        """
        _response = self._raw_client.deletelanguage(locale_id, request_options=request_options)
        return _response.data


class AsyncLanguagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLanguagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLanguagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLanguagesClient
        """
        return self._raw_client

    async def getlanguages(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsLanguage:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            limit the number of Language objects returned. Optional (defaults to 10).

        offset : typing.Optional[int]
            the number of Language objects to skip. Optional (defaults to 0).

        include_deleted : typing.Optional[bool]
            whether to include languages marked as deleted. Defaults to false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsLanguage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.languages.getlanguages()


        asyncio.run(main())
        """
        _response = await self._raw_client.getlanguages(
            limit=limit, offset=offset, include_deleted=include_deleted, request_options=request_options
        )
        return _response.data

    async def createlanguage(
        self,
        *,
        description: str,
        locale_id: int,
        is_deleted: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            The description of the language (e.g. “English – United States”).

        locale_id : int
            The Locale Id of the language.

        is_deleted : typing.Optional[bool]
            Indicates whether the API supports the language. Must be false when created. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.languages.createlanguage(
                description="Description",
                locale_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createlanguage(
            description=description, locale_id=locale_id, is_deleted=is_deleted, request_options=request_options
        )
        return _response.data

    async def getlanguage(
        self, locale_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsLanguage:
        """
        No Documentation Found.

        Parameters
        ----------
        locale_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsLanguage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.languages.getlanguage(
                locale_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getlanguage(locale_id, request_options=request_options)
        return _response.data

    async def updatelanguage(
        self,
        locale_id_: int,
        *,
        description: str,
        locale_id: int,
        is_deleted: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        locale_id_ : int


        description : str
            The description of the language (e.g. “English – United States”).

        locale_id : int
            The Locale Id of the language.

        is_deleted : typing.Optional[bool]
            Indicates whether the API supports the language. Must be false when created. Read Only.

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
            await client.languages.updatelanguage(
                locale_id_=1,
                description="Description",
                locale_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatelanguage(
            locale_id_,
            description=description,
            locale_id=locale_id,
            is_deleted=is_deleted,
            request_options=request_options,
        )
        return _response.data

    async def deletelanguage(self, locale_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        locale_id : int


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
            await client.languages.deletelanguage(
                locale_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletelanguage(locale_id, request_options=request_options)
        return _response.data
