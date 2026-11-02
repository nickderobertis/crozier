

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
from ..types.watch_rota import WatchRota
from .types.plan_voyage_rota_response import PlanVoyageRotaResponse
from .types.set_voyage_watch_response import SetVoyageWatchResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVoyagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def set_voyage_watch(
        self, voyage_id: str, *, rota: WatchRota, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SetVoyageWatchResponse]:
        """
        A nested field the request example gives an empty array.

        Parameters
        ----------
        voyage_id : str

        rota : WatchRota

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SetVoyageWatchResponse]
            Set
        """
        _response = self._client_wrapper.httpx_client.request(
            f"voyages/{encode_path_param(voyage_id)}/watch",
            method="PUT",
            json={
                "rota": convert_and_respect_annotation_metadata(object_=rota, annotation=WatchRota, direction="write"),
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
                    SetVoyageWatchResponse,
                    parse_obj_as(
                        type_=SetVoyageWatchResponse,
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

    def plan_voyage_rota(
        self, voyage_id: str, *, crew: str, rota: WatchRota, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PlanVoyageRotaResponse]:
        """
        The same field left out of a referenced body's referenced named example.

        Parameters
        ----------
        voyage_id : str

        crew : str

        rota : WatchRota

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PlanVoyageRotaResponse]
            Planned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"voyages/{encode_path_param(voyage_id)}/rota",
            method="POST",
            json={
                "crew": crew,
                "rota": convert_and_respect_annotation_metadata(object_=rota, annotation=WatchRota, direction="write"),
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
                    PlanVoyageRotaResponse,
                    parse_obj_as(
                        type_=PlanVoyageRotaResponse,
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


class AsyncRawVoyagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def set_voyage_watch(
        self, voyage_id: str, *, rota: WatchRota, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SetVoyageWatchResponse]:
        """
        A nested field the request example gives an empty array.

        Parameters
        ----------
        voyage_id : str

        rota : WatchRota

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SetVoyageWatchResponse]
            Set
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"voyages/{encode_path_param(voyage_id)}/watch",
            method="PUT",
            json={
                "rota": convert_and_respect_annotation_metadata(object_=rota, annotation=WatchRota, direction="write"),
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
                    SetVoyageWatchResponse,
                    parse_obj_as(
                        type_=SetVoyageWatchResponse,
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

    async def plan_voyage_rota(
        self, voyage_id: str, *, crew: str, rota: WatchRota, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PlanVoyageRotaResponse]:
        """
        The same field left out of a referenced body's referenced named example.

        Parameters
        ----------
        voyage_id : str

        crew : str

        rota : WatchRota

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PlanVoyageRotaResponse]
            Planned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"voyages/{encode_path_param(voyage_id)}/rota",
            method="POST",
            json={
                "crew": crew,
                "rota": convert_and_respect_annotation_metadata(object_=rota, annotation=WatchRota, direction="write"),
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
                    PlanVoyageRotaResponse,
                    parse_obj_as(
                        type_=PlanVoyageRotaResponse,
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
