

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPagesClient, RawPagesClient
from .types.get_content_pages_response import GetContentPagesResponse
from .types.get_metadata_pages_response import GetMetadataPagesResponse
from .types.list_pages_response import ListPagesResponse
from .types.update_page_settings_request_open_graph import UpdatePageSettingsRequestOpenGraph
from .types.update_page_settings_request_seo import UpdatePageSettingsRequestSeo
from .types.update_page_settings_response import UpdatePageSettingsResponse
from .types.update_static_content_request_nodes_item import UpdateStaticContentRequestNodesItem
from .types.update_static_content_response import UpdateStaticContentResponse

if typing.TYPE_CHECKING:
    from .scripts.client import AsyncScriptsClient, ScriptsClient

OMIT = typing.cast(typing.Any, ...)


class PagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPagesClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._scripts: typing.Optional[ScriptsClient] = None

    @property
    def with_raw_response(self) -> RawPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPagesClient
        """
        return self._raw_client

    def list(
        self,
        site_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPagesResponse:
        """
        List of all pages for a site.

        Required scope | `pages:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPagesResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.list(
            site_id="580e63e98c9a982ac9b8b741",
            locale_id="65427cf400e02b306eaa04a0",
        )
        """
        _response = self._raw_client.list(
            site_id, locale_id=locale_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def get_metadata(
        self,
        page_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        translatable: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMetadataPagesResponse:
        """
        Get metadata information for a single page.

        Required scope | `pages:read`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        translatable : typing.Optional[str]
            Unique identifier for the secondary Locale you're translating **into**. Returns only content that hasn't been excluded from translation for that locale.

            This is independent of `localeId`, which selects which version of the content is returned. To fetch the source text to translate, request the primary locale's content and set `translatable` to the locale you're translating into:

            `?localeId={primary locale id}&translatable={target locale id}`

            Only exclusion rules scoped to manual translation are respected — rules scoped only to automatic translation don't affect this parameter's response.

            Omitting `translatable` returns the same response as if this parameter didn't exist. The value must be the id of one of the site's secondary locales — the primary locale id, or any other value, returns a `400` error. Requires translation exclusions to be enabled for the site; if they aren't, the request returns a `403` error.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMetadataPagesResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.get_metadata(
            page_id="63c720f9347c2139b248e552",
            locale_id="65427cf400e02b306eaa04a0",
            translatable="65427cf400e02b306eaa04a0",
        )
        """
        _response = self._raw_client.get_metadata(
            page_id, locale_id=locale_id, translatable=translatable, request_options=request_options
        )
        return _response.data

    def update_page_settings(
        self,
        page_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        seo: typing.Optional[UpdatePageSettingsRequestSeo] = OMIT,
        open_graph: typing.Optional[UpdatePageSettingsRequestOpenGraph] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePageSettingsResponse:
        """
        Update Page-level metadata, including SEO and Open Graph fields.

        Required scope | `pages:write`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        title : typing.Optional[str]
            Title for the page

        slug : typing.Optional[str]
            Slug for the page.

            **Note:** The slug field is ignored in the following cases — all other fields in the same request still apply:
            - The site's home page, collection template pages, and utility pages (e.g. 404, password, search).
            - For secondary locales, updating the slug requires an <a href="https://webflow.com/feature/localization">Advanced or Enterprise localization add-on plan</a>.

        seo : typing.Optional[UpdatePageSettingsRequestSeo]
            SEO-related fields for the Page

        open_graph : typing.Optional[UpdatePageSettingsRequestOpenGraph]
            Open Graph fields for the Page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePageSettingsResponse
            Request was successful

        Examples
        --------
        from fern.pages import (
            UpdatePageSettingsRequestOpenGraph,
            UpdatePageSettingsRequestSeo,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.update_page_settings(
            page_id="63c720f9347c2139b248e552",
            locale_id="65427cf400e02b306eaa04a0",
            title="Guide to the Galaxy",
            slug="guide-to-the-galaxy",
            seo=UpdatePageSettingsRequestSeo(
                title="The Ultimate Hitchhiker's Guide to the Galaxy",
                description="Everything you need to know about the galaxy, from avoiding Vogon poetry to the importance of towels.",
            ),
            open_graph=UpdatePageSettingsRequestOpenGraph(
                title="Explore the Cosmos with The Ultimate Guide",
                title_copied=False,
                description="Dive deep into the mysteries of the universe with your guide to everything galactic.",
                description_copied=False,
            ),
        )
        """
        _response = self._raw_client.update_page_settings(
            page_id,
            locale_id=locale_id,
            title=title,
            slug=slug,
            seo=seo,
            open_graph=open_graph,
            request_options=request_options,
        )
        return _response.data

    def get_content(
        self,
        page_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        translatable: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetContentPagesResponse:
        """
        Get text and component instance content from a static page.

        <Badge intent="info">Localization</Badge>

        Required scope | `pages:read`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        translatable : typing.Optional[str]
            Unique identifier for the secondary Locale you're translating **into**. Returns only content that hasn't been excluded from translation for that locale.

            This is independent of `localeId`, which selects which version of the content is returned. To fetch the source text to translate, request the primary locale's content and set `translatable` to the locale you're translating into:

            `?localeId={primary locale id}&translatable={target locale id}`

            Only exclusion rules scoped to manual translation are respected — rules scoped only to automatic translation don't affect this parameter's response.

            Omitting `translatable` returns the same response as if this parameter didn't exist. The value must be the id of one of the site's secondary locales — the primary locale id, or any other value, returns a `400` error. Requires translation exclusions to be enabled for the site; if they aren't, the request returns a `403` error.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContentPagesResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.get_content(
            page_id="63c720f9347c2139b248e552",
            locale_id="65427cf400e02b306eaa04a0",
            translatable="65427cf400e02b306eaa04a0",
        )
        """
        _response = self._raw_client.get_content(
            page_id,
            locale_id=locale_id,
            limit=limit,
            offset=offset,
            translatable=translatable,
            request_options=request_options,
        )
        return _response.data

    def update_static_content(
        self,
        page_id: str,
        *,
        locale_id: str,
        nodes: typing.Sequence[UpdateStaticContentRequestNodesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateStaticContentResponse:
        """
        This endpoint updates content on a static page in **secondary locales**. It supports updating up to 1000 nodes in a single request.

        Before making updates:
        1. Use the [get page content](/data/reference/pages-and-components/pages/get-content) endpoint to identify available content nodes and their types.
        2. If the page has component instances, retrieve the component's properties that you'll override using the [get component properties](/data/reference/pages-and-components/components/get-properties) endpoint.
        3. DOM elements may include a `data-w-id` attribute. This attribute is used by Webflow to maintain custom attributes and links across locales. Always include the original `data-w-id` value in your update requests to ensure consistent behavior across all locales.

        <Note>
          This endpoint is specifically for localized pages. Ensure that the specified `localeId` is a valid **secondary locale** for the site otherwise the request will fail.
        </Note>

        Required scope | `pages:write`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

        locale_id : str
            The locale identifier.

        nodes : typing.Sequence[UpdateStaticContentRequestNodesItem]
            List of DOM Nodes with the new content that will be updated in each node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateStaticContentResponse
            Request was successful

        Examples
        --------
        from fern.pages import (
            UpdateStaticContentRequestNodesItemChoices,
            UpdateStaticContentRequestNodesItemChoicesChoicesItem,
            UpdateStaticContentRequestNodesItemPlaceholder,
            UpdateStaticContentRequestNodesItemPropertyOverrides,
            UpdateStaticContentRequestNodesItemPropertyOverridesPropertyOverridesItem,
            UpdateStaticContentRequestNodesItemText,
            UpdateStaticContentRequestNodesItemWaitingText,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.update_static_content(
            page_id="63c720f9347c2139b248e552",
            locale_id="localeId",
            nodes=[
                UpdateStaticContentRequestNodesItemText(
                    node_id="a245c12d-995b-55ee-5ec7-aa36a6cad623",
                    text="<h1>The Hitchhiker's Guide to the Galaxy</h1>",
                ),
                UpdateStaticContentRequestNodesItemText(
                    node_id="a245c12d-995b-55ee-5ec7-aa36a6cad627",
                    text="<div><h3>Don't Panic!</h3><p>Always know where your towel is.</p></div>",
                ),
                UpdateStaticContentRequestNodesItemChoices(
                    node_id="a245c12d-995b-55ee-5ec7-aa36a6cad635",
                    choices=[
                        UpdateStaticContentRequestNodesItemChoicesChoicesItem(
                            value="choice-1",
                            text="First choice",
                        ),
                        UpdateStaticContentRequestNodesItemChoicesChoicesItem(
                            value="choice-2",
                            text="Second choice",
                        ),
                    ],
                ),
                UpdateStaticContentRequestNodesItemPlaceholder(
                    node_id="a245c12d-995b-55ee-5ec7-aa36a6cad642",
                    placeholder="Enter something here...",
                ),
                UpdateStaticContentRequestNodesItemWaitingText(
                    node_id="a245c12d-995b-55ee-5ec7-aa36a6cad671",
                    value="Submit",
                    waiting_text="Submitting...",
                ),
                UpdateStaticContentRequestNodesItemPropertyOverrides(
                    node_id="a245c12d-995b-55ee-5ec7-aa36a6cad629",
                    property_overrides=[
                        UpdateStaticContentRequestNodesItemPropertyOverridesPropertyOverridesItem(
                            property_id="7dd14c08-2e96-8d3d-2b19-b5c03642a0f0",
                            text="<div><h1>Time is an <em>illusion</em></h1></div>",
                        ),
                        UpdateStaticContentRequestNodesItemPropertyOverridesPropertyOverridesItem(
                            property_id="7dd14c08-2e96-8d3d-2b19-b5c03642a0f1",
                            text="Life, the Universe and Everything",
                        ),
                    ],
                ),
            ],
        )
        """
        _response = self._raw_client.update_static_content(
            page_id, locale_id=locale_id, nodes=nodes, request_options=request_options
        )
        return _response.data

    @property
    def scripts(self):
        if self._scripts is None:
            from .scripts.client import ScriptsClient

            self._scripts = ScriptsClient(client_wrapper=self._client_wrapper)
        return self._scripts


class AsyncPagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPagesClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._scripts: typing.Optional[AsyncScriptsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPagesClient
        """
        return self._raw_client

    async def list(
        self,
        site_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPagesResponse:
        """
        List of all pages for a site.

        Required scope | `pages:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPagesResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.list(
                site_id="580e63e98c9a982ac9b8b741",
                locale_id="65427cf400e02b306eaa04a0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            site_id, locale_id=locale_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def get_metadata(
        self,
        page_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        translatable: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetMetadataPagesResponse:
        """
        Get metadata information for a single page.

        Required scope | `pages:read`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        translatable : typing.Optional[str]
            Unique identifier for the secondary Locale you're translating **into**. Returns only content that hasn't been excluded from translation for that locale.

            This is independent of `localeId`, which selects which version of the content is returned. To fetch the source text to translate, request the primary locale's content and set `translatable` to the locale you're translating into:

            `?localeId={primary locale id}&translatable={target locale id}`

            Only exclusion rules scoped to manual translation are respected — rules scoped only to automatic translation don't affect this parameter's response.

            Omitting `translatable` returns the same response as if this parameter didn't exist. The value must be the id of one of the site's secondary locales — the primary locale id, or any other value, returns a `400` error. Requires translation exclusions to be enabled for the site; if they aren't, the request returns a `403` error.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMetadataPagesResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.get_metadata(
                page_id="63c720f9347c2139b248e552",
                locale_id="65427cf400e02b306eaa04a0",
                translatable="65427cf400e02b306eaa04a0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_metadata(
            page_id, locale_id=locale_id, translatable=translatable, request_options=request_options
        )
        return _response.data

    async def update_page_settings(
        self,
        page_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        seo: typing.Optional[UpdatePageSettingsRequestSeo] = OMIT,
        open_graph: typing.Optional[UpdatePageSettingsRequestOpenGraph] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdatePageSettingsResponse:
        """
        Update Page-level metadata, including SEO and Open Graph fields.

        Required scope | `pages:write`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        title : typing.Optional[str]
            Title for the page

        slug : typing.Optional[str]
            Slug for the page.

            **Note:** The slug field is ignored in the following cases — all other fields in the same request still apply:
            - The site's home page, collection template pages, and utility pages (e.g. 404, password, search).
            - For secondary locales, updating the slug requires an <a href="https://webflow.com/feature/localization">Advanced or Enterprise localization add-on plan</a>.

        seo : typing.Optional[UpdatePageSettingsRequestSeo]
            SEO-related fields for the Page

        open_graph : typing.Optional[UpdatePageSettingsRequestOpenGraph]
            Open Graph fields for the Page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatePageSettingsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.pages import (
            UpdatePageSettingsRequestOpenGraph,
            UpdatePageSettingsRequestSeo,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.update_page_settings(
                page_id="63c720f9347c2139b248e552",
                locale_id="65427cf400e02b306eaa04a0",
                title="Guide to the Galaxy",
                slug="guide-to-the-galaxy",
                seo=UpdatePageSettingsRequestSeo(
                    title="The Ultimate Hitchhiker's Guide to the Galaxy",
                    description="Everything you need to know about the galaxy, from avoiding Vogon poetry to the importance of towels.",
                ),
                open_graph=UpdatePageSettingsRequestOpenGraph(
                    title="Explore the Cosmos with The Ultimate Guide",
                    title_copied=False,
                    description="Dive deep into the mysteries of the universe with your guide to everything galactic.",
                    description_copied=False,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_page_settings(
            page_id,
            locale_id=locale_id,
            title=title,
            slug=slug,
            seo=seo,
            open_graph=open_graph,
            request_options=request_options,
        )
        return _response.data

    async def get_content(
        self,
        page_id: str,
        *,
        locale_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        translatable: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetContentPagesResponse:
        """
        Get text and component instance content from a static page.

        <Badge intent="info">Localization</Badge>

        Required scope | `pages:read`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

        locale_id : typing.Optional[str]
            Unique identifier for a specific Locale.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        translatable : typing.Optional[str]
            Unique identifier for the secondary Locale you're translating **into**. Returns only content that hasn't been excluded from translation for that locale.

            This is independent of `localeId`, which selects which version of the content is returned. To fetch the source text to translate, request the primary locale's content and set `translatable` to the locale you're translating into:

            `?localeId={primary locale id}&translatable={target locale id}`

            Only exclusion rules scoped to manual translation are respected — rules scoped only to automatic translation don't affect this parameter's response.

            Omitting `translatable` returns the same response as if this parameter didn't exist. The value must be the id of one of the site's secondary locales — the primary locale id, or any other value, returns a `400` error. Requires translation exclusions to be enabled for the site; if they aren't, the request returns a `403` error.

            [Learn more about localization.](/data/v2.0.0/docs/working-with-localization)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContentPagesResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.get_content(
                page_id="63c720f9347c2139b248e552",
                locale_id="65427cf400e02b306eaa04a0",
                translatable="65427cf400e02b306eaa04a0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_content(
            page_id,
            locale_id=locale_id,
            limit=limit,
            offset=offset,
            translatable=translatable,
            request_options=request_options,
        )
        return _response.data

    async def update_static_content(
        self,
        page_id: str,
        *,
        locale_id: str,
        nodes: typing.Sequence[UpdateStaticContentRequestNodesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateStaticContentResponse:
        """
        This endpoint updates content on a static page in **secondary locales**. It supports updating up to 1000 nodes in a single request.

        Before making updates:
        1. Use the [get page content](/data/reference/pages-and-components/pages/get-content) endpoint to identify available content nodes and their types.
        2. If the page has component instances, retrieve the component's properties that you'll override using the [get component properties](/data/reference/pages-and-components/components/get-properties) endpoint.
        3. DOM elements may include a `data-w-id` attribute. This attribute is used by Webflow to maintain custom attributes and links across locales. Always include the original `data-w-id` value in your update requests to ensure consistent behavior across all locales.

        <Note>
          This endpoint is specifically for localized pages. Ensure that the specified `localeId` is a valid **secondary locale** for the site otherwise the request will fail.
        </Note>

        Required scope | `pages:write`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

        locale_id : str
            The locale identifier.

        nodes : typing.Sequence[UpdateStaticContentRequestNodesItem]
            List of DOM Nodes with the new content that will be updated in each node.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateStaticContentResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.pages import (
            UpdateStaticContentRequestNodesItemChoices,
            UpdateStaticContentRequestNodesItemChoicesChoicesItem,
            UpdateStaticContentRequestNodesItemPlaceholder,
            UpdateStaticContentRequestNodesItemPropertyOverrides,
            UpdateStaticContentRequestNodesItemPropertyOverridesPropertyOverridesItem,
            UpdateStaticContentRequestNodesItemText,
            UpdateStaticContentRequestNodesItemWaitingText,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.update_static_content(
                page_id="63c720f9347c2139b248e552",
                locale_id="localeId",
                nodes=[
                    UpdateStaticContentRequestNodesItemText(
                        node_id="a245c12d-995b-55ee-5ec7-aa36a6cad623",
                        text="<h1>The Hitchhiker's Guide to the Galaxy</h1>",
                    ),
                    UpdateStaticContentRequestNodesItemText(
                        node_id="a245c12d-995b-55ee-5ec7-aa36a6cad627",
                        text="<div><h3>Don't Panic!</h3><p>Always know where your towel is.</p></div>",
                    ),
                    UpdateStaticContentRequestNodesItemChoices(
                        node_id="a245c12d-995b-55ee-5ec7-aa36a6cad635",
                        choices=[
                            UpdateStaticContentRequestNodesItemChoicesChoicesItem(
                                value="choice-1",
                                text="First choice",
                            ),
                            UpdateStaticContentRequestNodesItemChoicesChoicesItem(
                                value="choice-2",
                                text="Second choice",
                            ),
                        ],
                    ),
                    UpdateStaticContentRequestNodesItemPlaceholder(
                        node_id="a245c12d-995b-55ee-5ec7-aa36a6cad642",
                        placeholder="Enter something here...",
                    ),
                    UpdateStaticContentRequestNodesItemWaitingText(
                        node_id="a245c12d-995b-55ee-5ec7-aa36a6cad671",
                        value="Submit",
                        waiting_text="Submitting...",
                    ),
                    UpdateStaticContentRequestNodesItemPropertyOverrides(
                        node_id="a245c12d-995b-55ee-5ec7-aa36a6cad629",
                        property_overrides=[
                            UpdateStaticContentRequestNodesItemPropertyOverridesPropertyOverridesItem(
                                property_id="7dd14c08-2e96-8d3d-2b19-b5c03642a0f0",
                                text="<div><h1>Time is an <em>illusion</em></h1></div>",
                            ),
                            UpdateStaticContentRequestNodesItemPropertyOverridesPropertyOverridesItem(
                                property_id="7dd14c08-2e96-8d3d-2b19-b5c03642a0f1",
                                text="Life, the Universe and Everything",
                            ),
                        ],
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_static_content(
            page_id, locale_id=locale_id, nodes=nodes, request_options=request_options
        )
        return _response.data

    @property
    def scripts(self):
        if self._scripts is None:
            from .scripts.client import AsyncScriptsClient

            self._scripts = AsyncScriptsClient(client_wrapper=self._client_wrapper)
        return self._scripts
