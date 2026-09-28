

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
from .types.get_mockserver_scenario_name_response import GetMockserverScenarioNameResponse
from .types.get_mockserver_scenario_response import GetMockserverScenarioResponse
from .types.put_mockserver_scenario_name_response import PutMockserverScenarioNameResponse
from .types.put_mockserver_scenario_name_trigger_response import PutMockserverScenarioNameTriggerResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawScenarioClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_scenarios_and_their_current_state(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMockserverScenarioResponse]:
        """
        Returns every known stateful scenario and its current state. Scenarios are created implicitly by registering expectations with a scenarioName / scenarioState, or explicitly via PUT /mockserver/scenario/{name}. All scenario state is reset when MockServer is reset.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMockserverScenarioResponse]
            scenarios listed
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/scenario",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverScenarioResponse,
                    parse_obj_as(
                        type_=GetMockserverScenarioResponse,
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

    def get_the_current_state_of_one_scenario(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMockserverScenarioNameResponse]:
        """
        Returns the current state of the named scenario (null when the scenario has no state yet).

        Parameters
        ----------
        name : str
            the scenario name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMockserverScenarioNameResponse]
            scenario state returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mockserver/scenario/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverScenarioNameResponse,
                    parse_obj_as(
                        type_=GetMockserverScenarioNameResponse,
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

    def set_a_scenarios_state_optionally_scheduling_a_timed_auto_transition(
        self,
        name: str,
        *,
        state: str,
        transition_after_ms: typing.Optional[int] = OMIT,
        next_state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutMockserverScenarioNameResponse]:
        """
        Sets the named scenario to the given state immediately. Optionally schedules a timed auto-transition to nextState after transitionAfterMs milliseconds; the transition only fires if the scenario is still in the set state when the timer expires, and scheduling a new transition cancels any pending one.

        Parameters
        ----------
        name : str
            the scenario name

        state : str
            the state to set immediately

        transition_after_ms : typing.Optional[int]
            delay in milliseconds before auto-transitioning to nextState (requires nextState)

        next_state : typing.Optional[str]
            the state to auto-transition to after transitionAfterMs (requires transitionAfterMs)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutMockserverScenarioNameResponse]
            scenario state set
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mockserver/scenario/{encode_path_param(name)}",
            method="PUT",
            json={
                "state": state,
                "transitionAfterMs": transition_after_ms,
                "nextState": next_state,
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
                    PutMockserverScenarioNameResponse,
                    parse_obj_as(
                        type_=PutMockserverScenarioNameResponse,
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

    def externally_trigger_a_scenario_state_transition(
        self, name: str, *, new_state: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PutMockserverScenarioNameTriggerResponse]:
        """
        Advances the named scenario to newState immediately. Intended for driving a scenario forward from a test harness or CI pipeline.

        Parameters
        ----------
        name : str
            the scenario name

        new_state : str
            the state to transition the scenario to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutMockserverScenarioNameTriggerResponse]
            scenario state transition triggered
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mockserver/scenario/{encode_path_param(name)}/trigger",
            method="PUT",
            json={
                "newState": new_state,
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
                    PutMockserverScenarioNameTriggerResponse,
                    parse_obj_as(
                        type_=PutMockserverScenarioNameTriggerResponse,
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


class AsyncRawScenarioClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_scenarios_and_their_current_state(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMockserverScenarioResponse]:
        """
        Returns every known stateful scenario and its current state. Scenarios are created implicitly by registering expectations with a scenarioName / scenarioState, or explicitly via PUT /mockserver/scenario/{name}. All scenario state is reset when MockServer is reset.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMockserverScenarioResponse]
            scenarios listed
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/scenario",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverScenarioResponse,
                    parse_obj_as(
                        type_=GetMockserverScenarioResponse,
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

    async def get_the_current_state_of_one_scenario(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMockserverScenarioNameResponse]:
        """
        Returns the current state of the named scenario (null when the scenario has no state yet).

        Parameters
        ----------
        name : str
            the scenario name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMockserverScenarioNameResponse]
            scenario state returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mockserver/scenario/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverScenarioNameResponse,
                    parse_obj_as(
                        type_=GetMockserverScenarioNameResponse,
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

    async def set_a_scenarios_state_optionally_scheduling_a_timed_auto_transition(
        self,
        name: str,
        *,
        state: str,
        transition_after_ms: typing.Optional[int] = OMIT,
        next_state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutMockserverScenarioNameResponse]:
        """
        Sets the named scenario to the given state immediately. Optionally schedules a timed auto-transition to nextState after transitionAfterMs milliseconds; the transition only fires if the scenario is still in the set state when the timer expires, and scheduling a new transition cancels any pending one.

        Parameters
        ----------
        name : str
            the scenario name

        state : str
            the state to set immediately

        transition_after_ms : typing.Optional[int]
            delay in milliseconds before auto-transitioning to nextState (requires nextState)

        next_state : typing.Optional[str]
            the state to auto-transition to after transitionAfterMs (requires transitionAfterMs)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutMockserverScenarioNameResponse]
            scenario state set
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mockserver/scenario/{encode_path_param(name)}",
            method="PUT",
            json={
                "state": state,
                "transitionAfterMs": transition_after_ms,
                "nextState": next_state,
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
                    PutMockserverScenarioNameResponse,
                    parse_obj_as(
                        type_=PutMockserverScenarioNameResponse,
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

    async def externally_trigger_a_scenario_state_transition(
        self, name: str, *, new_state: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PutMockserverScenarioNameTriggerResponse]:
        """
        Advances the named scenario to newState immediately. Intended for driving a scenario forward from a test harness or CI pipeline.

        Parameters
        ----------
        name : str
            the scenario name

        new_state : str
            the state to transition the scenario to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutMockserverScenarioNameTriggerResponse]
            scenario state transition triggered
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mockserver/scenario/{encode_path_param(name)}/trigger",
            method="PUT",
            json={
                "newState": new_state,
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
                    PutMockserverScenarioNameTriggerResponse,
                    parse_obj_as(
                        type_=PutMockserverScenarioNameTriggerResponse,
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
