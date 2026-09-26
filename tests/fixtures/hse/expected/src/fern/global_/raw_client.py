

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
from ..errors.locked_error import LockedError
from ..errors.not_found_error import NotFoundError
from ..types.error import Error
from ..types.events import Events
from ..types.performance_counters import PerformanceCounters
from .types.kmc_vmstat_get_response_item import KmcVmstatGetResponseItem
from .types.param_get_response import ParamGetResponse
from .types.param_set_request_body import ParamSetRequestBody
from .types.params_get_response import ParamsGetResponse
from .types.workqueues_get_response_item import WorkqueuesGetResponseItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGlobalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def events_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Events]:
        """
        Get all event counter information.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Events]
            Successfully retrieved event counter information.
        """
        _response = self._client_wrapper.httpx_client.request(
            "events",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Events,
                    parse_obj_as(
                        type_=Events,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def events_in_file_get(
        self,
        file: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Events]:
        """
        Get all event counter information for file.

        Parameters
        ----------
        file : str
            Basename of file.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Events]
            Successfully retrieved event counter information.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"events/{encode_path_param(file)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Events,
                    parse_obj_as(
                        type_=Events,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def events_in_file_in_function_get(
        self,
        file: str,
        function: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Events]:
        """
        Get all event counter information for function in file.

        Parameters
        ----------
        file : str
            Basename of file.

        function : str
            Function name.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Events]
            Successfully retrieved event counter information.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"events/{encode_path_param(file)}/{encode_path_param(function)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Events,
                    parse_obj_as(
                        type_=Events,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def events_in_file_in_function_on_lineno_get(
        self,
        file: str,
        function: str,
        lineno: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Events]:
        """
        Get all event counter information for function on line number of file.

        Parameters
        ----------
        file : str
            Basename of file.

        function : str
            Function name.

        lineno : str
            Line number.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Events]
            Successfully retrieved event counter information.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"events/{encode_path_param(file)}/{encode_path_param(function)}/{encode_path_param(lineno)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Events,
                    parse_obj_as(
                        type_=Events,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def kmc_vmstat_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[KmcVmstatGetResponseItem]]:
        """
        Get virtual memory statistics.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[KmcVmstatGetResponseItem]]
            Successfully retrieved virtual memory statistics.
        """
        _response = self._client_wrapper.httpx_client.request(
            "kmc/vmstat",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[KmcVmstatGetResponseItem],
                    parse_obj_as(
                        type_=typing.List[KmcVmstatGetResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def params_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ParamsGetResponse]:
        """
        Get all global parameters.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParamsGetResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "params",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParamsGetResponse,
                    parse_obj_as(
                        type_=ParamsGetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def param_get(
        self,
        param: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParamGetResponse]:
        """
        Get the value of the global parameter.

        Parameters
        ----------
        param : str
            Parameter to interact with.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParamGetResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"params/{encode_path_param(param)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParamGetResponse,
                    parse_obj_as(
                        type_=ParamGetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def param_set(
        self, param: str, *, request: ParamSetRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Set the value of the global parameter.

        Parameters
        ----------
        param : str
            Parameter to interact with.

        request : ParamSetRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"params/{encode_path_param(param)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ParamSetRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def perfc_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PerformanceCounters]:
        """
        Get all performance counter information.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PerformanceCounters]
            Successfully retrieved performance counter information.
        """
        _response = self._client_wrapper.httpx_client.request(
            "perfc",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PerformanceCounters,
                    parse_obj_as(
                        type_=PerformanceCounters,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def perfc_in_group_get(
        self,
        group: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PerformanceCounters]:
        """
        Get all performance counter information for group.

        Parameters
        ----------
        group : str
            Performance counter group.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PerformanceCounters]
            Successfully retrieved event counter information for group.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"perfc/{encode_path_param(group)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PerformanceCounters,
                    parse_obj_as(
                        type_=PerformanceCounters,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def perfc_in_group_in_set_get(
        self,
        group: str,
        set_: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PerformanceCounters]:
        """
        Get all performance counter information for group in set.

        Parameters
        ----------
        group : str
            Performance counter group.

        set_ : str
            Performance counter set.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PerformanceCounters]
            Successfully retrieved event counter information for group in set.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"perfc/{encode_path_param(group)}/{encode_path_param(set_)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PerformanceCounters,
                    parse_obj_as(
                        type_=PerformanceCounters,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def perfc_in_group_in_set_with_name_get(
        self,
        group: str,
        set_: str,
        counter_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PerformanceCounters]:
        """
        Get all performance counter information for group in set with name.

        Parameters
        ----------
        group : str
            Performance counter group.

        set_ : str
            Performance counter set.

        counter_name : str
            Performance counter name.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PerformanceCounters]
            Successfully retrieved event counter information for group in set with name.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"perfc/{encode_path_param(group)}/{encode_path_param(set_)}/{encode_path_param(counter_name)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PerformanceCounters,
                    parse_obj_as(
                        type_=PerformanceCounters,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def workqueues_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[WorkqueuesGetResponseItem]]:
        """
        Get the process' `/proc/self/task/[tid]/stat` information.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[WorkqueuesGetResponseItem]]
            Successfully retrieved all workqueue information.
        """
        _response = self._client_wrapper.httpx_client.request(
            "workqueues",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WorkqueuesGetResponseItem],
                    parse_obj_as(
                        type_=typing.List[WorkqueuesGetResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawGlobalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def events_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Events]:
        """
        Get all event counter information.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Events]
            Successfully retrieved event counter information.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "events",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Events,
                    parse_obj_as(
                        type_=Events,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def events_in_file_get(
        self,
        file: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Events]:
        """
        Get all event counter information for file.

        Parameters
        ----------
        file : str
            Basename of file.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Events]
            Successfully retrieved event counter information.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"events/{encode_path_param(file)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Events,
                    parse_obj_as(
                        type_=Events,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def events_in_file_in_function_get(
        self,
        file: str,
        function: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Events]:
        """
        Get all event counter information for function in file.

        Parameters
        ----------
        file : str
            Basename of file.

        function : str
            Function name.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Events]
            Successfully retrieved event counter information.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"events/{encode_path_param(file)}/{encode_path_param(function)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Events,
                    parse_obj_as(
                        type_=Events,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def events_in_file_in_function_on_lineno_get(
        self,
        file: str,
        function: str,
        lineno: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Events]:
        """
        Get all event counter information for function on line number of file.

        Parameters
        ----------
        file : str
            Basename of file.

        function : str
            Function name.

        lineno : str
            Line number.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Events]
            Successfully retrieved event counter information.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"events/{encode_path_param(file)}/{encode_path_param(function)}/{encode_path_param(lineno)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Events,
                    parse_obj_as(
                        type_=Events,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def kmc_vmstat_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[KmcVmstatGetResponseItem]]:
        """
        Get virtual memory statistics.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[KmcVmstatGetResponseItem]]
            Successfully retrieved virtual memory statistics.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "kmc/vmstat",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[KmcVmstatGetResponseItem],
                    parse_obj_as(
                        type_=typing.List[KmcVmstatGetResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def params_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ParamsGetResponse]:
        """
        Get all global parameters.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParamsGetResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "params",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParamsGetResponse,
                    parse_obj_as(
                        type_=ParamsGetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def param_get(
        self,
        param: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParamGetResponse]:
        """
        Get the value of the global parameter.

        Parameters
        ----------
        param : str
            Parameter to interact with.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParamGetResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"params/{encode_path_param(param)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParamGetResponse,
                    parse_obj_as(
                        type_=ParamGetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def param_set(
        self, param: str, *, request: ParamSetRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Set the value of the global parameter.

        Parameters
        ----------
        param : str
            Parameter to interact with.

        request : ParamSetRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"params/{encode_path_param(param)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ParamSetRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def perfc_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PerformanceCounters]:
        """
        Get all performance counter information.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PerformanceCounters]
            Successfully retrieved performance counter information.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "perfc",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PerformanceCounters,
                    parse_obj_as(
                        type_=PerformanceCounters,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def perfc_in_group_get(
        self,
        group: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PerformanceCounters]:
        """
        Get all performance counter information for group.

        Parameters
        ----------
        group : str
            Performance counter group.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PerformanceCounters]
            Successfully retrieved event counter information for group.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"perfc/{encode_path_param(group)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PerformanceCounters,
                    parse_obj_as(
                        type_=PerformanceCounters,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def perfc_in_group_in_set_get(
        self,
        group: str,
        set_: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PerformanceCounters]:
        """
        Get all performance counter information for group in set.

        Parameters
        ----------
        group : str
            Performance counter group.

        set_ : str
            Performance counter set.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PerformanceCounters]
            Successfully retrieved event counter information for group in set.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"perfc/{encode_path_param(group)}/{encode_path_param(set_)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PerformanceCounters,
                    parse_obj_as(
                        type_=PerformanceCounters,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def perfc_in_group_in_set_with_name_get(
        self,
        group: str,
        set_: str,
        counter_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PerformanceCounters]:
        """
        Get all performance counter information for group in set with name.

        Parameters
        ----------
        group : str
            Performance counter group.

        set_ : str
            Performance counter set.

        counter_name : str
            Performance counter name.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PerformanceCounters]
            Successfully retrieved event counter information for group in set with name.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"perfc/{encode_path_param(group)}/{encode_path_param(set_)}/{encode_path_param(counter_name)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PerformanceCounters,
                    parse_obj_as(
                        type_=PerformanceCounters,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def workqueues_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[WorkqueuesGetResponseItem]]:
        """
        Get the process' `/proc/self/task/[tid]/stat` information.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[WorkqueuesGetResponseItem]]
            Successfully retrieved all workqueue information.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "workqueues",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WorkqueuesGetResponseItem],
                    parse_obj_as(
                        type_=typing.List[WorkqueuesGetResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
