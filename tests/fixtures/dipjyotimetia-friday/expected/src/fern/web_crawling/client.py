

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWebCrawlingClient, RawWebCrawlingClient


OMIT = typing.cast(typing.Any, ...)


class WebCrawlingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebCrawlingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebCrawlingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebCrawlingClient
        """
        return self._raw_client

    def crawl_site(
        self,
        *,
        url: str,
        provider: typing.Optional[str] = OMIT,
        max_pages: typing.Optional[int] = OMIT,
        same_domain: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        url : str

        provider : typing.Optional[str]

        max_pages : typing.Optional[int]

        same_domain : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.web_crawling.crawl_site(
            url="url",
        )
        """
        _response = self._raw_client.crawl_site(
            url=url, provider=provider, max_pages=max_pages, same_domain=same_domain, request_options=request_options
        )
        return _response.data


class AsyncWebCrawlingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebCrawlingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebCrawlingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebCrawlingClient
        """
        return self._raw_client

    async def crawl_site(
        self,
        *,
        url: str,
        provider: typing.Optional[str] = OMIT,
        max_pages: typing.Optional[int] = OMIT,
        same_domain: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        url : str

        provider : typing.Optional[str]

        max_pages : typing.Optional[int]

        same_domain : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.web_crawling.crawl_site(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crawl_site(
            url=url, provider=provider, max_pages=max_pages, same_domain=same_domain, request_options=request_options
        )
        return _response.data
