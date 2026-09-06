

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDomainsClient, RawDomainsClient
from .types.get_api_domains_response_item import GetApiDomainsResponseItem
from .types.get_domains_domain_id_response import GetDomainsDomainIdResponse
from .types.post_domains_request_link_type import PostDomainsRequestLinkType
from .types.post_domains_response import PostDomainsResponse
from .types.post_domains_settings_domain_id_request_https_level import PostDomainsSettingsDomainIdRequestHttpsLevel
from .types.post_domains_settings_domain_id_request_link_type import PostDomainsSettingsDomainIdRequestLinkType
from .types.post_domains_settings_domain_id_request_robots import PostDomainsSettingsDomainIdRequestRobots
from .types.post_domains_settings_domain_id_request_webhook_url import PostDomainsSettingsDomainIdRequestWebhookUrl
from .types.post_domains_settings_domain_id_response import PostDomainsSettingsDomainIdResponse


OMIT = typing.cast(typing.Any, ...)


class DomainsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDomainsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDomainsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDomainsClient
        """
        return self._raw_client

    def list_domains(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        no_team_id: typing.Optional[bool] = None,
        pattern: typing.Optional[str] = None,
        team_id: typing.Optional[float] = None,
        type: typing.Optional[typing.Dict[str, typing.Any]] = None,
        additional_properties: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetApiDomainsResponseItem]:
        """
        Shows all domains of current user

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        no_team_id : typing.Optional[bool]

        pattern : typing.Optional[str]

        team_id : typing.Optional[float]

        type : typing.Optional[typing.Dict[str, typing.Any]]

        additional_properties : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetApiDomainsResponseItem]
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.domains.list_domains()
        """
        _response = self._raw_client.list_domains(
            limit=limit,
            offset=offset,
            no_team_id=no_team_id,
            pattern=pattern,
            team_id=team_id,
            type=type,
            additional_properties=additional_properties,
            request_options=request_options,
        )
        return _response.data

    def get_domain_details_by_id(
        self, domain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDomainsDomainIdResponse:
        """
        Parameters
        ----------
        domain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDomainsDomainIdResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.domains.get_domain_details_by_id(
            domain_id=1,
        )
        """
        _response = self._raw_client.get_domain_details_by_id(domain_id, request_options=request_options)
        return _response.data

    def update_domain_settings(
        self,
        domain_id: int,
        *,
        https_level: typing.Optional[PostDomainsSettingsDomainIdRequestHttpsLevel] = OMIT,
        robots: typing.Optional[PostDomainsSettingsDomainIdRequestRobots] = OMIT,
        segment_key: typing.Optional[str] = OMIT,
        link_type: typing.Optional[PostDomainsSettingsDomainIdRequestLinkType] = OMIT,
        cloaking: typing.Optional[bool] = OMIT,
        hide_referer: typing.Optional[bool] = OMIT,
        hide_visitor_ip: typing.Optional[bool] = OMIT,
        https_links: typing.Optional[bool] = OMIT,
        webhook_url: typing.Optional[PostDomainsSettingsDomainIdRequestWebhookUrl] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        enable_conversion_tracking: typing.Optional[bool] = OMIT,
        qr_scan_tracking: typing.Optional[bool] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        client_storage: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        purge_expired_links: typing.Optional[bool] = OMIT,
        enable_ai: typing.Optional[bool] = OMIT,
        case_sensitive: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostDomainsSettingsDomainIdResponse:
        """
        Update domain settings

        Parameters
        ----------
        domain_id : int

        https_level : typing.Optional[PostDomainsSettingsDomainIdRequestHttpsLevel]

        robots : typing.Optional[PostDomainsSettingsDomainIdRequestRobots]

        segment_key : typing.Optional[str]

        link_type : typing.Optional[PostDomainsSettingsDomainIdRequestLinkType]

        cloaking : typing.Optional[bool]
            Enable cloaking for all links on the domain

        hide_referer : typing.Optional[bool]

        hide_visitor_ip : typing.Optional[bool]
            Don't store visitor IPs in our database

        https_links : typing.Optional[bool]
            Set to null to reissue a certificate

        webhook_url : typing.Optional[PostDomainsSettingsDomainIdRequestWebhookUrl]

        integration_ga : typing.Optional[str]

        integration_fb : typing.Optional[str]

        integration_tt : typing.Optional[str]

        integration_adroll : typing.Optional[str]

        enable_conversion_tracking : typing.Optional[bool]

        qr_scan_tracking : typing.Optional[bool]

        integration_gtm : typing.Optional[str]

        client_storage : typing.Optional[typing.Dict[str, typing.Any]]
            For internal use

        purge_expired_links : typing.Optional[bool]
            [DEPRECATED] do not use

        enable_ai : typing.Optional[bool]

        case_sensitive : typing.Optional[bool]
            Enable case sensitivity for short links

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostDomainsSettingsDomainIdResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.domains.update_domain_settings(
            domain_id=1,
        )
        """
        _response = self._raw_client.update_domain_settings(
            domain_id,
            https_level=https_level,
            robots=robots,
            segment_key=segment_key,
            link_type=link_type,
            cloaking=cloaking,
            hide_referer=hide_referer,
            hide_visitor_ip=hide_visitor_ip,
            https_links=https_links,
            webhook_url=webhook_url,
            integration_ga=integration_ga,
            integration_fb=integration_fb,
            integration_tt=integration_tt,
            integration_adroll=integration_adroll,
            enable_conversion_tracking=enable_conversion_tracking,
            qr_scan_tracking=qr_scan_tracking,
            integration_gtm=integration_gtm,
            client_storage=client_storage,
            purge_expired_links=purge_expired_links,
            enable_ai=enable_ai,
            case_sensitive=case_sensitive,
            request_options=request_options,
        )
        return _response.data

    def create_a_domain(
        self,
        *,
        hostname: str,
        hide_referer: typing.Optional[bool] = OMIT,
        link_type: typing.Optional[PostDomainsRequestLinkType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostDomainsResponse:
        """
        Parameters
        ----------
        hostname : str
            Domain hostname

        hide_referer : typing.Optional[bool]

        link_type : typing.Optional[PostDomainsRequestLinkType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostDomainsResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.domains.create_a_domain(
            hostname="😀.link",
        )
        """
        _response = self._raw_client.create_a_domain(
            hostname=hostname, hide_referer=hide_referer, link_type=link_type, request_options=request_options
        )
        return _response.data


class AsyncDomainsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDomainsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDomainsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDomainsClient
        """
        return self._raw_client

    async def list_domains(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        no_team_id: typing.Optional[bool] = None,
        pattern: typing.Optional[str] = None,
        team_id: typing.Optional[float] = None,
        type: typing.Optional[typing.Dict[str, typing.Any]] = None,
        additional_properties: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetApiDomainsResponseItem]:
        """
        Shows all domains of current user

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        no_team_id : typing.Optional[bool]

        pattern : typing.Optional[str]

        team_id : typing.Optional[float]

        type : typing.Optional[typing.Dict[str, typing.Any]]

        additional_properties : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetApiDomainsResponseItem]
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.domains.list_domains()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_domains(
            limit=limit,
            offset=offset,
            no_team_id=no_team_id,
            pattern=pattern,
            team_id=team_id,
            type=type,
            additional_properties=additional_properties,
            request_options=request_options,
        )
        return _response.data

    async def get_domain_details_by_id(
        self, domain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDomainsDomainIdResponse:
        """
        Parameters
        ----------
        domain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDomainsDomainIdResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.domains.get_domain_details_by_id(
                domain_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_domain_details_by_id(domain_id, request_options=request_options)
        return _response.data

    async def update_domain_settings(
        self,
        domain_id: int,
        *,
        https_level: typing.Optional[PostDomainsSettingsDomainIdRequestHttpsLevel] = OMIT,
        robots: typing.Optional[PostDomainsSettingsDomainIdRequestRobots] = OMIT,
        segment_key: typing.Optional[str] = OMIT,
        link_type: typing.Optional[PostDomainsSettingsDomainIdRequestLinkType] = OMIT,
        cloaking: typing.Optional[bool] = OMIT,
        hide_referer: typing.Optional[bool] = OMIT,
        hide_visitor_ip: typing.Optional[bool] = OMIT,
        https_links: typing.Optional[bool] = OMIT,
        webhook_url: typing.Optional[PostDomainsSettingsDomainIdRequestWebhookUrl] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        enable_conversion_tracking: typing.Optional[bool] = OMIT,
        qr_scan_tracking: typing.Optional[bool] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        client_storage: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        purge_expired_links: typing.Optional[bool] = OMIT,
        enable_ai: typing.Optional[bool] = OMIT,
        case_sensitive: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostDomainsSettingsDomainIdResponse:
        """
        Update domain settings

        Parameters
        ----------
        domain_id : int

        https_level : typing.Optional[PostDomainsSettingsDomainIdRequestHttpsLevel]

        robots : typing.Optional[PostDomainsSettingsDomainIdRequestRobots]

        segment_key : typing.Optional[str]

        link_type : typing.Optional[PostDomainsSettingsDomainIdRequestLinkType]

        cloaking : typing.Optional[bool]
            Enable cloaking for all links on the domain

        hide_referer : typing.Optional[bool]

        hide_visitor_ip : typing.Optional[bool]
            Don't store visitor IPs in our database

        https_links : typing.Optional[bool]
            Set to null to reissue a certificate

        webhook_url : typing.Optional[PostDomainsSettingsDomainIdRequestWebhookUrl]

        integration_ga : typing.Optional[str]

        integration_fb : typing.Optional[str]

        integration_tt : typing.Optional[str]

        integration_adroll : typing.Optional[str]

        enable_conversion_tracking : typing.Optional[bool]

        qr_scan_tracking : typing.Optional[bool]

        integration_gtm : typing.Optional[str]

        client_storage : typing.Optional[typing.Dict[str, typing.Any]]
            For internal use

        purge_expired_links : typing.Optional[bool]
            [DEPRECATED] do not use

        enable_ai : typing.Optional[bool]

        case_sensitive : typing.Optional[bool]
            Enable case sensitivity for short links

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostDomainsSettingsDomainIdResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.domains.update_domain_settings(
                domain_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_domain_settings(
            domain_id,
            https_level=https_level,
            robots=robots,
            segment_key=segment_key,
            link_type=link_type,
            cloaking=cloaking,
            hide_referer=hide_referer,
            hide_visitor_ip=hide_visitor_ip,
            https_links=https_links,
            webhook_url=webhook_url,
            integration_ga=integration_ga,
            integration_fb=integration_fb,
            integration_tt=integration_tt,
            integration_adroll=integration_adroll,
            enable_conversion_tracking=enable_conversion_tracking,
            qr_scan_tracking=qr_scan_tracking,
            integration_gtm=integration_gtm,
            client_storage=client_storage,
            purge_expired_links=purge_expired_links,
            enable_ai=enable_ai,
            case_sensitive=case_sensitive,
            request_options=request_options,
        )
        return _response.data

    async def create_a_domain(
        self,
        *,
        hostname: str,
        hide_referer: typing.Optional[bool] = OMIT,
        link_type: typing.Optional[PostDomainsRequestLinkType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostDomainsResponse:
        """
        Parameters
        ----------
        hostname : str
            Domain hostname

        hide_referer : typing.Optional[bool]

        link_type : typing.Optional[PostDomainsRequestLinkType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostDomainsResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.domains.create_a_domain(
                hostname="😀.link",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_domain(
            hostname=hostname, hide_referer=hide_referer, link_type=link_type, request_options=request_options
        )
        return _response.data
