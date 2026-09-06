

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_global_resources_shared_models_string_definition import (
    ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition,
)
from ..types.global_resources_shared_models_string_definition import GlobalResourcesSharedModelsStringDefinition
from .raw_client import AsyncRawStringdefinitionsClient, RawStringdefinitionsClient


OMIT = typing.cast(typing.Any, ...)


class StringdefinitionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStringdefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStringdefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStringdefinitionsClient
        """
        return self._raw_client

    def getdefinitions(
        self,
        *,
        limit: typing.Optional[int] = None,
        modified_after_timestamp: typing.Optional[str] = None,
        include_translations: typing.Optional[bool] = None,
        string_text: typing.Optional[str] = None,
        description_text: typing.Optional[str] = None,
        use_full_text: typing.Optional[bool] = None,
        include_deleted_languages: typing.Optional[bool] = None,
        language_ids: typing.Optional[str] = None,
        string_ids: typing.Optional[str] = None,
        matching_translations_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10. Ignored if 'stringIds' is provided.

        modified_after_timestamp : typing.Optional[str]
            Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.

        include_translations : typing.Optional[bool]
            Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.

        string_text : typing.Optional[str]
            Optional. The text for which to search in the StringDefinition object’s translations. Only StringDefinition objects for matching StringTranslation objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards. includeTranslations must be true.

        description_text : typing.Optional[str]
            Optional. The text for which to search in the StringDefinition description field. Only matching objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards.

        use_full_text : typing.Optional[bool]
            Optional. This flag is used to determin whether to use the FullText Search or not.

        include_deleted_languages : typing.Optional[bool]
            Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.

        language_ids : typing.Optional[str]
            Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.

        string_ids : typing.Optional[str]
            Optional. A comma-delimited list of string ids. Up to 40 string IDs may be provided. May not be used with 'modifiedAfterTimestamp', 'stringText', 'descriptionText', or 'useFullText'.

        matching_translations_only : typing.Optional[bool]
            Optional. If false, all translations for returned String Definitions are included. Must be used with 'stringText' provided and 'includeTranslations' = true.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.stringdefinitions.getdefinitions()
        """
        _response = self._raw_client.getdefinitions(
            limit=limit,
            modified_after_timestamp=modified_after_timestamp,
            include_translations=include_translations,
            string_text=string_text,
            description_text=description_text,
            use_full_text=use_full_text,
            include_deleted_languages=include_deleted_languages,
            language_ids=language_ids,
            string_ids=string_ids,
            matching_translations_only=matching_translations_only,
            request_options=request_options,
        )
        return _response.data

    def postdefinition(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsStringDefinition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsStringDefinition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, GlobalResourcesSharedModelsStringDefinition

        client = FernApi()
        client.stringdefinitions.postdefinition(
            request=[
                GlobalResourcesSharedModelsStringDefinition(
                    description_for_translator="DescriptionForTranslator",
                )
            ],
        )
        """
        _response = self._raw_client.postdefinition(request=request, request_options=request_options)
        return _response.data

    def updatedefinitions(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsStringDefinition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsStringDefinition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, GlobalResourcesSharedModelsStringDefinition

        client = FernApi()
        client.stringdefinitions.updatedefinitions(
            request=[
                GlobalResourcesSharedModelsStringDefinition(
                    description_for_translator="DescriptionForTranslator",
                )
            ],
        )
        """
        _response = self._raw_client.updatedefinitions(request=request, request_options=request_options)
        return _response.data

    def getdefinition(
        self,
        id: str,
        *,
        include_translations: typing.Optional[bool] = None,
        include_deleted_languages: typing.Optional[bool] = None,
        language_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlobalResourcesSharedModelsStringDefinition:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        include_translations : typing.Optional[bool]
            Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.

        include_deleted_languages : typing.Optional[bool]
            Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.

        language_ids : typing.Optional[str]
            Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsStringDefinition
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.stringdefinitions.getdefinition(
            id="ID",
        )
        """
        _response = self._raw_client.getdefinition(
            id,
            include_translations=include_translations,
            include_deleted_languages=include_deleted_languages,
            language_ids=language_ids,
            request_options=request_options,
        )
        return _response.data


class AsyncStringdefinitionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStringdefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStringdefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStringdefinitionsClient
        """
        return self._raw_client

    async def getdefinitions(
        self,
        *,
        limit: typing.Optional[int] = None,
        modified_after_timestamp: typing.Optional[str] = None,
        include_translations: typing.Optional[bool] = None,
        string_text: typing.Optional[str] = None,
        description_text: typing.Optional[str] = None,
        use_full_text: typing.Optional[bool] = None,
        include_deleted_languages: typing.Optional[bool] = None,
        language_ids: typing.Optional[str] = None,
        string_ids: typing.Optional[str] = None,
        matching_translations_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10. Ignored if 'stringIds' is provided.

        modified_after_timestamp : typing.Optional[str]
            Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.

        include_translations : typing.Optional[bool]
            Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.

        string_text : typing.Optional[str]
            Optional. The text for which to search in the StringDefinition object’s translations. Only StringDefinition objects for matching StringTranslation objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards. includeTranslations must be true.

        description_text : typing.Optional[str]
            Optional. The text for which to search in the StringDefinition description field. Only matching objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards.

        use_full_text : typing.Optional[bool]
            Optional. This flag is used to determin whether to use the FullText Search or not.

        include_deleted_languages : typing.Optional[bool]
            Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.

        language_ids : typing.Optional[str]
            Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.

        string_ids : typing.Optional[str]
            Optional. A comma-delimited list of string ids. Up to 40 string IDs may be provided. May not be used with 'modifiedAfterTimestamp', 'stringText', 'descriptionText', or 'useFullText'.

        matching_translations_only : typing.Optional[bool]
            Optional. If false, all translations for returned String Definitions are included. Must be used with 'stringText' provided and 'includeTranslations' = true.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsStringDefinition
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.stringdefinitions.getdefinitions()


        asyncio.run(main())
        """
        _response = await self._raw_client.getdefinitions(
            limit=limit,
            modified_after_timestamp=modified_after_timestamp,
            include_translations=include_translations,
            string_text=string_text,
            description_text=description_text,
            use_full_text=use_full_text,
            include_deleted_languages=include_deleted_languages,
            language_ids=language_ids,
            string_ids=string_ids,
            matching_translations_only=matching_translations_only,
            request_options=request_options,
        )
        return _response.data

    async def postdefinition(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsStringDefinition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsStringDefinition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GlobalResourcesSharedModelsStringDefinition

        client = AsyncFernApi()


        async def main() -> None:
            await client.stringdefinitions.postdefinition(
                request=[
                    GlobalResourcesSharedModelsStringDefinition(
                        description_for_translator="DescriptionForTranslator",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postdefinition(request=request, request_options=request_options)
        return _response.data

    async def updatedefinitions(
        self,
        *,
        request: typing.Sequence[GlobalResourcesSharedModelsStringDefinition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[GlobalResourcesSharedModelsStringDefinition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GlobalResourcesSharedModelsStringDefinition

        client = AsyncFernApi()


        async def main() -> None:
            await client.stringdefinitions.updatedefinitions(
                request=[
                    GlobalResourcesSharedModelsStringDefinition(
                        description_for_translator="DescriptionForTranslator",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatedefinitions(request=request, request_options=request_options)
        return _response.data

    async def getdefinition(
        self,
        id: str,
        *,
        include_translations: typing.Optional[bool] = None,
        include_deleted_languages: typing.Optional[bool] = None,
        language_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlobalResourcesSharedModelsStringDefinition:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        include_translations : typing.Optional[bool]
            Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.

        include_deleted_languages : typing.Optional[bool]
            Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.

        language_ids : typing.Optional[str]
            Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsStringDefinition
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.stringdefinitions.getdefinition(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getdefinition(
            id,
            include_translations=include_translations,
            include_deleted_languages=include_deleted_languages,
            language_ids=language_ids,
            request_options=request_options,
        )
        return _response.data
