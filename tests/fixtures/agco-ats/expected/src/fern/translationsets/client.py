

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_global_resources_shared_models_translation_set import (
    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet,
)
from ..types.api_i_paged_response_global_resources_shared_models_translation_set_attribute import (
    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute,
)
from ..types.api_i_paged_response_global_resources_shared_models_translation_set_source_string import (
    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString,
)
from ..types.api_i_paged_response_global_resources_shared_models_translation_set_string import (
    ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString,
)
from ..types.global_resources_shared_models_translation_set import GlobalResourcesSharedModelsTranslationSet
from ..types.global_resources_shared_models_translation_set_attribute import (
    GlobalResourcesSharedModelsTranslationSetAttribute,
)
from ..types.global_resources_shared_models_translation_set_state import GlobalResourcesSharedModelsTranslationSetState
from ..types.global_resources_shared_models_translation_set_statistics import (
    GlobalResourcesSharedModelsTranslationSetStatistics,
)
from ..types.global_resources_shared_models_translation_set_string import (
    GlobalResourcesSharedModelsTranslationSetString,
)
from .raw_client import AsyncRawTranslationsetsClient, RawTranslationsetsClient
from .types.translation_sets_get_translation_sets_request_state import TranslationSetsGetTranslationSetsRequestState


OMIT = typing.cast(typing.Any, ...)


class TranslationsetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTranslationsetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTranslationsetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTranslationsetsClient
        """
        return self._raw_client

    def updatetranslationsetattributes(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, GlobalResourcesSharedModelsTranslationSetAttribute

        client = FernApi()
        client.translationsets.updatetranslationsetattributes(
            request=[
                GlobalResourcesSharedModelsTranslationSetAttribute(
                    name="Name",
                )
            ],
        )
        """
        _response = self._raw_client.updatetranslationsetattributes(request=request, request_options=request_options)
        return _response.data

    def updatetranslationsetattribute(
        self,
        id_: int,
        *,
        name: str,
        id: typing.Optional[int] = OMIT,
        translation_set_id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        name : str
            The name of this Attribute.

        id : typing.Optional[int]
            The ID of this attribute.

        translation_set_id : typing.Optional[int]
            The ID of the translation set to which this attribute belongs.

        value : typing.Optional[str]
            The value of this Attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationsets.updatetranslationsetattribute(
            id_=1,
            name="Name",
        )
        """
        _response = self._raw_client.updatetranslationsetattribute(
            id_, name=name, id=id, translation_set_id=translation_set_id, value=value, request_options=request_options
        )
        return _response.data

    def deletetranslationsetattribute(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationsets.deletetranslationsetattribute(
            id=1,
        )
        """
        _response = self._raw_client.deletetranslationsetattribute(id, request_options=request_options)
        return _response.data

    def gettranslationsets(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        translation_request_id: typing.Optional[int] = None,
        state: typing.Optional[TranslationSetsGetTranslationSetsRequestState] = None,
        string_id: typing.Optional[str] = None,
        language_id: typing.Optional[int] = None,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]


        offset : typing.Optional[int]


        translation_request_id : typing.Optional[int]


        state : typing.Optional[TranslationSetsGetTranslationSetsRequestState]


        string_id : typing.Optional[str]


        language_id : typing.Optional[int]


        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationsets.gettranslationsets()
        """
        _response = self._raw_client.gettranslationsets(
            limit=limit,
            offset=offset,
            translation_request_id=translation_request_id,
            state=state,
            string_id=string_id,
            language_id=language_id,
            include_attributes=include_attributes,
            request_options=request_options,
        )
        return _response.data

    def gettranslationset(
        self,
        id: int,
        *,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlobalResourcesSharedModelsTranslationSet:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this Translation set. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsTranslationSet
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationsets.gettranslationset(
            id=1,
        )
        """
        _response = self._raw_client.gettranslationset(
            id, include_attributes=include_attributes, request_options=request_options
        )
        return _response.data

    def updatetranslationset(
        self,
        id_: int,
        *,
        file_i_ds: typing.Sequence[str],
        state: GlobalResourcesSharedModelsTranslationSetState,
        attributes: typing.Optional[typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]] = OMIT,
        id: typing.Optional[int] = OMIT,
        in_date: typing.Optional[dt.datetime] = OMIT,
        notes: typing.Optional[str] = OMIT,
        out_date: typing.Optional[dt.datetime] = OMIT,
        translation_request_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        file_i_ds : typing.Sequence[str]
            IDs for files related to this translation set. For example, the original and processed files

        state : GlobalResourcesSharedModelsTranslationSetState
            An enum indicating the state of the translation set

        attributes : typing.Optional[typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]]
            Attributes of the Translation Set

        id : typing.Optional[int]
            The id of the TranslationSet.

        in_date : typing.Optional[dt.datetime]
            Read Only. The date the translation set was returned.

        notes : typing.Optional[str]
            Notes on the TranslationSet

        out_date : typing.Optional[dt.datetime]
            Read Only. The date the translation set was sent out.

        translation_request_id : typing.Optional[int]
            Read Only. The Id of the TranslationRequest which generated this translation set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, GlobalResourcesSharedModelsTranslationSetState

        client = FernApi()
        client.translationsets.updatetranslationset(
            id_=1,
            file_i_ds=["FileIDs"],
            state=GlobalResourcesSharedModelsTranslationSetState.OUT_FOR_PROCESSING,
        )
        """
        _response = self._raw_client.updatetranslationset(
            id_,
            file_i_ds=file_i_ds,
            state=state,
            attributes=attributes,
            id=id,
            in_date=in_date,
            notes=notes,
            out_date=out_date,
            translation_request_id=translation_request_id,
            request_options=request_options,
        )
        return _response.data

    def gettranslationsetattributes(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        limit : typing.Optional[int]


        offset : typing.Optional[int]


        name : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationsets.gettranslationsetattributes(
            id=1,
        )
        """
        _response = self._raw_client.gettranslationsetattributes(
            id, limit=limit, offset=offset, name=name, request_options=request_options
        )
        return _response.data

    def posttranslationsetattribute(
        self,
        id_: int,
        *,
        name: str,
        id: typing.Optional[int] = OMIT,
        translation_set_id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        name : str
            The name of this Attribute.

        id : typing.Optional[int]
            The ID of this attribute.

        translation_set_id : typing.Optional[int]
            The ID of the translation set to which this attribute belongs.

        value : typing.Optional[str]
            The value of this Attribute

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
        client.translationsets.posttranslationsetattribute(
            id_=1,
            name="Name",
        )
        """
        _response = self._raw_client.posttranslationsetattribute(
            id_, name=name, id=id, translation_set_id=translation_set_id, value=value, request_options=request_options
        )
        return _response.data

    def posttranslationsetattributes(
        self,
        id: int,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request : typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, GlobalResourcesSharedModelsTranslationSetAttribute

        client = FernApi()
        client.translationsets.posttranslationsetattributes(
            id=1,
            request=[
                GlobalResourcesSharedModelsTranslationSetAttribute(
                    name="Name",
                )
            ],
        )
        """
        _response = self._raw_client.posttranslationsetattributes(id, request=request, request_options=request_options)
        return _response.data

    def getsourcestrings(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        limit : typing.Optional[int]


        offset : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationsets.getsourcestrings(
            id=1,
        )
        """
        _response = self._raw_client.getsourcestrings(id, limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def getstatistics(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsTranslationSetStatistics:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsTranslationSetStatistics
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationsets.getstatistics(
            id=1,
        )
        """
        _response = self._raw_client.getstatistics(id, request_options=request_options)
        return _response.data

    def gettranslationsetstrings(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        limit : typing.Optional[int]


        offset : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.translationsets.gettranslationsetstrings(
            id=1,
        )
        """
        _response = self._raw_client.gettranslationsetstrings(
            id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def updatetranslationsetstrings(
        self,
        id: int,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsTranslationSetString],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request : typing.Sequence[GlobalResourcesSharedModelsTranslationSetString]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, GlobalResourcesSharedModelsTranslationSetString

        client = FernApi()
        client.translationsets.updatetranslationsetstrings(
            id=1,
            request=[
                GlobalResourcesSharedModelsTranslationSetString(
                    language_id=1,
                    string_id="StringID",
                    translation_set_id=1,
                )
            ],
        )
        """
        _response = self._raw_client.updatetranslationsetstrings(id, request=request, request_options=request_options)
        return _response.data


class AsyncTranslationsetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTranslationsetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTranslationsetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTranslationsetsClient
        """
        return self._raw_client

    async def updatetranslationsetattributes(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            GlobalResourcesSharedModelsTranslationSetAttribute,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationsets.updatetranslationsetattributes(
                request=[
                    GlobalResourcesSharedModelsTranslationSetAttribute(
                        name="Name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatetranslationsetattributes(
            request=request, request_options=request_options
        )
        return _response.data

    async def updatetranslationsetattribute(
        self,
        id_: int,
        *,
        name: str,
        id: typing.Optional[int] = OMIT,
        translation_set_id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        name : str
            The name of this Attribute.

        id : typing.Optional[int]
            The ID of this attribute.

        translation_set_id : typing.Optional[int]
            The ID of the translation set to which this attribute belongs.

        value : typing.Optional[str]
            The value of this Attribute

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
            await client.translationsets.updatetranslationsetattribute(
                id_=1,
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatetranslationsetattribute(
            id_, name=name, id=id, translation_set_id=translation_set_id, value=value, request_options=request_options
        )
        return _response.data

    async def deletetranslationsetattribute(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


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
            await client.translationsets.deletetranslationsetattribute(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletetranslationsetattribute(id, request_options=request_options)
        return _response.data

    async def gettranslationsets(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        translation_request_id: typing.Optional[int] = None,
        state: typing.Optional[TranslationSetsGetTranslationSetsRequestState] = None,
        string_id: typing.Optional[str] = None,
        language_id: typing.Optional[int] = None,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]


        offset : typing.Optional[int]


        translation_request_id : typing.Optional[int]


        state : typing.Optional[TranslationSetsGetTranslationSetsRequestState]


        string_id : typing.Optional[str]


        language_id : typing.Optional[int]


        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsTranslationSet
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationsets.gettranslationsets()


        asyncio.run(main())
        """
        _response = await self._raw_client.gettranslationsets(
            limit=limit,
            offset=offset,
            translation_request_id=translation_request_id,
            state=state,
            string_id=string_id,
            language_id=language_id,
            include_attributes=include_attributes,
            request_options=request_options,
        )
        return _response.data

    async def gettranslationset(
        self,
        id: int,
        *,
        include_attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlobalResourcesSharedModelsTranslationSet:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        include_attributes : typing.Optional[str]
            Names of Attributes to include when retrieving this Translation set. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsTranslationSet
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationsets.gettranslationset(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gettranslationset(
            id, include_attributes=include_attributes, request_options=request_options
        )
        return _response.data

    async def updatetranslationset(
        self,
        id_: int,
        *,
        file_i_ds: typing.Sequence[str],
        state: GlobalResourcesSharedModelsTranslationSetState,
        attributes: typing.Optional[typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]] = OMIT,
        id: typing.Optional[int] = OMIT,
        in_date: typing.Optional[dt.datetime] = OMIT,
        notes: typing.Optional[str] = OMIT,
        out_date: typing.Optional[dt.datetime] = OMIT,
        translation_request_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        file_i_ds : typing.Sequence[str]
            IDs for files related to this translation set. For example, the original and processed files

        state : GlobalResourcesSharedModelsTranslationSetState
            An enum indicating the state of the translation set

        attributes : typing.Optional[typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]]
            Attributes of the Translation Set

        id : typing.Optional[int]
            The id of the TranslationSet.

        in_date : typing.Optional[dt.datetime]
            Read Only. The date the translation set was returned.

        notes : typing.Optional[str]
            Notes on the TranslationSet

        out_date : typing.Optional[dt.datetime]
            Read Only. The date the translation set was sent out.

        translation_request_id : typing.Optional[int]
            Read Only. The Id of the TranslationRequest which generated this translation set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GlobalResourcesSharedModelsTranslationSetState

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationsets.updatetranslationset(
                id_=1,
                file_i_ds=["FileIDs"],
                state=GlobalResourcesSharedModelsTranslationSetState.OUT_FOR_PROCESSING,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatetranslationset(
            id_,
            file_i_ds=file_i_ds,
            state=state,
            attributes=attributes,
            id=id,
            in_date=in_date,
            notes=notes,
            out_date=out_date,
            translation_request_id=translation_request_id,
            request_options=request_options,
        )
        return _response.data

    async def gettranslationsetattributes(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        limit : typing.Optional[int]


        offset : typing.Optional[int]


        name : typing.Optional[str]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationsets.gettranslationsetattributes(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gettranslationsetattributes(
            id, limit=limit, offset=offset, name=name, request_options=request_options
        )
        return _response.data

    async def posttranslationsetattribute(
        self,
        id_: int,
        *,
        name: str,
        id: typing.Optional[int] = OMIT,
        translation_set_id: typing.Optional[int] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int


        name : str
            The name of this Attribute.

        id : typing.Optional[int]
            The ID of this attribute.

        translation_set_id : typing.Optional[int]
            The ID of the translation set to which this attribute belongs.

        value : typing.Optional[str]
            The value of this Attribute

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
            await client.translationsets.posttranslationsetattribute(
                id_=1,
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.posttranslationsetattribute(
            id_, name=name, id=id, translation_set_id=translation_set_id, value=value, request_options=request_options
        )
        return _response.data

    async def posttranslationsetattributes(
        self,
        id: int,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request : typing.Sequence[GlobalResourcesSharedModelsTranslationSetAttribute]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            GlobalResourcesSharedModelsTranslationSetAttribute,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationsets.posttranslationsetattributes(
                id=1,
                request=[
                    GlobalResourcesSharedModelsTranslationSetAttribute(
                        name="Name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.posttranslationsetattributes(
            id, request=request, request_options=request_options
        )
        return _response.data

    async def getsourcestrings(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        limit : typing.Optional[int]


        offset : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationsets.getsourcestrings(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getsourcestrings(
            id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def getstatistics(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsTranslationSetStatistics:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsTranslationSetStatistics
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationsets.getstatistics(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getstatistics(id, request_options=request_options)
        return _response.data

    async def gettranslationsetstrings(
        self,
        id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int


        limit : typing.Optional[int]


        offset : typing.Optional[int]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsTranslationSetString
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationsets.gettranslationsetstrings(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.gettranslationsetstrings(
            id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def updatetranslationsetstrings(
        self,
        id: int,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsTranslationSetString],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int

        request : typing.Sequence[GlobalResourcesSharedModelsTranslationSetString]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GlobalResourcesSharedModelsTranslationSetString

        client = AsyncFernApi()


        async def main() -> None:
            await client.translationsets.updatetranslationsetstrings(
                id=1,
                request=[
                    GlobalResourcesSharedModelsTranslationSetString(
                        language_id=1,
                        string_id="StringID",
                        translation_set_id=1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatetranslationsetstrings(
            id, request=request, request_options=request_options
        )
        return _response.data
