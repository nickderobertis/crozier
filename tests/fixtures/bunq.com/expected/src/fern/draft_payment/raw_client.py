

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
from ..types.draft_payment_create import DraftPaymentCreate
from ..types.draft_payment_entry import DraftPaymentEntry
from ..types.draft_payment_listing import DraftPaymentListing
from ..types.draft_payment_read import DraftPaymentRead
from ..types.draft_payment_update import DraftPaymentUpdate
from ..types.schedule import Schedule
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDraftPaymentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_draft_payment_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[DraftPaymentListing]]:
        """
        Get a listing of all DraftPayments from a given MonetaryAccount.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[DraftPaymentListing]]
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DraftPaymentListing],
                    parse_obj_as(
                        type_=typing.List[DraftPaymentListing],
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

    def create_draft_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        entries: typing.Sequence[DraftPaymentEntry],
        number_of_required_accepts: int,
        previous_updated_timestamp: typing.Optional[str] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DraftPaymentCreate]:
        """
        Create a new DraftPayment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        entries : typing.Sequence[DraftPaymentEntry]
            The list of entries in the DraftPayment. Each entry will result in a payment when the DraftPayment is accepted.

        number_of_required_accepts : int
            The number of accepts that are required for the draft payment to receive status ACCEPTED. Currently only 1 is valid.

        previous_updated_timestamp : typing.Optional[str]
            The last updated_timestamp that you received for this DraftPayment. This needs to be provided to prevent race conditions.

        schedule : typing.Optional[Schedule]
            The schedule details when creating or updating a scheduled payment.

        status : typing.Optional[str]
            The status of the DraftPayment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DraftPaymentCreate]
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment",
            method="POST",
            json={
                "entries": convert_and_respect_annotation_metadata(
                    object_=entries, annotation=typing.Sequence[DraftPaymentEntry], direction="write"
                ),
                "number_of_required_accepts": number_of_required_accepts,
                "previous_updated_timestamp": previous_updated_timestamp,
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
                    DraftPaymentCreate,
                    parse_obj_as(
                        type_=DraftPaymentCreate,
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

    def read_draft_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DraftPaymentRead]:
        """
        Get a specific DraftPayment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DraftPaymentRead]
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DraftPaymentRead,
                    parse_obj_as(
                        type_=DraftPaymentRead,
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

    def update_draft_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        entries: typing.Sequence[DraftPaymentEntry],
        number_of_required_accepts: int,
        previous_updated_timestamp: typing.Optional[str] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DraftPaymentUpdate]:
        """
        Update a DraftPayment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        entries : typing.Sequence[DraftPaymentEntry]
            The list of entries in the DraftPayment. Each entry will result in a payment when the DraftPayment is accepted.

        number_of_required_accepts : int
            The number of accepts that are required for the draft payment to receive status ACCEPTED. Currently only 1 is valid.

        previous_updated_timestamp : typing.Optional[str]
            The last updated_timestamp that you received for this DraftPayment. This needs to be provided to prevent race conditions.

        schedule : typing.Optional[Schedule]
            The schedule details when creating or updating a scheduled payment.

        status : typing.Optional[str]
            The status of the DraftPayment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DraftPaymentUpdate]
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "entries": convert_and_respect_annotation_metadata(
                    object_=entries, annotation=typing.Sequence[DraftPaymentEntry], direction="write"
                ),
                "number_of_required_accepts": number_of_required_accepts,
                "previous_updated_timestamp": previous_updated_timestamp,
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
                    DraftPaymentUpdate,
                    parse_obj_as(
                        type_=DraftPaymentUpdate,
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


class AsyncRawDraftPaymentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_draft_payment_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[DraftPaymentListing]]:
        """
        Get a listing of all DraftPayments from a given MonetaryAccount.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[DraftPaymentListing]]
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DraftPaymentListing],
                    parse_obj_as(
                        type_=typing.List[DraftPaymentListing],
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

    async def create_draft_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        entries: typing.Sequence[DraftPaymentEntry],
        number_of_required_accepts: int,
        previous_updated_timestamp: typing.Optional[str] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DraftPaymentCreate]:
        """
        Create a new DraftPayment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        entries : typing.Sequence[DraftPaymentEntry]
            The list of entries in the DraftPayment. Each entry will result in a payment when the DraftPayment is accepted.

        number_of_required_accepts : int
            The number of accepts that are required for the draft payment to receive status ACCEPTED. Currently only 1 is valid.

        previous_updated_timestamp : typing.Optional[str]
            The last updated_timestamp that you received for this DraftPayment. This needs to be provided to prevent race conditions.

        schedule : typing.Optional[Schedule]
            The schedule details when creating or updating a scheduled payment.

        status : typing.Optional[str]
            The status of the DraftPayment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DraftPaymentCreate]
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment",
            method="POST",
            json={
                "entries": convert_and_respect_annotation_metadata(
                    object_=entries, annotation=typing.Sequence[DraftPaymentEntry], direction="write"
                ),
                "number_of_required_accepts": number_of_required_accepts,
                "previous_updated_timestamp": previous_updated_timestamp,
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
                    DraftPaymentCreate,
                    parse_obj_as(
                        type_=DraftPaymentCreate,
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

    async def read_draft_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DraftPaymentRead]:
        """
        Get a specific DraftPayment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DraftPaymentRead]
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DraftPaymentRead,
                    parse_obj_as(
                        type_=DraftPaymentRead,
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

    async def update_draft_payment_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        entries: typing.Sequence[DraftPaymentEntry],
        number_of_required_accepts: int,
        previous_updated_timestamp: typing.Optional[str] = OMIT,
        schedule: typing.Optional[Schedule] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DraftPaymentUpdate]:
        """
        Update a DraftPayment.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        entries : typing.Sequence[DraftPaymentEntry]
            The list of entries in the DraftPayment. Each entry will result in a payment when the DraftPayment is accepted.

        number_of_required_accepts : int
            The number of accepts that are required for the draft payment to receive status ACCEPTED. Currently only 1 is valid.

        previous_updated_timestamp : typing.Optional[str]
            The last updated_timestamp that you received for this DraftPayment. This needs to be provided to prevent race conditions.

        schedule : typing.Optional[Schedule]
            The schedule details when creating or updating a scheduled payment.

        status : typing.Optional[str]
            The status of the DraftPayment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DraftPaymentUpdate]
            A DraftPayment is like a regular Payment, but it needs to be accepted by the sending party before the actual Payment is done.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/draft-payment/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "entries": convert_and_respect_annotation_metadata(
                    object_=entries, annotation=typing.Sequence[DraftPaymentEntry], direction="write"
                ),
                "number_of_required_accepts": number_of_required_accepts,
                "previous_updated_timestamp": previous_updated_timestamp,
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
                    DraftPaymentUpdate,
                    parse_obj_as(
                        type_=DraftPaymentUpdate,
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
