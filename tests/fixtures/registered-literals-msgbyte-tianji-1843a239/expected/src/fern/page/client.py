

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPageClient, RawPageClient
from .types.page_create_page_response import PageCreatePageResponse
from .types.page_delete_page_response import PageDeletePageResponse
from .types.page_edit_page_response import PageEditPageResponse
from .types.page_get_all_pages_request_type import PageGetAllPagesRequestType
from .types.page_get_all_pages_response_item import PageGetAllPagesResponseItem
from .types.page_get_page_info_response import PageGetPageInfoResponse


OMIT = typing.cast(typing.Any, ...)


class PageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPageClient
        """
        return self._raw_client

    def getallpages(
        self,
        workspace_id: str,
        *,
        type: typing.Optional[PageGetAllPagesRequestType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PageGetAllPagesResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        type : typing.Optional[PageGetAllPagesRequestType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PageGetAllPagesResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.page.getallpages(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.getallpages(workspace_id, type=type, request_options=request_options)
        return _response.data

    def getpageinfo(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[PageGetPageInfoResponse]:
        """
        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[PageGetPageInfoResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.page.getpageinfo(
            slug="slug",
        )
        """
        _response = self._raw_client.getpageinfo(slug, request_options=request_options)
        return _response.data

    def createpage(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PageCreatePageResponse:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageCreatePageResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.page.createpage(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.createpage(workspace_id, request_options=request_options)
        return _response.data

    def editpage(
        self,
        workspace_id: str,
        *,
        id: str,
        slug: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        body: typing.Optional[typing.Any] = OMIT,
        monitor_list: typing.Optional[typing.Any] = OMIT,
        payload: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageEditPageResponse:
        """
        Parameters
        ----------
        workspace_id : str

        id : str

        slug : typing.Optional[str]

        title : typing.Optional[str]

        description : typing.Optional[str]

        domain : typing.Optional[str]

        body : typing.Optional[typing.Any]

        monitor_list : typing.Optional[typing.Any]

        payload : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageEditPageResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.page.editpage(
            workspace_id="workspaceId",
            id="id",
        )
        """
        _response = self._raw_client.editpage(
            workspace_id,
            id=id,
            slug=slug,
            title=title,
            description=description,
            domain=domain,
            body=body,
            monitor_list=monitor_list,
            payload=payload,
            request_options=request_options,
        )
        return _response.data

    def deletepage(
        self, workspace_id: str, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PageDeletePageResponse:
        """
        Parameters
        ----------
        workspace_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageDeletePageResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.page.deletepage(
            workspace_id="workspaceId",
            id="id",
        )
        """
        _response = self._raw_client.deletepage(workspace_id, id=id, request_options=request_options)
        return _response.data


class AsyncPageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPageClient
        """
        return self._raw_client

    async def getallpages(
        self,
        workspace_id: str,
        *,
        type: typing.Optional[PageGetAllPagesRequestType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PageGetAllPagesResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        type : typing.Optional[PageGetAllPagesRequestType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PageGetAllPagesResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.page.getallpages(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getallpages(workspace_id, type=type, request_options=request_options)
        return _response.data

    async def getpageinfo(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[PageGetPageInfoResponse]:
        """
        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[PageGetPageInfoResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.page.getpageinfo(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpageinfo(slug, request_options=request_options)
        return _response.data

    async def createpage(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PageCreatePageResponse:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageCreatePageResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.page.createpage(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createpage(workspace_id, request_options=request_options)
        return _response.data

    async def editpage(
        self,
        workspace_id: str,
        *,
        id: str,
        slug: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        body: typing.Optional[typing.Any] = OMIT,
        monitor_list: typing.Optional[typing.Any] = OMIT,
        payload: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageEditPageResponse:
        """
        Parameters
        ----------
        workspace_id : str

        id : str

        slug : typing.Optional[str]

        title : typing.Optional[str]

        description : typing.Optional[str]

        domain : typing.Optional[str]

        body : typing.Optional[typing.Any]

        monitor_list : typing.Optional[typing.Any]

        payload : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageEditPageResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.page.editpage(
                workspace_id="workspaceId",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.editpage(
            workspace_id,
            id=id,
            slug=slug,
            title=title,
            description=description,
            domain=domain,
            body=body,
            monitor_list=monitor_list,
            payload=payload,
            request_options=request_options,
        )
        return _response.data

    async def deletepage(
        self, workspace_id: str, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PageDeletePageResponse:
        """
        Parameters
        ----------
        workspace_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageDeletePageResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.page.deletepage(
                workspace_id="workspaceId",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletepage(workspace_id, id=id, request_options=request_options)
        return _response.data
