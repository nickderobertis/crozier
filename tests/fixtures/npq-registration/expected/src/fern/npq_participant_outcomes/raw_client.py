

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
from ..types.list_participant_outcomes_filter import ListParticipantOutcomesFilter
from ..types.not_found_response import NotFoundResponse
from ..types.pagination_filter import PaginationFilter
from ..types.participant_outcome_response import ParticipantOutcomeResponse
from ..types.participant_outcomes_response import ParticipantOutcomesResponse
from ..types.unauthorised_response import UnauthorisedResponse
from ..types.unprocessable_entity_response import UnprocessableEntityResponse
from .types.participant_outcome_create_request_data import ParticipantOutcomeCreateRequestData
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNpqParticipantOutcomesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_multiple_npq_outcomes_for_all_participants(
        self,
        *,
        filter: typing.Optional[ListParticipantOutcomesFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParticipantOutcomesResponse]:
        """
        Parameters
        ----------
        filter : typing.Optional[ListParticipantOutcomesFilter]

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParticipantOutcomesResponse]
            A list of NPQ Outcomes for all participants
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v3/participants/npq/outcomes",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ListParticipantOutcomesFilter, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(
                    object_=page, annotation=PaginationFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParticipantOutcomesResponse,
                    parse_obj_as(
                        type_=ParticipantOutcomesResponse,
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

    def retrieve_multiple_npq_outcomes_for_a_single_participant(
        self,
        id: IdAttribute,
        *,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParticipantOutcomesResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParticipantOutcomesResponse]
            A list of NPQ Outcomes for a single participant
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}/outcomes",
            method="GET",
            params={
                "page": convert_and_respect_annotation_metadata(
                    object_=page, annotation=PaginationFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParticipantOutcomesResponse,
                    parse_obj_as(
                        type_=ParticipantOutcomesResponse,
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

    def submit_a_npq_outcome_for_a_single_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantOutcomeCreateRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParticipantOutcomeResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantOutcomeCreateRequestData
            The NPQ outcome submission request attributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParticipantOutcomeResponse]
            The details of an NPQ Outcome
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}/outcomes",
            method="POST",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ParticipantOutcomeCreateRequestData, direction="write"
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
                    ParticipantOutcomeResponse,
                    parse_obj_as(
                        type_=ParticipantOutcomeResponse,
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


class AsyncRawNpqParticipantOutcomesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_multiple_npq_outcomes_for_all_participants(
        self,
        *,
        filter: typing.Optional[ListParticipantOutcomesFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParticipantOutcomesResponse]:
        """
        Parameters
        ----------
        filter : typing.Optional[ListParticipantOutcomesFilter]

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParticipantOutcomesResponse]
            A list of NPQ Outcomes for all participants
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v3/participants/npq/outcomes",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ListParticipantOutcomesFilter, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(
                    object_=page, annotation=PaginationFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParticipantOutcomesResponse,
                    parse_obj_as(
                        type_=ParticipantOutcomesResponse,
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

    async def retrieve_multiple_npq_outcomes_for_a_single_participant(
        self,
        id: IdAttribute,
        *,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParticipantOutcomesResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParticipantOutcomesResponse]
            A list of NPQ Outcomes for a single participant
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}/outcomes",
            method="GET",
            params={
                "page": convert_and_respect_annotation_metadata(
                    object_=page, annotation=PaginationFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParticipantOutcomesResponse,
                    parse_obj_as(
                        type_=ParticipantOutcomesResponse,
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

    async def submit_a_npq_outcome_for_a_single_participant(
        self,
        id: IdAttribute,
        *,
        data: ParticipantOutcomeCreateRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParticipantOutcomeResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ParticipantOutcomeCreateRequestData
            The NPQ outcome submission request attributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParticipantOutcomeResponse]
            The details of an NPQ Outcome
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/participants/npq/{encode_path_param(id)}/outcomes",
            method="POST",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=ParticipantOutcomeCreateRequestData, direction="write"
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
                    ParticipantOutcomeResponse,
                    parse_obj_as(
                        type_=ParticipantOutcomeResponse,
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
