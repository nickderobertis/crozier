

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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.entry_mode import EntryMode
from ..types.payment_type import PaymentType
from ..types.transaction_full import TransactionFull
from .types.list_transactions_v21request_order import ListTransactionsV21RequestOrder
from .types.list_transactions_v21request_statuses_item import ListTransactionsV21RequestStatusesItem
from .types.list_transactions_v21request_types_item import ListTransactionsV21RequestTypesItem
from .types.list_transactions_v21response import ListTransactionsV21Response
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def refund_transaction(
        self,
        merchant_code: str,
        transaction_id: str,
        *,
        amount: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Refunds an identified transaction either in full or partially.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        transaction_id : str
            Unique identifier of the transaction.

        amount : typing.Optional[float]
            Amount to be refunded. Eligible amount can't exceed the amount of the transaction and varies based on country and currency. If you do not specify a value, the system performs a full refund of the transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            The transaction was refunded in full or partially based on the request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1.0/merchants/{encode_path_param(merchant_code)}/payments/{encode_path_param(transaction_id)}/refunds",
            method="POST",
            json={
                "amount": amount,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_transaction_v21(
        self,
        merchant_code: str,
        *,
        id: typing.Optional[str] = None,
        transaction_code: typing.Optional[str] = None,
        foreign_transaction_id: typing.Optional[str] = None,
        client_transaction_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TransactionFull]:
        """
        Retrieves the full details of an identified transaction. The transaction resource is identified by a query parameter and *one* of following parameters is required:
        - `id`
        - `transaction_code`
        - `foreign_transaction_id`
        - `client_transaction_id`

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        id : typing.Optional[str]
            Retrieves the transaction resource with the specified transaction ID (the `id` parameter in the transaction resource).

        transaction_code : typing.Optional[str]
            Retrieves the transaction resource with the specified transaction code.

        foreign_transaction_id : typing.Optional[str]
            External transaction identifier supplied by the client.

        client_transaction_id : typing.Optional[str]
            Client-supplied identifier of the transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TransactionFull]
            Returns the requested transaction resource.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2.1/merchants/{encode_path_param(merchant_code)}/transactions",
            method="GET",
            params={
                "id": id,
                "transaction_code": transaction_code,
                "foreign_transaction_id": foreign_transaction_id,
                "client_transaction_id": client_transaction_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TransactionFull,
                    parse_obj_as(
                        type_=TransactionFull,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def list_transactions_v21(
        self,
        merchant_code: str,
        *,
        transaction_code: typing.Optional[str] = None,
        order: typing.Optional[ListTransactionsV21RequestOrder] = None,
        limit: typing.Optional[int] = None,
        users: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        statuses: typing.Optional[
            typing.Union[
                ListTransactionsV21RequestStatusesItem, typing.Sequence[ListTransactionsV21RequestStatusesItem]
            ]
        ] = None,
        payment_types: typing.Optional[typing.Union[PaymentType, typing.Sequence[PaymentType]]] = None,
        entry_modes: typing.Optional[typing.Union[EntryMode, typing.Sequence[EntryMode]]] = None,
        types: typing.Optional[
            typing.Union[ListTransactionsV21RequestTypesItem, typing.Sequence[ListTransactionsV21RequestTypesItem]]
        ] = None,
        changes_since: typing.Optional[dt.datetime] = None,
        newest_time: typing.Optional[dt.datetime] = None,
        newest_ref: typing.Optional[str] = None,
        oldest_time: typing.Optional[dt.datetime] = None,
        oldest_ref: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListTransactionsV21Response]:
        """
        Lists detailed history of all transactions associated with the merchant profile.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        transaction_code : typing.Optional[str]
            Retrieves the transaction resource with the specified transaction code.

        order : typing.Optional[ListTransactionsV21RequestOrder]
            Specifies the order in which the returned results are displayed.

        limit : typing.Optional[int]
            Specifies the maximum number of results per page. Value must be a positive integer and if not specified, will return 10 results.

        users : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filters the returned results by user email.

        statuses : typing.Optional[typing.Union[ListTransactionsV21RequestStatusesItem, typing.Sequence[ListTransactionsV21RequestStatusesItem]]]
            Filters the returned results by the specified list of final statuses of the transactions.

        payment_types : typing.Optional[typing.Union[PaymentType, typing.Sequence[PaymentType]]]
            Filters the returned results by the specified list of payment types used for the transactions.

        entry_modes : typing.Optional[typing.Union[EntryMode, typing.Sequence[EntryMode]]]
            Filters the returned results by the specified list of entry modes.

        types : typing.Optional[typing.Union[ListTransactionsV21RequestTypesItem, typing.Sequence[ListTransactionsV21RequestTypesItem]]]
            Filters the returned results by the specified list of transaction types.

        changes_since : typing.Optional[dt.datetime]
            Filters the results by the latest modification time of resources and returns only transactions that are modified *at or after* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).

        newest_time : typing.Optional[dt.datetime]
            Filters the results by the creation time of resources and returns only transactions that are created *before* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).

        newest_ref : typing.Optional[str]
            Filters the results by the reference ID of transaction events and returns only transactions with events whose IDs are *smaller* than the specified value. This parameters supersedes the `newest_time` parameter (if both are provided in the request).

        oldest_time : typing.Optional[dt.datetime]
            Filters the results by the creation time of resources and returns only transactions that are created *at or after* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).

        oldest_ref : typing.Optional[str]
            Filters the results by the reference ID of transaction events and returns only transactions with events whose IDs are *greater* than the specified value. This parameters supersedes the `oldest_time` parameter (if both are provided in the request).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListTransactionsV21Response]
            Returns a page of transaction history items.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2.1/merchants/{encode_path_param(merchant_code)}/transactions/history",
            method="GET",
            params={
                "transaction_code": transaction_code,
                "order": order,
                "limit": limit,
                "users[]": users,
                "statuses[]": statuses,
                "payment_types[]": payment_types,
                "entry_modes[]": entry_modes,
                "types[]": types,
                "changes_since": serialize_datetime(changes_since) if changes_since is not None else None,
                "newest_time": serialize_datetime(newest_time) if newest_time is not None else None,
                "newest_ref": newest_ref,
                "oldest_time": serialize_datetime(oldest_time) if oldest_time is not None else None,
                "oldest_ref": oldest_ref,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTransactionsV21Response,
                    parse_obj_as(
                        type_=ListTransactionsV21Response,
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


class AsyncRawTransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def refund_transaction(
        self,
        merchant_code: str,
        transaction_id: str,
        *,
        amount: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Refunds an identified transaction either in full or partially.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        transaction_id : str
            Unique identifier of the transaction.

        amount : typing.Optional[float]
            Amount to be refunded. Eligible amount can't exceed the amount of the transaction and varies based on country and currency. If you do not specify a value, the system performs a full refund of the transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            The transaction was refunded in full or partially based on the request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1.0/merchants/{encode_path_param(merchant_code)}/payments/{encode_path_param(transaction_id)}/refunds",
            method="POST",
            json={
                "amount": amount,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_transaction_v21(
        self,
        merchant_code: str,
        *,
        id: typing.Optional[str] = None,
        transaction_code: typing.Optional[str] = None,
        foreign_transaction_id: typing.Optional[str] = None,
        client_transaction_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TransactionFull]:
        """
        Retrieves the full details of an identified transaction. The transaction resource is identified by a query parameter and *one* of following parameters is required:
        - `id`
        - `transaction_code`
        - `foreign_transaction_id`
        - `client_transaction_id`

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        id : typing.Optional[str]
            Retrieves the transaction resource with the specified transaction ID (the `id` parameter in the transaction resource).

        transaction_code : typing.Optional[str]
            Retrieves the transaction resource with the specified transaction code.

        foreign_transaction_id : typing.Optional[str]
            External transaction identifier supplied by the client.

        client_transaction_id : typing.Optional[str]
            Client-supplied identifier of the transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TransactionFull]
            Returns the requested transaction resource.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2.1/merchants/{encode_path_param(merchant_code)}/transactions",
            method="GET",
            params={
                "id": id,
                "transaction_code": transaction_code,
                "foreign_transaction_id": foreign_transaction_id,
                "client_transaction_id": client_transaction_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TransactionFull,
                    parse_obj_as(
                        type_=TransactionFull,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def list_transactions_v21(
        self,
        merchant_code: str,
        *,
        transaction_code: typing.Optional[str] = None,
        order: typing.Optional[ListTransactionsV21RequestOrder] = None,
        limit: typing.Optional[int] = None,
        users: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        statuses: typing.Optional[
            typing.Union[
                ListTransactionsV21RequestStatusesItem, typing.Sequence[ListTransactionsV21RequestStatusesItem]
            ]
        ] = None,
        payment_types: typing.Optional[typing.Union[PaymentType, typing.Sequence[PaymentType]]] = None,
        entry_modes: typing.Optional[typing.Union[EntryMode, typing.Sequence[EntryMode]]] = None,
        types: typing.Optional[
            typing.Union[ListTransactionsV21RequestTypesItem, typing.Sequence[ListTransactionsV21RequestTypesItem]]
        ] = None,
        changes_since: typing.Optional[dt.datetime] = None,
        newest_time: typing.Optional[dt.datetime] = None,
        newest_ref: typing.Optional[str] = None,
        oldest_time: typing.Optional[dt.datetime] = None,
        oldest_ref: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListTransactionsV21Response]:
        """
        Lists detailed history of all transactions associated with the merchant profile.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        transaction_code : typing.Optional[str]
            Retrieves the transaction resource with the specified transaction code.

        order : typing.Optional[ListTransactionsV21RequestOrder]
            Specifies the order in which the returned results are displayed.

        limit : typing.Optional[int]
            Specifies the maximum number of results per page. Value must be a positive integer and if not specified, will return 10 results.

        users : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filters the returned results by user email.

        statuses : typing.Optional[typing.Union[ListTransactionsV21RequestStatusesItem, typing.Sequence[ListTransactionsV21RequestStatusesItem]]]
            Filters the returned results by the specified list of final statuses of the transactions.

        payment_types : typing.Optional[typing.Union[PaymentType, typing.Sequence[PaymentType]]]
            Filters the returned results by the specified list of payment types used for the transactions.

        entry_modes : typing.Optional[typing.Union[EntryMode, typing.Sequence[EntryMode]]]
            Filters the returned results by the specified list of entry modes.

        types : typing.Optional[typing.Union[ListTransactionsV21RequestTypesItem, typing.Sequence[ListTransactionsV21RequestTypesItem]]]
            Filters the returned results by the specified list of transaction types.

        changes_since : typing.Optional[dt.datetime]
            Filters the results by the latest modification time of resources and returns only transactions that are modified *at or after* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).

        newest_time : typing.Optional[dt.datetime]
            Filters the results by the creation time of resources and returns only transactions that are created *before* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).

        newest_ref : typing.Optional[str]
            Filters the results by the reference ID of transaction events and returns only transactions with events whose IDs are *smaller* than the specified value. This parameters supersedes the `newest_time` parameter (if both are provided in the request).

        oldest_time : typing.Optional[dt.datetime]
            Filters the results by the creation time of resources and returns only transactions that are created *at or after* the specified timestamp (in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format).

        oldest_ref : typing.Optional[str]
            Filters the results by the reference ID of transaction events and returns only transactions with events whose IDs are *greater* than the specified value. This parameters supersedes the `oldest_time` parameter (if both are provided in the request).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListTransactionsV21Response]
            Returns a page of transaction history items.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2.1/merchants/{encode_path_param(merchant_code)}/transactions/history",
            method="GET",
            params={
                "transaction_code": transaction_code,
                "order": order,
                "limit": limit,
                "users[]": users,
                "statuses[]": statuses,
                "payment_types[]": payment_types,
                "entry_modes[]": entry_modes,
                "types[]": types,
                "changes_since": serialize_datetime(changes_since) if changes_since is not None else None,
                "newest_time": serialize_datetime(newest_time) if newest_time is not None else None,
                "newest_ref": newest_ref,
                "oldest_time": serialize_datetime(oldest_time) if oldest_time is not None else None,
                "oldest_ref": oldest_ref,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListTransactionsV21Response,
                    parse_obj_as(
                        type_=ListTransactionsV21Response,
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
