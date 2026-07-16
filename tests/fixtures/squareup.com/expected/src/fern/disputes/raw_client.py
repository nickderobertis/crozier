

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.accept_dispute_response import AcceptDisputeResponse
from ..types.create_dispute_evidence_text_response import CreateDisputeEvidenceTextResponse
from ..types.delete_dispute_evidence_response import DeleteDisputeEvidenceResponse
from ..types.list_dispute_evidence_response import ListDisputeEvidenceResponse
from ..types.list_disputes_response import ListDisputesResponse
from ..types.retrieve_dispute_evidence_response import RetrieveDisputeEvidenceResponse
from ..types.retrieve_dispute_response import RetrieveDisputeResponse
from ..types.submit_evidence_response import SubmitEvidenceResponse


OMIT = typing.cast(typing.Any, ...)


class RawDisputesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_disputes(
        self,
        *,
        cursor: typing.Optional[str] = None,
        states: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListDisputesResponse]:
        """
        Returns a list of disputes associated with a particular account.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        states : typing.Optional[str]
            The dispute states to filter the result.
            If not specified, the endpoint returns all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`,
            or `LOST`).

        location_id : typing.Optional[str]
            The ID of the location for which to return a list of disputes. If not specified, the endpoint returns
            all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`, or `LOST`) associated with all locations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListDisputesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/disputes",
            method="GET",
            params={
                "cursor": cursor,
                "states": states,
                "location_id": location_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDisputesResponse,
                    parse_obj_as(
                        type_=ListDisputesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_dispute(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveDisputeResponse]:
        """
        Returns details about a specific dispute.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want more details about.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveDisputeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveDisputeResponse,
                    parse_obj_as(
                        type_=RetrieveDisputeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def accept_dispute(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AcceptDisputeResponse]:
        """
        Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and
        updates the dispute state to ACCEPTED.

        Square debits the disputed amount from the seller’s Square account. If the Square account
        does not have sufficient funds, Square debits the associated bank account.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to accept.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AcceptDisputeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/accept",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AcceptDisputeResponse,
                    parse_obj_as(
                        type_=AcceptDisputeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_dispute_evidence(
        self,
        dispute_id: str,
        *,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListDisputeEvidenceResponse]:
        """
        Returns a list of evidence associated with a dispute.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListDisputeEvidenceResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/evidence",
            method="GET",
            params={
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDisputeEvidenceResponse,
                    parse_obj_as(
                        type_=ListDisputeEvidenceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_dispute_evidence_text(
        self,
        dispute_id: str,
        *,
        evidence_text: str,
        idempotency_key: str,
        evidence_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDisputeEvidenceTextResponse]:
        """
        Uploads text to use as evidence for a dispute challenge.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to upload evidence for.

        evidence_text : str
            The evidence string.

        idempotency_key : str
            The Unique ID. For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        evidence_type : typing.Optional[str]
            The type of evidence you are uploading.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDisputeEvidenceTextResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/evidence-text",
            method="POST",
            json={
                "evidence_text": evidence_text,
                "evidence_type": evidence_type,
                "idempotency_key": idempotency_key,
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
                    CreateDisputeEvidenceTextResponse,
                    parse_obj_as(
                        type_=CreateDisputeEvidenceTextResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveDisputeEvidenceResponse]:
        """
        Returns the evidence metadata specified by the evidence ID in the request URL path

        You must maintain a copy of the evidence you upload if you want to reference it later. You cannot
        download the evidence after you upload it.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute that you want to retrieve evidence from.

        evidence_id : str
            The ID of the evidence to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveDisputeEvidenceResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/evidence/{jsonable_encoder(evidence_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveDisputeEvidenceResponse,
                    parse_obj_as(
                        type_=RetrieveDisputeEvidenceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteDisputeEvidenceResponse]:
        """
        Removes specified evidence from a dispute.

        Square does not send the bank any evidence that is removed. Also, you cannot remove evidence after
        submitting it to the bank using [SubmitEvidence](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/submit-evidence).

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to remove evidence from.

        evidence_id : str
            The ID of the evidence you want to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteDisputeEvidenceResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/evidence/{jsonable_encoder(evidence_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDisputeEvidenceResponse,
                    parse_obj_as(
                        type_=DeleteDisputeEvidenceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def submit_evidence(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SubmitEvidenceResponse]:
        """
        Submits evidence to the cardholder's bank.

        Before submitting evidence, Square compiles all available evidence. This includes evidence uploaded
        using the [CreateDisputeEvidenceFile](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-file) and
        [CreateDisputeEvidenceText](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-text) endpoints and
        evidence automatically provided by Square, when available.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute that you want to submit evidence for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubmitEvidenceResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/submit-evidence",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubmitEvidenceResponse,
                    parse_obj_as(
                        type_=SubmitEvidenceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDisputesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_disputes(
        self,
        *,
        cursor: typing.Optional[str] = None,
        states: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListDisputesResponse]:
        """
        Returns a list of disputes associated with a particular account.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        states : typing.Optional[str]
            The dispute states to filter the result.
            If not specified, the endpoint returns all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`,
            or `LOST`).

        location_id : typing.Optional[str]
            The ID of the location for which to return a list of disputes. If not specified, the endpoint returns
            all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`, or `LOST`) associated with all locations.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListDisputesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/disputes",
            method="GET",
            params={
                "cursor": cursor,
                "states": states,
                "location_id": location_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDisputesResponse,
                    parse_obj_as(
                        type_=ListDisputesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_dispute(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveDisputeResponse]:
        """
        Returns details about a specific dispute.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want more details about.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveDisputeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveDisputeResponse,
                    parse_obj_as(
                        type_=RetrieveDisputeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def accept_dispute(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AcceptDisputeResponse]:
        """
        Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and
        updates the dispute state to ACCEPTED.

        Square debits the disputed amount from the seller’s Square account. If the Square account
        does not have sufficient funds, Square debits the associated bank account.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to accept.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AcceptDisputeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/accept",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AcceptDisputeResponse,
                    parse_obj_as(
                        type_=AcceptDisputeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_dispute_evidence(
        self,
        dispute_id: str,
        *,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListDisputeEvidenceResponse]:
        """
        Returns a list of evidence associated with a dispute.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListDisputeEvidenceResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/evidence",
            method="GET",
            params={
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDisputeEvidenceResponse,
                    parse_obj_as(
                        type_=ListDisputeEvidenceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_dispute_evidence_text(
        self,
        dispute_id: str,
        *,
        evidence_text: str,
        idempotency_key: str,
        evidence_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDisputeEvidenceTextResponse]:
        """
        Uploads text to use as evidence for a dispute challenge.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to upload evidence for.

        evidence_text : str
            The evidence string.

        idempotency_key : str
            The Unique ID. For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        evidence_type : typing.Optional[str]
            The type of evidence you are uploading.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDisputeEvidenceTextResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/evidence-text",
            method="POST",
            json={
                "evidence_text": evidence_text,
                "evidence_type": evidence_type,
                "idempotency_key": idempotency_key,
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
                    CreateDisputeEvidenceTextResponse,
                    parse_obj_as(
                        type_=CreateDisputeEvidenceTextResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveDisputeEvidenceResponse]:
        """
        Returns the evidence metadata specified by the evidence ID in the request URL path

        You must maintain a copy of the evidence you upload if you want to reference it later. You cannot
        download the evidence after you upload it.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute that you want to retrieve evidence from.

        evidence_id : str
            The ID of the evidence to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveDisputeEvidenceResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/evidence/{jsonable_encoder(evidence_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveDisputeEvidenceResponse,
                    parse_obj_as(
                        type_=RetrieveDisputeEvidenceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteDisputeEvidenceResponse]:
        """
        Removes specified evidence from a dispute.

        Square does not send the bank any evidence that is removed. Also, you cannot remove evidence after
        submitting it to the bank using [SubmitEvidence](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/submit-evidence).

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute you want to remove evidence from.

        evidence_id : str
            The ID of the evidence you want to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteDisputeEvidenceResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/evidence/{jsonable_encoder(evidence_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDisputeEvidenceResponse,
                    parse_obj_as(
                        type_=DeleteDisputeEvidenceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def submit_evidence(
        self, dispute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SubmitEvidenceResponse]:
        """
        Submits evidence to the cardholder's bank.

        Before submitting evidence, Square compiles all available evidence. This includes evidence uploaded
        using the [CreateDisputeEvidenceFile](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-file) and
        [CreateDisputeEvidenceText](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-text) endpoints and
        evidence automatically provided by Square, when available.

        Parameters
        ----------
        dispute_id : str
            The ID of the dispute that you want to submit evidence for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubmitEvidenceResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/disputes/{jsonable_encoder(dispute_id)}/submit-evidence",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubmitEvidenceResponse,
                    parse_obj_as(
                        type_=SubmitEvidenceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
