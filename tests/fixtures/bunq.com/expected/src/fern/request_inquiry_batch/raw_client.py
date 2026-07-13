

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
from ..types.amount import Amount
from ..types.request_inquiry import RequestInquiry
from ..types.request_inquiry_batch_create import RequestInquiryBatchCreate
from ..types.request_inquiry_batch_listing import RequestInquiryBatchListing
from ..types.request_inquiry_batch_read import RequestInquiryBatchRead
from ..types.request_inquiry_batch_update import RequestInquiryBatchUpdate
from ..types.request_reference_split_the_bill_anchor_object import RequestReferenceSplitTheBillAnchorObject


OMIT = typing.cast(typing.Any, ...)


class RawRequestInquiryBatchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_request_inquiry_batch_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RequestInquiryBatchListing]]:
        """
        Return all the request batches for a monetary account.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RequestInquiryBatchListing]]
            Create a batch of requests for payment, or show the request batches of a monetary account.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RequestInquiryBatchListing],
                    parse_obj_as(
                        type_=typing.List[RequestInquiryBatchListing],
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

    def create_request_inquiry_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        event_id: typing.Optional[int] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        request_inquiries: typing.Optional[typing.Sequence[RequestInquiry]] = OMIT,
        status: typing.Optional[str] = OMIT,
        total_amount_inquired: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RequestInquiryBatchCreate]:
        """
        Create a request batch by sending an array of single request objects, that will become part of the batch.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        event_id : typing.Optional[int]
            The ID of the associated event if the request batch was made using 'split the bill'.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        request_inquiries : typing.Optional[typing.Sequence[RequestInquiry]]
            The list of requests that were made.

        status : typing.Optional[str]
            The status of the request.

        total_amount_inquired : typing.Optional[Amount]
            The total amount originally inquired for this batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInquiryBatchCreate]
            Create a batch of requests for payment, or show the request batches of a monetary account.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch",
            method="POST",
            json={
                "event_id": event_id,
                "reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=reference_split_the_bill,
                    annotation=RequestReferenceSplitTheBillAnchorObject,
                    direction="write",
                ),
                "request_inquiries": convert_and_respect_annotation_metadata(
                    object_=request_inquiries, annotation=typing.Sequence[RequestInquiry], direction="write"
                ),
                "status": status,
                "total_amount_inquired": convert_and_respect_annotation_metadata(
                    object_=total_amount_inquired, annotation=Amount, direction="write"
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
                    RequestInquiryBatchCreate,
                    parse_obj_as(
                        type_=RequestInquiryBatchCreate,
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

    def read_request_inquiry_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RequestInquiryBatchRead]:
        """
        Return the details of a specific request batch.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInquiryBatchRead]
            Create a batch of requests for payment, or show the request batches of a monetary account.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInquiryBatchRead,
                    parse_obj_as(
                        type_=RequestInquiryBatchRead,
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

    def update_request_inquiry_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        event_id: typing.Optional[int] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        request_inquiries: typing.Optional[typing.Sequence[RequestInquiry]] = OMIT,
        status: typing.Optional[str] = OMIT,
        total_amount_inquired: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RequestInquiryBatchUpdate]:
        """
        Revoke a request batch. The status of all the requests will be set to REVOKED.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        event_id : typing.Optional[int]
            The ID of the associated event if the request batch was made using 'split the bill'.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        request_inquiries : typing.Optional[typing.Sequence[RequestInquiry]]
            The list of requests that were made.

        status : typing.Optional[str]
            The status of the request.

        total_amount_inquired : typing.Optional[Amount]
            The total amount originally inquired for this batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInquiryBatchUpdate]
            Create a batch of requests for payment, or show the request batches of a monetary account.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "event_id": event_id,
                "reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=reference_split_the_bill,
                    annotation=RequestReferenceSplitTheBillAnchorObject,
                    direction="write",
                ),
                "request_inquiries": convert_and_respect_annotation_metadata(
                    object_=request_inquiries, annotation=typing.Sequence[RequestInquiry], direction="write"
                ),
                "status": status,
                "total_amount_inquired": convert_and_respect_annotation_metadata(
                    object_=total_amount_inquired, annotation=Amount, direction="write"
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
                    RequestInquiryBatchUpdate,
                    parse_obj_as(
                        type_=RequestInquiryBatchUpdate,
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


class AsyncRawRequestInquiryBatchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_request_inquiry_batch_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RequestInquiryBatchListing]]:
        """
        Return all the request batches for a monetary account.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RequestInquiryBatchListing]]
            Create a batch of requests for payment, or show the request batches of a monetary account.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RequestInquiryBatchListing],
                    parse_obj_as(
                        type_=typing.List[RequestInquiryBatchListing],
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

    async def create_request_inquiry_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        event_id: typing.Optional[int] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        request_inquiries: typing.Optional[typing.Sequence[RequestInquiry]] = OMIT,
        status: typing.Optional[str] = OMIT,
        total_amount_inquired: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RequestInquiryBatchCreate]:
        """
        Create a request batch by sending an array of single request objects, that will become part of the batch.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        event_id : typing.Optional[int]
            The ID of the associated event if the request batch was made using 'split the bill'.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        request_inquiries : typing.Optional[typing.Sequence[RequestInquiry]]
            The list of requests that were made.

        status : typing.Optional[str]
            The status of the request.

        total_amount_inquired : typing.Optional[Amount]
            The total amount originally inquired for this batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInquiryBatchCreate]
            Create a batch of requests for payment, or show the request batches of a monetary account.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch",
            method="POST",
            json={
                "event_id": event_id,
                "reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=reference_split_the_bill,
                    annotation=RequestReferenceSplitTheBillAnchorObject,
                    direction="write",
                ),
                "request_inquiries": convert_and_respect_annotation_metadata(
                    object_=request_inquiries, annotation=typing.Sequence[RequestInquiry], direction="write"
                ),
                "status": status,
                "total_amount_inquired": convert_and_respect_annotation_metadata(
                    object_=total_amount_inquired, annotation=Amount, direction="write"
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
                    RequestInquiryBatchCreate,
                    parse_obj_as(
                        type_=RequestInquiryBatchCreate,
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

    async def read_request_inquiry_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RequestInquiryBatchRead]:
        """
        Return the details of a specific request batch.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInquiryBatchRead]
            Create a batch of requests for payment, or show the request batches of a monetary account.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInquiryBatchRead,
                    parse_obj_as(
                        type_=RequestInquiryBatchRead,
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

    async def update_request_inquiry_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        event_id: typing.Optional[int] = OMIT,
        reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = OMIT,
        request_inquiries: typing.Optional[typing.Sequence[RequestInquiry]] = OMIT,
        status: typing.Optional[str] = OMIT,
        total_amount_inquired: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RequestInquiryBatchUpdate]:
        """
        Revoke a request batch. The status of all the requests will be set to REVOKED.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        event_id : typing.Optional[int]
            The ID of the associated event if the request batch was made using 'split the bill'.

        reference_split_the_bill : typing.Optional[RequestReferenceSplitTheBillAnchorObject]
            The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction

        request_inquiries : typing.Optional[typing.Sequence[RequestInquiry]]
            The list of requests that were made.

        status : typing.Optional[str]
            The status of the request.

        total_amount_inquired : typing.Optional[Amount]
            The total amount originally inquired for this batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInquiryBatchUpdate]
            Create a batch of requests for payment, or show the request batches of a monetary account.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/request-inquiry-batch/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "event_id": event_id,
                "reference_split_the_bill": convert_and_respect_annotation_metadata(
                    object_=reference_split_the_bill,
                    annotation=RequestReferenceSplitTheBillAnchorObject,
                    direction="write",
                ),
                "request_inquiries": convert_and_respect_annotation_metadata(
                    object_=request_inquiries, annotation=typing.Sequence[RequestInquiry], direction="write"
                ),
                "status": status,
                "total_amount_inquired": convert_and_respect_annotation_metadata(
                    object_=total_amount_inquired, annotation=Amount, direction="write"
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
                    RequestInquiryBatchUpdate,
                    parse_obj_as(
                        type_=RequestInquiryBatchUpdate,
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
