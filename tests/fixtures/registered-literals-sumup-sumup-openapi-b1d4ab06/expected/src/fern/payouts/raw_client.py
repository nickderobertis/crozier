

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.financial_payouts import FinancialPayouts
from .types.list_payouts_v1request_format import ListPayoutsV1RequestFormat
from .types.list_payouts_v1request_order import ListPayoutsV1RequestOrder
from pydantic import ValidationError


class RawPayoutsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_payouts_v1(
        self,
        merchant_code: str,
        *,
        start_date: dt.date,
        end_date: dt.date,
        format: typing.Optional[ListPayoutsV1RequestFormat] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListPayoutsV1RequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FinancialPayouts]:
        """
        Lists payout and payout-deduction records for the specified merchant account within the requested date range.

        The response can include:
        - regular payouts (`type = PAYOUT`)
        - deduction records for refunds, chargebacks, direct debit returns, or balance adjustments

        Results are sorted by payout date in the requested `order`.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        start_date : dt.date
            Start date of the payout period filter, inclusive, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) `date` format (`YYYY-MM-DD`).

        end_date : dt.date
            End date of the payout period filter, inclusive, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) `date` format (`YYYY-MM-DD`). Must be greater than or equal to `start_date`.

        format : typing.Optional[ListPayoutsV1RequestFormat]
            Response format for the payout list.

        limit : typing.Optional[int]
            Maximum number of payout records to return.

        order : typing.Optional[ListPayoutsV1RequestOrder]
            Sort direction for the returned payouts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FinancialPayouts]
            Returns the list of payout and deduction records for the requested period.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1.0/merchants/{encode_path_param(merchant_code)}/payouts",
            method="GET",
            params={
                "start_date": str(start_date),
                "end_date": str(end_date),
                "format": format,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FinancialPayouts,
                    parse_obj_as(
                        type_=FinancialPayouts,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawPayoutsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_payouts_v1(
        self,
        merchant_code: str,
        *,
        start_date: dt.date,
        end_date: dt.date,
        format: typing.Optional[ListPayoutsV1RequestFormat] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListPayoutsV1RequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FinancialPayouts]:
        """
        Lists payout and payout-deduction records for the specified merchant account within the requested date range.

        The response can include:
        - regular payouts (`type = PAYOUT`)
        - deduction records for refunds, chargebacks, direct debit returns, or balance adjustments

        Results are sorted by payout date in the requested `order`.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        start_date : dt.date
            Start date of the payout period filter, inclusive, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) `date` format (`YYYY-MM-DD`).

        end_date : dt.date
            End date of the payout period filter, inclusive, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) `date` format (`YYYY-MM-DD`). Must be greater than or equal to `start_date`.

        format : typing.Optional[ListPayoutsV1RequestFormat]
            Response format for the payout list.

        limit : typing.Optional[int]
            Maximum number of payout records to return.

        order : typing.Optional[ListPayoutsV1RequestOrder]
            Sort direction for the returned payouts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FinancialPayouts]
            Returns the list of payout and deduction records for the requested period.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1.0/merchants/{encode_path_param(merchant_code)}/payouts",
            method="GET",
            params={
                "start_date": str(start_date),
                "end_date": str(end_date),
                "format": format,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FinancialPayouts,
                    parse_obj_as(
                        type_=FinancialPayouts,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
