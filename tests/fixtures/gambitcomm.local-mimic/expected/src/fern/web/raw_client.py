

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.config_web import ConfigWeb
from pydantic import ValidationError


class RawWebClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def protocol_web_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the WEB argument structure

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/get/args",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def protocol_web_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConfigWeb]:
        """
        Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the WEB configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfigWeb]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/get/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigWeb,
                    parse_obj_as(
                        type_=ConfigWeb,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def protocol_web_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[int]]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show WEB statistics

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[int]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/get/statistics",
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

    def protocol_web_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConfigWeb]:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether WEB tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfigWeb]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/get/trace",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigWeb,
                    parse_obj_as(
                        type_=ConfigWeb,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def protocol_web_port_add(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Add port

        Parameters
        ----------
        agent_num : int
            Agent to add WEB port

        port : int
            TCP port

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/port/add/{encode_path_param(port)}",
            method="POST",
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

    def protocol_web_port_exists(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        Check the port. 1 means existing, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show WEB configuration

        port : int
            TCP port

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/port/exists/{encode_path_param(port)}",
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

    def protocol_web_port_remove(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Remove port

        Parameters
        ----------
        agent_num : int
            Agent to remove WEB port

        port : int
            TCP port

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/port/remove/{encode_path_param(port)}",
            method="DELETE",
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

    def protocol_web_port_set(
        self,
        agent_num: int,
        port: int,
        protocol: str,
        version: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Set port

        Parameters
        ----------
        agent_num : int
            Agent to set WEB port

        port : int
            TCP port

        protocol : str
            Encryption or related protocol

        version : str
            Encryption or related protocol version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/port/set/{encode_path_param(port)}/{encode_path_param(protocol)}/{encode_path_param(version)}",
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

    def protocol_web_port_start(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Start port

        Parameters
        ----------
        agent_num : int
            Agent to start WEB port

        port : int
            TCP port

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/port/start/{encode_path_param(port)}",
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

    def protocol_web_port_stop(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Stop port

        Parameters
        ----------
        agent_num : int
            Agent to stop WEB port

        port : int
            TCP port

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/port/stop/{encode_path_param(port)}",
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

    def protocol_web_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the WEB configuration

        argument : str
            Parameter to set the WEB configuration

        value : str
            Value to set the WEB configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/set/config/{encode_path_param(argument)}/{encode_path_param(value)}",
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

    def protocol_web_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the WEB tracing

        enable_or_not : str
            Value to set the WEB tracing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/set/trace/{encode_path_param(enable_or_not)}",
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

    def protocol_web_get_stats_hdr(
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
            "mimic/protocol/msg/web/get/stats_hdr",
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


class AsyncRawWebClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def protocol_web_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the WEB argument structure

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/get/args",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def protocol_web_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConfigWeb]:
        """
        Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the WEB configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfigWeb]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/get/config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigWeb,
                    parse_obj_as(
                        type_=ConfigWeb,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def protocol_web_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[int]]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show WEB statistics

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[int]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/get/statistics",
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

    async def protocol_web_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConfigWeb]:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether WEB tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfigWeb]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/get/trace",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigWeb,
                    parse_obj_as(
                        type_=ConfigWeb,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def protocol_web_port_add(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Add port

        Parameters
        ----------
        agent_num : int
            Agent to add WEB port

        port : int
            TCP port

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/port/add/{encode_path_param(port)}",
            method="POST",
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

    async def protocol_web_port_exists(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Check the port. 1 means existing, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show WEB configuration

        port : int
            TCP port

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/port/exists/{encode_path_param(port)}",
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

    async def protocol_web_port_remove(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Remove port

        Parameters
        ----------
        agent_num : int
            Agent to remove WEB port

        port : int
            TCP port

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/port/remove/{encode_path_param(port)}",
            method="DELETE",
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

    async def protocol_web_port_set(
        self,
        agent_num: int,
        port: int,
        protocol: str,
        version: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Set port

        Parameters
        ----------
        agent_num : int
            Agent to set WEB port

        port : int
            TCP port

        protocol : str
            Encryption or related protocol

        version : str
            Encryption or related protocol version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/port/set/{encode_path_param(port)}/{encode_path_param(protocol)}/{encode_path_param(version)}",
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

    async def protocol_web_port_start(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Start port

        Parameters
        ----------
        agent_num : int
            Agent to start WEB port

        port : int
            TCP port

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/port/start/{encode_path_param(port)}",
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

    async def protocol_web_port_stop(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Stop port

        Parameters
        ----------
        agent_num : int
            Agent to stop WEB port

        port : int
            TCP port

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/port/stop/{encode_path_param(port)}",
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

    async def protocol_web_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the WEB configuration

        argument : str
            Parameter to set the WEB configuration

        value : str
            Value to set the WEB configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/set/config/{encode_path_param(argument)}/{encode_path_param(value)}",
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

    async def protocol_web_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the WEB tracing

        enable_or_not : str
            Value to set the WEB tracing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mimic/agent/{encode_path_param(agent_num)}/protocol/msg/web/set/trace/{encode_path_param(enable_or_not)}",
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

    async def protocol_web_get_stats_hdr(
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
            "mimic/protocol/msg/web/get/stats_hdr",
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
