

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_links_tweetbot_request_url_only import GetLinksTweetbotRequestUrlOnly
from .raw_client import AsyncRawLinkManagementClient, RawLinkManagementClient
from .types.delete_links_delete_bulk_response import DeleteLinksDeleteBulkResponse
from .types.delete_links_link_id_response import DeleteLinksLinkIdResponse
from .types.delete_links_permissions_domain_id_link_id_user_id_response import (
    DeleteLinksPermissionsDomainIdLinkIdUserIdResponse,
)
from .types.get_links_permissions_domain_id_link_id_response_item import GetLinksPermissionsDomainIdLinkIdResponseItem
from .types.post_links_archive_bulk_response import PostLinksArchiveBulkResponse
from .types.post_links_archive_response import PostLinksArchiveResponse
from .types.post_links_bulk_request_links_item import PostLinksBulkRequestLinksItem
from .types.post_links_duplicate_link_id_response import PostLinksDuplicateLinkIdResponse
from .types.post_links_examples_response import PostLinksExamplesResponse
from .types.post_links_link_id_request_created_at import PostLinksLinkIdRequestCreatedAt
from .types.post_links_link_id_request_expires_at import PostLinksLinkIdRequestExpiresAt
from .types.post_links_link_id_request_split_urlv2item import PostLinksLinkIdRequestSplitUrlv2Item
from .types.post_links_link_id_request_ttl import PostLinksLinkIdRequestTtl
from .types.post_links_link_id_response import PostLinksLinkIdResponse
from .types.post_links_permissions_domain_id_link_id_user_id_response import (
    PostLinksPermissionsDomainIdLinkIdUserIdResponse,
)
from .types.post_links_public_request_created_at import PostLinksPublicRequestCreatedAt
from .types.post_links_public_request_expires_at import PostLinksPublicRequestExpiresAt
from .types.post_links_public_request_split_urlv2item import PostLinksPublicRequestSplitUrlv2Item
from .types.post_links_public_request_ttl import PostLinksPublicRequestTtl
from .types.post_links_public_response import PostLinksPublicResponse
from .types.post_links_qr_bulk_request_type import PostLinksQrBulkRequestType
from .types.post_links_qr_link_id_string_request_type import PostLinksQrLinkIdStringRequestType
from .types.post_links_request_created_at import PostLinksRequestCreatedAt
from .types.post_links_request_expires_at import PostLinksRequestExpiresAt
from .types.post_links_request_split_urlv2item import PostLinksRequestSplitUrlv2Item
from .types.post_links_request_ttl import PostLinksRequestTtl
from .types.post_links_response import PostLinksResponse
from .types.post_links_unarchive_bulk_response import PostLinksUnarchiveBulkResponse
from .types.post_links_unarchive_response import PostLinksUnarchiveResponse


OMIT = typing.cast(typing.Any, ...)


class LinkManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLinkManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLinkManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLinkManagementClient
        """
        return self._raw_client

    def set_link_opengraph_properties(
        self,
        domain_id: float,
        link_id: str,
        *,
        request: typing.Sequence[typing.Sequence[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        domain_id : float

        link_id : str

        request : typing.Sequence[typing.Sequence[typing.Any]]

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
        client.link_management.set_link_opengraph_properties(
            domain_id=1.1,
            link_id="linkId",
            request=[[], []],
        )
        """
        _response = self._raw_client.set_link_opengraph_properties(
            domain_id, link_id, request=request, request_options=request_options
        )
        return _response.data

    def get_link_permissions(
        self, domain_id: str, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetLinksPermissionsDomainIdLinkIdResponseItem]:
        """
        Parameters
        ----------
        domain_id : str

        link_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetLinksPermissionsDomainIdLinkIdResponseItem]
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.get_link_permissions(
            domain_id="domainId",
            link_id="linkId",
        )
        """
        _response = self._raw_client.get_link_permissions(domain_id, link_id, request_options=request_options)
        return _response.data

    def add_link_permission(
        self, domain_id: str, link_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostLinksPermissionsDomainIdLinkIdUserIdResponse:
        """
        Parameters
        ----------
        domain_id : str

        link_id : str
            Link ID

        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksPermissionsDomainIdLinkIdUserIdResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.add_link_permission(
            domain_id="domainId",
            link_id="lnk_abc123_abcdef",
            user_id="userId",
        )
        """
        _response = self._raw_client.add_link_permission(domain_id, link_id, user_id, request_options=request_options)
        return _response.data

    def delete_link_permissions(
        self, domain_id: int, link_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteLinksPermissionsDomainIdLinkIdUserIdResponse:
        """
        Parameters
        ----------
        domain_id : int

        link_id : str

        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteLinksPermissionsDomainIdLinkIdUserIdResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.delete_link_permissions(
            domain_id=1,
            link_id="linkId",
            user_id="userId",
        )
        """
        _response = self._raw_client.delete_link_permissions(
            domain_id, link_id, user_id, request_options=request_options
        )
        return _response.data

    def generate_qr_code_for_the_link(
        self,
        link_id_string: str,
        *,
        use_domain_settings: bool,
        accept: typing.Optional[str] = None,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        size: typing.Optional[float] = OMIT,
        type: typing.Optional[PostLinksQrLinkIdStringRequestType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id_string : str
            Link ID

        use_domain_settings : bool

        accept : typing.Optional[str]

        color : typing.Optional[str]

        background_color : typing.Optional[str]

        size : typing.Optional[float]

        type : typing.Optional[PostLinksQrLinkIdStringRequestType]

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
        client.link_management.generate_qr_code_for_the_link(
            link_id_string="lnk_abc123_abcdef",
            use_domain_settings=True,
        )
        """
        _response = self._raw_client.generate_qr_code_for_the_link(
            link_id_string,
            use_domain_settings=use_domain_settings,
            accept=accept,
            color=color,
            background_color=background_color,
            size=size,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def generate_qr_codes_for_the_link_in_bulk(
        self,
        *,
        type: PostLinksQrBulkRequestType,
        use_domain_settings: bool,
        link_ids: typing.Sequence[str],
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        size: typing.Optional[float] = OMIT,
        no_excavate: typing.Optional[bool] = OMIT,
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Generate QR codes for the link in bulk. Rate limit - 1 request per minute

        Parameters
        ----------
        type : PostLinksQrBulkRequestType

        use_domain_settings : bool

        link_ids : typing.Sequence[str]

        color : typing.Optional[str]

        background_color : typing.Optional[str]

        size : typing.Optional[float]

        no_excavate : typing.Optional[bool]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            ZIP file containing QR codes

        Examples
        --------
        from fern.link_management import PostLinksQrBulkRequestType

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.generate_qr_codes_for_the_link_in_bulk(
            type=PostLinksQrBulkRequestType.PNG,
            use_domain_settings=True,
            link_ids=["linkIds"],
        )
        """
        _response = self._raw_client.generate_qr_codes_for_the_link_in_bulk(
            type=type,
            use_domain_settings=use_domain_settings,
            link_ids=link_ids,
            color=color,
            background_color=background_color,
            size=size,
            no_excavate=no_excavate,
            domain_id=domain_id,
            request_options=request_options,
        )
        return _response.data

    def delete_link(
        self, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteLinksLinkIdResponse:
        """
        Delete link by id

        **Rate limit**: 20/s

        Parameters
        ----------
        link_id : str
            Link ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteLinksLinkIdResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.delete_link(
            link_id="lnk_abc123_abcdef",
        )
        """
        _response = self._raw_client.delete_link(link_id, request_options=request_options)
        return _response.data

    def delete_links_in_bulk(
        self, *, link_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteLinksDeleteBulkResponse:
        """
        Delete links in bulk by ids

        **Rate limit**: 1/s

        Parameters
        ----------
        link_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteLinksDeleteBulkResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.delete_links_in_bulk(
            link_ids=["lnk_abc123_abcdef"],
        )
        """
        _response = self._raw_client.delete_links_in_bulk(link_ids=link_ids, request_options=request_options)
        return _response.data

    def archive_link(
        self,
        *,
        link_id: str,
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksArchiveResponse:
        """
        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksArchiveResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.archive_link(
            link_id="link_id",
        )
        """
        _response = self._raw_client.archive_link(link_id=link_id, domain_id=domain_id, request_options=request_options)
        return _response.data

    def archive_links_in_bulk(
        self,
        *,
        link_ids: typing.Sequence[str],
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksArchiveBulkResponse:
        """
        Parameters
        ----------
        link_ids : typing.Sequence[str]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksArchiveBulkResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.archive_links_in_bulk(
            link_ids=["link_ids"],
        )
        """
        _response = self._raw_client.archive_links_in_bulk(
            link_ids=link_ids, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    def unarchive_link(
        self,
        *,
        link_id: str,
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksUnarchiveResponse:
        """
        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksUnarchiveResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.unarchive_link(
            link_id="link_id",
        )
        """
        _response = self._raw_client.unarchive_link(
            link_id=link_id, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    def unarchive_links_in_bulk(
        self,
        *,
        link_ids: typing.Sequence[str],
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksUnarchiveBulkResponse:
        """
        Parameters
        ----------
        link_ids : typing.Sequence[str]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksUnarchiveBulkResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.unarchive_links_in_bulk(
            link_ids=["link_ids"],
        )
        """
        _response = self._raw_client.unarchive_links_in_bulk(
            link_ids=link_ids, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    def update_existing_url(
        self,
        link_id: str,
        *,
        domain_id: typing.Optional[str] = None,
        cloaking: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[PostLinksLinkIdRequestExpiresAt] = OMIT,
        expired_url: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        ttl: typing.Optional[PostLinksLinkIdRequestTtl] = OMIT,
        path: typing.Optional[str] = OMIT,
        android_url: typing.Optional[str] = OMIT,
        iphone_url: typing.Optional[str] = OMIT,
        created_at: typing.Optional[PostLinksLinkIdRequestCreatedAt] = OMIT,
        clicks_limit: typing.Optional[int] = OMIT,
        password_contact: typing.Optional[bool] = OMIT,
        skip_qs: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        split_url: typing.Optional[str] = OMIT,
        split_percent: typing.Optional[int] = OMIT,
        split_urlv2: typing.Optional[typing.Sequence[PostLinksLinkIdRequestSplitUrlv2Item]] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        original_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksLinkIdResponse:
        """
        Update original url, title or path for existing URL by id

        **Rate limit**: 20/s

        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        cloaking : typing.Optional[bool]
            Cloaking

        password : typing.Optional[str]
            Link password

        redirect_type : typing.Optional[int]
            HTTP code for redirect

        expires_at : typing.Optional[PostLinksLinkIdRequestExpiresAt]
            Link expiration date in milliseconds or ISO string

        expired_url : typing.Optional[str]
            Expired URL

        title : typing.Optional[str]
            Link title

        tags : typing.Optional[typing.Sequence[str]]
            Array of link tags

        utm_source : typing.Optional[str]
            set utm_source parameter to destination link

        utm_medium : typing.Optional[str]
            set utm_medium parameter to destination link

        utm_campaign : typing.Optional[str]
            set utm_campaign parameter to destination link

        utm_term : typing.Optional[str]
            set utm_term parameter to destination link

        utm_content : typing.Optional[str]
            set utm_content parameter to destination link

        ttl : typing.Optional[PostLinksLinkIdRequestTtl]
            Time to live in milliseconds or ISO string

        path : typing.Optional[str]
            Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.

        android_url : typing.Optional[str]
            Android URL

        iphone_url : typing.Optional[str]
            iPhone URL

        created_at : typing.Optional[PostLinksLinkIdRequestCreatedAt]
            Link creation date in milliseconds

        clicks_limit : typing.Optional[int]
            disable link after specified number of clicks

        password_contact : typing.Optional[bool]
            Provide your email to users to get a password

        skip_qs : typing.Optional[bool]
            Skip query string merging

        archived : typing.Optional[bool]
            Link is archived

        split_url : typing.Optional[str]
            Split URL

        split_percent : typing.Optional[int]
            Split URL percentage

        split_urlv2 : typing.Optional[typing.Sequence[PostLinksLinkIdRequestSplitUrlv2Item]]
            Split URL configurations for multi-way A/B testing

        integration_adroll : typing.Optional[str]
            Adroll integration

        integration_fb : typing.Optional[str]
            Facebook integration

        integration_tt : typing.Optional[str]
            TikTok integration

        integration_ga : typing.Optional[str]
            Google Analytics integration

        integration_gtm : typing.Optional[str]
            Google Tag Manager integration

        original_url : typing.Optional[str]
            Original URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksLinkIdResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.update_existing_url(
            link_id="linkId",
        )
        """
        _response = self._raw_client.update_existing_url(
            link_id,
            domain_id=domain_id,
            cloaking=cloaking,
            password=password,
            redirect_type=redirect_type,
            expires_at=expires_at,
            expired_url=expired_url,
            title=title,
            tags=tags,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            ttl=ttl,
            path=path,
            android_url=android_url,
            iphone_url=iphone_url,
            created_at=created_at,
            clicks_limit=clicks_limit,
            password_contact=password_contact,
            skip_qs=skip_qs,
            archived=archived,
            split_url=split_url,
            split_percent=split_percent,
            split_urlv2=split_urlv2,
            integration_adroll=integration_adroll,
            integration_fb=integration_fb,
            integration_tt=integration_tt,
            integration_ga=integration_ga,
            integration_gtm=integration_gtm,
            original_url=original_url,
            request_options=request_options,
        )
        return _response.data

    def create_a_new_link(
        self,
        *,
        original_url: str,
        domain: str,
        cloaking: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[PostLinksRequestExpiresAt] = OMIT,
        expired_url: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        ttl: typing.Optional[PostLinksRequestTtl] = OMIT,
        path: typing.Optional[str] = OMIT,
        android_url: typing.Optional[str] = OMIT,
        iphone_url: typing.Optional[str] = OMIT,
        created_at: typing.Optional[PostLinksRequestCreatedAt] = OMIT,
        clicks_limit: typing.Optional[int] = OMIT,
        password_contact: typing.Optional[bool] = OMIT,
        post_links_request_skip_qs: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        split_url: typing.Optional[str] = OMIT,
        split_percent: typing.Optional[int] = OMIT,
        split_urlv2: typing.Optional[typing.Sequence[PostLinksRequestSplitUrlv2Item]] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        allow_duplicates: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksResponse:
        """
        This method creates a new link. If parameter "path" is omitted, it
        generates path by algorithm, chosen in domain settings.

        Notes:

        1. If URL with a given path already exists and originalURL of the URL in database is equal to originalURL argument, it returns information about existing URL
        2. If URL with a given path already exists and originalURL is different from originalURL in database, it returns error with a status `409`
        3. If URL with a given originalURL exists, and no path is given, it returns information about existing URL and does not create anything
        4. If URL with a given originalURL exists, and custom path is given, it creates a new short URL

        **Rate limit**: 50/s

        Parameters
        ----------
        original_url : str
            Original URL

        domain : str
            Domain hostname

        cloaking : typing.Optional[bool]
            Cloaking

        password : typing.Optional[str]
            Link password

        redirect_type : typing.Optional[int]
            HTTP code for redirect

        expires_at : typing.Optional[PostLinksRequestExpiresAt]
            Link expiration date in milliseconds or ISO string

        expired_url : typing.Optional[str]
            Expired URL

        title : typing.Optional[str]
            Link title

        tags : typing.Optional[typing.Sequence[str]]
            Array of link tags

        utm_source : typing.Optional[str]
            set utm_source parameter to destination link

        utm_medium : typing.Optional[str]
            set utm_medium parameter to destination link

        utm_campaign : typing.Optional[str]
            set utm_campaign parameter to destination link

        utm_term : typing.Optional[str]
            set utm_term parameter to destination link

        utm_content : typing.Optional[str]
            set utm_content parameter to destination link

        ttl : typing.Optional[PostLinksRequestTtl]
            Time to live in milliseconds or ISO string

        path : typing.Optional[str]
            Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.

        android_url : typing.Optional[str]
            Android URL

        iphone_url : typing.Optional[str]
            iPhone URL

        created_at : typing.Optional[PostLinksRequestCreatedAt]
            Link creation date in milliseconds

        clicks_limit : typing.Optional[int]
            disable link after specified number of clicks

        password_contact : typing.Optional[bool]
            Provide your email to users to get a password

        post_links_request_skip_qs : typing.Optional[bool]
            Skip query string merging

        archived : typing.Optional[bool]
            Link is archived

        split_url : typing.Optional[str]
            Split URL

        split_percent : typing.Optional[int]
            Split URL percentage

        split_urlv2 : typing.Optional[typing.Sequence[PostLinksRequestSplitUrlv2Item]]
            Split URL configurations for multi-way A/B testing

        integration_adroll : typing.Optional[str]
            Adroll integration

        integration_fb : typing.Optional[str]
            Facebook integration

        integration_tt : typing.Optional[str]
            TikTok integration

        integration_ga : typing.Optional[str]
            Google Analytics integration

        integration_gtm : typing.Optional[str]
            Google Tag Manager integration

        allow_duplicates : typing.Optional[bool]
            Allow duplicates

        folder_id : typing.Optional[str]
            Folder ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.create_a_new_link(
            original_url="https://example.com",
            domain="domain",
        )
        """
        _response = self._raw_client.create_a_new_link(
            original_url=original_url,
            domain=domain,
            cloaking=cloaking,
            password=password,
            redirect_type=redirect_type,
            expires_at=expires_at,
            expired_url=expired_url,
            title=title,
            tags=tags,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            ttl=ttl,
            path=path,
            android_url=android_url,
            iphone_url=iphone_url,
            created_at=created_at,
            clicks_limit=clicks_limit,
            password_contact=password_contact,
            post_links_request_skip_qs=post_links_request_skip_qs,
            archived=archived,
            split_url=split_url,
            split_percent=split_percent,
            split_urlv2=split_urlv2,
            integration_adroll=integration_adroll,
            integration_fb=integration_fb,
            integration_tt=integration_tt,
            integration_ga=integration_ga,
            integration_gtm=integration_gtm,
            allow_duplicates=allow_duplicates,
            folder_id=folder_id,
            request_options=request_options,
        )
        return _response.data

    def create_a_new_link_simple_version(
        self,
        *,
        domain: str,
        original_url: str,
        api_key: str,
        path: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        url_only: typing.Optional[GetLinksTweetbotRequestUrlOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """

                            Simple version of link create endpoint. You can use it if you can not use POST method
                            **Rate limit**: 50/s


        Parameters
        ----------
        domain : str
            Domain hostname

        original_url : str
            Link original URL

        api_key : str
            API key

        path : typing.Optional[str]
            Link path

        title : typing.Optional[str]
            Link title

        url_only : typing.Optional[GetLinksTweetbotRequestUrlOnly]

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
        client.link_management.create_a_new_link_simple_version(
            domain="domain",
            original_url="originalURL",
            api_key="apiKey",
        )
        """
        _response = self._raw_client.create_a_new_link_simple_version(
            domain=domain,
            original_url=original_url,
            api_key=api_key,
            path=path,
            title=title,
            url_only=url_only,
            request_options=request_options,
        )
        return _response.data

    def create_a_new_link_using_public_api_key(
        self,
        *,
        original_url: str,
        domain: str,
        type: typing.Optional[typing.Dict[str, typing.Any]] = None,
        additional_properties: typing.Optional[str] = None,
        cloaking: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[PostLinksPublicRequestExpiresAt] = OMIT,
        expired_url: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        ttl: typing.Optional[PostLinksPublicRequestTtl] = OMIT,
        path: typing.Optional[str] = OMIT,
        android_url: typing.Optional[str] = OMIT,
        iphone_url: typing.Optional[str] = OMIT,
        created_at: typing.Optional[PostLinksPublicRequestCreatedAt] = OMIT,
        clicks_limit: typing.Optional[int] = OMIT,
        password_contact: typing.Optional[bool] = OMIT,
        skip_qs: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        split_url: typing.Optional[str] = OMIT,
        split_percent: typing.Optional[int] = OMIT,
        split_urlv2: typing.Optional[typing.Sequence[PostLinksPublicRequestSplitUrlv2Item]] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksPublicResponse:
        """
        This method creates a new link. Only this method should be used in client-side applications

        If parameter "path" is omitted, it generates path by algorithm, chosen in domain settings.

        You can use it with public API key in your frontend applications (client-side javascript, Android & iPhone apps)
        **Rate limit**: 50/s

        Parameters
        ----------
        original_url : str
            Original URL

        domain : str

        type : typing.Optional[typing.Dict[str, typing.Any]]

        additional_properties : typing.Optional[str]

        cloaking : typing.Optional[bool]
            Cloaking

        password : typing.Optional[str]
            Link password

        redirect_type : typing.Optional[int]
            HTTP code for redirect

        expires_at : typing.Optional[PostLinksPublicRequestExpiresAt]
            Link expiration date in milliseconds or ISO string

        expired_url : typing.Optional[str]
            Expired URL

        title : typing.Optional[str]
            Link title

        tags : typing.Optional[typing.Sequence[str]]
            Array of link tags

        utm_source : typing.Optional[str]
            set utm_source parameter to destination link

        utm_medium : typing.Optional[str]
            set utm_medium parameter to destination link

        utm_campaign : typing.Optional[str]
            set utm_campaign parameter to destination link

        utm_term : typing.Optional[str]
            set utm_term parameter to destination link

        utm_content : typing.Optional[str]
            set utm_content parameter to destination link

        ttl : typing.Optional[PostLinksPublicRequestTtl]
            Time to live in milliseconds or ISO string

        path : typing.Optional[str]
            Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.

        android_url : typing.Optional[str]
            Android URL

        iphone_url : typing.Optional[str]
            iPhone URL

        created_at : typing.Optional[PostLinksPublicRequestCreatedAt]
            Link creation date in milliseconds

        clicks_limit : typing.Optional[int]
            disable link after specified number of clicks

        password_contact : typing.Optional[bool]
            Provide your email to users to get a password

        skip_qs : typing.Optional[bool]
            Skip query string merging

        archived : typing.Optional[bool]
            Link is archived

        split_url : typing.Optional[str]
            Split URL

        split_percent : typing.Optional[int]
            Split URL percentage

        split_urlv2 : typing.Optional[typing.Sequence[PostLinksPublicRequestSplitUrlv2Item]]
            Split URL configurations for multi-way A/B testing

        integration_adroll : typing.Optional[str]
            Adroll integration

        integration_fb : typing.Optional[str]
            Facebook integration

        integration_tt : typing.Optional[str]
            TikTok integration

        integration_ga : typing.Optional[str]
            Google Analytics integration

        integration_gtm : typing.Optional[str]
            Google Tag Manager integration

        folder_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksPublicResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.create_a_new_link_using_public_api_key(
            original_url="https://example.com",
            domain="domain",
        )
        """
        _response = self._raw_client.create_a_new_link_using_public_api_key(
            original_url=original_url,
            domain=domain,
            type=type,
            additional_properties=additional_properties,
            cloaking=cloaking,
            password=password,
            redirect_type=redirect_type,
            expires_at=expires_at,
            expired_url=expired_url,
            title=title,
            tags=tags,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            ttl=ttl,
            path=path,
            android_url=android_url,
            iphone_url=iphone_url,
            created_at=created_at,
            clicks_limit=clicks_limit,
            password_contact=password_contact,
            skip_qs=skip_qs,
            archived=archived,
            split_url=split_url,
            split_percent=split_percent,
            split_urlv2=split_urlv2,
            integration_adroll=integration_adroll,
            integration_fb=integration_fb,
            integration_tt=integration_tt,
            integration_ga=integration_ga,
            integration_gtm=integration_gtm,
            folder_id=folder_id,
            request_options=request_options,
        )
        return _response.data

    def create_up_to1000links_in_one_call(
        self,
        *,
        domain: str,
        links: typing.Sequence[PostLinksBulkRequestLinksItem],
        allow_duplicates: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Please use this method if you need to create big packs of links. It
        accepts up to 1000 links in one API call.

        It works almost the same as single link creation endpoint, but accepts
        an array of URLs and returns an array of responses.

        Returns list of Link objects. If any URL is failed to insert, it returns
        error object instead as array element. Method is not transactional – it
        can insert some links from the list and return an error for others.

        **Rate limit**: 5 queries in 10 seconds

        Parameters
        ----------
        domain : str

        links : typing.Sequence[PostLinksBulkRequestLinksItem]

        allow_duplicates : typing.Optional[bool]

        folder_id : typing.Optional[str]
            Folder ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.link_management import PostLinksBulkRequestLinksItem

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.create_up_to1000links_in_one_call(
            domain="domain",
            links=[
                PostLinksBulkRequestLinksItem(
                    original_url="https://example.com",
                )
            ],
        )
        """
        _response = self._raw_client.create_up_to1000links_in_one_call(
            domain=domain,
            links=links,
            allow_duplicates=allow_duplicates,
            folder_id=folder_id,
            request_options=request_options,
        )
        return _response.data

    def generate_example_links_for_a_domain(
        self, *, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostLinksExamplesResponse:
        """
        Creates a set of demo/example links to showcase various features of the short link service.

        Example links include:
        - A/B testing with split URLs
        - Mobile targeting (different URLs for Android/iPhone)
        - Expiring links with time limits
        - File download links
        - Password-protected links

        **Rate limit**: 5/10s

        Parameters
        ----------
        domain : str
            Domain hostname to create examples for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksExamplesResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.generate_example_links_for_a_domain(
            domain="domain",
        )
        """
        _response = self._raw_client.generate_example_links_for_a_domain(domain=domain, request_options=request_options)
        return _response.data

    def duplicate_an_existing_link(
        self,
        link_id: str,
        *,
        path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksDuplicateLinkIdResponse:
        """
        Duplicates an existing link with all its properties, targeting rules, and settings.
        The duplicated link will have a new random path (or custom if provided) and be fully independent.

        **Rate limit**: 50/s

        Parameters
        ----------
        link_id : str

        path : typing.Optional[str]
            Custom path for duplicated link

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksDuplicateLinkIdResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_management.duplicate_an_existing_link(
            link_id="linkId",
        )
        """
        _response = self._raw_client.duplicate_an_existing_link(link_id, path=path, request_options=request_options)
        return _response.data

    def append_a_single_tag_to_the_links_in_bulk(
        self, *, tag: str, link_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tag : str

        link_ids : typing.Sequence[str]

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
        client.link_management.append_a_single_tag_to_the_links_in_bulk(
            tag="tag",
            link_ids=["lnk_abc123_abcdef"],
        )
        """
        _response = self._raw_client.append_a_single_tag_to_the_links_in_bulk(
            tag=tag, link_ids=link_ids, request_options=request_options
        )
        return _response.data


class AsyncLinkManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLinkManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLinkManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLinkManagementClient
        """
        return self._raw_client

    async def set_link_opengraph_properties(
        self,
        domain_id: float,
        link_id: str,
        *,
        request: typing.Sequence[typing.Sequence[typing.Any]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        domain_id : float

        link_id : str

        request : typing.Sequence[typing.Sequence[typing.Any]]

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
            await client.link_management.set_link_opengraph_properties(
                domain_id=1.1,
                link_id="linkId",
                request=[[], []],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_link_opengraph_properties(
            domain_id, link_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_link_permissions(
        self, domain_id: str, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetLinksPermissionsDomainIdLinkIdResponseItem]:
        """
        Parameters
        ----------
        domain_id : str

        link_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetLinksPermissionsDomainIdLinkIdResponseItem]
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.get_link_permissions(
                domain_id="domainId",
                link_id="linkId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_link_permissions(domain_id, link_id, request_options=request_options)
        return _response.data

    async def add_link_permission(
        self, domain_id: str, link_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostLinksPermissionsDomainIdLinkIdUserIdResponse:
        """
        Parameters
        ----------
        domain_id : str

        link_id : str
            Link ID

        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksPermissionsDomainIdLinkIdUserIdResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.add_link_permission(
                domain_id="domainId",
                link_id="lnk_abc123_abcdef",
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_link_permission(
            domain_id, link_id, user_id, request_options=request_options
        )
        return _response.data

    async def delete_link_permissions(
        self, domain_id: int, link_id: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteLinksPermissionsDomainIdLinkIdUserIdResponse:
        """
        Parameters
        ----------
        domain_id : int

        link_id : str

        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteLinksPermissionsDomainIdLinkIdUserIdResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.delete_link_permissions(
                domain_id=1,
                link_id="linkId",
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_link_permissions(
            domain_id, link_id, user_id, request_options=request_options
        )
        return _response.data

    async def generate_qr_code_for_the_link(
        self,
        link_id_string: str,
        *,
        use_domain_settings: bool,
        accept: typing.Optional[str] = None,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        size: typing.Optional[float] = OMIT,
        type: typing.Optional[PostLinksQrLinkIdStringRequestType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id_string : str
            Link ID

        use_domain_settings : bool

        accept : typing.Optional[str]

        color : typing.Optional[str]

        background_color : typing.Optional[str]

        size : typing.Optional[float]

        type : typing.Optional[PostLinksQrLinkIdStringRequestType]

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
            await client.link_management.generate_qr_code_for_the_link(
                link_id_string="lnk_abc123_abcdef",
                use_domain_settings=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_qr_code_for_the_link(
            link_id_string,
            use_domain_settings=use_domain_settings,
            accept=accept,
            color=color,
            background_color=background_color,
            size=size,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def generate_qr_codes_for_the_link_in_bulk(
        self,
        *,
        type: PostLinksQrBulkRequestType,
        use_domain_settings: bool,
        link_ids: typing.Sequence[str],
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        size: typing.Optional[float] = OMIT,
        no_excavate: typing.Optional[bool] = OMIT,
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Generate QR codes for the link in bulk. Rate limit - 1 request per minute

        Parameters
        ----------
        type : PostLinksQrBulkRequestType

        use_domain_settings : bool

        link_ids : typing.Sequence[str]

        color : typing.Optional[str]

        background_color : typing.Optional[str]

        size : typing.Optional[float]

        no_excavate : typing.Optional[bool]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            ZIP file containing QR codes

        Examples
        --------
        import asyncio

        from fern.link_management import PostLinksQrBulkRequestType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.generate_qr_codes_for_the_link_in_bulk(
                type=PostLinksQrBulkRequestType.PNG,
                use_domain_settings=True,
                link_ids=["linkIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_qr_codes_for_the_link_in_bulk(
            type=type,
            use_domain_settings=use_domain_settings,
            link_ids=link_ids,
            color=color,
            background_color=background_color,
            size=size,
            no_excavate=no_excavate,
            domain_id=domain_id,
            request_options=request_options,
        )
        return _response.data

    async def delete_link(
        self, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteLinksLinkIdResponse:
        """
        Delete link by id

        **Rate limit**: 20/s

        Parameters
        ----------
        link_id : str
            Link ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteLinksLinkIdResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.delete_link(
                link_id="lnk_abc123_abcdef",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_link(link_id, request_options=request_options)
        return _response.data

    async def delete_links_in_bulk(
        self, *, link_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteLinksDeleteBulkResponse:
        """
        Delete links in bulk by ids

        **Rate limit**: 1/s

        Parameters
        ----------
        link_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteLinksDeleteBulkResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.delete_links_in_bulk(
                link_ids=["lnk_abc123_abcdef"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_links_in_bulk(link_ids=link_ids, request_options=request_options)
        return _response.data

    async def archive_link(
        self,
        *,
        link_id: str,
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksArchiveResponse:
        """
        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksArchiveResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.archive_link(
                link_id="link_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.archive_link(
            link_id=link_id, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    async def archive_links_in_bulk(
        self,
        *,
        link_ids: typing.Sequence[str],
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksArchiveBulkResponse:
        """
        Parameters
        ----------
        link_ids : typing.Sequence[str]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksArchiveBulkResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.archive_links_in_bulk(
                link_ids=["link_ids"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.archive_links_in_bulk(
            link_ids=link_ids, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    async def unarchive_link(
        self,
        *,
        link_id: str,
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksUnarchiveResponse:
        """
        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksUnarchiveResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.unarchive_link(
                link_id="link_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unarchive_link(
            link_id=link_id, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    async def unarchive_links_in_bulk(
        self,
        *,
        link_ids: typing.Sequence[str],
        domain_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksUnarchiveBulkResponse:
        """
        Parameters
        ----------
        link_ids : typing.Sequence[str]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksUnarchiveBulkResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.unarchive_links_in_bulk(
                link_ids=["link_ids"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unarchive_links_in_bulk(
            link_ids=link_ids, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    async def update_existing_url(
        self,
        link_id: str,
        *,
        domain_id: typing.Optional[str] = None,
        cloaking: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[PostLinksLinkIdRequestExpiresAt] = OMIT,
        expired_url: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        ttl: typing.Optional[PostLinksLinkIdRequestTtl] = OMIT,
        path: typing.Optional[str] = OMIT,
        android_url: typing.Optional[str] = OMIT,
        iphone_url: typing.Optional[str] = OMIT,
        created_at: typing.Optional[PostLinksLinkIdRequestCreatedAt] = OMIT,
        clicks_limit: typing.Optional[int] = OMIT,
        password_contact: typing.Optional[bool] = OMIT,
        skip_qs: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        split_url: typing.Optional[str] = OMIT,
        split_percent: typing.Optional[int] = OMIT,
        split_urlv2: typing.Optional[typing.Sequence[PostLinksLinkIdRequestSplitUrlv2Item]] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        original_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksLinkIdResponse:
        """
        Update original url, title or path for existing URL by id

        **Rate limit**: 20/s

        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        cloaking : typing.Optional[bool]
            Cloaking

        password : typing.Optional[str]
            Link password

        redirect_type : typing.Optional[int]
            HTTP code for redirect

        expires_at : typing.Optional[PostLinksLinkIdRequestExpiresAt]
            Link expiration date in milliseconds or ISO string

        expired_url : typing.Optional[str]
            Expired URL

        title : typing.Optional[str]
            Link title

        tags : typing.Optional[typing.Sequence[str]]
            Array of link tags

        utm_source : typing.Optional[str]
            set utm_source parameter to destination link

        utm_medium : typing.Optional[str]
            set utm_medium parameter to destination link

        utm_campaign : typing.Optional[str]
            set utm_campaign parameter to destination link

        utm_term : typing.Optional[str]
            set utm_term parameter to destination link

        utm_content : typing.Optional[str]
            set utm_content parameter to destination link

        ttl : typing.Optional[PostLinksLinkIdRequestTtl]
            Time to live in milliseconds or ISO string

        path : typing.Optional[str]
            Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.

        android_url : typing.Optional[str]
            Android URL

        iphone_url : typing.Optional[str]
            iPhone URL

        created_at : typing.Optional[PostLinksLinkIdRequestCreatedAt]
            Link creation date in milliseconds

        clicks_limit : typing.Optional[int]
            disable link after specified number of clicks

        password_contact : typing.Optional[bool]
            Provide your email to users to get a password

        skip_qs : typing.Optional[bool]
            Skip query string merging

        archived : typing.Optional[bool]
            Link is archived

        split_url : typing.Optional[str]
            Split URL

        split_percent : typing.Optional[int]
            Split URL percentage

        split_urlv2 : typing.Optional[typing.Sequence[PostLinksLinkIdRequestSplitUrlv2Item]]
            Split URL configurations for multi-way A/B testing

        integration_adroll : typing.Optional[str]
            Adroll integration

        integration_fb : typing.Optional[str]
            Facebook integration

        integration_tt : typing.Optional[str]
            TikTok integration

        integration_ga : typing.Optional[str]
            Google Analytics integration

        integration_gtm : typing.Optional[str]
            Google Tag Manager integration

        original_url : typing.Optional[str]
            Original URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksLinkIdResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.update_existing_url(
                link_id="linkId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_existing_url(
            link_id,
            domain_id=domain_id,
            cloaking=cloaking,
            password=password,
            redirect_type=redirect_type,
            expires_at=expires_at,
            expired_url=expired_url,
            title=title,
            tags=tags,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            ttl=ttl,
            path=path,
            android_url=android_url,
            iphone_url=iphone_url,
            created_at=created_at,
            clicks_limit=clicks_limit,
            password_contact=password_contact,
            skip_qs=skip_qs,
            archived=archived,
            split_url=split_url,
            split_percent=split_percent,
            split_urlv2=split_urlv2,
            integration_adroll=integration_adroll,
            integration_fb=integration_fb,
            integration_tt=integration_tt,
            integration_ga=integration_ga,
            integration_gtm=integration_gtm,
            original_url=original_url,
            request_options=request_options,
        )
        return _response.data

    async def create_a_new_link(
        self,
        *,
        original_url: str,
        domain: str,
        cloaking: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[PostLinksRequestExpiresAt] = OMIT,
        expired_url: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        ttl: typing.Optional[PostLinksRequestTtl] = OMIT,
        path: typing.Optional[str] = OMIT,
        android_url: typing.Optional[str] = OMIT,
        iphone_url: typing.Optional[str] = OMIT,
        created_at: typing.Optional[PostLinksRequestCreatedAt] = OMIT,
        clicks_limit: typing.Optional[int] = OMIT,
        password_contact: typing.Optional[bool] = OMIT,
        post_links_request_skip_qs: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        split_url: typing.Optional[str] = OMIT,
        split_percent: typing.Optional[int] = OMIT,
        split_urlv2: typing.Optional[typing.Sequence[PostLinksRequestSplitUrlv2Item]] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        allow_duplicates: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksResponse:
        """
        This method creates a new link. If parameter "path" is omitted, it
        generates path by algorithm, chosen in domain settings.

        Notes:

        1. If URL with a given path already exists and originalURL of the URL in database is equal to originalURL argument, it returns information about existing URL
        2. If URL with a given path already exists and originalURL is different from originalURL in database, it returns error with a status `409`
        3. If URL with a given originalURL exists, and no path is given, it returns information about existing URL and does not create anything
        4. If URL with a given originalURL exists, and custom path is given, it creates a new short URL

        **Rate limit**: 50/s

        Parameters
        ----------
        original_url : str
            Original URL

        domain : str
            Domain hostname

        cloaking : typing.Optional[bool]
            Cloaking

        password : typing.Optional[str]
            Link password

        redirect_type : typing.Optional[int]
            HTTP code for redirect

        expires_at : typing.Optional[PostLinksRequestExpiresAt]
            Link expiration date in milliseconds or ISO string

        expired_url : typing.Optional[str]
            Expired URL

        title : typing.Optional[str]
            Link title

        tags : typing.Optional[typing.Sequence[str]]
            Array of link tags

        utm_source : typing.Optional[str]
            set utm_source parameter to destination link

        utm_medium : typing.Optional[str]
            set utm_medium parameter to destination link

        utm_campaign : typing.Optional[str]
            set utm_campaign parameter to destination link

        utm_term : typing.Optional[str]
            set utm_term parameter to destination link

        utm_content : typing.Optional[str]
            set utm_content parameter to destination link

        ttl : typing.Optional[PostLinksRequestTtl]
            Time to live in milliseconds or ISO string

        path : typing.Optional[str]
            Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.

        android_url : typing.Optional[str]
            Android URL

        iphone_url : typing.Optional[str]
            iPhone URL

        created_at : typing.Optional[PostLinksRequestCreatedAt]
            Link creation date in milliseconds

        clicks_limit : typing.Optional[int]
            disable link after specified number of clicks

        password_contact : typing.Optional[bool]
            Provide your email to users to get a password

        post_links_request_skip_qs : typing.Optional[bool]
            Skip query string merging

        archived : typing.Optional[bool]
            Link is archived

        split_url : typing.Optional[str]
            Split URL

        split_percent : typing.Optional[int]
            Split URL percentage

        split_urlv2 : typing.Optional[typing.Sequence[PostLinksRequestSplitUrlv2Item]]
            Split URL configurations for multi-way A/B testing

        integration_adroll : typing.Optional[str]
            Adroll integration

        integration_fb : typing.Optional[str]
            Facebook integration

        integration_tt : typing.Optional[str]
            TikTok integration

        integration_ga : typing.Optional[str]
            Google Analytics integration

        integration_gtm : typing.Optional[str]
            Google Tag Manager integration

        allow_duplicates : typing.Optional[bool]
            Allow duplicates

        folder_id : typing.Optional[str]
            Folder ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.create_a_new_link(
                original_url="https://example.com",
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_link(
            original_url=original_url,
            domain=domain,
            cloaking=cloaking,
            password=password,
            redirect_type=redirect_type,
            expires_at=expires_at,
            expired_url=expired_url,
            title=title,
            tags=tags,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            ttl=ttl,
            path=path,
            android_url=android_url,
            iphone_url=iphone_url,
            created_at=created_at,
            clicks_limit=clicks_limit,
            password_contact=password_contact,
            post_links_request_skip_qs=post_links_request_skip_qs,
            archived=archived,
            split_url=split_url,
            split_percent=split_percent,
            split_urlv2=split_urlv2,
            integration_adroll=integration_adroll,
            integration_fb=integration_fb,
            integration_tt=integration_tt,
            integration_ga=integration_ga,
            integration_gtm=integration_gtm,
            allow_duplicates=allow_duplicates,
            folder_id=folder_id,
            request_options=request_options,
        )
        return _response.data

    async def create_a_new_link_simple_version(
        self,
        *,
        domain: str,
        original_url: str,
        api_key: str,
        path: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        url_only: typing.Optional[GetLinksTweetbotRequestUrlOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """

                            Simple version of link create endpoint. You can use it if you can not use POST method
                            **Rate limit**: 50/s


        Parameters
        ----------
        domain : str
            Domain hostname

        original_url : str
            Link original URL

        api_key : str
            API key

        path : typing.Optional[str]
            Link path

        title : typing.Optional[str]
            Link title

        url_only : typing.Optional[GetLinksTweetbotRequestUrlOnly]

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
            await client.link_management.create_a_new_link_simple_version(
                domain="domain",
                original_url="originalURL",
                api_key="apiKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_link_simple_version(
            domain=domain,
            original_url=original_url,
            api_key=api_key,
            path=path,
            title=title,
            url_only=url_only,
            request_options=request_options,
        )
        return _response.data

    async def create_a_new_link_using_public_api_key(
        self,
        *,
        original_url: str,
        domain: str,
        type: typing.Optional[typing.Dict[str, typing.Any]] = None,
        additional_properties: typing.Optional[str] = None,
        cloaking: typing.Optional[bool] = OMIT,
        password: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at: typing.Optional[PostLinksPublicRequestExpiresAt] = OMIT,
        expired_url: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        ttl: typing.Optional[PostLinksPublicRequestTtl] = OMIT,
        path: typing.Optional[str] = OMIT,
        android_url: typing.Optional[str] = OMIT,
        iphone_url: typing.Optional[str] = OMIT,
        created_at: typing.Optional[PostLinksPublicRequestCreatedAt] = OMIT,
        clicks_limit: typing.Optional[int] = OMIT,
        password_contact: typing.Optional[bool] = OMIT,
        skip_qs: typing.Optional[bool] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        split_url: typing.Optional[str] = OMIT,
        split_percent: typing.Optional[int] = OMIT,
        split_urlv2: typing.Optional[typing.Sequence[PostLinksPublicRequestSplitUrlv2Item]] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksPublicResponse:
        """
        This method creates a new link. Only this method should be used in client-side applications

        If parameter "path" is omitted, it generates path by algorithm, chosen in domain settings.

        You can use it with public API key in your frontend applications (client-side javascript, Android & iPhone apps)
        **Rate limit**: 50/s

        Parameters
        ----------
        original_url : str
            Original URL

        domain : str

        type : typing.Optional[typing.Dict[str, typing.Any]]

        additional_properties : typing.Optional[str]

        cloaking : typing.Optional[bool]
            Cloaking

        password : typing.Optional[str]
            Link password

        redirect_type : typing.Optional[int]
            HTTP code for redirect

        expires_at : typing.Optional[PostLinksPublicRequestExpiresAt]
            Link expiration date in milliseconds or ISO string

        expired_url : typing.Optional[str]
            Expired URL

        title : typing.Optional[str]
            Link title

        tags : typing.Optional[typing.Sequence[str]]
            Array of link tags

        utm_source : typing.Optional[str]
            set utm_source parameter to destination link

        utm_medium : typing.Optional[str]
            set utm_medium parameter to destination link

        utm_campaign : typing.Optional[str]
            set utm_campaign parameter to destination link

        utm_term : typing.Optional[str]
            set utm_term parameter to destination link

        utm_content : typing.Optional[str]
            set utm_content parameter to destination link

        ttl : typing.Optional[PostLinksPublicRequestTtl]
            Time to live in milliseconds or ISO string

        path : typing.Optional[str]
            Link slug. For case-insensitive domains, the path is normalized to lowercase and the original value is preserved in displayPath.

        android_url : typing.Optional[str]
            Android URL

        iphone_url : typing.Optional[str]
            iPhone URL

        created_at : typing.Optional[PostLinksPublicRequestCreatedAt]
            Link creation date in milliseconds

        clicks_limit : typing.Optional[int]
            disable link after specified number of clicks

        password_contact : typing.Optional[bool]
            Provide your email to users to get a password

        skip_qs : typing.Optional[bool]
            Skip query string merging

        archived : typing.Optional[bool]
            Link is archived

        split_url : typing.Optional[str]
            Split URL

        split_percent : typing.Optional[int]
            Split URL percentage

        split_urlv2 : typing.Optional[typing.Sequence[PostLinksPublicRequestSplitUrlv2Item]]
            Split URL configurations for multi-way A/B testing

        integration_adroll : typing.Optional[str]
            Adroll integration

        integration_fb : typing.Optional[str]
            Facebook integration

        integration_tt : typing.Optional[str]
            TikTok integration

        integration_ga : typing.Optional[str]
            Google Analytics integration

        integration_gtm : typing.Optional[str]
            Google Tag Manager integration

        folder_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksPublicResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.create_a_new_link_using_public_api_key(
                original_url="https://example.com",
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_link_using_public_api_key(
            original_url=original_url,
            domain=domain,
            type=type,
            additional_properties=additional_properties,
            cloaking=cloaking,
            password=password,
            redirect_type=redirect_type,
            expires_at=expires_at,
            expired_url=expired_url,
            title=title,
            tags=tags,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            ttl=ttl,
            path=path,
            android_url=android_url,
            iphone_url=iphone_url,
            created_at=created_at,
            clicks_limit=clicks_limit,
            password_contact=password_contact,
            skip_qs=skip_qs,
            archived=archived,
            split_url=split_url,
            split_percent=split_percent,
            split_urlv2=split_urlv2,
            integration_adroll=integration_adroll,
            integration_fb=integration_fb,
            integration_tt=integration_tt,
            integration_ga=integration_ga,
            integration_gtm=integration_gtm,
            folder_id=folder_id,
            request_options=request_options,
        )
        return _response.data

    async def create_up_to1000links_in_one_call(
        self,
        *,
        domain: str,
        links: typing.Sequence[PostLinksBulkRequestLinksItem],
        allow_duplicates: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Please use this method if you need to create big packs of links. It
        accepts up to 1000 links in one API call.

        It works almost the same as single link creation endpoint, but accepts
        an array of URLs and returns an array of responses.

        Returns list of Link objects. If any URL is failed to insert, it returns
        error object instead as array element. Method is not transactional – it
        can insert some links from the list and return an error for others.

        **Rate limit**: 5 queries in 10 seconds

        Parameters
        ----------
        domain : str

        links : typing.Sequence[PostLinksBulkRequestLinksItem]

        allow_duplicates : typing.Optional[bool]

        folder_id : typing.Optional[str]
            Folder ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.link_management import PostLinksBulkRequestLinksItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.create_up_to1000links_in_one_call(
                domain="domain",
                links=[
                    PostLinksBulkRequestLinksItem(
                        original_url="https://example.com",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_up_to1000links_in_one_call(
            domain=domain,
            links=links,
            allow_duplicates=allow_duplicates,
            folder_id=folder_id,
            request_options=request_options,
        )
        return _response.data

    async def generate_example_links_for_a_domain(
        self, *, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostLinksExamplesResponse:
        """
        Creates a set of demo/example links to showcase various features of the short link service.

        Example links include:
        - A/B testing with split URLs
        - Mobile targeting (different URLs for Android/iPhone)
        - Expiring links with time limits
        - File download links
        - Password-protected links

        **Rate limit**: 5/10s

        Parameters
        ----------
        domain : str
            Domain hostname to create examples for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksExamplesResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.generate_example_links_for_a_domain(
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_example_links_for_a_domain(
            domain=domain, request_options=request_options
        )
        return _response.data

    async def duplicate_an_existing_link(
        self,
        link_id: str,
        *,
        path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinksDuplicateLinkIdResponse:
        """
        Duplicates an existing link with all its properties, targeting rules, and settings.
        The duplicated link will have a new random path (or custom if provided) and be fully independent.

        **Rate limit**: 50/s

        Parameters
        ----------
        link_id : str

        path : typing.Optional[str]
            Custom path for duplicated link

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinksDuplicateLinkIdResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_management.duplicate_an_existing_link(
                link_id="linkId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.duplicate_an_existing_link(
            link_id, path=path, request_options=request_options
        )
        return _response.data

    async def append_a_single_tag_to_the_links_in_bulk(
        self, *, tag: str, link_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tag : str

        link_ids : typing.Sequence[str]

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
            await client.link_management.append_a_single_tag_to_the_links_in_bulk(
                tag="tag",
                link_ids=["lnk_abc123_abcdef"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.append_a_single_tag_to_the_links_in_bulk(
            tag=tag, link_ids=link_ids, request_options=request_options
        )
        return _response.data
