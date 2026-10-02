

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.slo_objective import SloObjective
from ..types.slo_verdict import SloVerdict
from .raw_client import AsyncRawSloClient, RawSloClient
from .types.slo_criteria_window import SloCriteriaWindow


OMIT = typing.cast(typing.Any, ...)


class SloClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSloClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSloClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSloClient
        """
        return self._raw_client

    def verify_a_service_level_objective_over_a_window(
        self,
        *,
        objectives: typing.Sequence[SloObjective],
        name: typing.Optional[str] = OMIT,
        window: typing.Optional[SloCriteriaWindow] = OMIT,
        minimum_sample_count: typing.Optional[int] = OMIT,
        upstream_hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SloVerdict:
        """
        Evaluates a named set of objectives (latency percentiles, error rate) over a time window against the recorded forward-path SLI samples and returns a PASS / FAIL / INCONCLUSIVE verdict. The HTTP status encodes the verdict so a CI or chaos gate can assert on the status code alone: 200 when the verdict is PASS or INCONCLUSIVE, 406 when it is FAIL. A criteria PASSes only when all objectives hold (logical AND); it is INCONCLUSIVE when an indicator cannot be computed or the window holds fewer than minimumSampleCount samples. Off by default — returns 400 until sloTrackingEnabled=true.

        Parameters
        ----------
        objectives : typing.Sequence[SloObjective]

        name : typing.Optional[str]
            human-readable criteria name, echoed back in the verdict

        window : typing.Optional[SloCriteriaWindow]
            the time window to evaluate over

        minimum_sample_count : typing.Optional[int]
            minimum samples required in the window; below this the verdict is INCONCLUSIVE

        upstream_hosts : typing.Optional[typing.Sequence[str]]
            optional list of upstream hosts to restrict the evaluation to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SloVerdict
            verdict is PASS or INCONCLUSIVE

        Examples
        --------
        from fern.slo import SloCriteriaWindow

        from fern import FernApi, SloObjective

        client = FernApi()
        client.slo.verify_a_service_level_objective_over_a_window(
            name="checkout-slo",
            window=SloCriteriaWindow(
                type="LOOKBACK",
                lookback_millis=60000,
            ),
            minimum_sample_count=20,
            upstream_hosts=["payments.svc"],
            objectives=[
                SloObjective(
                    sli="LATENCY_P95",
                    comparator="LESS_THAN",
                    threshold=250.0,
                    scope="FORWARD",
                ),
                SloObjective(
                    sli="ERROR_RATE",
                    comparator="LESS_THAN_OR_EQUAL",
                    threshold=0.01,
                ),
            ],
        )
        """
        _response = self._raw_client.verify_a_service_level_objective_over_a_window(
            objectives=objectives,
            name=name,
            window=window,
            minimum_sample_count=minimum_sample_count,
            upstream_hosts=upstream_hosts,
            request_options=request_options,
        )
        return _response.data


class AsyncSloClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSloClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSloClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSloClient
        """
        return self._raw_client

    async def verify_a_service_level_objective_over_a_window(
        self,
        *,
        objectives: typing.Sequence[SloObjective],
        name: typing.Optional[str] = OMIT,
        window: typing.Optional[SloCriteriaWindow] = OMIT,
        minimum_sample_count: typing.Optional[int] = OMIT,
        upstream_hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SloVerdict:
        """
        Evaluates a named set of objectives (latency percentiles, error rate) over a time window against the recorded forward-path SLI samples and returns a PASS / FAIL / INCONCLUSIVE verdict. The HTTP status encodes the verdict so a CI or chaos gate can assert on the status code alone: 200 when the verdict is PASS or INCONCLUSIVE, 406 when it is FAIL. A criteria PASSes only when all objectives hold (logical AND); it is INCONCLUSIVE when an indicator cannot be computed or the window holds fewer than minimumSampleCount samples. Off by default — returns 400 until sloTrackingEnabled=true.

        Parameters
        ----------
        objectives : typing.Sequence[SloObjective]

        name : typing.Optional[str]
            human-readable criteria name, echoed back in the verdict

        window : typing.Optional[SloCriteriaWindow]
            the time window to evaluate over

        minimum_sample_count : typing.Optional[int]
            minimum samples required in the window; below this the verdict is INCONCLUSIVE

        upstream_hosts : typing.Optional[typing.Sequence[str]]
            optional list of upstream hosts to restrict the evaluation to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SloVerdict
            verdict is PASS or INCONCLUSIVE

        Examples
        --------
        import asyncio

        from fern.slo import SloCriteriaWindow

        from fern import AsyncFernApi, SloObjective

        client = AsyncFernApi()


        async def main() -> None:
            await client.slo.verify_a_service_level_objective_over_a_window(
                name="checkout-slo",
                window=SloCriteriaWindow(
                    type="LOOKBACK",
                    lookback_millis=60000,
                ),
                minimum_sample_count=20,
                upstream_hosts=["payments.svc"],
                objectives=[
                    SloObjective(
                        sli="LATENCY_P95",
                        comparator="LESS_THAN",
                        threshold=250.0,
                        scope="FORWARD",
                    ),
                    SloObjective(
                        sli="ERROR_RATE",
                        comparator="LESS_THAN_OR_EQUAL",
                        threshold=0.01,
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_a_service_level_objective_over_a_window(
            objectives=objectives,
            name=name,
            window=window,
            minimum_sample_count=minimum_sample_count,
            upstream_hosts=upstream_hosts,
            request_options=request_options,
        )
        return _response.data
