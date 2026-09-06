

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_oas_support_shared_models_translation_key import (
    ApiIPagedResponseOasSupportSharedModelsTranslationKey,
)
from ..types.oas_support_shared_models_translation_key import OasSupportSharedModelsTranslationKey
from .raw_client import AsyncRawTranslationkeysClient, RawTranslationkeysClient


OMIT = typing.cast(typing.Any, ...)


class TranslationkeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTranslationkeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTranslationkeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTranslationkeysClient
        """
        return self._raw_client

    def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        key_names: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseOasSupportSharedModelsTranslationKey:
        """


        Parameters
        ----------
        limit : typing.Optional[int]


        offset : typing.Optional[int]


        key_names : typing.Optional[str]
            Can filter by keyNames, a comma deliminated list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseOasSupportSharedModelsTranslationKey
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationkeys.get()
        """
        _response = self._raw_client.get(
            limit=limit, offset=offset, key_names=key_names, request_options=request_options
        )
        return _response.data

    def createtranslationkey(
        self,
        *,
        key_name: str,
        string_id: str,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        key_name : str
            The key name of the item. One example is tkODX_HWIKM14R01

        string_id : str
            Foreign key to StringDefinitionID

        id : typing.Optional[int]
            The identifier for the translationKey. Read Only.

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
        client.translationkeys.createtranslationkey(
            key_name="KeyName",
            string_id="StringID",
        )
        """
        _response = self._raw_client.createtranslationkey(
            key_name=key_name, string_id=string_id, id=id, request_options=request_options
        )
        return _response.data

    def gettranslationkey(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OasSupportSharedModelsTranslationKey:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OasSupportSharedModelsTranslationKey
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationkeys.gettranslationkey(
            id=1,
        )
        """
        _response = self._raw_client.gettranslationkey(id, request_options=request_options)
        return _response.data

    def updatetranslationkey(
        self,
        id_: int,
        *,
        key_name: str,
        string_id: str,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        key_name : str
            The key name of the item. One example is tkODX_HWIKM14R01

        string_id : str
            Foreign key to StringDefinitionID

        id : typing.Optional[int]
            The identifier for the translationKey. Read Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationkeys.updatetranslationkey(
            id_=1,
            key_name="KeyName",
            string_id="StringID",
        )
        """
        _response = self._raw_client.updatetranslationkey(
            id_, key_name=key_name, string_id=string_id, id=id, request_options=request_options
        )
        return _response.data


class AsyncTranslationkeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTranslationkeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTranslationkeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTranslationkeysClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        key_names: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseOasSupportSharedModelsTranslationKey:
        """


        Parameters
        ----------
        limit : typing.Optional[int]


        offset : typing.Optional[int]


        key_names : typing.Optional[str]
            Can filter by keyNames, a comma deliminated list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseOasSupportSharedModelsTranslationKey
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationkeys.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            limit=limit, offset=offset, key_names=key_names, request_options=request_options
        )
        return _response.data

    async def createtranslationkey(
        self,
        *,
        key_name: str,
        string_id: str,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        key_name : str
            The key name of the item. One example is tkODX_HWIKM14R01

        string_id : str
            Foreign key to StringDefinitionID

        id : typing.Optional[int]
            The identifier for the translationKey. Read Only.

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
            await client.translationkeys.createtranslationkey(
                key_name="KeyName",
                string_id="StringID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createtranslationkey(
            key_name=key_name, string_id=string_id, id=id, request_options=request_options
        )
        return _response.data

    async def gettranslationkey(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OasSupportSharedModelsTranslationKey:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OasSupportSharedModelsTranslationKey
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationkeys.gettranslationkey(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gettranslationkey(id, request_options=request_options)
        return _response.data

    async def updatetranslationkey(
        self,
        id_: int,
        *,
        key_name: str,
        string_id: str,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        key_name : str
            The key name of the item. One example is tkODX_HWIKM14R01

        string_id : str
            Foreign key to StringDefinitionID

        id : typing.Optional[int]
            The identifier for the translationKey. Read Only.

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
            await client.translationkeys.updatetranslationkey(
                id_=1,
                key_name="KeyName",
                string_id="StringID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatetranslationkey(
            id_, key_name=key_name, string_id=string_id, id=id, request_options=request_options
        )
        return _response.data
