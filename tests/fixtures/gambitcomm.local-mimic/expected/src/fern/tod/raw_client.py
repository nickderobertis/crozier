

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.config_tod import ConfigTod


class RawTodClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def protocol_tod_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Optional[typing.Any]]]:
        """
        Agent's TOD configuration

        Parameters
        ----------
        agent_num : int
            Agent to show the TOD argument structure

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Optional[typing.Any]]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/get/args",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Optional[typing.Any]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Optional[typing.Any]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def protocol_tod_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConfigTod]:
        """
        Agent's TOD configuration

        Parameters
        ----------
        agent_num : int
            Agent to show the TOD configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfigTod]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/get/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigTod,
                    parse_obj_as(
                        type_=ConfigTod,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def protocol_tod_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[int]]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show TOD statistics

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[int]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/get/statistics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[int],
                    parse_obj_as(
                        type_=typing.List[int],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def protocol_tod_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConfigTod]:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether TOD tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfigTod]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/get/trace",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigTod,
                    parse_obj_as(
                        type_=ConfigTod,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def protocol_tod_gettime(
        self,
        agent_num: int,
        server_addr: str,
        port_num: int,
        script_name: str,
        time_sec: int,
        num_retries: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Retrive time from server

        Parameters
        ----------
        agent_num : int
            Agent to show TOD return

        server_addr : str
            serverAddr

        port_num : int
            portNum

        script_name : str
            scriptName

        time_sec : int
            timeSec

        num_retries : int
            numRetries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/gettime/server/{jsonable_encoder(server_addr)}/port/{jsonable_encoder(port_num)}/script/{jsonable_encoder(script_name)}/timeout/{jsonable_encoder(time_sec)}/retries/{jsonable_encoder(num_retries)}",
            method="GET",
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def protocol_tod_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Agent's TOD configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the TOD configuration

        argument : str
            Parameter to set the TOD configuration

        value : str
            Value to set the TOD configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/set/config/{jsonable_encoder(argument)}/{jsonable_encoder(value)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def protocol_tod_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the TOD tracing

        enable_or_not : str
            Value to set the TOD tracing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/set/trace/{jsonable_encoder(enable_or_not)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def protocol_tod_get_stats_hdr(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        The headers of statistics fields

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "mimic/protocol/msg/tod/get/stats_hdr",
            method="GET",
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTodClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def protocol_tod_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Optional[typing.Any]]]:
        """
        Agent's TOD configuration

        Parameters
        ----------
        agent_num : int
            Agent to show the TOD argument structure

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Optional[typing.Any]]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/get/args",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Optional[typing.Any]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Optional[typing.Any]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def protocol_tod_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConfigTod]:
        """
        Agent's TOD configuration

        Parameters
        ----------
        agent_num : int
            Agent to show the TOD configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfigTod]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/get/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigTod,
                    parse_obj_as(
                        type_=ConfigTod,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def protocol_tod_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[int]]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show TOD statistics

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[int]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/get/statistics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[int],
                    parse_obj_as(
                        type_=typing.List[int],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def protocol_tod_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConfigTod]:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether TOD tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfigTod]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/get/trace",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigTod,
                    parse_obj_as(
                        type_=ConfigTod,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def protocol_tod_gettime(
        self,
        agent_num: int,
        server_addr: str,
        port_num: int,
        script_name: str,
        time_sec: int,
        num_retries: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Retrive time from server

        Parameters
        ----------
        agent_num : int
            Agent to show TOD return

        server_addr : str
            serverAddr

        port_num : int
            portNum

        script_name : str
            scriptName

        time_sec : int
            timeSec

        num_retries : int
            numRetries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/gettime/server/{jsonable_encoder(server_addr)}/port/{jsonable_encoder(port_num)}/script/{jsonable_encoder(script_name)}/timeout/{jsonable_encoder(time_sec)}/retries/{jsonable_encoder(num_retries)}",
            method="GET",
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def protocol_tod_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Agent's TOD configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the TOD configuration

        argument : str
            Parameter to set the TOD configuration

        value : str
            Value to set the TOD configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/set/config/{jsonable_encoder(argument)}/{jsonable_encoder(value)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def protocol_tod_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the TOD tracing

        enable_or_not : str
            Value to set the TOD tracing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{jsonable_encoder(agent_num)}/protocol/msg/tod/set/trace/{jsonable_encoder(enable_or_not)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def protocol_tod_get_stats_hdr(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        The headers of statistics fields

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mimic/protocol/msg/tod/get/stats_hdr",
            method="GET",
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
