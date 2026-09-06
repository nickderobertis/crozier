

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLinkQueriesClient, RawLinkQueriesClient
from .types.get_api_links_request_date_sort_order import GetApiLinksRequestDateSortOrder
from .types.get_api_links_response import GetApiLinksResponse
from .types.get_links_expand_response import GetLinksExpandResponse
from .types.get_links_link_id_response import GetLinksLinkIdResponse
from .types.post_links_opengraph_debug_response import PostLinksOpengraphDebugResponse


OMIT = typing.cast(typing.Any, ...)


class LinkQueriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLinkQueriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLinkQueriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLinkQueriesClient
        """
        return self._raw_client

    def fetch_and_inspect_open_graph_tags_for_a_url_public_h_captcha_protected(
        self, *, hcaptcha_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostLinksOpengraphDebugResponse:
        """
        Parameters
        ----------
        hcaptcha_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksOpengraphDebugResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_queries.fetch_and_inspect_open_graph_tags_for_a_url_public_h_captcha_protected(
            hcaptcha_token="hcaptchaToken",
        )
        """
        _response = self._raw_client.fetch_and_inspect_open_graph_tags_for_a_url_public_h_captcha_protected(
            hcaptcha_token=hcaptcha_token, request_options=request_options
        )
        return _response.data

    def get_link_opengraph_properties(
        self, domain_id: float, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        domain_id : float

        link_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_queries.get_link_opengraph_properties(
            domain_id=1.1,
            link_id="linkId",
        )
        """
        _response = self._raw_client.get_link_opengraph_properties(domain_id, link_id, request_options=request_options)
        return _response.data

    def link_list(
        self,
        *,
        domain_id: int,
        limit: typing.Optional[int] = None,
        id_string: typing.Optional[str] = None,
        created_at: typing.Optional[str] = None,
        before_date: typing.Optional[dt.datetime] = None,
        after_date: typing.Optional[dt.datetime] = None,
        date_sort_order: typing.Optional[GetApiLinksRequestDateSortOrder] = None,
        page_token: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiLinksResponse:
        """
        Get domain links

        Parameters
        ----------
        domain_id : int
            Domain ID

        limit : typing.Optional[int]

        id_string : typing.Optional[str]

        created_at : typing.Optional[str]

        before_date : typing.Optional[dt.datetime]

        after_date : typing.Optional[dt.datetime]

        date_sort_order : typing.Optional[GetApiLinksRequestDateSortOrder]

        page_token : typing.Optional[str]

        folder_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiLinksResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_queries.link_list(
            domain_id=1,
        )
        """
        _response = self._raw_client.link_list(
            domain_id=domain_id,
            limit=limit,
            id_string=id_string,
            created_at=created_at,
            before_date=before_date,
            after_date=after_date,
            date_sort_order=date_sort_order,
            page_token=page_token,
            folder_id=folder_id,
            request_options=request_options,
        )
        return _response.data

    def get_link_info_by_link_id(
        self,
        link_id: str,
        *,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLinksLinkIdResponse:
        """
        Get link info by link id. Rate limit: 20/s

        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]
            [DEPRECATED] Domain ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLinksLinkIdResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_queries.get_link_info_by_link_id(
            link_id="linkId",
        )
        """
        _response = self._raw_client.get_link_info_by_link_id(
            link_id, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    def get_link_info_by_path(
        self, *, domain: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetLinksExpandResponse:
        """
        Get link info by path. Rate limit: 20/s

        Parameters
        ----------
        domain : str
            Domain hostname

        path : str
            Link path

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLinksExpandResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_queries.get_link_info_by_path(
            domain="domain",
            path="path",
        )
        """
        _response = self._raw_client.get_link_info_by_path(domain=domain, path=path, request_options=request_options)
        return _response.data

    def get_link_info_by_original_url(
        self, *, domain: str, original_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        **DEPRECATED** Get link info by original URL. Rate limit: 20/s

        Parameters
        ----------
        domain : str
            Domain hostname

        original_url : str
            Link original URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_queries.get_link_info_by_original_url(
            domain="domain",
            original_url="originalURL",
        )
        """
        _response = self._raw_client.get_link_info_by_original_url(
            domain=domain, original_url=original_url, request_options=request_options
        )
        return _response.data

    def get_links_info_by_original_url(
        self, *, domain: str, original_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns all links with the same original URL

        Parameters
        ----------
        domain : str
            Domain hostname

        original_url : str
            Link original URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_queries.get_links_info_by_original_url(
            domain="domain",
            original_url="originalURL",
        )
        """
        _response = self._raw_client.get_links_info_by_original_url(
            domain=domain, original_url=original_url, request_options=request_options
        )
        return _response.data

    def get_links_folders_domain_id(
        self, domain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get links folders for the specified domain id

        Parameters
        ----------
        domain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_queries.get_links_folders_domain_id(
            domain_id=1,
        )
        """
        _response = self._raw_client.get_links_folders_domain_id(domain_id, request_options=request_options)
        return _response.data

    def get_links_folders_domain_id_folder_id(
        self, domain_id: int, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get links folder for the specified domain id and user id

        Parameters
        ----------
        domain_id : int

        folder_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_queries.get_links_folders_domain_id_folder_id(
            domain_id=1,
            folder_id="folderId",
        )
        """
        _response = self._raw_client.get_links_folders_domain_id_folder_id(
            domain_id, folder_id, request_options=request_options
        )
        return _response.data

    def post_links_folders(
        self,
        *,
        domain_id: int,
        name: str,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        logo_height: typing.Optional[int] = OMIT,
        logo_width: typing.Optional[int] = OMIT,
        ec_level: typing.Optional[str] = OMIT,
        border_radius: typing.Optional[int] = OMIT,
        no_excavate: typing.Optional[bool] = OMIT,
        finder_outer_shape: typing.Optional[str] = OMIT,
        finder_inner_shape: typing.Optional[str] = OMIT,
        finder_color: typing.Optional[str] = OMIT,
        corner_mode: typing.Optional[str] = OMIT,
        label_text: typing.Optional[str] = OMIT,
        label_style: typing.Optional[str] = OMIT,
        label_color: typing.Optional[str] = OMIT,
        label_bg_color: typing.Optional[str] = OMIT,
        label_font_size: typing.Optional[int] = OMIT,
        label_font_family: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at_days: typing.Optional[int] = OMIT,
        icon: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create a new folder

        Parameters
        ----------
        domain_id : int

        name : str

        color : typing.Optional[str]

        background_color : typing.Optional[str]

        logo_url : typing.Optional[str]

        logo_height : typing.Optional[int]

        logo_width : typing.Optional[int]

        ec_level : typing.Optional[str]

        border_radius : typing.Optional[int]

        no_excavate : typing.Optional[bool]

        finder_outer_shape : typing.Optional[str]

        finder_inner_shape : typing.Optional[str]

        finder_color : typing.Optional[str]

        corner_mode : typing.Optional[str]

        label_text : typing.Optional[str]

        label_style : typing.Optional[str]

        label_color : typing.Optional[str]

        label_bg_color : typing.Optional[str]

        label_font_size : typing.Optional[int]

        label_font_family : typing.Optional[str]

        integration_fb : typing.Optional[str]

        integration_tt : typing.Optional[str]

        integration_ga : typing.Optional[str]

        integration_gtm : typing.Optional[str]

        integration_adroll : typing.Optional[str]

        utm_campaign : typing.Optional[str]

        utm_medium : typing.Optional[str]

        utm_source : typing.Optional[str]

        utm_term : typing.Optional[str]

        utm_content : typing.Optional[str]

        redirect_type : typing.Optional[int]

        expires_at_days : typing.Optional[int]

        icon : typing.Optional[str]

        prefix : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_queries.post_links_folders(
            domain_id=1,
            name="name",
        )
        """
        _response = self._raw_client.post_links_folders(
            domain_id=domain_id,
            name=name,
            color=color,
            background_color=background_color,
            logo_url=logo_url,
            logo_height=logo_height,
            logo_width=logo_width,
            ec_level=ec_level,
            border_radius=border_radius,
            no_excavate=no_excavate,
            finder_outer_shape=finder_outer_shape,
            finder_inner_shape=finder_inner_shape,
            finder_color=finder_color,
            corner_mode=corner_mode,
            label_text=label_text,
            label_style=label_style,
            label_color=label_color,
            label_bg_color=label_bg_color,
            label_font_size=label_font_size,
            label_font_family=label_font_family,
            integration_fb=integration_fb,
            integration_tt=integration_tt,
            integration_ga=integration_ga,
            integration_gtm=integration_gtm,
            integration_adroll=integration_adroll,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_source=utm_source,
            utm_term=utm_term,
            utm_content=utm_content,
            redirect_type=redirect_type,
            expires_at_days=expires_at_days,
            icon=icon,
            prefix=prefix,
            request_options=request_options,
        )
        return _response.data


class AsyncLinkQueriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLinkQueriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLinkQueriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLinkQueriesClient
        """
        return self._raw_client

    async def fetch_and_inspect_open_graph_tags_for_a_url_public_h_captcha_protected(
        self, *, hcaptcha_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostLinksOpengraphDebugResponse:
        """
        Parameters
        ----------
        hcaptcha_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksOpengraphDebugResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_queries.fetch_and_inspect_open_graph_tags_for_a_url_public_h_captcha_protected(
                hcaptcha_token="hcaptchaToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_and_inspect_open_graph_tags_for_a_url_public_h_captcha_protected(
            hcaptcha_token=hcaptcha_token, request_options=request_options
        )
        return _response.data

    async def get_link_opengraph_properties(
        self, domain_id: float, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        domain_id : float

        link_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_queries.get_link_opengraph_properties(
                domain_id=1.1,
                link_id="linkId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_link_opengraph_properties(
            domain_id, link_id, request_options=request_options
        )
        return _response.data

    async def link_list(
        self,
        *,
        domain_id: int,
        limit: typing.Optional[int] = None,
        id_string: typing.Optional[str] = None,
        created_at: typing.Optional[str] = None,
        before_date: typing.Optional[dt.datetime] = None,
        after_date: typing.Optional[dt.datetime] = None,
        date_sort_order: typing.Optional[GetApiLinksRequestDateSortOrder] = None,
        page_token: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiLinksResponse:
        """
        Get domain links

        Parameters
        ----------
        domain_id : int
            Domain ID

        limit : typing.Optional[int]

        id_string : typing.Optional[str]

        created_at : typing.Optional[str]

        before_date : typing.Optional[dt.datetime]

        after_date : typing.Optional[dt.datetime]

        date_sort_order : typing.Optional[GetApiLinksRequestDateSortOrder]

        page_token : typing.Optional[str]

        folder_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiLinksResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_queries.link_list(
                domain_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.link_list(
            domain_id=domain_id,
            limit=limit,
            id_string=id_string,
            created_at=created_at,
            before_date=before_date,
            after_date=after_date,
            date_sort_order=date_sort_order,
            page_token=page_token,
            folder_id=folder_id,
            request_options=request_options,
        )
        return _response.data

    async def get_link_info_by_link_id(
        self,
        link_id: str,
        *,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLinksLinkIdResponse:
        """
        Get link info by link id. Rate limit: 20/s

        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]
            [DEPRECATED] Domain ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLinksLinkIdResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_queries.get_link_info_by_link_id(
                link_id="linkId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_link_info_by_link_id(
            link_id, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    async def get_link_info_by_path(
        self, *, domain: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetLinksExpandResponse:
        """
        Get link info by path. Rate limit: 20/s

        Parameters
        ----------
        domain : str
            Domain hostname

        path : str
            Link path

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLinksExpandResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_queries.get_link_info_by_path(
                domain="domain",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_link_info_by_path(
            domain=domain, path=path, request_options=request_options
        )
        return _response.data

    async def get_link_info_by_original_url(
        self, *, domain: str, original_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        **DEPRECATED** Get link info by original URL. Rate limit: 20/s

        Parameters
        ----------
        domain : str
            Domain hostname

        original_url : str
            Link original URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_queries.get_link_info_by_original_url(
                domain="domain",
                original_url="originalURL",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_link_info_by_original_url(
            domain=domain, original_url=original_url, request_options=request_options
        )
        return _response.data

    async def get_links_info_by_original_url(
        self, *, domain: str, original_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns all links with the same original URL

        Parameters
        ----------
        domain : str
            Domain hostname

        original_url : str
            Link original URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_queries.get_links_info_by_original_url(
                domain="domain",
                original_url="originalURL",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_links_info_by_original_url(
            domain=domain, original_url=original_url, request_options=request_options
        )
        return _response.data

    async def get_links_folders_domain_id(
        self, domain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get links folders for the specified domain id

        Parameters
        ----------
        domain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_queries.get_links_folders_domain_id(
                domain_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_links_folders_domain_id(domain_id, request_options=request_options)
        return _response.data

    async def get_links_folders_domain_id_folder_id(
        self, domain_id: int, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get links folder for the specified domain id and user id

        Parameters
        ----------
        domain_id : int

        folder_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_queries.get_links_folders_domain_id_folder_id(
                domain_id=1,
                folder_id="folderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_links_folders_domain_id_folder_id(
            domain_id, folder_id, request_options=request_options
        )
        return _response.data

    async def post_links_folders(
        self,
        *,
        domain_id: int,
        name: str,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        logo_height: typing.Optional[int] = OMIT,
        logo_width: typing.Optional[int] = OMIT,
        ec_level: typing.Optional[str] = OMIT,
        border_radius: typing.Optional[int] = OMIT,
        no_excavate: typing.Optional[bool] = OMIT,
        finder_outer_shape: typing.Optional[str] = OMIT,
        finder_inner_shape: typing.Optional[str] = OMIT,
        finder_color: typing.Optional[str] = OMIT,
        corner_mode: typing.Optional[str] = OMIT,
        label_text: typing.Optional[str] = OMIT,
        label_style: typing.Optional[str] = OMIT,
        label_color: typing.Optional[str] = OMIT,
        label_bg_color: typing.Optional[str] = OMIT,
        label_font_size: typing.Optional[int] = OMIT,
        label_font_family: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at_days: typing.Optional[int] = OMIT,
        icon: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create a new folder

        Parameters
        ----------
        domain_id : int

        name : str

        color : typing.Optional[str]

        background_color : typing.Optional[str]

        logo_url : typing.Optional[str]

        logo_height : typing.Optional[int]

        logo_width : typing.Optional[int]

        ec_level : typing.Optional[str]

        border_radius : typing.Optional[int]

        no_excavate : typing.Optional[bool]

        finder_outer_shape : typing.Optional[str]

        finder_inner_shape : typing.Optional[str]

        finder_color : typing.Optional[str]

        corner_mode : typing.Optional[str]

        label_text : typing.Optional[str]

        label_style : typing.Optional[str]

        label_color : typing.Optional[str]

        label_bg_color : typing.Optional[str]

        label_font_size : typing.Optional[int]

        label_font_family : typing.Optional[str]

        integration_fb : typing.Optional[str]

        integration_tt : typing.Optional[str]

        integration_ga : typing.Optional[str]

        integration_gtm : typing.Optional[str]

        integration_adroll : typing.Optional[str]

        utm_campaign : typing.Optional[str]

        utm_medium : typing.Optional[str]

        utm_source : typing.Optional[str]

        utm_term : typing.Optional[str]

        utm_content : typing.Optional[str]

        redirect_type : typing.Optional[int]

        expires_at_days : typing.Optional[int]

        icon : typing.Optional[str]

        prefix : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_queries.post_links_folders(
                domain_id=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_links_folders(
            domain_id=domain_id,
            name=name,
            color=color,
            background_color=background_color,
            logo_url=logo_url,
            logo_height=logo_height,
            logo_width=logo_width,
            ec_level=ec_level,
            border_radius=border_radius,
            no_excavate=no_excavate,
            finder_outer_shape=finder_outer_shape,
            finder_inner_shape=finder_inner_shape,
            finder_color=finder_color,
            corner_mode=corner_mode,
            label_text=label_text,
            label_style=label_style,
            label_color=label_color,
            label_bg_color=label_bg_color,
            label_font_size=label_font_size,
            label_font_family=label_font_family,
            integration_fb=integration_fb,
            integration_tt=integration_tt,
            integration_ga=integration_ga,
            integration_gtm=integration_gtm,
            integration_adroll=integration_adroll,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_source=utm_source,
            utm_term=utm_term,
            utm_content=utm_content,
            redirect_type=redirect_type,
            expires_at_days=expires_at_days,
            icon=icon,
            prefix=prefix,
            request_options=request_options,
        )
        return _response.data
