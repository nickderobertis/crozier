

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.harvest import Harvest
from ..types.harvest_container import HarvestContainer
from ..types.harvest_grade import HarvestGrade
from ..types.harvest_holder import HarvestHolder
from ..types.harvest_yield_note import HarvestYieldNote
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawHarvestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def record_harvest(
        self,
        *,
        orchard: str,
        yield_note: typing.Optional[HarvestYieldNote] = OMIT,
        grade: typing.Optional[HarvestGrade] = OMIT,
        container: typing.Optional[HarvestContainer] = OMIT,
        holder: typing.Optional[HarvestHolder] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Harvest]:
        """
        Parameters
        ----------
        orchard : str

        yield_note : typing.Optional[HarvestYieldNote]

        grade : typing.Optional[HarvestGrade]

        container : typing.Optional[HarvestContainer]

        holder : typing.Optional[HarvestHolder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Harvest]
            The recorded harvest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "harvests",
            method="POST",
            json={
                "orchard": orchard,
                "yield_note": convert_and_respect_annotation_metadata(
                    object_=yield_note, annotation=HarvestYieldNote, direction="write"
                ),
                "grade": convert_and_respect_annotation_metadata(
                    object_=grade, annotation=HarvestGrade, direction="write"
                ),
                "container": convert_and_respect_annotation_metadata(
                    object_=container, annotation=HarvestContainer, direction="write"
                ),
                "holder": convert_and_respect_annotation_metadata(
                    object_=holder, annotation=typing.Optional[HarvestHolder], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Harvest,
                    parse_obj_as(
                        type_=Harvest,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawHarvestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def record_harvest(
        self,
        *,
        orchard: str,
        yield_note: typing.Optional[HarvestYieldNote] = OMIT,
        grade: typing.Optional[HarvestGrade] = OMIT,
        container: typing.Optional[HarvestContainer] = OMIT,
        holder: typing.Optional[HarvestHolder] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Harvest]:
        """
        Parameters
        ----------
        orchard : str

        yield_note : typing.Optional[HarvestYieldNote]

        grade : typing.Optional[HarvestGrade]

        container : typing.Optional[HarvestContainer]

        holder : typing.Optional[HarvestHolder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Harvest]
            The recorded harvest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "harvests",
            method="POST",
            json={
                "orchard": orchard,
                "yield_note": convert_and_respect_annotation_metadata(
                    object_=yield_note, annotation=HarvestYieldNote, direction="write"
                ),
                "grade": convert_and_respect_annotation_metadata(
                    object_=grade, annotation=HarvestGrade, direction="write"
                ),
                "container": convert_and_respect_annotation_metadata(
                    object_=container, annotation=HarvestContainer, direction="write"
                ),
                "holder": convert_and_respect_annotation_metadata(
                    object_=holder, annotation=typing.Optional[HarvestHolder], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Harvest,
                    parse_obj_as(
                        type_=Harvest,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
