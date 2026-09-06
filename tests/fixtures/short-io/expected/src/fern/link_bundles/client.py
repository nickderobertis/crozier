

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLinkBundlesClient, RawLinkBundlesClient
from .types.patch_links_bundle_id_links_request_body_item import PatchLinksBundleIdLinksRequestBodyItem


OMIT = typing.cast(typing.Any, ...)


class LinkBundlesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLinkBundlesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLinkBundlesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLinkBundlesClient
        """
        return self._raw_client

    def get_bundle_templates(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns all available bundle templates

        Parameters
        ----------
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
        client.link_bundles.get_bundle_templates()
        """
        _response = self._raw_client.get_bundle_templates(request_options=request_options)
        return _response.data

    def get_bundle_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns bundle details by ULID id

        Parameters
        ----------
        id : str
            Bundle ULID id

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
        client.link_bundles.get_bundle_by_id(
            id="id",
        )
        """
        _response = self._raw_client.get_bundle_by_id(id, request_options=request_options)
        return _response.data

    def update_bundle(
        self,
        id: str,
        *,
        domain_id: typing.Optional[float] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        background_image_url: typing.Optional[str] = OMIT,
        twitter_username: typing.Optional[str] = OMIT,
        fb_username: typing.Optional[str] = OMIT,
        linkedin_companyname: typing.Optional[str] = OMIT,
        linkedin_username: typing.Optional[str] = OMIT,
        instagram_username: typing.Optional[str] = OMIT,
        whatsapp_url: typing.Optional[str] = OMIT,
        viber_url: typing.Optional[str] = OMIT,
        telegram_url: typing.Optional[str] = OMIT,
        threads_username: typing.Optional[str] = OMIT,
        mastodon_username: typing.Optional[str] = OMIT,
        bluesky_username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates bundle details, social media links, and branding

        Parameters
        ----------
        id : str
            Bundle ULID id

        domain_id : typing.Optional[float]

        template_id : typing.Optional[str]
            Template ID

        title : typing.Optional[str]
            Bundle title

        description : typing.Optional[str]
            Bundle description

        logo_url : typing.Optional[str]
            Profile or logo URL

        background_image_url : typing.Optional[str]
            Background image URL

        twitter_username : typing.Optional[str]
            Twitter username (without @)

        fb_username : typing.Optional[str]
            Facebook username

        linkedin_companyname : typing.Optional[str]
            LinkedIn company name (mutually exclusive with linkedinUsername)

        linkedin_username : typing.Optional[str]
            LinkedIn username (mutually exclusive with linkedinCompanyname)

        instagram_username : typing.Optional[str]
            Instagram username (without @)

        whatsapp_url : typing.Optional[str]
            WhatsApp URL (must start with whatsapp:// or https://)

        viber_url : typing.Optional[str]
            Viber URL (must start with viber:// or https://)

        telegram_url : typing.Optional[str]
            Telegram URL

        threads_username : typing.Optional[str]
            Threads username (without @)

        mastodon_username : typing.Optional[str]
            Mastodon username

        bluesky_username : typing.Optional[str]
            Bluesky username

        email : typing.Optional[str]
            Contact email address

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
        client.link_bundles.update_bundle(
            id="id",
        )
        """
        _response = self._raw_client.update_bundle(
            id,
            domain_id=domain_id,
            template_id=template_id,
            title=title,
            description=description,
            logo_url=logo_url,
            background_image_url=background_image_url,
            twitter_username=twitter_username,
            fb_username=fb_username,
            linkedin_companyname=linkedin_companyname,
            linkedin_username=linkedin_username,
            instagram_username=instagram_username,
            whatsapp_url=whatsapp_url,
            viber_url=viber_url,
            telegram_url=telegram_url,
            threads_username=threads_username,
            mastodon_username=mastodon_username,
            bluesky_username=bluesky_username,
            email=email,
            request_options=request_options,
        )
        return _response.data

    def delete_bundle(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a bundle by ULID id

        Parameters
        ----------
        id : str
            Bundle ULID id

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
        client.link_bundles.delete_bundle(
            id="id",
        )
        """
        _response = self._raw_client.delete_bundle(id, request_options=request_options)
        return _response.data

    def upload_bundle_logo(
        self, id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Uploads a logo image for a bundle

        Parameters
        ----------
        id : str
            Bundle ULID id

        request : typing.Any

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
        client.link_bundles.upload_bundle_logo(
            id="id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.upload_bundle_logo(id, request=request, request_options=request_options)
        return _response.data

    def upload_bundle_background_image(
        self, id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Uploads a background image for a bundle

        Parameters
        ----------
        id : str
            Bundle ULID id

        request : typing.Any

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
        client.link_bundles.upload_bundle_background_image(
            id="id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.upload_bundle_background_image(
            id, request=request, request_options=request_options
        )
        return _response.data

    def create_bundle(
        self,
        *,
        domain_id: float,
        template_id: str,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        background_image_url: typing.Optional[str] = OMIT,
        twitter_username: typing.Optional[str] = OMIT,
        fb_username: typing.Optional[str] = OMIT,
        linkedin_companyname: typing.Optional[str] = OMIT,
        linkedin_username: typing.Optional[str] = OMIT,
        instagram_username: typing.Optional[str] = OMIT,
        whatsapp_url: typing.Optional[str] = OMIT,
        viber_url: typing.Optional[str] = OMIT,
        telegram_url: typing.Optional[str] = OMIT,
        threads_username: typing.Optional[str] = OMIT,
        mastodon_username: typing.Optional[str] = OMIT,
        bluesky_username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new link bundle with customizable template, social media links, and branding

        Parameters
        ----------
        domain_id : float
            Domain ID where the bundle will be created

        template_id : str
            Template ID from available templates

        title : typing.Optional[str]
            Bundle title

        description : typing.Optional[str]
            Bundle description

        logo_url : typing.Optional[str]
            Profile or logo URL

        background_image_url : typing.Optional[str]
            Background image URL

        twitter_username : typing.Optional[str]
            Twitter username (without @)

        fb_username : typing.Optional[str]
            Facebook username

        linkedin_companyname : typing.Optional[str]
            LinkedIn company name (mutually exclusive with linkedinUsername)

        linkedin_username : typing.Optional[str]
            LinkedIn username (mutually exclusive with linkedinCompanyname)

        instagram_username : typing.Optional[str]
            Instagram username (without @)

        whatsapp_url : typing.Optional[str]
            WhatsApp URL (must start with whatsapp:// or https://)

        viber_url : typing.Optional[str]
            Viber URL (must start with viber:// or https://)

        telegram_url : typing.Optional[str]
            Telegram URL

        threads_username : typing.Optional[str]
            Threads username (without @)

        mastodon_username : typing.Optional[str]
            Mastodon username

        bluesky_username : typing.Optional[str]
            Bluesky username

        email : typing.Optional[str]
            Contact email address

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
        client.link_bundles.create_bundle(
            domain_id=1.1,
            template_id="TemplateId",
        )
        """
        _response = self._raw_client.create_bundle(
            domain_id=domain_id,
            template_id=template_id,
            title=title,
            description=description,
            logo_url=logo_url,
            background_image_url=background_image_url,
            twitter_username=twitter_username,
            fb_username=fb_username,
            linkedin_companyname=linkedin_companyname,
            linkedin_username=linkedin_username,
            instagram_username=instagram_username,
            whatsapp_url=whatsapp_url,
            viber_url=viber_url,
            telegram_url=telegram_url,
            threads_username=threads_username,
            mastodon_username=mastodon_username,
            bluesky_username=bluesky_username,
            email=email,
            request_options=request_options,
        )
        return _response.data

    def get_bundle_links(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns all links in a bundle, ordered by sort order

        Parameters
        ----------
        id : str
            Bundle ULID id

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
        client.link_bundles.get_bundle_links(
            id="id",
        )
        """
        _response = self._raw_client.get_bundle_links(id, request_options=request_options)
        return _response.data

    def add_link_to_bundle(
        self, id: str, *, path: str, title: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Adds a short link to a bundle. If the link doesn't exist, it will be created.

        Parameters
        ----------
        id : str
            Bundle ULID id

        path : str
            Short link path or full URL

        title : str
            Display title for the link

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
        client.link_bundles.add_link_to_bundle(
            id="id",
            path="path",
            title="title",
        )
        """
        _response = self._raw_client.add_link_to_bundle(id, path=path, title=title, request_options=request_options)
        return _response.data

    def update_link_sort_order(
        self,
        id: str,
        *,
        request: typing.Sequence[PatchLinksBundleIdLinksRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the sort order of links in a bundle

        Parameters
        ----------
        id : str
            Bundle ULID id

        request : typing.Sequence[PatchLinksBundleIdLinksRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.link_bundles import PatchLinksBundleIdLinksRequestBodyItem

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_bundles.update_link_sort_order(
            id="id",
            request=[
                PatchLinksBundleIdLinksRequestBodyItem(
                    id="id",
                    sort_order=1.1,
                )
            ],
        )
        """
        _response = self._raw_client.update_link_sort_order(id, request=request, request_options=request_options)
        return _response.data

    def remove_link_from_bundle(
        self, id: str, link_template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a link from a bundle by its link template ID

        Parameters
        ----------
        id : str
            Bundle ULID id

        link_template_id : str
            Link template ID to remove

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
        client.link_bundles.remove_link_from_bundle(
            id="id",
            link_template_id="linkTemplateId",
        )
        """
        _response = self._raw_client.remove_link_from_bundle(id, link_template_id, request_options=request_options)
        return _response.data


class AsyncLinkBundlesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLinkBundlesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLinkBundlesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLinkBundlesClient
        """
        return self._raw_client

    async def get_bundle_templates(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns all available bundle templates

        Parameters
        ----------
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
            await client.link_bundles.get_bundle_templates()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bundle_templates(request_options=request_options)
        return _response.data

    async def get_bundle_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns bundle details by ULID id

        Parameters
        ----------
        id : str
            Bundle ULID id

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
            await client.link_bundles.get_bundle_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bundle_by_id(id, request_options=request_options)
        return _response.data

    async def update_bundle(
        self,
        id: str,
        *,
        domain_id: typing.Optional[float] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        background_image_url: typing.Optional[str] = OMIT,
        twitter_username: typing.Optional[str] = OMIT,
        fb_username: typing.Optional[str] = OMIT,
        linkedin_companyname: typing.Optional[str] = OMIT,
        linkedin_username: typing.Optional[str] = OMIT,
        instagram_username: typing.Optional[str] = OMIT,
        whatsapp_url: typing.Optional[str] = OMIT,
        viber_url: typing.Optional[str] = OMIT,
        telegram_url: typing.Optional[str] = OMIT,
        threads_username: typing.Optional[str] = OMIT,
        mastodon_username: typing.Optional[str] = OMIT,
        bluesky_username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates bundle details, social media links, and branding

        Parameters
        ----------
        id : str
            Bundle ULID id

        domain_id : typing.Optional[float]

        template_id : typing.Optional[str]
            Template ID

        title : typing.Optional[str]
            Bundle title

        description : typing.Optional[str]
            Bundle description

        logo_url : typing.Optional[str]
            Profile or logo URL

        background_image_url : typing.Optional[str]
            Background image URL

        twitter_username : typing.Optional[str]
            Twitter username (without @)

        fb_username : typing.Optional[str]
            Facebook username

        linkedin_companyname : typing.Optional[str]
            LinkedIn company name (mutually exclusive with linkedinUsername)

        linkedin_username : typing.Optional[str]
            LinkedIn username (mutually exclusive with linkedinCompanyname)

        instagram_username : typing.Optional[str]
            Instagram username (without @)

        whatsapp_url : typing.Optional[str]
            WhatsApp URL (must start with whatsapp:// or https://)

        viber_url : typing.Optional[str]
            Viber URL (must start with viber:// or https://)

        telegram_url : typing.Optional[str]
            Telegram URL

        threads_username : typing.Optional[str]
            Threads username (without @)

        mastodon_username : typing.Optional[str]
            Mastodon username

        bluesky_username : typing.Optional[str]
            Bluesky username

        email : typing.Optional[str]
            Contact email address

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
            await client.link_bundles.update_bundle(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_bundle(
            id,
            domain_id=domain_id,
            template_id=template_id,
            title=title,
            description=description,
            logo_url=logo_url,
            background_image_url=background_image_url,
            twitter_username=twitter_username,
            fb_username=fb_username,
            linkedin_companyname=linkedin_companyname,
            linkedin_username=linkedin_username,
            instagram_username=instagram_username,
            whatsapp_url=whatsapp_url,
            viber_url=viber_url,
            telegram_url=telegram_url,
            threads_username=threads_username,
            mastodon_username=mastodon_username,
            bluesky_username=bluesky_username,
            email=email,
            request_options=request_options,
        )
        return _response.data

    async def delete_bundle(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a bundle by ULID id

        Parameters
        ----------
        id : str
            Bundle ULID id

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
            await client.link_bundles.delete_bundle(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_bundle(id, request_options=request_options)
        return _response.data

    async def upload_bundle_logo(
        self, id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Uploads a logo image for a bundle

        Parameters
        ----------
        id : str
            Bundle ULID id

        request : typing.Any

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
            await client.link_bundles.upload_bundle_logo(
                id="id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_bundle_logo(id, request=request, request_options=request_options)
        return _response.data

    async def upload_bundle_background_image(
        self, id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Uploads a background image for a bundle

        Parameters
        ----------
        id : str
            Bundle ULID id

        request : typing.Any

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
            await client.link_bundles.upload_bundle_background_image(
                id="id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_bundle_background_image(
            id, request=request, request_options=request_options
        )
        return _response.data

    async def create_bundle(
        self,
        *,
        domain_id: float,
        template_id: str,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        background_image_url: typing.Optional[str] = OMIT,
        twitter_username: typing.Optional[str] = OMIT,
        fb_username: typing.Optional[str] = OMIT,
        linkedin_companyname: typing.Optional[str] = OMIT,
        linkedin_username: typing.Optional[str] = OMIT,
        instagram_username: typing.Optional[str] = OMIT,
        whatsapp_url: typing.Optional[str] = OMIT,
        viber_url: typing.Optional[str] = OMIT,
        telegram_url: typing.Optional[str] = OMIT,
        threads_username: typing.Optional[str] = OMIT,
        mastodon_username: typing.Optional[str] = OMIT,
        bluesky_username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a new link bundle with customizable template, social media links, and branding

        Parameters
        ----------
        domain_id : float
            Domain ID where the bundle will be created

        template_id : str
            Template ID from available templates

        title : typing.Optional[str]
            Bundle title

        description : typing.Optional[str]
            Bundle description

        logo_url : typing.Optional[str]
            Profile or logo URL

        background_image_url : typing.Optional[str]
            Background image URL

        twitter_username : typing.Optional[str]
            Twitter username (without @)

        fb_username : typing.Optional[str]
            Facebook username

        linkedin_companyname : typing.Optional[str]
            LinkedIn company name (mutually exclusive with linkedinUsername)

        linkedin_username : typing.Optional[str]
            LinkedIn username (mutually exclusive with linkedinCompanyname)

        instagram_username : typing.Optional[str]
            Instagram username (without @)

        whatsapp_url : typing.Optional[str]
            WhatsApp URL (must start with whatsapp:// or https://)

        viber_url : typing.Optional[str]
            Viber URL (must start with viber:// or https://)

        telegram_url : typing.Optional[str]
            Telegram URL

        threads_username : typing.Optional[str]
            Threads username (without @)

        mastodon_username : typing.Optional[str]
            Mastodon username

        bluesky_username : typing.Optional[str]
            Bluesky username

        email : typing.Optional[str]
            Contact email address

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
            await client.link_bundles.create_bundle(
                domain_id=1.1,
                template_id="TemplateId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_bundle(
            domain_id=domain_id,
            template_id=template_id,
            title=title,
            description=description,
            logo_url=logo_url,
            background_image_url=background_image_url,
            twitter_username=twitter_username,
            fb_username=fb_username,
            linkedin_companyname=linkedin_companyname,
            linkedin_username=linkedin_username,
            instagram_username=instagram_username,
            whatsapp_url=whatsapp_url,
            viber_url=viber_url,
            telegram_url=telegram_url,
            threads_username=threads_username,
            mastodon_username=mastodon_username,
            bluesky_username=bluesky_username,
            email=email,
            request_options=request_options,
        )
        return _response.data

    async def get_bundle_links(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns all links in a bundle, ordered by sort order

        Parameters
        ----------
        id : str
            Bundle ULID id

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
            await client.link_bundles.get_bundle_links(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bundle_links(id, request_options=request_options)
        return _response.data

    async def add_link_to_bundle(
        self, id: str, *, path: str, title: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Adds a short link to a bundle. If the link doesn't exist, it will be created.

        Parameters
        ----------
        id : str
            Bundle ULID id

        path : str
            Short link path or full URL

        title : str
            Display title for the link

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
            await client.link_bundles.add_link_to_bundle(
                id="id",
                path="path",
                title="title",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_link_to_bundle(
            id, path=path, title=title, request_options=request_options
        )
        return _response.data

    async def update_link_sort_order(
        self,
        id: str,
        *,
        request: typing.Sequence[PatchLinksBundleIdLinksRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the sort order of links in a bundle

        Parameters
        ----------
        id : str
            Bundle ULID id

        request : typing.Sequence[PatchLinksBundleIdLinksRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.link_bundles import PatchLinksBundleIdLinksRequestBodyItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_bundles.update_link_sort_order(
                id="id",
                request=[
                    PatchLinksBundleIdLinksRequestBodyItem(
                        id="id",
                        sort_order=1.1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_link_sort_order(id, request=request, request_options=request_options)
        return _response.data

    async def remove_link_from_bundle(
        self, id: str, link_template_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a link from a bundle by its link template ID

        Parameters
        ----------
        id : str
            Bundle ULID id

        link_template_id : str
            Link template ID to remove

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
            await client.link_bundles.remove_link_from_bundle(
                id="id",
                link_template_id="linkTemplateId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_link_from_bundle(
            id, link_template_id, request_options=request_options
        )
        return _response.data
