

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawRobotsTxtClient, RawRobotsTxtClient
from .types.delete_robots_txt_request_rules_item import DeleteRobotsTxtRequestRulesItem
from .types.delete_robots_txt_response import DeleteRobotsTxtResponse
from .types.get_robots_txt_response import GetRobotsTxtResponse
from .types.patch_robots_txt_request_rules_item import PatchRobotsTxtRequestRulesItem
from .types.patch_robots_txt_response import PatchRobotsTxtResponse
from .types.put_robots_txt_request_rules_item import PutRobotsTxtRequestRulesItem
from .types.put_robots_txt_response import PutRobotsTxtResponse


OMIT = typing.cast(typing.Any, ...)


class RobotsTxtClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRobotsTxtClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRobotsTxtClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRobotsTxtClient
        """
        return self._raw_client

    def get(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetRobotsTxtResponse:
        """
        Retrieve the robots.txt configuration for various user agents.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `site_config:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRobotsTxtResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.robots_txt.get(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.get(site_id, request_options=request_options)
        return _response.data

    def put(
        self,
        site_id: str,
        *,
        rules: typing.Optional[typing.Sequence[PutRobotsTxtRequestRulesItem]] = OMIT,
        sitemap: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutRobotsTxtResponse:
        """
        Replace the `robots.txt` configuration for various user agents.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `site_config:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        rules : typing.Optional[typing.Sequence[PutRobotsTxtRequestRulesItem]]
            List of rules for user agents.

        sitemap : typing.Optional[str]
            URL to the sitemap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutRobotsTxtResponse
            Request was successful

        Examples
        --------
        from fern.sites.robots_txt import PutRobotsTxtRequestRulesItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.robots_txt.put(
            site_id="580e63e98c9a982ac9b8b741",
            rules=[
                PutRobotsTxtRequestRulesItem(
                    user_agent="googlebot",
                    allows=["/public"],
                    disallows=["/vogon-poetry", "/total-perspective-vortex"],
                )
            ],
            sitemap="https://heartofgold.ship/sitemap.xml",
        )
        """
        _response = self._raw_client.put(site_id, rules=rules, sitemap=sitemap, request_options=request_options)
        return _response.data

    def delete(
        self,
        site_id: str,
        *,
        rules: typing.Optional[typing.Sequence[DeleteRobotsTxtRequestRulesItem]] = OMIT,
        sitemap: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteRobotsTxtResponse:
        """
        Remove specific rules for a user-agent in your `robots.txt` file. To delete all rules for a user-agent, provide an empty rule set. This will remove the user-agent's entry entirely, leaving it subject to your site's default crawling behavior.

        **Note:** Deleting a user-agent with no rules will make the user-agent's access unrestricted unless other directives apply.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `site_config:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        rules : typing.Optional[typing.Sequence[DeleteRobotsTxtRequestRulesItem]]
            List of rules for user agents.

        sitemap : typing.Optional[str]
            URL to the sitemap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteRobotsTxtResponse
            Request was successful

        Examples
        --------
        from fern.sites.robots_txt import DeleteRobotsTxtRequestRulesItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.robots_txt.delete(
            site_id="580e63e98c9a982ac9b8b741",
            rules=[
                DeleteRobotsTxtRequestRulesItem(
                    user_agent="*",
                    allows=["/public"],
                    disallows=["/bubbles"],
                )
            ],
        )
        """
        _response = self._raw_client.delete(site_id, rules=rules, sitemap=sitemap, request_options=request_options)
        return _response.data

    def patch(
        self,
        site_id: str,
        *,
        rules: typing.Optional[typing.Sequence[PatchRobotsTxtRequestRulesItem]] = OMIT,
        sitemap: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchRobotsTxtResponse:
        """
        Update the `robots.txt` configuration for various user agents.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `site_config:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        rules : typing.Optional[typing.Sequence[PatchRobotsTxtRequestRulesItem]]
            List of rules for user agents.

        sitemap : typing.Optional[str]
            URL to the sitemap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchRobotsTxtResponse
            Request was successful

        Examples
        --------
        from fern.sites.robots_txt import PatchRobotsTxtRequestRulesItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.robots_txt.patch(
            site_id="580e63e98c9a982ac9b8b741",
            rules=[
                PatchRobotsTxtRequestRulesItem(
                    user_agent="googlebot",
                    allows=["/public"],
                    disallows=["/vogon-poetry", "/total-perspective-vortex"],
                )
            ],
            sitemap="https://heartofgold.ship/sitemap.xml",
        )
        """
        _response = self._raw_client.patch(site_id, rules=rules, sitemap=sitemap, request_options=request_options)
        return _response.data


class AsyncRobotsTxtClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRobotsTxtClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRobotsTxtClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRobotsTxtClient
        """
        return self._raw_client

    async def get(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetRobotsTxtResponse:
        """
        Retrieve the robots.txt configuration for various user agents.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `site_config:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRobotsTxtResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.robots_txt.get(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(site_id, request_options=request_options)
        return _response.data

    async def put(
        self,
        site_id: str,
        *,
        rules: typing.Optional[typing.Sequence[PutRobotsTxtRequestRulesItem]] = OMIT,
        sitemap: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutRobotsTxtResponse:
        """
        Replace the `robots.txt` configuration for various user agents.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `site_config:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        rules : typing.Optional[typing.Sequence[PutRobotsTxtRequestRulesItem]]
            List of rules for user agents.

        sitemap : typing.Optional[str]
            URL to the sitemap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutRobotsTxtResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.sites.robots_txt import PutRobotsTxtRequestRulesItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.robots_txt.put(
                site_id="580e63e98c9a982ac9b8b741",
                rules=[
                    PutRobotsTxtRequestRulesItem(
                        user_agent="googlebot",
                        allows=["/public"],
                        disallows=["/vogon-poetry", "/total-perspective-vortex"],
                    )
                ],
                sitemap="https://heartofgold.ship/sitemap.xml",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put(site_id, rules=rules, sitemap=sitemap, request_options=request_options)
        return _response.data

    async def delete(
        self,
        site_id: str,
        *,
        rules: typing.Optional[typing.Sequence[DeleteRobotsTxtRequestRulesItem]] = OMIT,
        sitemap: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteRobotsTxtResponse:
        """
        Remove specific rules for a user-agent in your `robots.txt` file. To delete all rules for a user-agent, provide an empty rule set. This will remove the user-agent's entry entirely, leaving it subject to your site's default crawling behavior.

        **Note:** Deleting a user-agent with no rules will make the user-agent's access unrestricted unless other directives apply.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `site_config:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        rules : typing.Optional[typing.Sequence[DeleteRobotsTxtRequestRulesItem]]
            List of rules for user agents.

        sitemap : typing.Optional[str]
            URL to the sitemap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteRobotsTxtResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.sites.robots_txt import DeleteRobotsTxtRequestRulesItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.robots_txt.delete(
                site_id="580e63e98c9a982ac9b8b741",
                rules=[
                    DeleteRobotsTxtRequestRulesItem(
                        user_agent="*",
                        allows=["/public"],
                        disallows=["/bubbles"],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(
            site_id, rules=rules, sitemap=sitemap, request_options=request_options
        )
        return _response.data

    async def patch(
        self,
        site_id: str,
        *,
        rules: typing.Optional[typing.Sequence[PatchRobotsTxtRequestRulesItem]] = OMIT,
        sitemap: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchRobotsTxtResponse:
        """
        Update the `robots.txt` configuration for various user agents.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `site_config:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        rules : typing.Optional[typing.Sequence[PatchRobotsTxtRequestRulesItem]]
            List of rules for user agents.

        sitemap : typing.Optional[str]
            URL to the sitemap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchRobotsTxtResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.sites.robots_txt import PatchRobotsTxtRequestRulesItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.robots_txt.patch(
                site_id="580e63e98c9a982ac9b8b741",
                rules=[
                    PatchRobotsTxtRequestRulesItem(
                        user_agent="googlebot",
                        allows=["/public"],
                        disallows=["/vogon-poetry", "/total-perspective-vortex"],
                    )
                ],
                sitemap="https://heartofgold.ship/sitemap.xml",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch(site_id, rules=rules, sitemap=sitemap, request_options=request_options)
        return _response.data
