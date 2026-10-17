

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_experiments_request_started_after import ListExperimentsRequestStartedAfter
from ..types.list_experiments_request_started_before import ListExperimentsRequestStartedBefore
from .raw_client import AsyncRawExperimentsClient, RawExperimentsClient
from .types.delete_experiment_response import DeleteExperimentResponse
from .types.get_active_experiment_response import GetActiveExperimentResponse
from .types.get_experiment_response import GetExperimentResponse
from .types.list_experiments_request_status import ListExperimentsRequestStatus
from .types.list_experiments_response import ListExperimentsResponse
from .types.start_experiment_response import StartExperimentResponse
from .types.stop_experiment_response import StopExperimentResponse
from .types.update_experiment_response import UpdateExperimentResponse


OMIT = typing.cast(typing.Any, ...)


class ExperimentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExperimentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExperimentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExperimentsClient
        """
        return self._raw_client

    def list_experiments(
        self,
        *,
        system_id: typing.Optional[str] = None,
        channel: typing.Optional[float] = None,
        status: typing.Optional[ListExperimentsRequestStatus] = None,
        name_contains: typing.Optional[str] = None,
        started_after: typing.Optional[ListExperimentsRequestStartedAfter] = None,
        started_before: typing.Optional[ListExperimentsRequestStartedBefore] = None,
        limit: typing.Optional[float] = None,
        offset: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListExperimentsResponse:
        """
        List experiments with optional filters by system, channel, status, name, and start-time range. Sorted by startedAt desc.

        Parameters
        ----------
        system_id : typing.Optional[str]

        channel : typing.Optional[float]

        status : typing.Optional[ListExperimentsRequestStatus]

        name_contains : typing.Optional[str]

        started_after : typing.Optional[ListExperimentsRequestStartedAfter]

        started_before : typing.Optional[ListExperimentsRequestStartedBefore]

        limit : typing.Optional[float]

        offset : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListExperimentsResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.experiments.list_experiments()
        """
        _response = self._raw_client.list_experiments(
            system_id=system_id,
            channel=channel,
            status=status,
            name_contains=name_contains,
            started_after=started_after,
            started_before=started_before,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def start_experiment(
        self,
        *,
        name: str,
        system_id: str,
        channel: float,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StartExperimentResponse:
        """
        Create an experiment and start the PID loop. Captures setpoint and Kp/Ki/Kd as the experiment's start snapshot. Refuses if PID is already active or another experiment is running on the same channel.

        Parameters
        ----------
        name : str
            Experiment name

        system_id : str

        channel : float

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StartExperimentResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.experiments.start_experiment(
            name="name",
            system_id="systemId",
            channel=1.1,
        )
        """
        _response = self._raw_client.start_experiment(
            name=name, system_id=system_id, channel=channel, notes=notes, request_options=request_options
        )
        return _response.data

    def get_active_experiment(
        self, *, system_id: str, channel: float, request_options: typing.Optional[RequestOptions] = None
    ) -> GetActiveExperimentResponse:
        """
        Return the currently running experiment for a given (systemId, channel), or null if none.

        Parameters
        ----------
        system_id : str

        channel : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetActiveExperimentResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.experiments.get_active_experiment(
            system_id="systemId",
            channel=1.1,
        )
        """
        _response = self._raw_client.get_active_experiment(
            system_id=system_id, channel=channel, request_options=request_options
        )
        return _response.data

    def get_experiment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetExperimentResponse:
        """
        Get a single experiment by id.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetExperimentResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.experiments.get_experiment(
            id="id",
        )
        """
        _response = self._raw_client.get_experiment(id, request_options=request_options)
        return _response.data

    def delete_experiment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteExperimentResponse:
        """
        Delete a non-running experiment. Refuses to delete a running one.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteExperimentResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.experiments.delete_experiment(
            id="id",
        )
        """
        _response = self._raw_client.delete_experiment(id, request_options=request_options)
        return _response.data

    def update_experiment(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateExperimentResponse:
        """
        Update an experiment's name or notes (no other fields).

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateExperimentResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.experiments.update_experiment(
            id="id",
        )
        """
        _response = self._raw_client.update_experiment(id, name=name, notes=notes, request_options=request_options)
        return _response.data

    def stop_experiment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StopExperimentResponse:
        """
        Stop a running experiment. Calls the heater PID stop endpoint and finalizes the experiment row.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StopExperimentResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.experiments.stop_experiment(
            id="id",
        )
        """
        _response = self._raw_client.stop_experiment(id, request_options=request_options)
        return _response.data


class AsyncExperimentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExperimentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExperimentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExperimentsClient
        """
        return self._raw_client

    async def list_experiments(
        self,
        *,
        system_id: typing.Optional[str] = None,
        channel: typing.Optional[float] = None,
        status: typing.Optional[ListExperimentsRequestStatus] = None,
        name_contains: typing.Optional[str] = None,
        started_after: typing.Optional[ListExperimentsRequestStartedAfter] = None,
        started_before: typing.Optional[ListExperimentsRequestStartedBefore] = None,
        limit: typing.Optional[float] = None,
        offset: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListExperimentsResponse:
        """
        List experiments with optional filters by system, channel, status, name, and start-time range. Sorted by startedAt desc.

        Parameters
        ----------
        system_id : typing.Optional[str]

        channel : typing.Optional[float]

        status : typing.Optional[ListExperimentsRequestStatus]

        name_contains : typing.Optional[str]

        started_after : typing.Optional[ListExperimentsRequestStartedAfter]

        started_before : typing.Optional[ListExperimentsRequestStartedBefore]

        limit : typing.Optional[float]

        offset : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListExperimentsResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.experiments.list_experiments()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_experiments(
            system_id=system_id,
            channel=channel,
            status=status,
            name_contains=name_contains,
            started_after=started_after,
            started_before=started_before,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def start_experiment(
        self,
        *,
        name: str,
        system_id: str,
        channel: float,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StartExperimentResponse:
        """
        Create an experiment and start the PID loop. Captures setpoint and Kp/Ki/Kd as the experiment's start snapshot. Refuses if PID is already active or another experiment is running on the same channel.

        Parameters
        ----------
        name : str
            Experiment name

        system_id : str

        channel : float

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StartExperimentResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.experiments.start_experiment(
                name="name",
                system_id="systemId",
                channel=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_experiment(
            name=name, system_id=system_id, channel=channel, notes=notes, request_options=request_options
        )
        return _response.data

    async def get_active_experiment(
        self, *, system_id: str, channel: float, request_options: typing.Optional[RequestOptions] = None
    ) -> GetActiveExperimentResponse:
        """
        Return the currently running experiment for a given (systemId, channel), or null if none.

        Parameters
        ----------
        system_id : str

        channel : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetActiveExperimentResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.experiments.get_active_experiment(
                system_id="systemId",
                channel=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_active_experiment(
            system_id=system_id, channel=channel, request_options=request_options
        )
        return _response.data

    async def get_experiment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetExperimentResponse:
        """
        Get a single experiment by id.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetExperimentResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.experiments.get_experiment(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_experiment(id, request_options=request_options)
        return _response.data

    async def delete_experiment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteExperimentResponse:
        """
        Delete a non-running experiment. Refuses to delete a running one.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteExperimentResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.experiments.delete_experiment(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_experiment(id, request_options=request_options)
        return _response.data

    async def update_experiment(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateExperimentResponse:
        """
        Update an experiment's name or notes (no other fields).

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateExperimentResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.experiments.update_experiment(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_experiment(
            id, name=name, notes=notes, request_options=request_options
        )
        return _response.data

    async def stop_experiment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StopExperimentResponse:
        """
        Stop a running experiment. Calls the heater PID stop endpoint and finalizes the experiment row.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StopExperimentResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.experiments.stop_experiment(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_experiment(id, request_options=request_options)
        return _response.data
