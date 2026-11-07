

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.collected_data import CollectedData
from ..types.problem_details import ProblemDetails
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawHeartBeatClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_api_v1heart_beat(
        self,
        *,
        agent_version: typing.Optional[str] = OMIT,
        collected_data_list: typing.Optional[typing.Sequence[CollectedData]] = OMIT,
        environment_id: typing.Optional[str] = OMIT,
        resource_id: typing.Optional[str] = OMIT,
        time_stamp: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        agent_version : typing.Optional[str]

        collected_data_list : typing.Optional[typing.Sequence[CollectedData]]

        environment_id : typing.Optional[str]

        resource_id : typing.Optional[str]

        time_stamp : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/HeartBeat",
            method="POST",
            json={
                "agentVersion": agent_version,
                "collectedDataList": convert_and_respect_annotation_metadata(
                    object_=collected_data_list,
                    annotation=typing.Optional[typing.Sequence[CollectedData]],
                    direction="write",
                ),
                "environmentId": environment_id,
                "resourceId": resource_id,
                "timeStamp": time_stamp,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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


class AsyncRawHeartBeatClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_api_v1heart_beat(
        self,
        *,
        agent_version: typing.Optional[str] = OMIT,
        collected_data_list: typing.Optional[typing.Sequence[CollectedData]] = OMIT,
        environment_id: typing.Optional[str] = OMIT,
        resource_id: typing.Optional[str] = OMIT,
        time_stamp: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        agent_version : typing.Optional[str]

        collected_data_list : typing.Optional[typing.Sequence[CollectedData]]

        environment_id : typing.Optional[str]

        resource_id : typing.Optional[str]

        time_stamp : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/HeartBeat",
            method="POST",
            json={
                "agentVersion": agent_version,
                "collectedDataList": convert_and_respect_annotation_metadata(
                    object_=collected_data_list,
                    annotation=typing.Optional[typing.Sequence[CollectedData]],
                    direction="write",
                ),
                "environmentId": environment_id,
                "resourceId": resource_id,
                "timeStamp": time_stamp,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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
