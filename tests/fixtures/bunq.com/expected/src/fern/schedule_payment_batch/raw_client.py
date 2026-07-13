

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.schedule import Schedule
from ..types.schedule_payment_batch_create import SchedulePaymentBatchCreate
from ..types.schedule_payment_batch_delete import SchedulePaymentBatchDelete
from ..types.schedule_payment_batch_read import SchedulePaymentBatchRead
from ..types.schedule_payment_batch_update import SchedulePaymentBatchUpdate
from ..types.schedule_payment_entry import SchedulePaymentEntry


OMIT = typing.cast(typing.Any, ...)


class RawSchedulePaymentBatchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        payments: typing.Optional[typing.Sequence[SchedulePaymentEntry]] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SchedulePaymentBatchCreate]:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payments : typing.Optional[typing.Sequence[SchedulePaymentEntry]]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchedulePaymentBatchCreate]
            Endpoint for schedule payment batches.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch",
            method="POST",
            json={
                "payments": convert_and_respect_annotation_metadata(
                    object_=payments, annotation=typing.Sequence[SchedulePaymentEntry], direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=Schedule, direction="write"
                ),
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
                    SchedulePaymentBatchCreate,
                    parse_obj_as(
                        type_=SchedulePaymentBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SchedulePaymentBatchRead]:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchedulePaymentBatchRead]
            Endpoint for schedule payment batches.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchedulePaymentBatchRead,
                    parse_obj_as(
                        type_=SchedulePaymentBatchRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        payments: typing.Optional[typing.Sequence[SchedulePaymentEntry]] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SchedulePaymentBatchUpdate]:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        payments : typing.Optional[typing.Sequence[SchedulePaymentEntry]]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchedulePaymentBatchUpdate]
            Endpoint for schedule payment batches.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "payments": convert_and_respect_annotation_metadata(
                    object_=payments, annotation=typing.Sequence[SchedulePaymentEntry], direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=Schedule, direction="write"
                ),
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
                    SchedulePaymentBatchUpdate,
                    parse_obj_as(
                        type_=SchedulePaymentBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SchedulePaymentBatchDelete]:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchedulePaymentBatchDelete]
            Endpoint for schedule payment batches.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchedulePaymentBatchDelete,
                    parse_obj_as(
                        type_=SchedulePaymentBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSchedulePaymentBatchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        payments: typing.Optional[typing.Sequence[SchedulePaymentEntry]] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SchedulePaymentBatchCreate]:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payments : typing.Optional[typing.Sequence[SchedulePaymentEntry]]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchedulePaymentBatchCreate]
            Endpoint for schedule payment batches.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch",
            method="POST",
            json={
                "payments": convert_and_respect_annotation_metadata(
                    object_=payments, annotation=typing.Sequence[SchedulePaymentEntry], direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=Schedule, direction="write"
                ),
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
                    SchedulePaymentBatchCreate,
                    parse_obj_as(
                        type_=SchedulePaymentBatchCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SchedulePaymentBatchRead]:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchedulePaymentBatchRead]
            Endpoint for schedule payment batches.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchedulePaymentBatchRead,
                    parse_obj_as(
                        type_=SchedulePaymentBatchRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        payments: typing.Optional[typing.Sequence[SchedulePaymentEntry]] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SchedulePaymentBatchUpdate]:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        payments : typing.Optional[typing.Sequence[SchedulePaymentEntry]]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchedulePaymentBatchUpdate]
            Endpoint for schedule payment batches.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "payments": convert_and_respect_annotation_metadata(
                    object_=payments, annotation=typing.Sequence[SchedulePaymentEntry], direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=Schedule, direction="write"
                ),
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
                    SchedulePaymentBatchUpdate,
                    parse_obj_as(
                        type_=SchedulePaymentBatchUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_schedule_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SchedulePaymentBatchDelete]:
        """
        Endpoint for schedule payment batches.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchedulePaymentBatchDelete]
            Endpoint for schedule payment batches.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/schedule-payment-batch/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchedulePaymentBatchDelete,
                    parse_obj_as(
                        type_=SchedulePaymentBatchDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
