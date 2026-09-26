

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address_payload import AddressPayload
from ..types.person_payload import PersonPayload
from ..types.site_by_id_response import SiteByIdResponse
from ..types.sites_response import SitesResponse
from .raw_client import AsyncRawSitesClient, RawSitesClient
from .types.get_sites_request_sort_field import GetSitesRequestSortField
from .types.get_sites_request_sort_order import GetSitesRequestSortOrder


OMIT = typing.cast(typing.Any, ...)


class SitesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSitesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSitesClient
        """
        return self._raw_client

    def get_sites(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetSitesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_site_name: typing.Optional[str] = None,
        filter_address_city: typing.Optional[str] = None,
        filter_address_postal_code: typing.Optional[str] = None,
        sort_field: typing.Optional[GetSitesRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SitesResponse:
        """
        Returns a list of sites. The list can be filtered by site name, address city, and address postal code.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetSitesRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_site_name : typing.Optional[str]

        filter_address_city : typing.Optional[str]

        filter_address_postal_code : typing.Optional[str]

        sort_field : typing.Optional[GetSitesRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `name`
            - `defaultContact.firstName`
            - `defaultContact.lastName`
            - `customer.customerFullName`
            - `billingContact.firstName`
            - `billingContact.lastName`
            - `physicalAddress.address1`
            - `physicalAddress.address2`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SitesResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.get_sites()
        """
        _response = self._raw_client.get_sites(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            filter_site_name=filter_site_name,
            filter_address_city=filter_address_city,
            filter_address_postal_code=filter_address_postal_code,
            sort_field=sort_field,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    def post_sites(
        self,
        *,
        default_contact: PersonPayload,
        site_address: AddressPayload,
        name: typing.Optional[str] = OMIT,
        billing_contact: typing.Optional[PersonPayload] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SiteByIdResponse:
        """
        Create a new site

        Parameters
        ----------
        default_contact : PersonPayload

        site_address : AddressPayload

        name : typing.Optional[str]

        billing_contact : typing.Optional[PersonPayload]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiteByIdResponse
            Resource created successfully

        Examples
        --------
        from fern import AddressPayload, FernApi, PersonPayload

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.post_sites(
            default_contact=PersonPayload(
                first_name="firstName",
            ),
            site_address=AddressPayload(
                address1="address1",
            ),
        )
        """
        _response = self._raw_client.post_sites(
            default_contact=default_contact,
            site_address=site_address,
            name=name,
            billing_contact=billing_contact,
            postal_address=postal_address,
            request_options=request_options,
        )
        return _response.data

    def get_sites_site_id(
        self, site_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SiteByIdResponse:
        """
        Returns a site by ID.

        Parameters
        ----------
        site_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiteByIdResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.get_sites_site_id(
            site_id=1.1,
        )
        """
        _response = self._raw_client.get_sites_site_id(site_id, request_options=request_options)
        return _response.data

    def patch_sites_site_id(
        self,
        site_id: str,
        *,
        site_address: AddressPayload,
        name: typing.Optional[str] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SiteByIdResponse:
        """
        Update site

        Parameters
        ----------
        site_id : str

        site_address : AddressPayload

        name : typing.Optional[str]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiteByIdResponse
            Successful Response

        Examples
        --------
        from fern import AddressPayload, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.patch_sites_site_id(
            site_id="siteId",
            site_address=AddressPayload(
                address1="address1",
            ),
        )
        """
        _response = self._raw_client.patch_sites_site_id(
            site_id,
            site_address=site_address,
            name=name,
            postal_address=postal_address,
            request_options=request_options,
        )
        return _response.data

    def post_sites_site_id_archive(
        self, site_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Archive Site.

        Parameters
        ----------
        site_id : float

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
        client.sites.post_sites_site_id_archive(
            site_id=1.1,
        )
        """
        _response = self._raw_client.post_sites_site_id_archive(site_id, request_options=request_options)
        return _response.data

    def post_sites_site_id_restore(
        self, site_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SiteByIdResponse:
        """
        Restore Site.

        Parameters
        ----------
        site_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiteByIdResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.post_sites_site_id_restore(
            site_id=1.1,
        )
        """
        _response = self._raw_client.post_sites_site_id_restore(site_id, request_options=request_options)
        return _response.data


class AsyncSitesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSitesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSitesClient
        """
        return self._raw_client

    async def get_sites(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetSitesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_site_name: typing.Optional[str] = None,
        filter_address_city: typing.Optional[str] = None,
        filter_address_postal_code: typing.Optional[str] = None,
        sort_field: typing.Optional[GetSitesRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SitesResponse:
        """
        Returns a list of sites. The list can be filtered by site name, address city, and address postal code.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetSitesRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_site_name : typing.Optional[str]

        filter_address_city : typing.Optional[str]

        filter_address_postal_code : typing.Optional[str]

        sort_field : typing.Optional[GetSitesRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `name`
            - `defaultContact.firstName`
            - `defaultContact.lastName`
            - `customer.customerFullName`
            - `billingContact.firstName`
            - `billingContact.lastName`
            - `physicalAddress.address1`
            - `physicalAddress.address2`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SitesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.get_sites()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sites(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            filter_site_name=filter_site_name,
            filter_address_city=filter_address_city,
            filter_address_postal_code=filter_address_postal_code,
            sort_field=sort_field,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    async def post_sites(
        self,
        *,
        default_contact: PersonPayload,
        site_address: AddressPayload,
        name: typing.Optional[str] = OMIT,
        billing_contact: typing.Optional[PersonPayload] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SiteByIdResponse:
        """
        Create a new site

        Parameters
        ----------
        default_contact : PersonPayload

        site_address : AddressPayload

        name : typing.Optional[str]

        billing_contact : typing.Optional[PersonPayload]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiteByIdResponse
            Resource created successfully

        Examples
        --------
        import asyncio

        from fern import AddressPayload, AsyncFernApi, PersonPayload

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.post_sites(
                default_contact=PersonPayload(
                    first_name="firstName",
                ),
                site_address=AddressPayload(
                    address1="address1",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_sites(
            default_contact=default_contact,
            site_address=site_address,
            name=name,
            billing_contact=billing_contact,
            postal_address=postal_address,
            request_options=request_options,
        )
        return _response.data

    async def get_sites_site_id(
        self, site_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SiteByIdResponse:
        """
        Returns a site by ID.

        Parameters
        ----------
        site_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiteByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.get_sites_site_id(
                site_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sites_site_id(site_id, request_options=request_options)
        return _response.data

    async def patch_sites_site_id(
        self,
        site_id: str,
        *,
        site_address: AddressPayload,
        name: typing.Optional[str] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SiteByIdResponse:
        """
        Update site

        Parameters
        ----------
        site_id : str

        site_address : AddressPayload

        name : typing.Optional[str]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiteByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AddressPayload, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.patch_sites_site_id(
                site_id="siteId",
                site_address=AddressPayload(
                    address1="address1",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_sites_site_id(
            site_id,
            site_address=site_address,
            name=name,
            postal_address=postal_address,
            request_options=request_options,
        )
        return _response.data

    async def post_sites_site_id_archive(
        self, site_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Archive Site.

        Parameters
        ----------
        site_id : float

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
            await client.sites.post_sites_site_id_archive(
                site_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_sites_site_id_archive(site_id, request_options=request_options)
        return _response.data

    async def post_sites_site_id_restore(
        self, site_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SiteByIdResponse:
        """
        Restore Site.

        Parameters
        ----------
        site_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SiteByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.post_sites_site_id_restore(
                site_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_sites_site_id_restore(site_id, request_options=request_options)
        return _response.data
