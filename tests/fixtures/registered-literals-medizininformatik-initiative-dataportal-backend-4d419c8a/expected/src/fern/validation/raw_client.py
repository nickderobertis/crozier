

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.ccdl import Ccdl
from ..types.criterion_list import CriterionList
from ..types.crtdl import Crtdl
from ..types.data_extraction_query import DataExtractionQuery
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawValidationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def validate_crtdl(
        self,
        *,
        display: typing.Optional[str] = OMIT,
        cohort_definition: typing.Optional[Ccdl] = OMIT,
        data_extraction: typing.Optional[DataExtractionQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Check if the json matches the schema and if the content does not contain invalid entries

        Parameters
        ----------
        display : typing.Optional[str]

        cohort_definition : typing.Optional[Ccdl]

        data_extraction : typing.Optional[DataExtractionQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "validation/crtdl",
            method="POST",
            json={
                "display": display,
                "cohortDefinition": convert_and_respect_annotation_metadata(
                    object_=cohort_definition, annotation=Ccdl, direction="write"
                ),
                "dataExtraction": convert_and_respect_annotation_metadata(
                    object_=data_extraction, annotation=DataExtractionQuery, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def validate_ccdl(
        self,
        *,
        version: str,
        inclusion_criteria: typing.Sequence[CriterionList],
        display: typing.Optional[str] = OMIT,
        exclusion_criteria: typing.Optional[typing.Sequence[CriterionList]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Check if the json matches the schema and if the content does not contain invalid entries

        Parameters
        ----------
        version : str
            The json schema version

        inclusion_criteria : typing.Sequence[CriterionList]

        display : typing.Optional[str]

        exclusion_criteria : typing.Optional[typing.Sequence[CriterionList]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "validation/ccdl",
            method="POST",
            json={
                "version": version,
                "display": display,
                "inclusionCriteria": convert_and_respect_annotation_metadata(
                    object_=inclusion_criteria, annotation=typing.Sequence[CriterionList], direction="write"
                ),
                "exclusionCriteria": convert_and_respect_annotation_metadata(
                    object_=exclusion_criteria, annotation=typing.Sequence[CriterionList], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def validate_dataquery(
        self,
        *,
        content: Crtdl,
        label: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        total_number_of_results: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Check if the json matches the schema and if the content does not contain invalid entries

        Parameters
        ----------
        content : Crtdl

        label : typing.Optional[str]

        comment : typing.Optional[str]

        total_number_of_results : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "validation/dataquery",
            method="POST",
            json={
                "label": label,
                "comment": comment,
                "totalNumberOfResults": total_number_of_results,
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=Crtdl, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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


class AsyncRawValidationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def validate_crtdl(
        self,
        *,
        display: typing.Optional[str] = OMIT,
        cohort_definition: typing.Optional[Ccdl] = OMIT,
        data_extraction: typing.Optional[DataExtractionQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Check if the json matches the schema and if the content does not contain invalid entries

        Parameters
        ----------
        display : typing.Optional[str]

        cohort_definition : typing.Optional[Ccdl]

        data_extraction : typing.Optional[DataExtractionQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "validation/crtdl",
            method="POST",
            json={
                "display": display,
                "cohortDefinition": convert_and_respect_annotation_metadata(
                    object_=cohort_definition, annotation=Ccdl, direction="write"
                ),
                "dataExtraction": convert_and_respect_annotation_metadata(
                    object_=data_extraction, annotation=DataExtractionQuery, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def validate_ccdl(
        self,
        *,
        version: str,
        inclusion_criteria: typing.Sequence[CriterionList],
        display: typing.Optional[str] = OMIT,
        exclusion_criteria: typing.Optional[typing.Sequence[CriterionList]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Check if the json matches the schema and if the content does not contain invalid entries

        Parameters
        ----------
        version : str
            The json schema version

        inclusion_criteria : typing.Sequence[CriterionList]

        display : typing.Optional[str]

        exclusion_criteria : typing.Optional[typing.Sequence[CriterionList]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "validation/ccdl",
            method="POST",
            json={
                "version": version,
                "display": display,
                "inclusionCriteria": convert_and_respect_annotation_metadata(
                    object_=inclusion_criteria, annotation=typing.Sequence[CriterionList], direction="write"
                ),
                "exclusionCriteria": convert_and_respect_annotation_metadata(
                    object_=exclusion_criteria, annotation=typing.Sequence[CriterionList], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def validate_dataquery(
        self,
        *,
        content: Crtdl,
        label: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        total_number_of_results: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Check if the json matches the schema and if the content does not contain invalid entries

        Parameters
        ----------
        content : Crtdl

        label : typing.Optional[str]

        comment : typing.Optional[str]

        total_number_of_results : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "validation/dataquery",
            method="POST",
            json={
                "label": label,
                "comment": comment,
                "totalNumberOfResults": total_number_of_results,
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=Crtdl, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
