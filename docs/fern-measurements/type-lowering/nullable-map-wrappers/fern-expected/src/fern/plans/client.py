

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.job_results import JobResults
from ..types.plan import Plan
from .raw_client import AsyncRawPlansClient, RawPlansClient


class PlansClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPlansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPlansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPlansClient
        """
        return self._raw_client

    def get_plan(self, plan_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Plan:
        """
        Parameters
        ----------
        plan_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plan
            The plan.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plans.get_plan(
            plan_id="planId",
        )
        """
        _response = self._raw_client.get_plan(plan_id, request_options=request_options)
        return _response.data

    def get_job_results(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[JobResults]:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[JobResults]
            The job's results.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.plans.get_job_results(
            job_id="jobId",
        )
        """
        _response = self._raw_client.get_job_results(job_id, request_options=request_options)
        return _response.data


class AsyncPlansClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPlansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPlansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPlansClient
        """
        return self._raw_client

    async def get_plan(self, plan_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Plan:
        """
        Parameters
        ----------
        plan_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plan
            The plan.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plans.get_plan(
                plan_id="planId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_plan(plan_id, request_options=request_options)
        return _response.data

    async def get_job_results(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[JobResults]:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[JobResults]
            The job's results.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.plans.get_job_results(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_results(job_id, request_options=request_options)
        return _response.data
