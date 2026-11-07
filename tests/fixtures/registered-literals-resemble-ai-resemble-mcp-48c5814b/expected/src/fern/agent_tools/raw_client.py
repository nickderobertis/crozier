

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.create_agent_tool_request_tool_type import CreateAgentToolRequestToolType
from .types.create_agent_tool_response import CreateAgentToolResponse
from .types.delete_agent_tool_response import DeleteAgentToolResponse
from .types.get_agent_tool_response import GetAgentToolResponse
from .types.list_agent_tools_response import ListAgentToolsResponse
from .types.update_agent_tool_response import UpdateAgentToolResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAgentToolsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_agent_tools(
        self, agent_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListAgentToolsResponse]:
        """
        List all tools for an agent

        Parameters
        ----------
        agent_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListAgentToolsResponse]
            List of tools
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/tools",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAgentToolsResponse,
                    parse_obj_as(
                        type_=ListAgentToolsResponse,
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

    def create_agent_tool(
        self,
        agent_uuid: str,
        *,
        name: str,
        description: str,
        tool_type: CreateAgentToolRequestToolType,
        tool_config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAgentToolResponse]:
        """
        Create a new tool for an agent

        Parameters
        ----------
        agent_uuid : str

        name : str

        description : str

        tool_type : CreateAgentToolRequestToolType

        tool_config : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateAgentToolResponse]
            Tool created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/tools",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "name": name,
                "description": description,
                "tool_type": tool_type,
                "tool_config": tool_config,
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
                    CreateAgentToolResponse,
                    parse_obj_as(
                        type_=CreateAgentToolResponse,
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

    def get_agent_tool(
        self, agent_uuid: str, tool_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAgentToolResponse]:
        """
        Get details of a specific tool

        Parameters
        ----------
        agent_uuid : str

        tool_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAgentToolResponse]
            Tool details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/tools/{encode_path_param(tool_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentToolResponse,
                    parse_obj_as(
                        type_=GetAgentToolResponse,
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

    def delete_agent_tool(
        self, agent_uuid: str, tool_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteAgentToolResponse]:
        """
        Delete a tool

        Parameters
        ----------
        agent_uuid : str

        tool_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteAgentToolResponse]
            Tool deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/tools/{encode_path_param(tool_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAgentToolResponse,
                    parse_obj_as(
                        type_=DeleteAgentToolResponse,
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

    def update_agent_tool(
        self,
        agent_uuid: str,
        tool_uuid: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tool_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateAgentToolResponse]:
        """
        Update an existing tool

        Parameters
        ----------
        agent_uuid : str

        tool_uuid : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        tool_config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateAgentToolResponse]
            Tool updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/tools/{encode_path_param(tool_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "tool_config": tool_config,
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
                    UpdateAgentToolResponse,
                    parse_obj_as(
                        type_=UpdateAgentToolResponse,
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


class AsyncRawAgentToolsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_agent_tools(
        self, agent_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListAgentToolsResponse]:
        """
        List all tools for an agent

        Parameters
        ----------
        agent_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListAgentToolsResponse]
            List of tools
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/tools",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAgentToolsResponse,
                    parse_obj_as(
                        type_=ListAgentToolsResponse,
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

    async def create_agent_tool(
        self,
        agent_uuid: str,
        *,
        name: str,
        description: str,
        tool_type: CreateAgentToolRequestToolType,
        tool_config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateAgentToolResponse]:
        """
        Create a new tool for an agent

        Parameters
        ----------
        agent_uuid : str

        name : str

        description : str

        tool_type : CreateAgentToolRequestToolType

        tool_config : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateAgentToolResponse]
            Tool created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/tools",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "name": name,
                "description": description,
                "tool_type": tool_type,
                "tool_config": tool_config,
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
                    CreateAgentToolResponse,
                    parse_obj_as(
                        type_=CreateAgentToolResponse,
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

    async def get_agent_tool(
        self, agent_uuid: str, tool_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAgentToolResponse]:
        """
        Get details of a specific tool

        Parameters
        ----------
        agent_uuid : str

        tool_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAgentToolResponse]
            Tool details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/tools/{encode_path_param(tool_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentToolResponse,
                    parse_obj_as(
                        type_=GetAgentToolResponse,
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

    async def delete_agent_tool(
        self, agent_uuid: str, tool_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteAgentToolResponse]:
        """
        Delete a tool

        Parameters
        ----------
        agent_uuid : str

        tool_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteAgentToolResponse]
            Tool deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/tools/{encode_path_param(tool_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAgentToolResponse,
                    parse_obj_as(
                        type_=DeleteAgentToolResponse,
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

    async def update_agent_tool(
        self,
        agent_uuid: str,
        tool_uuid: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tool_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateAgentToolResponse]:
        """
        Update an existing tool

        Parameters
        ----------
        agent_uuid : str

        tool_uuid : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        tool_config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateAgentToolResponse]
            Tool updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/tools/{encode_path_param(tool_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "tool_config": tool_config,
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
                    UpdateAgentToolResponse,
                    parse_obj_as(
                        type_=UpdateAgentToolResponse,
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
