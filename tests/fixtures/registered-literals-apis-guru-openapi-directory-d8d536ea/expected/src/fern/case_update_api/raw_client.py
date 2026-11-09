

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
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unavailable_for_legal_reasons_error import UnavailableForLegalReasonsError
from ..types.case_update import CaseUpdate
from ..types.case_update_list_response import CaseUpdateListResponse
from ..types.case_update_pacer_options import CaseUpdatePacerOptions
from ..types.exception import Exception
from .types.get_case_updates_request_status import GetCaseUpdatesRequestStatus
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCaseUpdateApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def update_case(
        self,
        *,
        case_id: str,
        pacer_options: typing.Optional[CaseUpdatePacerOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaseUpdate]:
        """
        Request case updates for the specified case.

        Parameters
        ----------
        case_id : str
            UniCourt's Case Id for update.

        pacer_options : typing.Optional[CaseUpdatePacerOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaseUpdate]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "caseUpdate",
            method="PUT",
            json={
                "caseId": case_id,
                "pacerOptions": convert_and_respect_annotation_metadata(
                    object_=pacer_options, annotation=CaseUpdatePacerOptions, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseUpdate,
                    parse_obj_as(
                        type_=CaseUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    def get_case_update_by_case_id(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CaseUpdate]:
        """
        Retrieve case updates for the specified case object.

        Parameters
        ----------
        case_id : str
            The caseId value of the case object for which updates are to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaseUpdate]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"caseUpdate/{encode_path_param(case_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseUpdate,
                    parse_obj_as(
                        type_=CaseUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    def get_case_updates(
        self,
        *,
        case_id: typing.Optional[str] = None,
        requested_date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCaseUpdatesRequestStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaseUpdateListResponse]:
        """
        Retrieve case updates for the specified date.

        Parameters
        ----------
        case_id : typing.Optional[str]
            The caseId value of the case for which updates should be retrieved.

        requested_date : typing.Optional[dt.datetime]
            The date for which case updates are to be retrieved.

        status : typing.Optional[GetCaseUpdatesRequestStatus]
            Status of the case updates to be retrieved.

        page_number : typing.Optional[int]
            The page number of the callbacks to be retrieved.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaseUpdateListResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "caseUpdates",
            method="GET",
            params={
                "caseId": case_id,
                "requestedDate": serialize_datetime(requested_date) if requested_date is not None else None,
                "status": status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseUpdateListResponse,
                    parse_obj_as(
                        type_=CaseUpdateListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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


class AsyncRawCaseUpdateApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def update_case(
        self,
        *,
        case_id: str,
        pacer_options: typing.Optional[CaseUpdatePacerOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaseUpdate]:
        """
        Request case updates for the specified case.

        Parameters
        ----------
        case_id : str
            UniCourt's Case Id for update.

        pacer_options : typing.Optional[CaseUpdatePacerOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaseUpdate]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "caseUpdate",
            method="PUT",
            json={
                "caseId": case_id,
                "pacerOptions": convert_and_respect_annotation_metadata(
                    object_=pacer_options, annotation=CaseUpdatePacerOptions, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseUpdate,
                    parse_obj_as(
                        type_=CaseUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    async def get_case_update_by_case_id(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CaseUpdate]:
        """
        Retrieve case updates for the specified case object.

        Parameters
        ----------
        case_id : str
            The caseId value of the case object for which updates are to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaseUpdate]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"caseUpdate/{encode_path_param(case_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseUpdate,
                    parse_obj_as(
                        type_=CaseUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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

    async def get_case_updates(
        self,
        *,
        case_id: typing.Optional[str] = None,
        requested_date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCaseUpdatesRequestStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaseUpdateListResponse]:
        """
        Retrieve case updates for the specified date.

        Parameters
        ----------
        case_id : typing.Optional[str]
            The caseId value of the case for which updates should be retrieved.

        requested_date : typing.Optional[dt.datetime]
            The date for which case updates are to be retrieved.

        status : typing.Optional[GetCaseUpdatesRequestStatus]
            Status of the case updates to be retrieved.

        page_number : typing.Optional[int]
            The page number of the callbacks to be retrieved.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaseUpdateListResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "caseUpdates",
            method="GET",
            params={
                "caseId": case_id,
                "requestedDate": serialize_datetime(requested_date) if requested_date is not None else None,
                "status": status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseUpdateListResponse,
                    parse_obj_as(
                        type_=CaseUpdateListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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
