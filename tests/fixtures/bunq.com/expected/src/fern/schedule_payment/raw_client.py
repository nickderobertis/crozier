

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.schedule import Schedule
from ..types.schedule_payment_create import SchedulePaymentCreate
from ..types.schedule_payment_delete import SchedulePaymentDelete
from ..types.schedule_payment_entry import SchedulePaymentEntry
from ..types.schedule_payment_listing import SchedulePaymentListing
from ..types.schedule_payment_read import SchedulePaymentRead
from ..types.schedule_payment_update import SchedulePaymentUpdate
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSchedulePaymentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_schedule_payment_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[SchedulePaymentListing]]:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[SchedulePaymentListing]]
            Endpoint for schedule payments.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SchedulePaymentListing],
                    parse_obj_as(
                        type_=typing.List[SchedulePaymentListing],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        payment: typing.Optional[SchedulePaymentEntry] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SchedulePaymentCreate]:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment : typing.Optional[SchedulePaymentEntry]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        status : typing.Optional[str]
            The schedule status, options: ACTIVE, FINISHED, CANCELLED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchedulePaymentCreate]
            Endpoint for schedule payments.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment",
            method="POST",
            json={
                "payment": convert_and_respect_annotation_metadata(
                    object_=payment, annotation=SchedulePaymentEntry, direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=Schedule, direction="write"
                ),
                "status": status,
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
                    SchedulePaymentCreate,
                    parse_obj_as(
                        type_=SchedulePaymentCreate,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SchedulePaymentRead]:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchedulePaymentRead]
            Endpoint for schedule payments.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchedulePaymentRead,
                    parse_obj_as(
                        type_=SchedulePaymentRead,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        payment: typing.Optional[SchedulePaymentEntry] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SchedulePaymentUpdate]:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        payment : typing.Optional[SchedulePaymentEntry]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        status : typing.Optional[str]
            The schedule status, options: ACTIVE, FINISHED, CANCELLED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchedulePaymentUpdate]
            Endpoint for schedule payments.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "payment": convert_and_respect_annotation_metadata(
                    object_=payment, annotation=SchedulePaymentEntry, direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=Schedule, direction="write"
                ),
                "status": status,
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
                    SchedulePaymentUpdate,
                    parse_obj_as(
                        type_=SchedulePaymentUpdate,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SchedulePaymentDelete]:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchedulePaymentDelete]
            Endpoint for schedule payments.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchedulePaymentDelete,
                    parse_obj_as(
                        type_=SchedulePaymentDelete,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSchedulePaymentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_schedule_payment_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[SchedulePaymentListing]]:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[SchedulePaymentListing]]
            Endpoint for schedule payments.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SchedulePaymentListing],
                    parse_obj_as(
                        type_=typing.List[SchedulePaymentListing],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        payment: typing.Optional[SchedulePaymentEntry] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SchedulePaymentCreate]:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payment : typing.Optional[SchedulePaymentEntry]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        status : typing.Optional[str]
            The schedule status, options: ACTIVE, FINISHED, CANCELLED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchedulePaymentCreate]
            Endpoint for schedule payments.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment",
            method="POST",
            json={
                "payment": convert_and_respect_annotation_metadata(
                    object_=payment, annotation=SchedulePaymentEntry, direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=Schedule, direction="write"
                ),
                "status": status,
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
                    SchedulePaymentCreate,
                    parse_obj_as(
                        type_=SchedulePaymentCreate,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SchedulePaymentRead]:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchedulePaymentRead]
            Endpoint for schedule payments.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchedulePaymentRead,
                    parse_obj_as(
                        type_=SchedulePaymentRead,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        payment: typing.Optional[SchedulePaymentEntry] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SchedulePaymentUpdate]:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        payment : typing.Optional[SchedulePaymentEntry]
            The payment details.

        schedule : typing.Optional[Schedule]
            The schedule details.

        status : typing.Optional[str]
            The schedule status, options: ACTIVE, FINISHED, CANCELLED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchedulePaymentUpdate]
            Endpoint for schedule payments.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "payment": convert_and_respect_annotation_metadata(
                    object_=payment, annotation=SchedulePaymentEntry, direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=Schedule, direction="write"
                ),
                "status": status,
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
                    SchedulePaymentUpdate,
                    parse_obj_as(
                        type_=SchedulePaymentUpdate,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_schedule_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SchedulePaymentDelete]:
        """
        Endpoint for schedule payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchedulePaymentDelete]
            Endpoint for schedule payments.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule-payment/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchedulePaymentDelete,
                    parse_obj_as(
                        type_=SchedulePaymentDelete,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
