

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.enquiries_response import EnquiriesResponse
from ..types.enquiry_by_id_response import EnquiryByIdResponse
from ..types.enquiry_created_response import EnquiryCreatedResponse
from .raw_client import AsyncRawEnquiriesClient, RawEnquiriesClient
from .types.get_enquiries_request_filter_status import GetEnquiriesRequestFilterStatus
from .types.get_enquiries_request_sort_field import GetEnquiriesRequestSortField
from .types.get_enquiries_request_sort_order import GetEnquiriesRequestSortOrder


OMIT = typing.cast(typing.Any, ...)


class EnquiriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEnquiriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEnquiriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEnquiriesClient
        """
        return self._raw_client

    def get_enquiries(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetEnquiriesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetEnquiriesRequestSortField] = None,
        filter_status: typing.Optional[GetEnquiriesRequestFilterStatus] = None,
        filter_source: typing.Optional[str] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnquiriesResponse:
        """
        Get all enquiries

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetEnquiriesRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetEnquiriesRequestSortField]

        filter_status : typing.Optional[GetEnquiriesRequestFilterStatus]

        filter_source : typing.Optional[str]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `name`
            - `description`
            - `phone`
            - `email`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnquiriesResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.enquiries.get_enquiries()
        """
        _response = self._raw_client.get_enquiries(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_status=filter_status,
            filter_source=filter_source,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    def post_enquiries(
        self,
        *,
        name: str,
        email: str,
        phone_number: str,
        description: str,
        source: str,
        address1: str,
        post_enquiries_request_address_city: str,
        address2: typing.Optional[str] = OMIT,
        address_suburb: typing.Optional[str] = OMIT,
        address_region: typing.Optional[str] = OMIT,
        address_postcode: typing.Optional[str] = OMIT,
        address_country: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnquiryCreatedResponse:
        """
        Create Enquiry

        Parameters
        ----------
        name : str

        email : str

        phone_number : str

        description : str

        source : str

        address1 : str

        post_enquiries_request_address_city : str

        address2 : typing.Optional[str]

        address_suburb : typing.Optional[str]

        address_region : typing.Optional[str]

        address_postcode : typing.Optional[str]

        address_country : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnquiryCreatedResponse
            Resource created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.enquiries.post_enquiries(
            name="name",
            email="email",
            phone_number="phoneNumber",
            description="description",
            source="source",
            address1="address1",
            post_enquiries_request_address_city="addressCity",
        )
        """
        _response = self._raw_client.post_enquiries(
            name=name,
            email=email,
            phone_number=phone_number,
            description=description,
            source=source,
            address1=address1,
            post_enquiries_request_address_city=post_enquiries_request_address_city,
            address2=address2,
            address_suburb=address_suburb,
            address_region=address_region,
            address_postcode=address_postcode,
            address_country=address_country,
            request_options=request_options,
        )
        return _response.data

    def get_enquiries_enquiry_id(
        self, enquiry_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnquiryByIdResponse:
        """
        Returns enquiry by ID.

        Parameters
        ----------
        enquiry_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnquiryByIdResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.enquiries.get_enquiries_enquiry_id(
            enquiry_id=1.1,
        )
        """
        _response = self._raw_client.get_enquiries_enquiry_id(enquiry_id, request_options=request_options)
        return _response.data


class AsyncEnquiriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEnquiriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEnquiriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEnquiriesClient
        """
        return self._raw_client

    async def get_enquiries(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetEnquiriesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetEnquiriesRequestSortField] = None,
        filter_status: typing.Optional[GetEnquiriesRequestFilterStatus] = None,
        filter_source: typing.Optional[str] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnquiriesResponse:
        """
        Get all enquiries

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetEnquiriesRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetEnquiriesRequestSortField]

        filter_status : typing.Optional[GetEnquiriesRequestFilterStatus]

        filter_source : typing.Optional[str]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `name`
            - `description`
            - `phone`
            - `email`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnquiriesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.enquiries.get_enquiries()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_enquiries(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_status=filter_status,
            filter_source=filter_source,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    async def post_enquiries(
        self,
        *,
        name: str,
        email: str,
        phone_number: str,
        description: str,
        source: str,
        address1: str,
        post_enquiries_request_address_city: str,
        address2: typing.Optional[str] = OMIT,
        address_suburb: typing.Optional[str] = OMIT,
        address_region: typing.Optional[str] = OMIT,
        address_postcode: typing.Optional[str] = OMIT,
        address_country: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnquiryCreatedResponse:
        """
        Create Enquiry

        Parameters
        ----------
        name : str

        email : str

        phone_number : str

        description : str

        source : str

        address1 : str

        post_enquiries_request_address_city : str

        address2 : typing.Optional[str]

        address_suburb : typing.Optional[str]

        address_region : typing.Optional[str]

        address_postcode : typing.Optional[str]

        address_country : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnquiryCreatedResponse
            Resource created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.enquiries.post_enquiries(
                name="name",
                email="email",
                phone_number="phoneNumber",
                description="description",
                source="source",
                address1="address1",
                post_enquiries_request_address_city="addressCity",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_enquiries(
            name=name,
            email=email,
            phone_number=phone_number,
            description=description,
            source=source,
            address1=address1,
            post_enquiries_request_address_city=post_enquiries_request_address_city,
            address2=address2,
            address_suburb=address_suburb,
            address_region=address_region,
            address_postcode=address_postcode,
            address_country=address_country,
            request_options=request_options,
        )
        return _response.data

    async def get_enquiries_enquiry_id(
        self, enquiry_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnquiryByIdResponse:
        """
        Returns enquiry by ID.

        Parameters
        ----------
        enquiry_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnquiryByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.enquiries.get_enquiries_enquiry_id(
                enquiry_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_enquiries_enquiry_id(enquiry_id, request_options=request_options)
        return _response.data
