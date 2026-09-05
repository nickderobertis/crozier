

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.page_osparc_credits_aggregated_by_service_get import PageOsparcCreditsAggregatedByServiceGet
from ..types.page_service_run_get import PageServiceRunGet
from ..types.services_aggregated_usages_time_period import ServicesAggregatedUsagesTimePeriod
from ..types.services_aggregated_usages_type import ServicesAggregatedUsagesType
from ..types.wallet_id_int import WalletIdInt
from pydantic import ValidationError


class RawUsageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_resource_usage_services(
        self,
        *,
        order_by: typing.Optional[str] = None,
        wallet_id: typing.Optional[WalletIdInt] = None,
        filters: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageServiceRunGet]:
        """
        Retrieve finished and currently running user services (user and product are taken from context, optionally wallet_id parameter might be provided).

        Parameters
        ----------
        order_by : typing.Optional[str]

        wallet_id : typing.Optional[WalletIdInt]

        filters : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageServiceRunGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/services/-/resource-usages",
            method="GET",
            params={
                "order_by": order_by,
                "wallet_id": wallet_id,
                "filters": filters,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageServiceRunGet,
                    parse_obj_as(
                        type_=PageServiceRunGet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_osparc_credits_aggregated_usages(
        self,
        *,
        aggregated_by: ServicesAggregatedUsagesType,
        time_period: ServicesAggregatedUsagesTimePeriod,
        wallet_id: WalletIdInt,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageOsparcCreditsAggregatedByServiceGet]:
        """
        Used credits based on aggregate by type, currently supported `services`. (user and product are taken from context, optionally wallet_id parameter might be provided).

        Parameters
        ----------
        aggregated_by : ServicesAggregatedUsagesType

        time_period : ServicesAggregatedUsagesTimePeriod

        wallet_id : WalletIdInt

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageOsparcCreditsAggregatedByServiceGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/services/-/aggregated-usages",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "aggregated_by": aggregated_by,
                "time_period": time_period,
                "wallet_id": wallet_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageOsparcCreditsAggregatedByServiceGet,
                    parse_obj_as(
                        type_=PageOsparcCreditsAggregatedByServiceGet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def export_resource_usage_services(
        self,
        *,
        order_by: typing.Optional[str] = None,
        wallet_id: typing.Optional[WalletIdInt] = None,
        filters: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Redirects to download CSV link. CSV obtains finished and currently running user services (user and product are taken from context, optionally wallet_id parameter might be provided).

        Parameters
        ----------
        order_by : typing.Optional[str]

        wallet_id : typing.Optional[WalletIdInt]

        filters : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/services/-/usage-report",
            method="GET",
            params={
                "order_by": order_by,
                "wallet_id": wallet_id,
                "filters": filters,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawUsageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_resource_usage_services(
        self,
        *,
        order_by: typing.Optional[str] = None,
        wallet_id: typing.Optional[WalletIdInt] = None,
        filters: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageServiceRunGet]:
        """
        Retrieve finished and currently running user services (user and product are taken from context, optionally wallet_id parameter might be provided).

        Parameters
        ----------
        order_by : typing.Optional[str]

        wallet_id : typing.Optional[WalletIdInt]

        filters : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageServiceRunGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/services/-/resource-usages",
            method="GET",
            params={
                "order_by": order_by,
                "wallet_id": wallet_id,
                "filters": filters,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageServiceRunGet,
                    parse_obj_as(
                        type_=PageServiceRunGet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_osparc_credits_aggregated_usages(
        self,
        *,
        aggregated_by: ServicesAggregatedUsagesType,
        time_period: ServicesAggregatedUsagesTimePeriod,
        wallet_id: WalletIdInt,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageOsparcCreditsAggregatedByServiceGet]:
        """
        Used credits based on aggregate by type, currently supported `services`. (user and product are taken from context, optionally wallet_id parameter might be provided).

        Parameters
        ----------
        aggregated_by : ServicesAggregatedUsagesType

        time_period : ServicesAggregatedUsagesTimePeriod

        wallet_id : WalletIdInt

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageOsparcCreditsAggregatedByServiceGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/services/-/aggregated-usages",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "aggregated_by": aggregated_by,
                "time_period": time_period,
                "wallet_id": wallet_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageOsparcCreditsAggregatedByServiceGet,
                    parse_obj_as(
                        type_=PageOsparcCreditsAggregatedByServiceGet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def export_resource_usage_services(
        self,
        *,
        order_by: typing.Optional[str] = None,
        wallet_id: typing.Optional[WalletIdInt] = None,
        filters: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Redirects to download CSV link. CSV obtains finished and currently running user services (user and product are taken from context, optionally wallet_id parameter might be provided).

        Parameters
        ----------
        order_by : typing.Optional[str]

        wallet_id : typing.Optional[WalletIdInt]

        filters : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/services/-/usage-report",
            method="GET",
            params={
                "order_by": order_by,
                "wallet_id": wallet_id,
                "filters": filters,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
