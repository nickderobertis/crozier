

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_global_resources_shared_models_global_image_category import (
    ApiIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory,
)
from ..types.global_resources_shared_models_global_image_category import GlobalResourcesSharedModelsGlobalImageCategory
from .raw_client import AsyncRawGlobalimagecategoriesClient, RawGlobalimagecategoriesClient


OMIT = typing.cast(typing.Any, ...)


class GlobalimagecategoriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGlobalimagecategoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGlobalimagecategoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGlobalimagecategoriesClient
        """
        return self._raw_client

    def getfiles(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.globalimagecategories.getfiles()
        """
        _response = self._raw_client.getfiles(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def postfile(
        self, *, name: str, id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        name : str
            The name of the globalImage Catetory.

        id : typing.Optional[str]
            The Id of the GlobalImage Categories.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.globalimagecategories.postfile(
            name="Name",
        )
        """
        _response = self._raw_client.postfile(name=name, id=id, request_options=request_options)
        return _response.data

    def getfile(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsGlobalImageCategory:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsGlobalImageCategory
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.globalimagecategories.getfile(
            id="ID",
        )
        """
        _response = self._raw_client.getfile(id, request_options=request_options)
        return _response.data


class AsyncGlobalimagecategoriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGlobalimagecategoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGlobalimagecategoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGlobalimagecategoriesClient
        """
        return self._raw_client

    async def getfiles(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsGlobalImageCategory
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.globalimagecategories.getfiles()


        asyncio.run(main())
        """
        _response = await self._raw_client.getfiles(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    async def postfile(
        self, *, name: str, id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        name : str
            The name of the globalImage Catetory.

        id : typing.Optional[str]
            The Id of the GlobalImage Categories.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.globalimagecategories.postfile(
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postfile(name=name, id=id, request_options=request_options)
        return _response.data

    async def getfile(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsGlobalImageCategory:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsGlobalImageCategory
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.globalimagecategories.getfile(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getfile(id, request_options=request_options)
        return _response.data
