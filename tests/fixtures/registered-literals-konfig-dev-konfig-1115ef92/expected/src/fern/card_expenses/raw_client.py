

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.expandable_expense import ExpandableExpense
from ..types.expense import Expense
from ..types.expense_payment_status import ExpensePaymentStatus
from ..types.expense_status import ExpenseStatus
from ..types.page_expandable_expense import PageExpandableExpense
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCardExpensesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_expenses(
        self,
        *,
        expand: typing.Optional[typing.Sequence[str]] = None,
        user_id: typing.Optional[typing.Sequence[str]] = None,
        parent_expense_id: typing.Optional[typing.Sequence[str]] = None,
        budget_id: typing.Optional[typing.Sequence[str]] = None,
        status: typing.Optional[typing.Sequence[ExpenseStatus]] = None,
        payment_status: typing.Optional[typing.Sequence[ExpensePaymentStatus]] = None,
        purchased_at_start: typing.Optional[dt.datetime] = None,
        purchased_at_end: typing.Optional[dt.datetime] = None,
        load_custom_fields: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageExpandableExpense]:
        """
        List expenses under the same account. Admin and bookkeeper have access to any expense, and regular users can only access their own.

        Parameters
        ----------
        expand : typing.Optional[typing.Sequence[str]]
            Get additional details for the expense, e.g. merchant mcc code, by passing in `expand[]=merchant`. Query parameters include `location`, `department`, `merchant`, `receipts.download_uris`, `user`, `budget` and `payment`.

        user_id : typing.Optional[typing.Sequence[str]]
            Get expenses belong to provided user(s).

        parent_expense_id : typing.Optional[typing.Sequence[str]]
            Get itemized expenses belong to provided parent expenses ID(s).

        budget_id : typing.Optional[typing.Sequence[str]]

        status : typing.Optional[typing.Sequence[ExpenseStatus]]

        payment_status : typing.Optional[typing.Sequence[ExpensePaymentStatus]]

        purchased_at_start : typing.Optional[dt.datetime]

            Shows only expenses with a `purchased_at` on or after this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), e.g. 2022-11-12T23:59:59.999

        purchased_at_end : typing.Optional[dt.datetime]

            Shows only expenses with a `purchased_at` on or before this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), e.g. 2022-11-12T23:59:59.999

        load_custom_fields : typing.Optional[bool]
            Load custom fields for the expenses.

        cursor : typing.Optional[str]

            The cursor to use for pagination. This is the `next_cursor` value returned from the previous response.

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageExpandableExpense]
            listExpenses 200 response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/expenses/card",
            method="GET",
            params={
                "expand[]": expand,
                "user_id[]": user_id,
                "parent_expense_id[]": parent_expense_id,
                "budget_id[]": budget_id,
                "status[]": status,
                "payment_status[]": payment_status,
                "purchased_at_start": serialize_datetime(purchased_at_start)
                if purchased_at_start is not None
                else None,
                "purchased_at_end": serialize_datetime(purchased_at_end) if purchased_at_end is not None else None,
                "load_custom_fields": load_custom_fields,
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageExpandableExpense,
                    parse_obj_as(
                        type_=PageExpandableExpense,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def get_expense(
        self,
        expense_id: str,
        *,
        expand: typing.Optional[typing.Sequence[str]] = None,
        load_custom_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExpandableExpense]:
        """
        Get an expense by its ID.

        Parameters
        ----------
        expense_id : str

        expand : typing.Optional[typing.Sequence[str]]
            Get additional details for the expense, e.g. merchant mcc code, by passing in `expand[]=merchant`. Query parameters include `location`, `department`, `merchant`, `receipts.download_uris`, `user`, `budget` and `payment`.

        load_custom_fields : typing.Optional[bool]
            Load custom fields for the expense.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExpandableExpense]
            getExpense 200 response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/expenses/card/{encode_path_param(expense_id)}",
            method="GET",
            params={
                "expand[]": expand,
                "load_custom_fields": load_custom_fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExpandableExpense,
                    parse_obj_as(
                        type_=ExpandableExpense,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def update_expense(
        self,
        expense_id: str,
        *,
        memo: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Expense]:
        """
        Update an expense. Admin and bookkeeper have access to any expense, and regular users can only access their own.

        Parameters
        ----------
        expense_id : str

        memo : typing.Optional[str]
            Expense memo.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Expense]
            updateExpense 200 response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/expenses/card/{encode_path_param(expense_id)}",
            method="PUT",
            json={
                "memo": memo,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Expense,
                    parse_obj_as(
                        type_=Expense,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawCardExpensesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_expenses(
        self,
        *,
        expand: typing.Optional[typing.Sequence[str]] = None,
        user_id: typing.Optional[typing.Sequence[str]] = None,
        parent_expense_id: typing.Optional[typing.Sequence[str]] = None,
        budget_id: typing.Optional[typing.Sequence[str]] = None,
        status: typing.Optional[typing.Sequence[ExpenseStatus]] = None,
        payment_status: typing.Optional[typing.Sequence[ExpensePaymentStatus]] = None,
        purchased_at_start: typing.Optional[dt.datetime] = None,
        purchased_at_end: typing.Optional[dt.datetime] = None,
        load_custom_fields: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageExpandableExpense]:
        """
        List expenses under the same account. Admin and bookkeeper have access to any expense, and regular users can only access their own.

        Parameters
        ----------
        expand : typing.Optional[typing.Sequence[str]]
            Get additional details for the expense, e.g. merchant mcc code, by passing in `expand[]=merchant`. Query parameters include `location`, `department`, `merchant`, `receipts.download_uris`, `user`, `budget` and `payment`.

        user_id : typing.Optional[typing.Sequence[str]]
            Get expenses belong to provided user(s).

        parent_expense_id : typing.Optional[typing.Sequence[str]]
            Get itemized expenses belong to provided parent expenses ID(s).

        budget_id : typing.Optional[typing.Sequence[str]]

        status : typing.Optional[typing.Sequence[ExpenseStatus]]

        payment_status : typing.Optional[typing.Sequence[ExpensePaymentStatus]]

        purchased_at_start : typing.Optional[dt.datetime]

            Shows only expenses with a `purchased_at` on or after this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), e.g. 2022-11-12T23:59:59.999

        purchased_at_end : typing.Optional[dt.datetime]

            Shows only expenses with a `purchased_at` on or before this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), e.g. 2022-11-12T23:59:59.999

        load_custom_fields : typing.Optional[bool]
            Load custom fields for the expenses.

        cursor : typing.Optional[str]

            The cursor to use for pagination. This is the `next_cursor` value returned from the previous response.

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageExpandableExpense]
            listExpenses 200 response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/expenses/card",
            method="GET",
            params={
                "expand[]": expand,
                "user_id[]": user_id,
                "parent_expense_id[]": parent_expense_id,
                "budget_id[]": budget_id,
                "status[]": status,
                "payment_status[]": payment_status,
                "purchased_at_start": serialize_datetime(purchased_at_start)
                if purchased_at_start is not None
                else None,
                "purchased_at_end": serialize_datetime(purchased_at_end) if purchased_at_end is not None else None,
                "load_custom_fields": load_custom_fields,
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageExpandableExpense,
                    parse_obj_as(
                        type_=PageExpandableExpense,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def get_expense(
        self,
        expense_id: str,
        *,
        expand: typing.Optional[typing.Sequence[str]] = None,
        load_custom_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExpandableExpense]:
        """
        Get an expense by its ID.

        Parameters
        ----------
        expense_id : str

        expand : typing.Optional[typing.Sequence[str]]
            Get additional details for the expense, e.g. merchant mcc code, by passing in `expand[]=merchant`. Query parameters include `location`, `department`, `merchant`, `receipts.download_uris`, `user`, `budget` and `payment`.

        load_custom_fields : typing.Optional[bool]
            Load custom fields for the expense.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExpandableExpense]
            getExpense 200 response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/expenses/card/{encode_path_param(expense_id)}",
            method="GET",
            params={
                "expand[]": expand,
                "load_custom_fields": load_custom_fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExpandableExpense,
                    parse_obj_as(
                        type_=ExpandableExpense,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def update_expense(
        self,
        expense_id: str,
        *,
        memo: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Expense]:
        """
        Update an expense. Admin and bookkeeper have access to any expense, and regular users can only access their own.

        Parameters
        ----------
        expense_id : str

        memo : typing.Optional[str]
            Expense memo.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Expense]
            updateExpense 200 response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/expenses/card/{encode_path_param(expense_id)}",
            method="PUT",
            json={
                "memo": memo,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Expense,
                    parse_obj_as(
                        type_=Expense,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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
