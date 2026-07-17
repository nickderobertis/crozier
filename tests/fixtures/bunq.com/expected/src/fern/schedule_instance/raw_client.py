

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
from ..types.error import Error
from ..types.request_inquiry_reference import RequestInquiryReference
from ..types.schedule_anchor_object import ScheduleAnchorObject
from ..types.schedule_instance_anchor_object import ScheduleInstanceAnchorObject
from ..types.schedule_instance_listing import ScheduleInstanceListing
from ..types.schedule_instance_read import ScheduleInstanceRead
from ..types.schedule_instance_update import ScheduleInstanceUpdate
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawScheduleInstanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_schedule_instance_for_user_monetary_account_schedule(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ScheduleInstanceListing]]:
        """
        view for reading, updating and listing the scheduled instance.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ScheduleInstanceListing]]
            view for reading, updating and listing the scheduled instance.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ScheduleInstanceListing],
                    parse_obj_as(
                        type_=typing.List[ScheduleInstanceListing],
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

    def read_schedule_instance_for_user_monetary_account_schedule(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ScheduleInstanceRead]:
        """
        view for reading, updating and listing the scheduled instance.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScheduleInstanceRead]
            view for reading, updating and listing the scheduled instance.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduleInstanceRead,
                    parse_obj_as(
                        type_=ScheduleInstanceRead,
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

    def update_schedule_instance_for_user_monetary_account_schedule(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        item_id: int,
        *,
        error_message: typing.Optional[typing.Sequence[Error]] = OMIT,
        request_reference_split_the_bill: typing.Optional[typing.Sequence[RequestInquiryReference]] = OMIT,
        result_object: typing.Optional[ScheduleInstanceAnchorObject] = OMIT,
        scheduled_object: typing.Optional[ScheduleAnchorObject] = OMIT,
        state: typing.Optional[str] = OMIT,
        time_end: typing.Optional[str] = OMIT,
        time_start: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ScheduleInstanceUpdate]:
        """
        view for reading, updating and listing the scheduled instance.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        item_id : int


        error_message : typing.Optional[typing.Sequence[Error]]
            The message when the scheduled instance has run and failed due to user error.

        request_reference_split_the_bill : typing.Optional[typing.Sequence[RequestInquiryReference]]
            The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch

        result_object : typing.Optional[ScheduleInstanceAnchorObject]
            The result object of this schedule instance. (Payment, PaymentBatch)

        scheduled_object : typing.Optional[ScheduleAnchorObject]
            The scheduled object. (Payment, PaymentBatch)

        state : typing.Optional[str]
            The state of the scheduleInstance. (FINISHED_SUCCESSFULLY, RETRY, FAILED_USER_ERROR)

        time_end : typing.Optional[str]
            The schedule end time (UTC).

        time_start : typing.Optional[str]
            The schedule start time (UTC).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScheduleInstanceUpdate]
            view for reading, updating and listing the scheduled instance.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "error_message": convert_and_respect_annotation_metadata(
                    object_=error_message, annotation=typing.Sequence[Error], direction="write"
                ),
                "request_reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=request_reference_split_the_bill,
                    annotation=typing.Sequence[RequestInquiryReference],
                    direction="write",
                ),
                "result_object": convert_and_respect_annotation_metadata(
                    object_=result_object, annotation=ScheduleInstanceAnchorObject, direction="write"
                ),
                "scheduled_object": convert_and_respect_annotation_metadata(
                    object_=scheduled_object, annotation=ScheduleAnchorObject, direction="write"
                ),
                "state": state,
                "time_end": time_end,
                "time_start": time_start,
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
                    ScheduleInstanceUpdate,
                    parse_obj_as(
                        type_=ScheduleInstanceUpdate,
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


class AsyncRawScheduleInstanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_schedule_instance_for_user_monetary_account_schedule(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ScheduleInstanceListing]]:
        """
        view for reading, updating and listing the scheduled instance.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ScheduleInstanceListing]]
            view for reading, updating and listing the scheduled instance.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ScheduleInstanceListing],
                    parse_obj_as(
                        type_=typing.List[ScheduleInstanceListing],
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

    async def read_schedule_instance_for_user_monetary_account_schedule(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ScheduleInstanceRead]:
        """
        view for reading, updating and listing the scheduled instance.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScheduleInstanceRead]
            view for reading, updating and listing the scheduled instance.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduleInstanceRead,
                    parse_obj_as(
                        type_=ScheduleInstanceRead,
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

    async def update_schedule_instance_for_user_monetary_account_schedule(
        self,
        user_id: int,
        monetary_account_id: int,
        schedule_id: int,
        item_id: int,
        *,
        error_message: typing.Optional[typing.Sequence[Error]] = OMIT,
        request_reference_split_the_bill: typing.Optional[typing.Sequence[RequestInquiryReference]] = OMIT,
        result_object: typing.Optional[ScheduleInstanceAnchorObject] = OMIT,
        scheduled_object: typing.Optional[ScheduleAnchorObject] = OMIT,
        state: typing.Optional[str] = OMIT,
        time_end: typing.Optional[str] = OMIT,
        time_start: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ScheduleInstanceUpdate]:
        """
        view for reading, updating and listing the scheduled instance.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        schedule_id : int


        item_id : int


        error_message : typing.Optional[typing.Sequence[Error]]
            The message when the scheduled instance has run and failed due to user error.

        request_reference_split_the_bill : typing.Optional[typing.Sequence[RequestInquiryReference]]
            The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch

        result_object : typing.Optional[ScheduleInstanceAnchorObject]
            The result object of this schedule instance. (Payment, PaymentBatch)

        scheduled_object : typing.Optional[ScheduleAnchorObject]
            The scheduled object. (Payment, PaymentBatch)

        state : typing.Optional[str]
            The state of the scheduleInstance. (FINISHED_SUCCESSFULLY, RETRY, FAILED_USER_ERROR)

        time_end : typing.Optional[str]
            The schedule end time (UTC).

        time_start : typing.Optional[str]
            The schedule start time (UTC).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScheduleInstanceUpdate]
            view for reading, updating and listing the scheduled instance.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/monetary-account/{encode_path_param(monetary_account_id)}/schedule/{encode_path_param(schedule_id)}/schedule-instance/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "error_message": convert_and_respect_annotation_metadata(
                    object_=error_message, annotation=typing.Sequence[Error], direction="write"
                ),
                "request_reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=request_reference_split_the_bill,
                    annotation=typing.Sequence[RequestInquiryReference],
                    direction="write",
                ),
                "result_object": convert_and_respect_annotation_metadata(
                    object_=result_object, annotation=ScheduleInstanceAnchorObject, direction="write"
                ),
                "scheduled_object": convert_and_respect_annotation_metadata(
                    object_=scheduled_object, annotation=ScheduleAnchorObject, direction="write"
                ),
                "state": state,
                "time_end": time_end,
                "time_start": time_start,
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
                    ScheduleInstanceUpdate,
                    parse_obj_as(
                        type_=ScheduleInstanceUpdate,
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
