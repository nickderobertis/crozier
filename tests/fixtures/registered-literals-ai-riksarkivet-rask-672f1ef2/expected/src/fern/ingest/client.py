

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIngestClient, RawIngestClient


OMIT = typing.cast(typing.Any, ...)


class IngestClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIngestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIngestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIngestClient
        """
        return self._raw_client

    def ingest_event(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[str]]:
        """
        Ingest one OpenLineage event — a ``RunEvent``, or a ``DatasetEvent`` for a change no job performed.

        PARSED HERE RATHER THAN BY THE SIGNATURE, so this door and the bus door share ONE discriminator
        (`models.parse_event`). Declaring the body as `RunEvent` is what made a static event 422 before
        any handler ran: [[LIN-004]] moved catalog DDL onto `DatasetEvent` and taught only the bus. The
        catalog's HTTP emitter is best-effort, so every create it sent lost its provenance in silence —
        measured 2026-09-24, three creates, `{"events":[]}` in the durable feed, and a governance
        assertion reading `expected lineage creator=..., got None`.

        A body that is neither shape raises `RequestValidationError`, which `install_problem_handlers`
        renders exactly as FastAPI's own 422 — the wire answer for a malformed payload is unchanged.

        This is the OpenLineage HTTP-transport default path, so any OpenLineage producer
        (our emitter, Airflow, Spark, dbt, …) configured with ``OPENLINEAGE_URL`` pointed
        here ingests with no glue — the lightweight-Marquez contract.

        When OIDC is enabled the ``CurrentToken`` dependency requires a verified bearer token
        (401 otherwise), :func:`~lineage.api.fga_deps.enforce_author` binds the run author to that
        token's subject (no self-asserted identity), and :func:`~lineage.api.fga_deps.enforce_output_authz`
        requires ``can_write_data`` on every output dataset (a producer can't record provenance for a table
        it can't write). Both are no-ops when auth is off.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[str]]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.ingest.ingest_event(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.ingest_event(request=request, request_options=request_options)
        return _response.data


class AsyncIngestClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIngestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIngestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIngestClient
        """
        return self._raw_client

    async def ingest_event(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[str]]:
        """
        Ingest one OpenLineage event — a ``RunEvent``, or a ``DatasetEvent`` for a change no job performed.

        PARSED HERE RATHER THAN BY THE SIGNATURE, so this door and the bus door share ONE discriminator
        (`models.parse_event`). Declaring the body as `RunEvent` is what made a static event 422 before
        any handler ran: [[LIN-004]] moved catalog DDL onto `DatasetEvent` and taught only the bus. The
        catalog's HTTP emitter is best-effort, so every create it sent lost its provenance in silence —
        measured 2026-09-24, three creates, `{"events":[]}` in the durable feed, and a governance
        assertion reading `expected lineage creator=..., got None`.

        A body that is neither shape raises `RequestValidationError`, which `install_problem_handlers`
        renders exactly as FastAPI's own 422 — the wire answer for a malformed payload is unchanged.

        This is the OpenLineage HTTP-transport default path, so any OpenLineage producer
        (our emitter, Airflow, Spark, dbt, …) configured with ``OPENLINEAGE_URL`` pointed
        here ingests with no glue — the lightweight-Marquez contract.

        When OIDC is enabled the ``CurrentToken`` dependency requires a verified bearer token
        (401 otherwise), :func:`~lineage.api.fga_deps.enforce_author` binds the run author to that
        token's subject (no self-asserted identity), and :func:`~lineage.api.fga_deps.enforce_output_authz`
        requires ``can_write_data`` on every output dataset (a producer can't record provenance for a table
        it can't write). Both are no-ops when auth is off.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[str]]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ingest.ingest_event(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ingest_event(request=request, request_options=request_options)
        return _response.data
