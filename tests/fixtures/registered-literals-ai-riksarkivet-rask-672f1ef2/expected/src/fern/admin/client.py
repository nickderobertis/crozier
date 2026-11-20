

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dlq_backlog import DlqBacklog
from ..types.dlq_replay_response import DlqReplayResponse
from .raw_client import AsyncRawAdminClient, RawAdminClient


class AdminClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdminClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdminClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdminClient
        """
        return self._raw_client

    def list_dlq(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DlqBacklog:
        """
        The outbox saturation snapshot + the visible at-risk events (oldest first, capped at ``limit``).

        ``depth``/``oldest_age_seconds`` are the raw system-health signal; ``events`` is the per-dataset-governed
        subset the caller may see. Requires an authenticated principal when FGA is on (else the raw depth would
        leak to an anonymous caller); the event list is then filtered by dataset visibility.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DlqBacklog
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
        client.admin.list_dlq()
        """
        _response = self._raw_client.list_dlq(limit=limit, request_options=request_options)
        return _response.data

    def replay_dlq(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DlqReplayResponse:
        """
        Re-ingest one staged event on demand, re-publish it, then drop it — the manual twin of the reconcile relay's drain.

        A replay IS a re-ingest, so it carries the SAME authz as a fresh ingest, twice over: the relay's gate on
        the staged bytes (:func:`enforce_bus_authz` — signature and stamped author) and the ingest door's on the
        operator (:func:`enforce_output_authz` — ``can_write_data`` on the outputs, ``can_get_metadata`` on the
        inputs, fail-closed). Both doors are idempotent: a run MERGEs on its run id, a static change on its
        derived feed id, and the durable feed insert is ON CONFLICT DO NOTHING. The staged bytes are re-published
        to the lineage topic exactly as the relay re-publishes them, so subscribers hear of the event as well as
        the graph. The drop is only reached on success — a failed re-ingest or re-publish leaves the object
        staged for the relay to retry, and a failed re-publish answers 503 because the graph is already
        repaired.

        Non-disclosure (audit 2026-07-20): replay must not become an oracle for events ``list_dlq`` hid. So a
        run whose datasets the caller cannot SEE (or an unparseable poison object, which the governed list also
        hides) returns the SAME 404 as a missing run — never a distinct 422 or a 403 echoing hidden dataset
        names. Only an event the caller could have listed reaches ``enforce_output_authz``.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DlqReplayResponse
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
        client.admin.replay_dlq(
            run_id="run_id",
        )
        """
        _response = self._raw_client.replay_dlq(run_id, request_options=request_options)
        return _response.data


class AsyncAdminClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdminClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdminClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdminClient
        """
        return self._raw_client

    async def list_dlq(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DlqBacklog:
        """
        The outbox saturation snapshot + the visible at-risk events (oldest first, capped at ``limit``).

        ``depth``/``oldest_age_seconds`` are the raw system-health signal; ``events`` is the per-dataset-governed
        subset the caller may see. Requires an authenticated principal when FGA is on (else the raw depth would
        leak to an anonymous caller); the event list is then filtered by dataset visibility.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DlqBacklog
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
            await client.admin.list_dlq()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_dlq(limit=limit, request_options=request_options)
        return _response.data

    async def replay_dlq(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DlqReplayResponse:
        """
        Re-ingest one staged event on demand, re-publish it, then drop it — the manual twin of the reconcile relay's drain.

        A replay IS a re-ingest, so it carries the SAME authz as a fresh ingest, twice over: the relay's gate on
        the staged bytes (:func:`enforce_bus_authz` — signature and stamped author) and the ingest door's on the
        operator (:func:`enforce_output_authz` — ``can_write_data`` on the outputs, ``can_get_metadata`` on the
        inputs, fail-closed). Both doors are idempotent: a run MERGEs on its run id, a static change on its
        derived feed id, and the durable feed insert is ON CONFLICT DO NOTHING. The staged bytes are re-published
        to the lineage topic exactly as the relay re-publishes them, so subscribers hear of the event as well as
        the graph. The drop is only reached on success — a failed re-ingest or re-publish leaves the object
        staged for the relay to retry, and a failed re-publish answers 503 because the graph is already
        repaired.

        Non-disclosure (audit 2026-07-20): replay must not become an oracle for events ``list_dlq`` hid. So a
        run whose datasets the caller cannot SEE (or an unparseable poison object, which the governed list also
        hides) returns the SAME 404 as a missing run — never a distinct 422 or a 403 echoing hidden dataset
        names. Only an event the caller could have listed reaches ``enforce_output_authz``.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DlqReplayResponse
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
            await client.admin.replay_dlq(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replay_dlq(run_id, request_options=request_options)
        return _response.data
