

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unauthorized_error import UnauthorizedError
from ..types.delivery_partners_response import DeliveryPartnersResponse
from ..types.delivery_partners_sorting_options import DeliveryPartnersSortingOptions
from ..types.list_delivery_partners_filter import ListDeliveryPartnersFilter
from ..types.pagination_filter import PaginationFilter
from ..types.unauthorised_response import UnauthorisedResponse
from pydantic import ValidationError


class RawDeliveryPartnersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_multiple_delivery_partners(
        self,
        *,
        filter: typing.Optional[ListDeliveryPartnersFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        sort: typing.Optional[DeliveryPartnersSortingOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeliveryPartnersResponse]:
        """
        Parameters
        ----------
        filter : typing.Optional[ListDeliveryPartnersFilter]

        page : typing.Optional[PaginationFilter]

        sort : typing.Optional[DeliveryPartnersSortingOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeliveryPartnersResponse]
            A list of Delivery Partners
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v3/delivery-partners",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ListDeliveryPartnersFilter, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(
                    object_=page, annotation=PaginationFilter, direction="write"
                ),
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeliveryPartnersResponse,
                    parse_obj_as(
                        type_=DeliveryPartnersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDeliveryPartnersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_multiple_delivery_partners(
        self,
        *,
        filter: typing.Optional[ListDeliveryPartnersFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        sort: typing.Optional[DeliveryPartnersSortingOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeliveryPartnersResponse]:
        """
        Parameters
        ----------
        filter : typing.Optional[ListDeliveryPartnersFilter]

        page : typing.Optional[PaginationFilter]

        sort : typing.Optional[DeliveryPartnersSortingOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeliveryPartnersResponse]
            A list of Delivery Partners
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v3/delivery-partners",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ListDeliveryPartnersFilter, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(
                    object_=page, annotation=PaginationFilter, direction="write"
                ),
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeliveryPartnersResponse,
                    parse_obj_as(
                        type_=DeliveryPartnersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
