

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
from ..types.data_extraction_query import DataExtractionQuery
from ..types.upgrade_wrapper import UpgradeWrapper
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUpgradeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def crtdl(
        self,
        *,
        display: typing.Optional[str] = OMIT,
        cohort_definition: typing.Optional[Ccdl] = OMIT,
        data_extraction: typing.Optional[DataExtractionQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpgradeWrapper]:
        """
        Some common problems can be automatically fixed by either removing parts of the CRTDL or renaming things. Try to fix as many as possible

        Parameters
        ----------
        display : typing.Optional[str]

        cohort_definition : typing.Optional[Ccdl]

        data_extraction : typing.Optional[DataExtractionQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpgradeWrapper]
            CRTDL upgrade finished. If any changes were made, they are listed in "annotations"
        """
        _response = self._client_wrapper.httpx_client.request(
            "upgrade/crtdl",
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
                _data = typing.cast(
                    UpgradeWrapper,
                    parse_obj_as(
                        type_=UpgradeWrapper,
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


class AsyncRawUpgradeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def crtdl(
        self,
        *,
        display: typing.Optional[str] = OMIT,
        cohort_definition: typing.Optional[Ccdl] = OMIT,
        data_extraction: typing.Optional[DataExtractionQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpgradeWrapper]:
        """
        Some common problems can be automatically fixed by either removing parts of the CRTDL or renaming things. Try to fix as many as possible

        Parameters
        ----------
        display : typing.Optional[str]

        cohort_definition : typing.Optional[Ccdl]

        data_extraction : typing.Optional[DataExtractionQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpgradeWrapper]
            CRTDL upgrade finished. If any changes were made, they are listed in "annotations"
        """
        _response = await self._client_wrapper.httpx_client.request(
            "upgrade/crtdl",
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
                _data = typing.cast(
                    UpgradeWrapper,
                    parse_obj_as(
                        type_=UpgradeWrapper,
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
