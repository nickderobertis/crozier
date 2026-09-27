

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawScenarioClient, RawScenarioClient
from .types.get_mockserver_scenario_name_response import GetMockserverScenarioNameResponse
from .types.get_mockserver_scenario_response import GetMockserverScenarioResponse
from .types.put_mockserver_scenario_name_response import PutMockserverScenarioNameResponse
from .types.put_mockserver_scenario_name_trigger_response import PutMockserverScenarioNameTriggerResponse


OMIT = typing.cast(typing.Any, ...)


class ScenarioClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScenarioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScenarioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScenarioClient
        """
        return self._raw_client

    def list_all_scenarios_and_their_current_state(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverScenarioResponse:
        """
        Returns every known stateful scenario and its current state. Scenarios are created implicitly by registering expectations with a scenarioName / scenarioState, or explicitly via PUT /mockserver/scenario/{name}. All scenario state is reset when MockServer is reset.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverScenarioResponse
            scenarios listed

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.scenario.list_all_scenarios_and_their_current_state()
        """
        _response = self._raw_client.list_all_scenarios_and_their_current_state(request_options=request_options)
        return _response.data

    def get_the_current_state_of_one_scenario(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverScenarioNameResponse:
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
        GetMockserverScenarioNameResponse
            scenario state returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.scenario.get_the_current_state_of_one_scenario(
            name="name",
        )
        """
        _response = self._raw_client.get_the_current_state_of_one_scenario(name, request_options=request_options)
        return _response.data

    def set_a_scenarios_state_optionally_scheduling_a_timed_auto_transition(
        self,
        name: str,
        *,
        state: str,
        transition_after_ms: typing.Optional[int] = OMIT,
        next_state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverScenarioNameResponse:
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
        PutMockserverScenarioNameResponse
            scenario state set

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.scenario.set_a_scenarios_state_optionally_scheduling_a_timed_auto_transition(
            name="name",
            state="Pending",
            transition_after_ms=5000,
            next_state="Completed",
        )
        """
        _response = self._raw_client.set_a_scenarios_state_optionally_scheduling_a_timed_auto_transition(
            name,
            state=state,
            transition_after_ms=transition_after_ms,
            next_state=next_state,
            request_options=request_options,
        )
        return _response.data

    def externally_trigger_a_scenario_state_transition(
        self, name: str, *, new_state: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverScenarioNameTriggerResponse:
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
        PutMockserverScenarioNameTriggerResponse
            scenario state transition triggered

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.scenario.externally_trigger_a_scenario_state_transition(
            name="name",
            new_state="Failed",
        )
        """
        _response = self._raw_client.externally_trigger_a_scenario_state_transition(
            name, new_state=new_state, request_options=request_options
        )
        return _response.data


class AsyncScenarioClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScenarioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScenarioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScenarioClient
        """
        return self._raw_client

    async def list_all_scenarios_and_their_current_state(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverScenarioResponse:
        """
        Returns every known stateful scenario and its current state. Scenarios are created implicitly by registering expectations with a scenarioName / scenarioState, or explicitly via PUT /mockserver/scenario/{name}. All scenario state is reset when MockServer is reset.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverScenarioResponse
            scenarios listed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.scenario.list_all_scenarios_and_their_current_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_scenarios_and_their_current_state(request_options=request_options)
        return _response.data

    async def get_the_current_state_of_one_scenario(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverScenarioNameResponse:
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
        GetMockserverScenarioNameResponse
            scenario state returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.scenario.get_the_current_state_of_one_scenario(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_current_state_of_one_scenario(name, request_options=request_options)
        return _response.data

    async def set_a_scenarios_state_optionally_scheduling_a_timed_auto_transition(
        self,
        name: str,
        *,
        state: str,
        transition_after_ms: typing.Optional[int] = OMIT,
        next_state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverScenarioNameResponse:
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
        PutMockserverScenarioNameResponse
            scenario state set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.scenario.set_a_scenarios_state_optionally_scheduling_a_timed_auto_transition(
                name="name",
                state="Pending",
                transition_after_ms=5000,
                next_state="Completed",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_a_scenarios_state_optionally_scheduling_a_timed_auto_transition(
            name,
            state=state,
            transition_after_ms=transition_after_ms,
            next_state=next_state,
            request_options=request_options,
        )
        return _response.data

    async def externally_trigger_a_scenario_state_transition(
        self, name: str, *, new_state: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PutMockserverScenarioNameTriggerResponse:
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
        PutMockserverScenarioNameTriggerResponse
            scenario state transition triggered

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.scenario.externally_trigger_a_scenario_state_transition(
                name="name",
                new_state="Failed",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.externally_trigger_a_scenario_state_transition(
            name, new_state=new_state, request_options=request_options
        )
        return _response.data
