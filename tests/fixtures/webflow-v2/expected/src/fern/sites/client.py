

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSitesClient, RawSitesClient
from .types.create_sites_response import CreateSitesResponse
from .types.get_custom_domain_sites_response import GetCustomDomainSitesResponse
from .types.get_sites_response import GetSitesResponse
from .types.list_sites_response import ListSitesResponse
from .types.publish_sites_response import PublishSitesResponse
from .types.update_sites_response import UpdateSitesResponse

if typing.TYPE_CHECKING:
    from .activity_logs.client import ActivityLogsClient, AsyncActivityLogsClient
    from .comments.client import AsyncCommentsClient, CommentsClient
    from .forms.client import AsyncFormsClient, FormsClient
    from .google_tag.client import AsyncGoogleTagClient, GoogleTagClient
    from .plans.client import AsyncPlansClient, PlansClient
    from .redirects.client import AsyncRedirectsClient, RedirectsClient
    from .robots_txt.client import AsyncRobotsTxtClient, RobotsTxtClient
    from .scripts.client import AsyncScriptsClient, ScriptsClient
    from .well_known.client import AsyncWellKnownClient, WellKnownClient

OMIT = typing.cast(typing.Any, ...)


class SitesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSitesClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._redirects: typing.Optional[RedirectsClient] = None
        self._plans: typing.Optional[PlansClient] = None
        self._robots_txt: typing.Optional[RobotsTxtClient] = None
        self._well_known: typing.Optional[WellKnownClient] = None
        self._google_tag: typing.Optional[GoogleTagClient] = None
        self._activity_logs: typing.Optional[ActivityLogsClient] = None
        self._comments: typing.Optional[CommentsClient] = None
        self._scripts: typing.Optional[ScriptsClient] = None
        self._forms: typing.Optional[FormsClient] = None

    @property
    def with_raw_response(self) -> RawSitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSitesClient
        """
        return self._raw_client

    def create(
        self,
        workspace_id: str,
        *,
        name: str,
        template_name: typing.Optional[str] = OMIT,
        parent_folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSitesResponse:
        """
        Create a site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `workspace:write`

        Parameters
        ----------
        workspace_id : str
            Unique identifier for a Workspace

        name : str
            The name of the site

        template_name : typing.Optional[str]
            The workspace or marketplace template to use

        parent_folder_id : typing.Optional[str]
            MegaDodo Publications - Potential Book Ideas

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSitesResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.create(
            workspace_id="580e63e98c9a982ac9b8b741",
            name="The Hitchhiker's Guide to the Galaxy",
        )
        """
        _response = self._raw_client.create(
            workspace_id,
            name=name,
            template_name=template_name,
            parent_folder_id=parent_folder_id,
            request_options=request_options,
        )
        return _response.data

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListSitesResponse:
        """
        List of all sites the provided access token is able to access.

        Required scope | `sites:read`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSitesResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def get(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetSitesResponse:
        """
        Get details of a site.

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSitesResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.get(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.get(site_id, request_options=request_options)
        return _response.data

    def delete(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.delete(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.delete(site_id, request_options=request_options)
        return _response.data

    def update(
        self,
        site_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        parent_folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSitesResponse:
        """
        Update a site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        name : typing.Optional[str]
            The name of the site

        parent_folder_id : typing.Optional[str]
            The parent folder ID of the site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSitesResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.update(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.update(
            site_id, name=name, parent_folder_id=parent_folder_id, request_options=request_options
        )
        return _response.data

    def get_custom_domain(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomDomainSitesResponse:
        """
        Get a list of all custom domains related to site.

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomDomainSitesResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.get_custom_domain(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.get_custom_domain(site_id, request_options=request_options)
        return _response.data

    def publish(
        self,
        site_id: str,
        *,
        custom_domains: typing.Optional[typing.Sequence[str]] = OMIT,
        publish_to_webflow_subdomain: typing.Optional[bool] = OMIT,
        page_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublishSitesResponse:
        """
        Publishes a site or an individual page to one or more domains.
        If multiple individual pages are published to staging, publishing from staging to production publishes all staged changes.

        To publish to a specific custom domain, use the domain IDs from the [Get Custom Domains](/data/reference/sites/get-custom-domain) endpoint.

        You must include at least one of the `customDomains` or `publishToWebflowSubdomain` properties in the request body.

        To publish an individual page instead of the entire site, provide the ID of the page in the `pageId` parameter.

        <Note title="Rate limit: 1 publish per minute">This endpoint has a specific rate limit of one successful publish queue per minute.</Note>

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        custom_domains : typing.Optional[typing.Sequence[str]]
            Array of Custom Domain IDs to publish

        publish_to_webflow_subdomain : typing.Optional[bool]
            Choice of whether to publish to the default Webflow Subdomain

        page_id : typing.Optional[str]
            The ID of the page to publish

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishSitesResponse
            Request accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.publish(
            site_id="580e63e98c9a982ac9b8b741",
            custom_domains=["660c6449dd97ebc7346ac629", "660c6449dd97ebc7346ac62f"],
            publish_to_webflow_subdomain=False,
        )
        """
        _response = self._raw_client.publish(
            site_id,
            custom_domains=custom_domains,
            publish_to_webflow_subdomain=publish_to_webflow_subdomain,
            page_id=page_id,
            request_options=request_options,
        )
        return _response.data

    @property
    def redirects(self):
        if self._redirects is None:
            from .redirects.client import RedirectsClient

            self._redirects = RedirectsClient(client_wrapper=self._client_wrapper)
        return self._redirects

    @property
    def plans(self):
        if self._plans is None:
            from .plans.client import PlansClient

            self._plans = PlansClient(client_wrapper=self._client_wrapper)
        return self._plans

    @property
    def robots_txt(self):
        if self._robots_txt is None:
            from .robots_txt.client import RobotsTxtClient

            self._robots_txt = RobotsTxtClient(client_wrapper=self._client_wrapper)
        return self._robots_txt

    @property
    def well_known(self):
        if self._well_known is None:
            from .well_known.client import WellKnownClient

            self._well_known = WellKnownClient(client_wrapper=self._client_wrapper)
        return self._well_known

    @property
    def google_tag(self):
        if self._google_tag is None:
            from .google_tag.client import GoogleTagClient

            self._google_tag = GoogleTagClient(client_wrapper=self._client_wrapper)
        return self._google_tag

    @property
    def activity_logs(self):
        if self._activity_logs is None:
            from .activity_logs.client import ActivityLogsClient

            self._activity_logs = ActivityLogsClient(client_wrapper=self._client_wrapper)
        return self._activity_logs

    @property
    def comments(self):
        if self._comments is None:
            from .comments.client import CommentsClient

            self._comments = CommentsClient(client_wrapper=self._client_wrapper)
        return self._comments

    @property
    def scripts(self):
        if self._scripts is None:
            from .scripts.client import ScriptsClient

            self._scripts = ScriptsClient(client_wrapper=self._client_wrapper)
        return self._scripts

    @property
    def forms(self):
        if self._forms is None:
            from .forms.client import FormsClient

            self._forms = FormsClient(client_wrapper=self._client_wrapper)
        return self._forms


class AsyncSitesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSitesClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._redirects: typing.Optional[AsyncRedirectsClient] = None
        self._plans: typing.Optional[AsyncPlansClient] = None
        self._robots_txt: typing.Optional[AsyncRobotsTxtClient] = None
        self._well_known: typing.Optional[AsyncWellKnownClient] = None
        self._google_tag: typing.Optional[AsyncGoogleTagClient] = None
        self._activity_logs: typing.Optional[AsyncActivityLogsClient] = None
        self._comments: typing.Optional[AsyncCommentsClient] = None
        self._scripts: typing.Optional[AsyncScriptsClient] = None
        self._forms: typing.Optional[AsyncFormsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawSitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSitesClient
        """
        return self._raw_client

    async def create(
        self,
        workspace_id: str,
        *,
        name: str,
        template_name: typing.Optional[str] = OMIT,
        parent_folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSitesResponse:
        """
        Create a site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `workspace:write`

        Parameters
        ----------
        workspace_id : str
            Unique identifier for a Workspace

        name : str
            The name of the site

        template_name : typing.Optional[str]
            The workspace or marketplace template to use

        parent_folder_id : typing.Optional[str]
            MegaDodo Publications - Potential Book Ideas

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSitesResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.create(
                workspace_id="580e63e98c9a982ac9b8b741",
                name="The Hitchhiker's Guide to the Galaxy",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            workspace_id,
            name=name,
            template_name=template_name,
            parent_folder_id=parent_folder_id,
            request_options=request_options,
        )
        return _response.data

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListSitesResponse:
        """
        List of all sites the provided access token is able to access.

        Required scope | `sites:read`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSitesResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def get(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetSitesResponse:
        """
        Get details of a site.

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSitesResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.get(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(site_id, request_options=request_options)
        return _response.data

    async def delete(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.delete(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(site_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        site_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        parent_folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSitesResponse:
        """
        Update a site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        name : typing.Optional[str]
            The name of the site

        parent_folder_id : typing.Optional[str]
            The parent folder ID of the site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSitesResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.update(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            site_id, name=name, parent_folder_id=parent_folder_id, request_options=request_options
        )
        return _response.data

    async def get_custom_domain(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomDomainSitesResponse:
        """
        Get a list of all custom domains related to site.

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomDomainSitesResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.get_custom_domain(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_custom_domain(site_id, request_options=request_options)
        return _response.data

    async def publish(
        self,
        site_id: str,
        *,
        custom_domains: typing.Optional[typing.Sequence[str]] = OMIT,
        publish_to_webflow_subdomain: typing.Optional[bool] = OMIT,
        page_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublishSitesResponse:
        """
        Publishes a site or an individual page to one or more domains.
        If multiple individual pages are published to staging, publishing from staging to production publishes all staged changes.

        To publish to a specific custom domain, use the domain IDs from the [Get Custom Domains](/data/reference/sites/get-custom-domain) endpoint.

        You must include at least one of the `customDomains` or `publishToWebflowSubdomain` properties in the request body.

        To publish an individual page instead of the entire site, provide the ID of the page in the `pageId` parameter.

        <Note title="Rate limit: 1 publish per minute">This endpoint has a specific rate limit of one successful publish queue per minute.</Note>

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        custom_domains : typing.Optional[typing.Sequence[str]]
            Array of Custom Domain IDs to publish

        publish_to_webflow_subdomain : typing.Optional[bool]
            Choice of whether to publish to the default Webflow Subdomain

        page_id : typing.Optional[str]
            The ID of the page to publish

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishSitesResponse
            Request accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.publish(
                site_id="580e63e98c9a982ac9b8b741",
                custom_domains=["660c6449dd97ebc7346ac629", "660c6449dd97ebc7346ac62f"],
                publish_to_webflow_subdomain=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish(
            site_id,
            custom_domains=custom_domains,
            publish_to_webflow_subdomain=publish_to_webflow_subdomain,
            page_id=page_id,
            request_options=request_options,
        )
        return _response.data

    @property
    def redirects(self):
        if self._redirects is None:
            from .redirects.client import AsyncRedirectsClient

            self._redirects = AsyncRedirectsClient(client_wrapper=self._client_wrapper)
        return self._redirects

    @property
    def plans(self):
        if self._plans is None:
            from .plans.client import AsyncPlansClient

            self._plans = AsyncPlansClient(client_wrapper=self._client_wrapper)
        return self._plans

    @property
    def robots_txt(self):
        if self._robots_txt is None:
            from .robots_txt.client import AsyncRobotsTxtClient

            self._robots_txt = AsyncRobotsTxtClient(client_wrapper=self._client_wrapper)
        return self._robots_txt

    @property
    def well_known(self):
        if self._well_known is None:
            from .well_known.client import AsyncWellKnownClient

            self._well_known = AsyncWellKnownClient(client_wrapper=self._client_wrapper)
        return self._well_known

    @property
    def google_tag(self):
        if self._google_tag is None:
            from .google_tag.client import AsyncGoogleTagClient

            self._google_tag = AsyncGoogleTagClient(client_wrapper=self._client_wrapper)
        return self._google_tag

    @property
    def activity_logs(self):
        if self._activity_logs is None:
            from .activity_logs.client import AsyncActivityLogsClient

            self._activity_logs = AsyncActivityLogsClient(client_wrapper=self._client_wrapper)
        return self._activity_logs

    @property
    def comments(self):
        if self._comments is None:
            from .comments.client import AsyncCommentsClient

            self._comments = AsyncCommentsClient(client_wrapper=self._client_wrapper)
        return self._comments

    @property
    def scripts(self):
        if self._scripts is None:
            from .scripts.client import AsyncScriptsClient

            self._scripts = AsyncScriptsClient(client_wrapper=self._client_wrapper)
        return self._scripts

    @property
    def forms(self):
        if self._forms is None:
            from .forms.client import AsyncFormsClient

            self._forms = AsyncFormsClient(client_wrapper=self._client_wrapper)
        return self._forms
