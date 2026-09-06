

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawRedirectsClient, RawRedirectsClient
from .types.create_redirects_response import CreateRedirectsResponse
from .types.delete_redirects_response import DeleteRedirectsResponse
from .types.list_redirects_response import ListRedirectsResponse
from .types.update_redirects_response import UpdateRedirectsResponse


OMIT = typing.cast(typing.Any, ...)


class RedirectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRedirectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRedirectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRedirectsClient
        """
        return self._raw_client

    def list(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ListRedirectsResponse:
        """
        Fetch a list of all 301 redirect rules configured for a specific site.

        Use this endpoint to review, audit, or manage the redirection rules that control how traffic is rerouted on your site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRedirectsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.redirects.list(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.list(site_id, request_options=request_options)
        return _response.data

    def create(
        self,
        site_id: str,
        *,
        from_url: typing.Optional[str] = OMIT,
        to_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateRedirectsResponse:
        """
        Add a new 301 redirection rule to a site.

        This endpoint allows you to define a source path (`fromUrl`) and its corresponding destination path (`toUrl`), which will dictate how traffic is rerouted on your site. This is useful for managing site changes, restructuring URLs, or handling outdated links.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        from_url : typing.Optional[str]
            The source URL path that will be redirected.

        to_url : typing.Optional[str]
            The target URL path where the user or client will be redirected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateRedirectsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.redirects.create(
            site_id="580e63e98c9a982ac9b8b741",
            from_url="/mostly-harmless",
            to_url="/earth",
        )
        """
        _response = self._raw_client.create(site_id, from_url=from_url, to_url=to_url, request_options=request_options)
        return _response.data

    def delete(
        self, site_id: str, redirect_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteRedirectsResponse:
        """
        Remove a 301 redirection rule from a site.

        This is useful for cleaning up outdated or unnecessary redirects, ensuring that your site's routing behavior remains efficient and up-to-date.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        redirect_id : str
            Unique identifier site redirect

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteRedirectsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.redirects.delete(
            site_id="580e63e98c9a982ac9b8b741",
            redirect_id="66c4cb9a20cac35ed19500e6",
        )
        """
        _response = self._raw_client.delete(site_id, redirect_id, request_options=request_options)
        return _response.data

    def update(
        self,
        site_id: str,
        redirect_id: str,
        *,
        from_url: typing.Optional[str] = OMIT,
        to_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateRedirectsResponse:
        """
        Update a 301 redirection rule from a site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        redirect_id : str
            Unique identifier site redirect

        from_url : typing.Optional[str]
            The source URL path that will be redirected.

        to_url : typing.Optional[str]
            The target URL path where the user or client will be redirected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateRedirectsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.redirects.update(
            site_id="580e63e98c9a982ac9b8b741",
            redirect_id="66c4cb9a20cac35ed19500e6",
            from_url="/mostly-harmless",
            to_url="/earth",
        )
        """
        _response = self._raw_client.update(
            site_id, redirect_id, from_url=from_url, to_url=to_url, request_options=request_options
        )
        return _response.data


class AsyncRedirectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRedirectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRedirectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRedirectsClient
        """
        return self._raw_client

    async def list(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListRedirectsResponse:
        """
        Fetch a list of all 301 redirect rules configured for a specific site.

        Use this endpoint to review, audit, or manage the redirection rules that control how traffic is rerouted on your site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRedirectsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.redirects.list(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(site_id, request_options=request_options)
        return _response.data

    async def create(
        self,
        site_id: str,
        *,
        from_url: typing.Optional[str] = OMIT,
        to_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateRedirectsResponse:
        """
        Add a new 301 redirection rule to a site.

        This endpoint allows you to define a source path (`fromUrl`) and its corresponding destination path (`toUrl`), which will dictate how traffic is rerouted on your site. This is useful for managing site changes, restructuring URLs, or handling outdated links.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        from_url : typing.Optional[str]
            The source URL path that will be redirected.

        to_url : typing.Optional[str]
            The target URL path where the user or client will be redirected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateRedirectsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.redirects.create(
                site_id="580e63e98c9a982ac9b8b741",
                from_url="/mostly-harmless",
                to_url="/earth",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            site_id, from_url=from_url, to_url=to_url, request_options=request_options
        )
        return _response.data

    async def delete(
        self, site_id: str, redirect_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteRedirectsResponse:
        """
        Remove a 301 redirection rule from a site.

        This is useful for cleaning up outdated or unnecessary redirects, ensuring that your site's routing behavior remains efficient and up-to-date.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        redirect_id : str
            Unique identifier site redirect

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteRedirectsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.redirects.delete(
                site_id="580e63e98c9a982ac9b8b741",
                redirect_id="66c4cb9a20cac35ed19500e6",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(site_id, redirect_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        site_id: str,
        redirect_id: str,
        *,
        from_url: typing.Optional[str] = OMIT,
        to_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateRedirectsResponse:
        """
        Update a 301 redirection rule from a site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        redirect_id : str
            Unique identifier site redirect

        from_url : typing.Optional[str]
            The source URL path that will be redirected.

        to_url : typing.Optional[str]
            The target URL path where the user or client will be redirected.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateRedirectsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.redirects.update(
                site_id="580e63e98c9a982ac9b8b741",
                redirect_id="66c4cb9a20cac35ed19500e6",
                from_url="/mostly-harmless",
                to_url="/earth",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            site_id, redirect_id, from_url=from_url, to_url=to_url, request_options=request_options
        )
        return _response.data
