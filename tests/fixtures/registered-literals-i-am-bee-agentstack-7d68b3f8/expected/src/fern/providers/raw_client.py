

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.agent_card_input import AgentCardInput
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output2 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output3 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3,
)
from ..types.create_provider_request_location import CreateProviderRequestLocation
from ..types.http_validation_error import HttpValidationError
from ..types.list_variables_schema import ListVariablesSchema
from ..types.paginated_result_model_output import PaginatedResultModelOutput
from ..types.provider_with_state import ProviderWithState
from .types.patch_provider_request_location import PatchProviderRequestLocation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_providers(
        self,
        *,
        user_owned: typing.Optional[bool] = None,
        origin: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedResultModelOutput]:
        """
        Parameters
        ----------
        user_owned : typing.Optional[bool]

        origin : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedResultModelOutput]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/providers",
            method="GET",
            params={
                "user_owned": user_owned,
                "origin": origin,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultModelOutput,
                    parse_obj_as(
                        type_=PaginatedResultModelOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def create_provider(
        self,
        *,
        location: CreateProviderRequestLocation,
        agent_card: typing.Optional[AgentCardInput] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        auto_stop_timeout_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProviderWithState]:
        """
        Parameters
        ----------
        location : CreateProviderRequestLocation

        agent_card : typing.Optional[AgentCardInput]

        variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        origin : typing.Optional[str]
            A unique origin of the provider: most often a docker or github repository url (without tag). This is used to determine multiple versions of the same agent.

        auto_stop_timeout_sec : typing.Optional[int]
            Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProviderWithState]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/providers",
            method="POST",
            json={
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=CreateProviderRequestLocation, direction="write"
                ),
                "agent_card": convert_and_respect_annotation_metadata(
                    object_=agent_card, annotation=typing.Optional[AgentCardInput], direction="write"
                ),
                "variables": variables,
                "origin": origin,
                "auto_stop_timeout_sec": auto_stop_timeout_sec,
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
                    ProviderWithState,
                    parse_obj_as(
                        type_=ProviderWithState,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_provider(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/providers/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def delete_provider(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/providers/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def patch_provider(
        self,
        id: str,
        *,
        location: typing.Optional[PatchProviderRequestLocation] = OMIT,
        agent_card: typing.Optional[AgentCardInput] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        auto_stop_timeout_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProviderWithState]:
        """
        Parameters
        ----------
        id : str

        location : typing.Optional[PatchProviderRequestLocation]

        agent_card : typing.Optional[AgentCardInput]

        variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        origin : typing.Optional[str]
            A unique origin of the provider: most often a docker or github repository url (without tag). This is used to determine multiple versions of the same agent. None means that origin will be recomputed from location. To preserve original value, set it explicitly.

        auto_stop_timeout_sec : typing.Optional[int]
            Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProviderWithState]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/providers/{encode_path_param(id)}",
            method="PATCH",
            json={
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=typing.Optional[PatchProviderRequestLocation], direction="write"
                ),
                "agent_card": convert_and_respect_annotation_metadata(
                    object_=agent_card, annotation=typing.Optional[AgentCardInput], direction="write"
                ),
                "variables": variables,
                "origin": origin,
                "auto_stop_timeout_sec": auto_stop_timeout_sec,
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
                    ProviderWithState,
                    parse_obj_as(
                        type_=ProviderWithState,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def preview_provider(
        self,
        *,
        location: CreateProviderRequestLocation,
        agent_card: typing.Optional[AgentCardInput] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        auto_stop_timeout_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProviderWithState]:
        """
        Parameters
        ----------
        location : CreateProviderRequestLocation

        agent_card : typing.Optional[AgentCardInput]

        variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        origin : typing.Optional[str]
            A unique origin of the provider: most often a docker or github repository url (without tag). This is used to determine multiple versions of the same agent.

        auto_stop_timeout_sec : typing.Optional[int]
            Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProviderWithState]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/providers/preview",
            method="POST",
            json={
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=CreateProviderRequestLocation, direction="write"
                ),
                "agent_card": convert_and_respect_annotation_metadata(
                    object_=agent_card, annotation=typing.Optional[AgentCardInput], direction="write"
                ),
                "variables": variables,
                "origin": origin,
                "auto_stop_timeout_sec": auto_stop_timeout_sec,
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
                    ProviderWithState,
                    parse_obj_as(
                        type_=ProviderWithState,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_provider_by_location(
        self, location: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3]:
        """
        Parameters
        ----------
        location : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/providers/by-location/{encode_path_param(location)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def stream_logs(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/providers/{encode_path_param(id)}/logs",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def list_provider_variables(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListVariablesSchema]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListVariablesSchema]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/providers/{encode_path_param(id)}/variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListVariablesSchema,
                    parse_obj_as(
                        type_=ListVariablesSchema,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def update_provider_variables(
        self,
        id: str,
        *,
        variables: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        id : str

        variables : typing.Dict[str, typing.Optional[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/providers/{encode_path_param(id)}/variables",
            method="PUT",
            json={
                "variables": variables,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_providers(
        self,
        *,
        user_owned: typing.Optional[bool] = None,
        origin: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedResultModelOutput]:
        """
        Parameters
        ----------
        user_owned : typing.Optional[bool]

        origin : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedResultModelOutput]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/providers",
            method="GET",
            params={
                "user_owned": user_owned,
                "origin": origin,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultModelOutput,
                    parse_obj_as(
                        type_=PaginatedResultModelOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def create_provider(
        self,
        *,
        location: CreateProviderRequestLocation,
        agent_card: typing.Optional[AgentCardInput] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        auto_stop_timeout_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProviderWithState]:
        """
        Parameters
        ----------
        location : CreateProviderRequestLocation

        agent_card : typing.Optional[AgentCardInput]

        variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        origin : typing.Optional[str]
            A unique origin of the provider: most often a docker or github repository url (without tag). This is used to determine multiple versions of the same agent.

        auto_stop_timeout_sec : typing.Optional[int]
            Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProviderWithState]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/providers",
            method="POST",
            json={
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=CreateProviderRequestLocation, direction="write"
                ),
                "agent_card": convert_and_respect_annotation_metadata(
                    object_=agent_card, annotation=typing.Optional[AgentCardInput], direction="write"
                ),
                "variables": variables,
                "origin": origin,
                "auto_stop_timeout_sec": auto_stop_timeout_sec,
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
                    ProviderWithState,
                    parse_obj_as(
                        type_=ProviderWithState,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_provider(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/providers/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def delete_provider(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/providers/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def patch_provider(
        self,
        id: str,
        *,
        location: typing.Optional[PatchProviderRequestLocation] = OMIT,
        agent_card: typing.Optional[AgentCardInput] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        auto_stop_timeout_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProviderWithState]:
        """
        Parameters
        ----------
        id : str

        location : typing.Optional[PatchProviderRequestLocation]

        agent_card : typing.Optional[AgentCardInput]

        variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        origin : typing.Optional[str]
            A unique origin of the provider: most often a docker or github repository url (without tag). This is used to determine multiple versions of the same agent. None means that origin will be recomputed from location. To preserve original value, set it explicitly.

        auto_stop_timeout_sec : typing.Optional[int]
            Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProviderWithState]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/providers/{encode_path_param(id)}",
            method="PATCH",
            json={
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=typing.Optional[PatchProviderRequestLocation], direction="write"
                ),
                "agent_card": convert_and_respect_annotation_metadata(
                    object_=agent_card, annotation=typing.Optional[AgentCardInput], direction="write"
                ),
                "variables": variables,
                "origin": origin,
                "auto_stop_timeout_sec": auto_stop_timeout_sec,
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
                    ProviderWithState,
                    parse_obj_as(
                        type_=ProviderWithState,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def preview_provider(
        self,
        *,
        location: CreateProviderRequestLocation,
        agent_card: typing.Optional[AgentCardInput] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        auto_stop_timeout_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProviderWithState]:
        """
        Parameters
        ----------
        location : CreateProviderRequestLocation

        agent_card : typing.Optional[AgentCardInput]

        variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        origin : typing.Optional[str]
            A unique origin of the provider: most often a docker or github repository url (without tag). This is used to determine multiple versions of the same agent.

        auto_stop_timeout_sec : typing.Optional[int]
            Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProviderWithState]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/providers/preview",
            method="POST",
            json={
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=CreateProviderRequestLocation, direction="write"
                ),
                "agent_card": convert_and_respect_annotation_metadata(
                    object_=agent_card, annotation=typing.Optional[AgentCardInput], direction="write"
                ),
                "variables": variables,
                "origin": origin,
                "auto_stop_timeout_sec": auto_stop_timeout_sec,
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
                    ProviderWithState,
                    parse_obj_as(
                        type_=ProviderWithState,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_provider_by_location(
        self, location: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3]:
        """
        Parameters
        ----------
        location : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/providers/by-location/{encode_path_param(location)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def stream_logs(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/providers/{encode_path_param(id)}/logs",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def list_provider_variables(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListVariablesSchema]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListVariablesSchema]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/providers/{encode_path_param(id)}/variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListVariablesSchema,
                    parse_obj_as(
                        type_=ListVariablesSchema,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def update_provider_variables(
        self,
        id: str,
        *,
        variables: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        id : str

        variables : typing.Dict[str, typing.Optional[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/providers/{encode_path_param(id)}/variables",
            method="PUT",
            json={
                "variables": variables,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
