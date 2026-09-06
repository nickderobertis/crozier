

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_paged_response_dealer_db_models_voucher_history import ApiPagedResponseDealerDbModelsVoucherHistory
from pydantic import ValidationError


class RawVoucherhistoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getvoucherhistory(
        self,
        *,
        voucher_code: typing.Optional[str] = None,
        changed_before: typing.Optional[dt.datetime] = None,
        changed_after: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseDealerDbModelsVoucherHistory]:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : typing.Optional[str]
            Optional. Filter history data by Voucher Code.

        changed_before : typing.Optional[dt.datetime]
            Optional. Filter history data where changes occured before provided date.

        changed_after : typing.Optional[dt.datetime]
            Optional. Filter history data where changes occured after provided date.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseDealerDbModelsVoucherHistory]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/VoucherHistory",
            method="GET",
            params={
                "VoucherCode": voucher_code,
                "ChangedBefore": serialize_datetime(changed_before) if changed_before is not None else None,
                "ChangedAfter": serialize_datetime(changed_after) if changed_after is not None else None,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseDealerDbModelsVoucherHistory,
                    parse_obj_as(
                        type_=ApiPagedResponseDealerDbModelsVoucherHistory,
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


class AsyncRawVoucherhistoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getvoucherhistory(
        self,
        *,
        voucher_code: typing.Optional[str] = None,
        changed_before: typing.Optional[dt.datetime] = None,
        changed_after: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseDealerDbModelsVoucherHistory]:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : typing.Optional[str]
            Optional. Filter history data by Voucher Code.

        changed_before : typing.Optional[dt.datetime]
            Optional. Filter history data where changes occured before provided date.

        changed_after : typing.Optional[dt.datetime]
            Optional. Filter history data where changes occured after provided date.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseDealerDbModelsVoucherHistory]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/VoucherHistory",
            method="GET",
            params={
                "VoucherCode": voucher_code,
                "ChangedBefore": serialize_datetime(changed_before) if changed_before is not None else None,
                "ChangedAfter": serialize_datetime(changed_after) if changed_after is not None else None,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseDealerDbModelsVoucherHistory,
                    parse_obj_as(
                        type_=ApiPagedResponseDealerDbModelsVoucherHistory,
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
