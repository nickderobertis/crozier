

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
from ..types.performance_counters import PerformanceCounters
from .types.kvs_cn_tree_get_response import KvsCnTreeGetResponse
from .types.kvs_param_get_response import KvsParamGetResponse
from .types.kvs_param_set_request_body import KvsParamSetRequestBody
from .types.kvs_params_get_response import KvsParamsGetResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawKvsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def cn_tree_get(
        self,
        alias: str,
        kvs_name: str,
        *,
        human: typing.Optional[bool] = None,
        kvsets: typing.Optional[bool] = None,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[KvsCnTreeGetResponse]:
        """
        Get information about the KVS's cN tree.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        human : typing.Optional[bool]
            Humanize certain values.

        kvsets : typing.Optional[bool]
            Include kvset details in output.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KvsCnTreeGetResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/cn/tree",
            method="GET",
            params={
                "human": human,
                "kvsets": kvsets,
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KvsCnTreeGetResponse,
                    parse_obj_as(
                        type_=KvsCnTreeGetResponse,
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
        self,
        alias: str,
        kvs_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[KvsParamsGetResponse]:
        """
        Get all KVS parameters.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KvsParamsGetResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/params",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KvsParamsGetResponse,
                    parse_obj_as(
                        type_=KvsParamsGetResponse,
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

    def param_get(
        self,
        alias: str,
        kvs_name: str,
        param: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[KvsParamGetResponse]:
        """
        Get the value of the KVS parameter.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        param : str
            Parameter to interact with.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KvsParamGetResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/params/{encode_path_param(param)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KvsParamGetResponse,
                    parse_obj_as(
                        type_=KvsParamGetResponse,
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
        self,
        alias: str,
        kvs_name: str,
        param: str,
        *,
        request: KvsParamSetRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Set the value of the KVS parameter.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        param : str
            Parameter to interact with.

        request : KvsParamSetRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/params/{encode_path_param(param)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=KvsParamSetRequestBody, direction="write"
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
        self,
        alias: str,
        kvs_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PerformanceCounters]:
        """
        Get all performance counter information.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

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
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/perfc",
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

    def perfc_in_set_get(
        self,
        alias: str,
        kvs_name: str,
        set_: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PerformanceCounters]:
        """
        Get all performance counter information.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        set_ : str
            Performance counter set.

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
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/perfc/{encode_path_param(set_)}",
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

    def perfc_in_set_with_name_get(
        self,
        alias: str,
        kvs_name: str,
        set_: str,
        counter_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PerformanceCounters]:
        """
        Get all performance counter information.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

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
            Successfully retrieved performance counter information.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/perfc/{encode_path_param(set_)}/{encode_path_param(counter_name)}",
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


class AsyncRawKvsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def cn_tree_get(
        self,
        alias: str,
        kvs_name: str,
        *,
        human: typing.Optional[bool] = None,
        kvsets: typing.Optional[bool] = None,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[KvsCnTreeGetResponse]:
        """
        Get information about the KVS's cN tree.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        human : typing.Optional[bool]
            Humanize certain values.

        kvsets : typing.Optional[bool]
            Include kvset details in output.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KvsCnTreeGetResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/cn/tree",
            method="GET",
            params={
                "human": human,
                "kvsets": kvsets,
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KvsCnTreeGetResponse,
                    parse_obj_as(
                        type_=KvsCnTreeGetResponse,
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
        self,
        alias: str,
        kvs_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[KvsParamsGetResponse]:
        """
        Get all KVS parameters.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KvsParamsGetResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/params",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KvsParamsGetResponse,
                    parse_obj_as(
                        type_=KvsParamsGetResponse,
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

    async def param_get(
        self,
        alias: str,
        kvs_name: str,
        param: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[KvsParamGetResponse]:
        """
        Get the value of the KVS parameter.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        param : str
            Parameter to interact with.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KvsParamGetResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/params/{encode_path_param(param)}",
            method="GET",
            params={
                "pretty": pretty,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KvsParamGetResponse,
                    parse_obj_as(
                        type_=KvsParamGetResponse,
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
        self,
        alias: str,
        kvs_name: str,
        param: str,
        *,
        request: KvsParamSetRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Set the value of the KVS parameter.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        param : str
            Parameter to interact with.

        request : KvsParamSetRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/params/{encode_path_param(param)}",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=KvsParamSetRequestBody, direction="write"
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
        self,
        alias: str,
        kvs_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PerformanceCounters]:
        """
        Get all performance counter information.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

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
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/perfc",
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

    async def perfc_in_set_get(
        self,
        alias: str,
        kvs_name: str,
        set_: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PerformanceCounters]:
        """
        Get all performance counter information.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        set_ : str
            Performance counter set.

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
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/perfc/{encode_path_param(set_)}",
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

    async def perfc_in_set_with_name_get(
        self,
        alias: str,
        kvs_name: str,
        set_: str,
        counter_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PerformanceCounters]:
        """
        Get all performance counter information.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

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
            Successfully retrieved performance counter information.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"kvdbs/{encode_path_param(alias)}/kvs/{encode_path_param(kvs_name)}/perfc/{encode_path_param(set_)}/{encode_path_param(counter_name)}",
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
