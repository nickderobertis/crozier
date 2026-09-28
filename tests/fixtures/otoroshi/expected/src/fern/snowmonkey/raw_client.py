

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.done import Done
from ..types.empty import Empty
from ..types.error_response import ErrorResponse
from ..types.otoroshi_models_snow_monkey_config import OtoroshiModelsSnowMonkeyConfig
from ..types.outages_list import OutagesList
from ..types.patch_body import PatchBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSnowmonkeyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Done]:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Done]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/snowmonkey/_start",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Done]:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Done]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/snowmonkey/_stop",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OutagesList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OutagesList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/snowmonkey/outages",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OutagesList,
                    parse_obj_as(
                        type_=OutagesList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Done]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Done]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/snowmonkey/outages",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiModelsSnowMonkeyConfig]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsSnowMonkeyConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/snowmonkey/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsSnowMonkeyConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsSnowMonkeyConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey(
        self,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        outage_duration_to: typing.Optional[float] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        times_per_day: typing.Optional[int] = OMIT,
        outage_duration_from: typing.Optional[float] = OMIT,
        start_time: typing.Optional[str] = OMIT,
        include_user_facing_descriptors: typing.Optional[bool] = OMIT,
        target_groups: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stop_time: typing.Optional[str] = OMIT,
        outage_strategy: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiModelsSnowMonkeyConfig]:
        """
        Parameters
        ----------
        dry_run : typing.Optional[bool]
            Whether or not outages will actualy impact requests

        outage_duration_to : typing.Optional[float]
            End of outage duration range

        chaos_config : typing.Optional[typing.Any]

        times_per_day : typing.Optional[int]
            Number of time per day each service will be outage

        outage_duration_from : typing.Optional[float]
            Start of outage duration range

        start_time : typing.Optional[str]
            Start time of Snow Monkey each day

        include_user_facing_descriptors : typing.Optional[bool]
            Whether or not user facing apps. will be impacted by Snow Monkey

        target_groups : typing.Optional[typing.Sequence[str]]
            Groups impacted by Snow Monkey. If empty, all groups will be impacted

        enabled : typing.Optional[bool]
            Whether or not this config is enabled

        stop_time : typing.Optional[str]
            Stop time of Snow Monkey each day

        outage_strategy : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsSnowMonkeyConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/snowmonkey/config",
            method="PUT",
            json={
                "dryRun": dry_run,
                "outageDurationTo": outage_duration_to,
                "chaosConfig": chaos_config,
                "timesPerDay": times_per_day,
                "outageDurationFrom": outage_duration_from,
                "startTime": start_time,
                "includeUserFacingDescriptors": include_user_facing_descriptors,
                "targetGroups": target_groups,
                "enabled": enabled,
                "stopTime": stop_time,
                "outageStrategy": outage_strategy,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsSnowMonkeyConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsSnowMonkeyConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey(
        self, *, request: PatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiModelsSnowMonkeyConfig]:
        """
        Parameters
        ----------
        request : PatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsSnowMonkeyConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/snowmonkey/config",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=PatchBody, direction="write"),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsSnowMonkeyConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsSnowMonkeyConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawSnowmonkeyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Done]:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Done]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/snowmonkey/_start",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Done]:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Done]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/snowmonkey/_stop",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OutagesList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OutagesList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/snowmonkey/outages",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OutagesList,
                    parse_obj_as(
                        type_=OutagesList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Done]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Done]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/snowmonkey/outages",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Done,
                    parse_obj_as(
                        type_=Done,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiModelsSnowMonkeyConfig]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsSnowMonkeyConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/snowmonkey/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsSnowMonkeyConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsSnowMonkeyConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey(
        self,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        outage_duration_to: typing.Optional[float] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        times_per_day: typing.Optional[int] = OMIT,
        outage_duration_from: typing.Optional[float] = OMIT,
        start_time: typing.Optional[str] = OMIT,
        include_user_facing_descriptors: typing.Optional[bool] = OMIT,
        target_groups: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stop_time: typing.Optional[str] = OMIT,
        outage_strategy: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiModelsSnowMonkeyConfig]:
        """
        Parameters
        ----------
        dry_run : typing.Optional[bool]
            Whether or not outages will actualy impact requests

        outage_duration_to : typing.Optional[float]
            End of outage duration range

        chaos_config : typing.Optional[typing.Any]

        times_per_day : typing.Optional[int]
            Number of time per day each service will be outage

        outage_duration_from : typing.Optional[float]
            Start of outage duration range

        start_time : typing.Optional[str]
            Start time of Snow Monkey each day

        include_user_facing_descriptors : typing.Optional[bool]
            Whether or not user facing apps. will be impacted by Snow Monkey

        target_groups : typing.Optional[typing.Sequence[str]]
            Groups impacted by Snow Monkey. If empty, all groups will be impacted

        enabled : typing.Optional[bool]
            Whether or not this config is enabled

        stop_time : typing.Optional[str]
            Stop time of Snow Monkey each day

        outage_strategy : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsSnowMonkeyConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/snowmonkey/config",
            method="PUT",
            json={
                "dryRun": dry_run,
                "outageDurationTo": outage_duration_to,
                "chaosConfig": chaos_config,
                "timesPerDay": times_per_day,
                "outageDurationFrom": outage_duration_from,
                "startTime": start_time,
                "includeUserFacingDescriptors": include_user_facing_descriptors,
                "targetGroups": target_groups,
                "enabled": enabled,
                "stopTime": stop_time,
                "outageStrategy": outage_strategy,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsSnowMonkeyConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsSnowMonkeyConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey(
        self, *, request: PatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiModelsSnowMonkeyConfig]:
        """
        Parameters
        ----------
        request : PatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsSnowMonkeyConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/snowmonkey/config",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=PatchBody, direction="write"),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsSnowMonkeyConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsSnowMonkeyConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
