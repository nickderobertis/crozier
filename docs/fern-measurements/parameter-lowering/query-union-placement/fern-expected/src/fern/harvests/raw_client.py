

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.list_weighed_harvests_request_grade import ListWeighedHarvestsRequestGrade
from ..types.list_weighed_harvests_request_unit import ListWeighedHarvestsRequestUnit
from .types.list_harvests_request_crate import ListHarvestsRequestCrate
from .types.list_harvests_request_ripeness import ListHarvestsRequestRipeness
from pydantic import ValidationError


class RawHarvestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_harvests(
        self,
        *,
        ripeness: typing.Optional[ListHarvestsRequestRipeness] = None,
        crate: typing.Optional[ListHarvestsRequestCrate] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        ripeness : typing.Optional[ListHarvestsRequestRipeness]

        crate : typing.Optional[ListHarvestsRequestCrate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Harvests matching the filters.
        """
        _response = self._client_wrapper.httpx_client.request(
            "harvests",
            method="GET",
            params={
                "ripeness": ripeness,
                "crate": crate,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def list_weighed_harvests(
        self,
        *,
        unit: typing.Optional[ListWeighedHarvestsRequestUnit] = None,
        grade: typing.Optional[ListWeighedHarvestsRequestGrade] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        unit : typing.Optional[ListWeighedHarvestsRequestUnit]

        grade : typing.Optional[ListWeighedHarvestsRequestGrade]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Weighed harvests.
        """
        _response = self._client_wrapper.httpx_client.request(
            "harvests/weighed",
            method="GET",
            params={
                "unit": unit,
                "grade": grade,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def list_harvests(
        self,
        *,
        ripeness: typing.Optional[ListHarvestsRequestRipeness] = None,
        crate: typing.Optional[ListHarvestsRequestCrate] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        ripeness : typing.Optional[ListHarvestsRequestRipeness]

        crate : typing.Optional[ListHarvestsRequestCrate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Harvests matching the filters.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "harvests",
            method="GET",
            params={
                "ripeness": ripeness,
                "crate": crate,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def list_weighed_harvests(
        self,
        *,
        unit: typing.Optional[ListWeighedHarvestsRequestUnit] = None,
        grade: typing.Optional[ListWeighedHarvestsRequestGrade] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        unit : typing.Optional[ListWeighedHarvestsRequestUnit]

        grade : typing.Optional[ListWeighedHarvestsRequestGrade]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Weighed harvests.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "harvests/weighed",
            method="GET",
            params={
                "unit": unit,
                "grade": grade,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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
