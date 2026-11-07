

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
from .types.create_agent_request_asr import CreateAgentRequestAsr
from .types.create_agent_request_dynamic_variables_value import CreateAgentRequestDynamicVariablesValue
from .types.create_agent_request_llm import CreateAgentRequestLlm
from .types.create_agent_request_search_mode import CreateAgentRequestSearchMode
from .types.create_agent_request_turn import CreateAgentRequestTurn
from .types.create_agent_response import CreateAgentResponse
from .types.delete_agent_response import DeleteAgentResponse
from .types.dispatch_agent_response import DispatchAgentResponse
from .types.get_agent_capabilities_response import GetAgentCapabilitiesResponse
from .types.get_agent_response import GetAgentResponse
from .types.get_system_tools_response import GetSystemToolsResponse
from .types.list_agents_response import ListAgentsResponse
from .types.update_agent_request_search_mode import UpdateAgentRequestSearchMode
from .types.update_agent_response import UpdateAgentResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAgentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_agents(
        self,
        *,
        phone_number: typing.Optional[str] = None,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListAgentsResponse]:
        """
        Retrieve all agents for the authenticated team

        Parameters
        ----------
        phone_number : typing.Optional[str]
            Filter by associated phone number

        advanced : typing.Optional[bool]
            Include detailed configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListAgentsResponse]
            List of agents
        """
        _response = self._client_wrapper.httpx_client.request(
            "agents",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "phone_number": phone_number,
                "advanced": advanced,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAgentsResponse,
                    parse_obj_as(
                        type_=ListAgentsResponse,
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

    def create_agent(
        self,
        *,
        name: str,
        voice_uuid: str,
        phone_number_id: typing.Optional[int] = OMIT,
        languages: typing.Optional[typing.Sequence[str]] = OMIT,
        dynamic_variables: typing.Optional[typing.Dict[str, CreateAgentRequestDynamicVariablesValue]] = OMIT,
        asr: typing.Optional[CreateAgentRequestAsr] = OMIT,
        turn: typing.Optional[CreateAgentRequestTurn] = OMIT,
        llm: typing.Optional[CreateAgentRequestLlm] = OMIT,
        search_mode: typing.Optional[CreateAgentRequestSearchMode] = OMIT,
        max_chunks_per_query: typing.Optional[int] = OMIT,
        webhooks: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        system_tools: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAgentResponse]:
        """
        Create a new voice agent

        Parameters
        ----------
        name : str

        voice_uuid : str

        phone_number_id : typing.Optional[int]

        languages : typing.Optional[typing.Sequence[str]]

        dynamic_variables : typing.Optional[typing.Dict[str, CreateAgentRequestDynamicVariablesValue]]

        asr : typing.Optional[CreateAgentRequestAsr]

        turn : typing.Optional[CreateAgentRequestTurn]

        llm : typing.Optional[CreateAgentRequestLlm]

        search_mode : typing.Optional[CreateAgentRequestSearchMode]
            RAG search strategy - speed (faster) or accuracy (more thorough)

        max_chunks_per_query : typing.Optional[int]
            Number of relevant chunks to retrieve per query for RAG

        webhooks : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        system_tools : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateAgentResponse]
            Agent created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "agents",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "name": name,
                "voice_uuid": voice_uuid,
                "phone_number_id": phone_number_id,
                "languages": languages,
                "dynamic_variables": convert_and_respect_annotation_metadata(
                    object_=dynamic_variables,
                    annotation=typing.Dict[str, CreateAgentRequestDynamicVariablesValue],
                    direction="write",
                ),
                "asr": convert_and_respect_annotation_metadata(
                    object_=asr, annotation=CreateAgentRequestAsr, direction="write"
                ),
                "turn": convert_and_respect_annotation_metadata(
                    object_=turn, annotation=CreateAgentRequestTurn, direction="write"
                ),
                "llm": convert_and_respect_annotation_metadata(
                    object_=llm, annotation=CreateAgentRequestLlm, direction="write"
                ),
                "search_mode": search_mode,
                "max_chunks_per_query": max_chunks_per_query,
                "webhooks": webhooks,
                "system_tools": system_tools,
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
                    CreateAgentResponse,
                    parse_obj_as(
                        type_=CreateAgentResponse,
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

    def get_agent(
        self,
        uuid_: str,
        *,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentResponse]:
        """
        Retrieve a specific agent's details

        Parameters
        ----------
        uuid_ : str

        advanced : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAgentResponse]
            Agent details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "advanced": advanced,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentResponse,
                    parse_obj_as(
                        type_=GetAgentResponse,
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

    def delete_agent(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteAgentResponse]:
        """
        Delete an agent and all its configurations

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteAgentResponse]
            Agent deleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAgentResponse,
                    parse_obj_as(
                        type_=DeleteAgentResponse,
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

    def update_agent(
        self,
        uuid_: str,
        *,
        name: typing.Optional[str] = OMIT,
        voice_uuid: typing.Optional[str] = OMIT,
        phone_number_id: typing.Optional[int] = OMIT,
        languages: typing.Optional[typing.Sequence[str]] = OMIT,
        dynamic_variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        asr: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        turn: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        search_mode: typing.Optional[UpdateAgentRequestSearchMode] = OMIT,
        max_chunks_per_query: typing.Optional[int] = OMIT,
        webhooks: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        system_tools: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateAgentResponse]:
        """
        Update an existing agent's configuration

        Parameters
        ----------
        uuid_ : str

        name : typing.Optional[str]

        voice_uuid : typing.Optional[str]

        phone_number_id : typing.Optional[int]

        languages : typing.Optional[typing.Sequence[str]]

        dynamic_variables : typing.Optional[typing.Dict[str, typing.Any]]

        asr : typing.Optional[typing.Dict[str, typing.Any]]

        turn : typing.Optional[typing.Dict[str, typing.Any]]

        llm : typing.Optional[typing.Dict[str, typing.Any]]

        search_mode : typing.Optional[UpdateAgentRequestSearchMode]
            RAG search strategy

        max_chunks_per_query : typing.Optional[int]
            Number of chunks to retrieve per query for RAG

        webhooks : typing.Optional[typing.Sequence[typing.Any]]

        system_tools : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateAgentResponse]
            Agent updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "name": name,
                "voice_uuid": voice_uuid,
                "phone_number_id": phone_number_id,
                "languages": languages,
                "dynamic_variables": dynamic_variables,
                "asr": asr,
                "turn": turn,
                "llm": llm,
                "search_mode": search_mode,
                "max_chunks_per_query": max_chunks_per_query,
                "webhooks": webhooks,
                "system_tools": system_tools,
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
                    UpdateAgentResponse,
                    parse_obj_as(
                        type_=UpdateAgentResponse,
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

    def dispatch_agent(
        self,
        uuid_: str,
        *,
        phone_number: str,
        dynamic_variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DispatchAgentResponse]:
        """
        Make an outbound call with an agent

        Parameters
        ----------
        uuid_ : str

        phone_number : str
            Destination phone number

        dynamic_variables : typing.Optional[typing.Dict[str, typing.Any]]
            Runtime variable overrides

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DispatchAgentResponse]
            Call dispatched
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(uuid_)}/dispatch",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "phone_number": phone_number,
                "dynamic_variables": dynamic_variables,
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
                    DispatchAgentResponse,
                    parse_obj_as(
                        type_=DispatchAgentResponse,
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

    def get_agent_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAgentCapabilitiesResponse]:
        """
        List supported ASR and LLM providers and models

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAgentCapabilitiesResponse]
            Agent capabilities
        """
        _response = self._client_wrapper.httpx_client.request(
            "agents/capabilities",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentCapabilitiesResponse,
                    parse_obj_as(
                        type_=GetAgentCapabilitiesResponse,
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

    def get_system_tools(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSystemToolsResponse]:
        """
        List available system tools

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSystemToolsResponse]
            System tools
        """
        _response = self._client_wrapper.httpx_client.request(
            "agents/system-tools",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSystemToolsResponse,
                    parse_obj_as(
                        type_=GetSystemToolsResponse,
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


class AsyncRawAgentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_agents(
        self,
        *,
        phone_number: typing.Optional[str] = None,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListAgentsResponse]:
        """
        Retrieve all agents for the authenticated team

        Parameters
        ----------
        phone_number : typing.Optional[str]
            Filter by associated phone number

        advanced : typing.Optional[bool]
            Include detailed configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListAgentsResponse]
            List of agents
        """
        _response = await self._client_wrapper.httpx_client.request(
            "agents",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "phone_number": phone_number,
                "advanced": advanced,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAgentsResponse,
                    parse_obj_as(
                        type_=ListAgentsResponse,
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

    async def create_agent(
        self,
        *,
        name: str,
        voice_uuid: str,
        phone_number_id: typing.Optional[int] = OMIT,
        languages: typing.Optional[typing.Sequence[str]] = OMIT,
        dynamic_variables: typing.Optional[typing.Dict[str, CreateAgentRequestDynamicVariablesValue]] = OMIT,
        asr: typing.Optional[CreateAgentRequestAsr] = OMIT,
        turn: typing.Optional[CreateAgentRequestTurn] = OMIT,
        llm: typing.Optional[CreateAgentRequestLlm] = OMIT,
        search_mode: typing.Optional[CreateAgentRequestSearchMode] = OMIT,
        max_chunks_per_query: typing.Optional[int] = OMIT,
        webhooks: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        system_tools: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateAgentResponse]:
        """
        Create a new voice agent

        Parameters
        ----------
        name : str

        voice_uuid : str

        phone_number_id : typing.Optional[int]

        languages : typing.Optional[typing.Sequence[str]]

        dynamic_variables : typing.Optional[typing.Dict[str, CreateAgentRequestDynamicVariablesValue]]

        asr : typing.Optional[CreateAgentRequestAsr]

        turn : typing.Optional[CreateAgentRequestTurn]

        llm : typing.Optional[CreateAgentRequestLlm]

        search_mode : typing.Optional[CreateAgentRequestSearchMode]
            RAG search strategy - speed (faster) or accuracy (more thorough)

        max_chunks_per_query : typing.Optional[int]
            Number of relevant chunks to retrieve per query for RAG

        webhooks : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        system_tools : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateAgentResponse]
            Agent created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "agents",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "name": name,
                "voice_uuid": voice_uuid,
                "phone_number_id": phone_number_id,
                "languages": languages,
                "dynamic_variables": convert_and_respect_annotation_metadata(
                    object_=dynamic_variables,
                    annotation=typing.Dict[str, CreateAgentRequestDynamicVariablesValue],
                    direction="write",
                ),
                "asr": convert_and_respect_annotation_metadata(
                    object_=asr, annotation=CreateAgentRequestAsr, direction="write"
                ),
                "turn": convert_and_respect_annotation_metadata(
                    object_=turn, annotation=CreateAgentRequestTurn, direction="write"
                ),
                "llm": convert_and_respect_annotation_metadata(
                    object_=llm, annotation=CreateAgentRequestLlm, direction="write"
                ),
                "search_mode": search_mode,
                "max_chunks_per_query": max_chunks_per_query,
                "webhooks": webhooks,
                "system_tools": system_tools,
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
                    CreateAgentResponse,
                    parse_obj_as(
                        type_=CreateAgentResponse,
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

    async def get_agent(
        self,
        uuid_: str,
        *,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetAgentResponse]:
        """
        Retrieve a specific agent's details

        Parameters
        ----------
        uuid_ : str

        advanced : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAgentResponse]
            Agent details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "advanced": advanced,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentResponse,
                    parse_obj_as(
                        type_=GetAgentResponse,
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

    async def delete_agent(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteAgentResponse]:
        """
        Delete an agent and all its configurations

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteAgentResponse]
            Agent deleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAgentResponse,
                    parse_obj_as(
                        type_=DeleteAgentResponse,
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

    async def update_agent(
        self,
        uuid_: str,
        *,
        name: typing.Optional[str] = OMIT,
        voice_uuid: typing.Optional[str] = OMIT,
        phone_number_id: typing.Optional[int] = OMIT,
        languages: typing.Optional[typing.Sequence[str]] = OMIT,
        dynamic_variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        asr: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        turn: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        search_mode: typing.Optional[UpdateAgentRequestSearchMode] = OMIT,
        max_chunks_per_query: typing.Optional[int] = OMIT,
        webhooks: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        system_tools: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateAgentResponse]:
        """
        Update an existing agent's configuration

        Parameters
        ----------
        uuid_ : str

        name : typing.Optional[str]

        voice_uuid : typing.Optional[str]

        phone_number_id : typing.Optional[int]

        languages : typing.Optional[typing.Sequence[str]]

        dynamic_variables : typing.Optional[typing.Dict[str, typing.Any]]

        asr : typing.Optional[typing.Dict[str, typing.Any]]

        turn : typing.Optional[typing.Dict[str, typing.Any]]

        llm : typing.Optional[typing.Dict[str, typing.Any]]

        search_mode : typing.Optional[UpdateAgentRequestSearchMode]
            RAG search strategy

        max_chunks_per_query : typing.Optional[int]
            Number of chunks to retrieve per query for RAG

        webhooks : typing.Optional[typing.Sequence[typing.Any]]

        system_tools : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateAgentResponse]
            Agent updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "name": name,
                "voice_uuid": voice_uuid,
                "phone_number_id": phone_number_id,
                "languages": languages,
                "dynamic_variables": dynamic_variables,
                "asr": asr,
                "turn": turn,
                "llm": llm,
                "search_mode": search_mode,
                "max_chunks_per_query": max_chunks_per_query,
                "webhooks": webhooks,
                "system_tools": system_tools,
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
                    UpdateAgentResponse,
                    parse_obj_as(
                        type_=UpdateAgentResponse,
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

    async def dispatch_agent(
        self,
        uuid_: str,
        *,
        phone_number: str,
        dynamic_variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DispatchAgentResponse]:
        """
        Make an outbound call with an agent

        Parameters
        ----------
        uuid_ : str

        phone_number : str
            Destination phone number

        dynamic_variables : typing.Optional[typing.Dict[str, typing.Any]]
            Runtime variable overrides

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DispatchAgentResponse]
            Call dispatched
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(uuid_)}/dispatch",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "phone_number": phone_number,
                "dynamic_variables": dynamic_variables,
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
                    DispatchAgentResponse,
                    parse_obj_as(
                        type_=DispatchAgentResponse,
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

    async def get_agent_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAgentCapabilitiesResponse]:
        """
        List supported ASR and LLM providers and models

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAgentCapabilitiesResponse]
            Agent capabilities
        """
        _response = await self._client_wrapper.httpx_client.request(
            "agents/capabilities",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentCapabilitiesResponse,
                    parse_obj_as(
                        type_=GetAgentCapabilitiesResponse,
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

    async def get_system_tools(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSystemToolsResponse]:
        """
        List available system tools

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSystemToolsResponse]
            System tools
        """
        _response = await self._client_wrapper.httpx_client.request(
            "agents/system-tools",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSystemToolsResponse,
                    parse_obj_as(
                        type_=GetSystemToolsResponse,
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
