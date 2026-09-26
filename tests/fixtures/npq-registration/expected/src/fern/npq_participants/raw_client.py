

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.bad_request_response import BadRequestResponse
from ..types.id_attribute import IdAttribute
from ..types.list_participants_filter import ListParticipantsFilter
from ..types.not_found_response import NotFoundResponse
from ..types.pagination_filter import PaginationFilter
from ..types.participant_response import ParticipantResponse
from ..types.participants_response import ParticipantsResponse
from ..types.sorting_options import SortingOptions
from ..types.unauthorised_response import UnauthorisedResponse
from ..types.unprocessable_entity_response import UnprocessableEntityResponse
from .types.participant_change_schedule_request_data import ParticipantChangeScheduleRequestData
from .types.participant_defer_request_data import ParticipantDeferRequestData
from .types.participant_resume_request_data import ParticipantResumeRequestData
from .types.participant_withdraw_request_data import ParticipantWithdrawRequestData
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNpqParticipantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_multiple_npq_participants(
        self,
        *,
        filter: typing.Optional[ListParticipantsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        sort: typing.Optional[SortingOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParticipantsResponse]:
        """
        Parameters
        ----------
        filter : typing.Optional[ListParticipantsFilter]

        page : typing.Optional[PaginationFilter]

        sort : typing.Optional[SortingOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParticipantsResponse]
            A list of NPQ participants
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v3/participants/npq",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ListParticipantsFilter, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(
                    object_=page, annotation=PaginationFilter, direction="write"
                ),
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParticipantsResponse,
                    parse_obj_as(
                        type_=ParticipantsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
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

    def retrieve_a_single_npq_participant(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ParticipantResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParticipantResponse]
            A single NPQ participant
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParticipantResponse,
                    parse_obj_as(
                        type_=ParticipantResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
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

    def resume_an_npq_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantResumeRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParticipantResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantResumeRequestData
            A participant resume request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParticipantResponse]
            The NPQ participant being resumed
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}/resume",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ParticipantResumeRequestData, direction="write"
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
                    ParticipantResponse,
                    parse_obj_as(
                        type_=ParticipantResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityResponse,
                        parse_obj_as(
                            type_=UnprocessableEntityResponse,
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

    def defer_an_npq_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantDeferRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParticipantResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantDeferRequestData
            A participant defer request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParticipantResponse]
            The NPQ participant being deferred
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}/defer",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ParticipantDeferRequestData, direction="write"
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
                    ParticipantResponse,
                    parse_obj_as(
                        type_=ParticipantResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityResponse,
                        parse_obj_as(
                            type_=UnprocessableEntityResponse,
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

    def withdraw_an_npq_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantWithdrawRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParticipantResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantWithdrawRequestData
            A participant withdraw request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParticipantResponse]
            The NPQ participant being withdrawn
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}/withdraw",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ParticipantWithdrawRequestData, direction="write"
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
                    ParticipantResponse,
                    parse_obj_as(
                        type_=ParticipantResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityResponse,
                        parse_obj_as(
                            type_=UnprocessableEntityResponse,
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

    def notify_that_an_npq_participant_is_changing_training_schedule(
        self,
        id: IdAttribute,
        *,
        data: ParticipantChangeScheduleRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParticipantResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantChangeScheduleRequestData
            An NPQ participant change schedule request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParticipantResponse]
            The NPQ participant changing schedule
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}/change-schedule",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ParticipantChangeScheduleRequestData, direction="write"
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
                    ParticipantResponse,
                    parse_obj_as(
                        type_=ParticipantResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityResponse,
                        parse_obj_as(
                            type_=UnprocessableEntityResponse,
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


class AsyncRawNpqParticipantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_multiple_npq_participants(
        self,
        *,
        filter: typing.Optional[ListParticipantsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        sort: typing.Optional[SortingOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParticipantsResponse]:
        """
        Parameters
        ----------
        filter : typing.Optional[ListParticipantsFilter]

        page : typing.Optional[PaginationFilter]

        sort : typing.Optional[SortingOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParticipantsResponse]
            A list of NPQ participants
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v3/participants/npq",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ListParticipantsFilter, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(
                    object_=page, annotation=PaginationFilter, direction="write"
                ),
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParticipantsResponse,
                    parse_obj_as(
                        type_=ParticipantsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
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

    async def retrieve_a_single_npq_participant(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ParticipantResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParticipantResponse]
            A single NPQ participant
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParticipantResponse,
                    parse_obj_as(
                        type_=ParticipantResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
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

    async def resume_an_npq_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantResumeRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParticipantResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantResumeRequestData
            A participant resume request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParticipantResponse]
            The NPQ participant being resumed
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}/resume",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ParticipantResumeRequestData, direction="write"
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
                    ParticipantResponse,
                    parse_obj_as(
                        type_=ParticipantResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityResponse,
                        parse_obj_as(
                            type_=UnprocessableEntityResponse,
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

    async def defer_an_npq_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantDeferRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParticipantResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantDeferRequestData
            A participant defer request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParticipantResponse]
            The NPQ participant being deferred
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}/defer",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ParticipantDeferRequestData, direction="write"
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
                    ParticipantResponse,
                    parse_obj_as(
                        type_=ParticipantResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityResponse,
                        parse_obj_as(
                            type_=UnprocessableEntityResponse,
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

    async def withdraw_an_npq_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantWithdrawRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParticipantResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantWithdrawRequestData
            A participant withdraw request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParticipantResponse]
            The NPQ participant being withdrawn
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}/withdraw",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ParticipantWithdrawRequestData, direction="write"
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
                    ParticipantResponse,
                    parse_obj_as(
                        type_=ParticipantResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityResponse,
                        parse_obj_as(
                            type_=UnprocessableEntityResponse,
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

    async def notify_that_an_npq_participant_is_changing_training_schedule(
        self,
        id: IdAttribute,
        *,
        data: ParticipantChangeScheduleRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParticipantResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantChangeScheduleRequestData
            An NPQ participant change schedule request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParticipantResponse]
            The NPQ participant changing schedule
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}/change-schedule",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ParticipantChangeScheduleRequestData, direction="write"
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
                    ParticipantResponse,
                    parse_obj_as(
                        type_=ParticipantResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableEntityResponse,
                        parse_obj_as(
                            type_=UnprocessableEntityResponse,
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
