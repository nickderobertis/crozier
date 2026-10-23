

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.not_found_error_body import NotFoundErrorBody
from ..types.too_many_requests_error_body import TooManyRequestsErrorBody
from .types.get_chains_chain_id_status_response import GetChainsChainIdStatusResponse
from .types.get_status_response import GetStatusResponse
from pydantic import ValidationError


class RawStatusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def whether_the_registry_is_live_the_daemons_heartbeat_every_job_against_its_cadence_the_scanners_still_reading_history_and_the_age_of_every_published_figure(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetChainsChainIdStatusResponse]:
        """
        Public. Always 200; the verdict is in the body ('live', 'degraded', 'stale', 'never'), so a stale registry is a fact to read rather than an error to retry. Each job carries its cadence, last successful run, age and verdict ('fresh', 'late', 'failing', 'filling', 'stalled', 'never'); metadataBacklog reports the measured due, visible, never-read and failed token counts after the last successful metadata batch; filling does not mean complete coverage; each figure names the job that writes it and the newest timestamp behind it. Also served at /api/v1/status.

        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdStatusResponse]
            Freshness
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdStatusResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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

    def alias_of_chains4663status_whether_the_registry_is_live(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetStatusResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetStatusResponse]
            Freshness
        """
        _response = self._client_wrapper.httpx_client.request(
            "status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetStatusResponse,
                    parse_obj_as(
                        type_=GetStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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


class AsyncRawStatusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def whether_the_registry_is_live_the_daemons_heartbeat_every_job_against_its_cadence_the_scanners_still_reading_history_and_the_age_of_every_published_figure(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetChainsChainIdStatusResponse]:
        """
        Public. Always 200; the verdict is in the body ('live', 'degraded', 'stale', 'never'), so a stale registry is a fact to read rather than an error to retry. Each job carries its cadence, last successful run, age and verdict ('fresh', 'late', 'failing', 'filling', 'stalled', 'never'); metadataBacklog reports the measured due, visible, never-read and failed token counts after the last successful metadata batch; filling does not mean complete coverage; each figure names the job that writes it and the newest timestamp behind it. Also served at /api/v1/status.

        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdStatusResponse]
            Freshness
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdStatusResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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

    async def alias_of_chains4663status_whether_the_registry_is_live(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetStatusResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetStatusResponse]
            Freshness
        """
        _response = await self._client_wrapper.httpx_client.request(
            "status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetStatusResponse,
                    parse_obj_as(
                        type_=GetStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
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
