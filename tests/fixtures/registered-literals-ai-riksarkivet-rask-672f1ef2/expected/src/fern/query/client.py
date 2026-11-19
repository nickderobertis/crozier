

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.column_graph import ColumnGraph
from ..types.column_neighbors import ColumnNeighbors
from ..types.creator import Creator
from ..types.dataset_schema import DatasetSchema
from ..types.events import Events
from ..types.lineage_graph import LineageGraph
from ..types.neighbors import Neighbors
from ..types.producers import Producers
from ..types.readers import Readers
from ..types.reconcile_status import ReconcileStatus
from ..types.run_inputs import RunInputs
from ..types.run_status import RunStatus
from ..types.runs import Runs
from .raw_client import AsyncRawQueryClient, RawQueryClient


class QueryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQueryClient
        """
        return self._raw_client

    def get_dataset_columns(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ColumnGraph:
        """
        The column-level lineage subgraph around ``name`` (#24) — the field-to-field analogue of
        ``/graph``, for a DAG view of how each column was produced.

        ``depth`` counts DATASET hops outward; 1 is the single-hop answer this returned before the
        parameter existed, so every existing caller is unaffected. The bound is FastAPI's here AND the
        repository's — governance below runs over whatever the walk returned, so a depth the service did
        not agree to would enlarge the set being filtered, not the set being disclosed.

        Nodes/edges touching a dataset the caller can't see are dropped (an edge needs BOTH endpoints'
        datasets visible); ``name``'s own columns are always shown (the route gate authorized it).

        Parameters
        ----------
        name : str

        depth : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ColumnGraph
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
        client.query.get_dataset_columns(
            name="name",
        )
        """
        _response = self._raw_client.get_dataset_columns(name, depth=depth, request_options=request_options)
        return _response.data

    def get_column_downstream(
        self,
        name: str,
        field: str,
        *,
        depth: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ColumnNeighbors:
        """
        Column-level impact (#24): the columns (transitively) derived from ``name.field``. Gated +
        governed exactly like the column upstream view — related columns in datasets the caller can't see
        are dropped.

        Parameters
        ----------
        name : str

        field : str

        depth : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ColumnNeighbors
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
        client.query.get_column_downstream(
            name="name",
            field="field",
        )
        """
        _response = self._raw_client.get_column_downstream(name, field, depth=depth, request_options=request_options)
        return _response.data

    def get_column_upstream(
        self,
        name: str,
        field: str,
        *,
        depth: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ColumnNeighbors:
        """
        Column-level provenance (#24): the columns ``name.field`` was (transitively) derived from.

        Our deepest moat — field-to-field lineage a format-unaware catalog cannot derive. Gated on
        ``can_get_metadata`` for the owning ``name``; related columns whose *owning dataset* the caller can't
        see are dropped (a column has no ACL of its own — it inherits its table's), closing the same
        transitive-disclosure hole at column resolution. Auth off → pass-through.

        Parameters
        ----------
        name : str

        field : str

        depth : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ColumnNeighbors
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
        client.query.get_column_upstream(
            name="name",
            field="field",
        )
        """
        _response = self._raw_client.get_column_upstream(name, field, depth=depth, request_options=request_options)
        return _response.data

    def get_creator(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Creator:
        """
        Who created ``name`` (the verified catalog principal). Gated on ``can_get_metadata``.

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Creator
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
        client.query.get_creator(
            name="name",
        )
        """
        _response = self._raw_client.get_creator(name, request_options=request_options)
        return _response.data

    def get_downstream(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Neighbors:
        """
        What derives from ``name`` (impact). Gated; non-visible related datasets are dropped.

        ``depth`` bounds the walk exactly as on `/upstream` — impact is the direction that fans OUT, so a
        hub dataset is where an unbounded walk costs most.

        Parameters
        ----------
        name : str

        depth : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Neighbors
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
        client.query.get_downstream(
            name="name",
        )
        """
        _response = self._raw_client.get_downstream(name, depth=depth, request_options=request_options)
        return _response.data

    def get_graph(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> LineageGraph:
        """
        The connected lineage subgraph around ``name`` (nodes + edges) for a DAG view.

        ``depth`` bounds the walk to that many hops in each direction, making this a ROOTED
        NEIGHBOURHOOD rather than a whole connected component — the shape Marquez serves at
        ``/lineage?nodeId=&depth=N``. Omitted, the walk is unbounded, which is the previous behaviour and
        still what an un-rooted caller wants.

        Bounding here rather than in the client is the point: a UI depth control that filters an
        already-fetched window cannot reach anything the window excluded, however small the depth.

        `ge=1, le=MAX_WALK_DEPTH` is the FIRST of two guards and the one that answers the caller: a bad
        depth is a 422 here rather than a 500 from the repository. The repository re-checks anyway,
        because the hop range is interpolated into Cypher and that check must not depend on every caller
        having gone through this route.

        Nodes the caller may not see (and edges touching them) are dropped; the requested ``name``
        is already authorized by the route gate.

        Parameters
        ----------
        name : str

        depth : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LineageGraph
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
        client.query.get_graph(
            name="name",
        )
        """
        _response = self._raw_client.get_graph(name, depth=depth, request_options=request_options)
        return _response.data

    def get_producers(
        self, name: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Producers:
        """
        The runs that wrote ``name`` — who / when / how. Gated on ``can_get_metadata``.

        Bounded like ``/readers`` beside it: newest-first, so the page a caller gets is the part that
        answers "what wrote this", and the tail it loses is history the run board serves instead.

        Parameters
        ----------
        name : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Producers
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
        client.query.get_producers(
            name="name",
        )
        """
        _response = self._raw_client.get_producers(name, limit=limit, request_options=request_options)
        return _response.data

    def get_readers(
        self, name: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Readers:
        """
        Who has READ ``name`` — the read-audit log's query surface (#41 was capture-only until now).

        Owner/writer-gated (``require_write_access``, on TOP of the router's ``can_get_metadata``): an access
        log reveals *who* touched a dataset, so only a data owner may audit it — a casual reader can trace the
        dataset's provenance but not enumerate who else viewed it. Aggregated per principal (last read + count,
        newest first). Empty when read-auditing is/was off (the log table exists but has no rows).

        Parameters
        ----------
        name : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Readers
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
        client.query.get_readers(
            name="name",
        )
        """
        _response = self._raw_client.get_readers(name, limit=limit, request_options=request_options)
        return _response.data

    def get_reconcile(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ReconcileStatus:
        """
        Does the lineage graph agree with the **actual Lance file on storage**? (#23)

        Our moat over format-unaware catalogs: because we own a Lance lakehouse we
        read the real on-disk version and cross-check it against the version the graph recorded on the
        ``WROTE`` edge — surfacing a write that bypassed lineage (``storage_ahead``) or a lineage claim
        with no data behind it (``missing_on_storage``). Gated on ``can_get_metadata`` for ``name``; the
        Lance read runs in the threadpool so the blocking object-store I/O never stalls the event loop.

        ``versions_without_lineage`` is the axis the version comparison cannot answer: it compares two
        MAXIMA, so a write whose event was lost and which a later write superseded leaves both equal and the
        dataset reports ``in_sync``. Measured on the live estate 2026-09-11, ``bronze$events`` answered
        in_sync at 87/87 with four retained versions carrying no lineage at all. READ-ONLY here — this door
        reports the holes and the cron sweep is what recovers them, so an operator asking a question never
        mutates the graph as a side effect.

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReconcileStatus
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
        client.query.get_reconcile(
            name="name",
        )
        """
        _response = self._raw_client.get_reconcile(name, request_options=request_options)
        return _response.data

    def get_schema(
        self,
        name: str,
        *,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetSchema:
        """
        The persisted column schema for ``name`` — at ``?version=N`` if given, else the latest. (#24)

        Captured from the standard ``SchemaDatasetFacet`` at ingest and stored per-version on the ``WROTE``
        edge (previously the facet was received and discarded). Gated on ``can_get_metadata`` for ``name``;
        this is the prerequisite for column-level lineage and powers schema-diffing between Lance versions.

        Parameters
        ----------
        name : str

        version : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSchema
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
        client.query.get_schema(
            name="name",
        )
        """
        _response = self._raw_client.get_schema(name, version=version, request_options=request_options)
        return _response.data

    def get_upstream(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Neighbors:
        """
        What ``name`` was derived from (provenance).

        Gated on ``can_get_metadata`` for ``name``; related datasets the caller may not see are
        dropped so the graph can't disclose tables outside its reach.

        ``depth`` bounds the walk, the same shape and ceiling `/graph` already offers. The repository has
        accepted it since the helper landed; only this door never declared it, so every request reached the
        unbounded `*1..` statement whatever the caller wanted. Omitted it stays unbounded — the previous
        behaviour, and what an un-rooted caller asks for — but it is now a caller's CHOICE rather than the
        only thing the door can do. `age.py` names that unbounded path over a grown graph as the reason a
        pooled connection cannot be pinned.

        Parameters
        ----------
        name : str

        depth : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Neighbors
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
        client.query.get_upstream(
            name="name",
        )
        """
        _response = self._raw_client.get_upstream(name, depth=depth, request_options=request_options)
        return _response.data

    def get_events(
        self,
        *,
        after: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        summary: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Events:
        """
        The most-recent ingested OpenLineage events (newest first) — the Marquez-style event feed.

        **Durable** (read from Postgres, survives restart / replica-shared) and **governed**: when auth is
        on the feed is filtered like the per-dataset reads — an event is shown only if the caller
        ``can_get_metadata`` on *every* dataset it references (and a dataset-less event is hidden), so the
        audit feed never discloses a table outside the caller's reach. Auth off → pass-through. (#22)

        Pagination (additive, defaults = the old behavior): ``after`` = keyset cursor (the previous
        page's ``next_cursor``); ``limit`` ≤ 500 (server-capped); ``summary=true`` drops the full-JSONB
        ``event`` payload at the SQL layer. The governance filter ALWAYS runs before the slice —
        pagination can never disclose a hidden row's CONTENT. ``next_cursor`` is a WINDOW FLOOR, not
        necessarily a visible row's seq (on a hidden-dense page it is the fetch window's last seq —
        exclusive, so the hidden row itself is never returned; bare seq numbers were already inferable
        from gaps in the pre-pagination feed, so this adds no new disclosure class — reviewed
        2026-07-11).

        Parameters
        ----------
        after : typing.Optional[int]

        limit : typing.Optional[int]

        summary : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Events
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
        client.query.get_events()
        """
        _response = self._raw_client.get_events(
            after=after, limit=limit, summary=summary, request_options=request_options
        )
        return _response.data

    def get_events_projection(
        self,
        *,
        after: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        summary: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Events:
        """
        The feed WITHOUT the per-dataset filter, for a caller that observes the estate (§ G1).

        WHY A SECOND DOOR RATHER THAN A FLAG ON THE FIRST. `/events` is governed per dataset, which is
        right for a person: an event naming a table you cannot see must not disclose it. It is wrong for a
        SERVICE that has to reconcile the whole estate, and the wrongness is silent in both directions —
        measured on this estate 2026-09-09, a run that demonstrably exists answered **404** to a service
        principal, and its inputs answered **200 with an empty list**. A walker sees "nothing here", and an
        estate with no work looks identical to an estate it cannot see.

        THE SERVICE IS NOT THE DISCLOSURE BOUNDARY, and that is what makes this sound rather than a hole.
        A reconciler reads the feed to decide who to TELL; the telling is gated per subject at delivery
        (`can_be_notified`), which is the check that actually protects a person's inbox. Filtering the
        reconciler's own view protects nobody and only guarantees it cannot find the events it exists to
        catch. `can_be_notified` stays the sole disclosure gate; this door moves the estate-read decision
        to the rung that means "may observe the estate".

        `can_observe_events` ON THE ROOT OBJECT — the same rung `POST /v1/projects` and `POST /v1/stores`
        already gate on, so an estate privilege means one thing everywhere. It is `owner` on the root in
        `model.fga`, so nobody holds it by accident and granting it is a deliberate act.

        Identical shape to `/events` otherwise — same keyset cursor, same cap, same `summary` — so a caller
        can move between the two without a second client. `oldest_seq` is reported here too: a walker whose
        cursor falls below it lost a window to the prune, which is the one signal that distinguishes
        "caught up" from "rows went past me".

        Parameters
        ----------
        after : typing.Optional[int]

        limit : typing.Optional[int]

        summary : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Events
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
        client.query.get_events_projection()
        """
        _response = self._raw_client.get_events_projection(
            after=after, limit=limit, summary=summary, request_options=request_options
        )
        return _response.data

    def get_runs(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Runs:
        """
        Live run-status board — each run's current state folded onto its ``(:Run)`` node in Apache AGE.

        **Durable** (survives restart / replica-shared) and **governed** like ``/events`` and the per-dataset
        reads: a run is shown only if the caller ``can_get_metadata`` on every dataset it wrote, so the board
        can't enumerate dataset names / creators / errors outside the caller's reach. Auth off → pass-through.

        **BOUNDED AT THE QUERY, newest first.** The board is polled every two seconds and the graph has no run
        retention, so an unbounded read grows without limit: measured live 2026-09-07 it answered 5,122 runs /
        2.65 MB, against 272 rows fifteen days earlier. A limit applied here rather than in the Cypher would
        change nothing — the cost is the READ, and asking for one run took 2.5 s while asking for a hundred
        took 1.4 s.

        The over-fetch window is ``/events``' answer, for the same reason: governance drops rows AFTER the
        read, so a page cut to size first comes back short — or empty — while visible runs sit below it. With
        auth off the filter is pass-through and the headroom is pure waste, so the fetch is exactly ``limit``.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Runs
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
        client.query.get_runs()
        """
        _response = self._raw_client.get_runs(limit=limit, request_options=request_options)
        return _response.data

    def get_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RunStatus:
        """
        ONE run's state — the point read the board is not.

        "Is this run in the graph?" was answered by downloading `/runs` and scanning it, which is
        O(estate) for a one-row question and became WRONG once the board was bounded: a run outside the
        newest page is missing from the response while present in the graph, so the caller concluded
        ABSENT and reported a provenance defect that did not exist.

        GOVERNED EXACTLY LIKE THE BOARD — visible only if the caller `can_get_metadata` on every dataset
        the run wrote — and an invisible run answers 404, the same as one that is not there. Deliberately
        the same answer: distinguishing them would let a caller enumerate runs it may not see by watching
        which ids give a different refusal.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunStatus
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
        client.query.get_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.get_run(run_id, request_options=request_options)
        return _response.data

    def get_run_inputs(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RunInputs:
        """
        The inputs a run consumed, each with the version it PINNED — the per-run reproducibility answer.

        The pinned version rides the graph's ``READ`` edge (the Ray TRAIN job pins every feature — #115
        D1); this endpoint is its API surface (before, Cypher-only). Kept OFF the 2s-polled ``/runs`` board
        — it's a per-run drill-in, and adding a per-run READ-edge fetch to the board would be N+1 on the hot
        path. Governed like every read: an input the caller can't ``can_get_metadata`` is dropped (an empty
        list for a run the caller can't see into is itself non-disclosing). Auth off → pass-through.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunInputs
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
        client.query.get_run_inputs(
            run_id="run_id",
        )
        """
        _response = self._raw_client.get_run_inputs(run_id, request_options=request_options)
        return _response.data


class AsyncQueryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQueryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQueryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQueryClient
        """
        return self._raw_client

    async def get_dataset_columns(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ColumnGraph:
        """
        The column-level lineage subgraph around ``name`` (#24) — the field-to-field analogue of
        ``/graph``, for a DAG view of how each column was produced.

        ``depth`` counts DATASET hops outward; 1 is the single-hop answer this returned before the
        parameter existed, so every existing caller is unaffected. The bound is FastAPI's here AND the
        repository's — governance below runs over whatever the walk returned, so a depth the service did
        not agree to would enlarge the set being filtered, not the set being disclosed.

        Nodes/edges touching a dataset the caller can't see are dropped (an edge needs BOTH endpoints'
        datasets visible); ``name``'s own columns are always shown (the route gate authorized it).

        Parameters
        ----------
        name : str

        depth : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ColumnGraph
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
            await client.query.get_dataset_columns(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dataset_columns(name, depth=depth, request_options=request_options)
        return _response.data

    async def get_column_downstream(
        self,
        name: str,
        field: str,
        *,
        depth: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ColumnNeighbors:
        """
        Column-level impact (#24): the columns (transitively) derived from ``name.field``. Gated +
        governed exactly like the column upstream view — related columns in datasets the caller can't see
        are dropped.

        Parameters
        ----------
        name : str

        field : str

        depth : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ColumnNeighbors
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
            await client.query.get_column_downstream(
                name="name",
                field="field",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_column_downstream(
            name, field, depth=depth, request_options=request_options
        )
        return _response.data

    async def get_column_upstream(
        self,
        name: str,
        field: str,
        *,
        depth: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ColumnNeighbors:
        """
        Column-level provenance (#24): the columns ``name.field`` was (transitively) derived from.

        Our deepest moat — field-to-field lineage a format-unaware catalog cannot derive. Gated on
        ``can_get_metadata`` for the owning ``name``; related columns whose *owning dataset* the caller can't
        see are dropped (a column has no ACL of its own — it inherits its table's), closing the same
        transitive-disclosure hole at column resolution. Auth off → pass-through.

        Parameters
        ----------
        name : str

        field : str

        depth : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ColumnNeighbors
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
            await client.query.get_column_upstream(
                name="name",
                field="field",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_column_upstream(
            name, field, depth=depth, request_options=request_options
        )
        return _response.data

    async def get_creator(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Creator:
        """
        Who created ``name`` (the verified catalog principal). Gated on ``can_get_metadata``.

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Creator
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
            await client.query.get_creator(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_creator(name, request_options=request_options)
        return _response.data

    async def get_downstream(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Neighbors:
        """
        What derives from ``name`` (impact). Gated; non-visible related datasets are dropped.

        ``depth`` bounds the walk exactly as on `/upstream` — impact is the direction that fans OUT, so a
        hub dataset is where an unbounded walk costs most.

        Parameters
        ----------
        name : str

        depth : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Neighbors
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
            await client.query.get_downstream(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_downstream(name, depth=depth, request_options=request_options)
        return _response.data

    async def get_graph(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> LineageGraph:
        """
        The connected lineage subgraph around ``name`` (nodes + edges) for a DAG view.

        ``depth`` bounds the walk to that many hops in each direction, making this a ROOTED
        NEIGHBOURHOOD rather than a whole connected component — the shape Marquez serves at
        ``/lineage?nodeId=&depth=N``. Omitted, the walk is unbounded, which is the previous behaviour and
        still what an un-rooted caller wants.

        Bounding here rather than in the client is the point: a UI depth control that filters an
        already-fetched window cannot reach anything the window excluded, however small the depth.

        `ge=1, le=MAX_WALK_DEPTH` is the FIRST of two guards and the one that answers the caller: a bad
        depth is a 422 here rather than a 500 from the repository. The repository re-checks anyway,
        because the hop range is interpolated into Cypher and that check must not depend on every caller
        having gone through this route.

        Nodes the caller may not see (and edges touching them) are dropped; the requested ``name``
        is already authorized by the route gate.

        Parameters
        ----------
        name : str

        depth : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LineageGraph
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
            await client.query.get_graph(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_graph(name, depth=depth, request_options=request_options)
        return _response.data

    async def get_producers(
        self, name: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Producers:
        """
        The runs that wrote ``name`` — who / when / how. Gated on ``can_get_metadata``.

        Bounded like ``/readers`` beside it: newest-first, so the page a caller gets is the part that
        answers "what wrote this", and the tail it loses is history the run board serves instead.

        Parameters
        ----------
        name : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Producers
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
            await client.query.get_producers(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_producers(name, limit=limit, request_options=request_options)
        return _response.data

    async def get_readers(
        self, name: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Readers:
        """
        Who has READ ``name`` — the read-audit log's query surface (#41 was capture-only until now).

        Owner/writer-gated (``require_write_access``, on TOP of the router's ``can_get_metadata``): an access
        log reveals *who* touched a dataset, so only a data owner may audit it — a casual reader can trace the
        dataset's provenance but not enumerate who else viewed it. Aggregated per principal (last read + count,
        newest first). Empty when read-auditing is/was off (the log table exists but has no rows).

        Parameters
        ----------
        name : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Readers
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
            await client.query.get_readers(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_readers(name, limit=limit, request_options=request_options)
        return _response.data

    async def get_reconcile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReconcileStatus:
        """
        Does the lineage graph agree with the **actual Lance file on storage**? (#23)

        Our moat over format-unaware catalogs: because we own a Lance lakehouse we
        read the real on-disk version and cross-check it against the version the graph recorded on the
        ``WROTE`` edge — surfacing a write that bypassed lineage (``storage_ahead``) or a lineage claim
        with no data behind it (``missing_on_storage``). Gated on ``can_get_metadata`` for ``name``; the
        Lance read runs in the threadpool so the blocking object-store I/O never stalls the event loop.

        ``versions_without_lineage`` is the axis the version comparison cannot answer: it compares two
        MAXIMA, so a write whose event was lost and which a later write superseded leaves both equal and the
        dataset reports ``in_sync``. Measured on the live estate 2026-09-11, ``bronze$events`` answered
        in_sync at 87/87 with four retained versions carrying no lineage at all. READ-ONLY here — this door
        reports the holes and the cron sweep is what recovers them, so an operator asking a question never
        mutates the graph as a side effect.

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReconcileStatus
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
            await client.query.get_reconcile(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_reconcile(name, request_options=request_options)
        return _response.data

    async def get_schema(
        self,
        name: str,
        *,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetSchema:
        """
        The persisted column schema for ``name`` — at ``?version=N`` if given, else the latest. (#24)

        Captured from the standard ``SchemaDatasetFacet`` at ingest and stored per-version on the ``WROTE``
        edge (previously the facet was received and discarded). Gated on ``can_get_metadata`` for ``name``;
        this is the prerequisite for column-level lineage and powers schema-diffing between Lance versions.

        Parameters
        ----------
        name : str

        version : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSchema
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
            await client.query.get_schema(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schema(name, version=version, request_options=request_options)
        return _response.data

    async def get_upstream(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Neighbors:
        """
        What ``name`` was derived from (provenance).

        Gated on ``can_get_metadata`` for ``name``; related datasets the caller may not see are
        dropped so the graph can't disclose tables outside its reach.

        ``depth`` bounds the walk, the same shape and ceiling `/graph` already offers. The repository has
        accepted it since the helper landed; only this door never declared it, so every request reached the
        unbounded `*1..` statement whatever the caller wanted. Omitted it stays unbounded — the previous
        behaviour, and what an un-rooted caller asks for — but it is now a caller's CHOICE rather than the
        only thing the door can do. `age.py` names that unbounded path over a grown graph as the reason a
        pooled connection cannot be pinned.

        Parameters
        ----------
        name : str

        depth : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Neighbors
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
            await client.query.get_upstream(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_upstream(name, depth=depth, request_options=request_options)
        return _response.data

    async def get_events(
        self,
        *,
        after: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        summary: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Events:
        """
        The most-recent ingested OpenLineage events (newest first) — the Marquez-style event feed.

        **Durable** (read from Postgres, survives restart / replica-shared) and **governed**: when auth is
        on the feed is filtered like the per-dataset reads — an event is shown only if the caller
        ``can_get_metadata`` on *every* dataset it references (and a dataset-less event is hidden), so the
        audit feed never discloses a table outside the caller's reach. Auth off → pass-through. (#22)

        Pagination (additive, defaults = the old behavior): ``after`` = keyset cursor (the previous
        page's ``next_cursor``); ``limit`` ≤ 500 (server-capped); ``summary=true`` drops the full-JSONB
        ``event`` payload at the SQL layer. The governance filter ALWAYS runs before the slice —
        pagination can never disclose a hidden row's CONTENT. ``next_cursor`` is a WINDOW FLOOR, not
        necessarily a visible row's seq (on a hidden-dense page it is the fetch window's last seq —
        exclusive, so the hidden row itself is never returned; bare seq numbers were already inferable
        from gaps in the pre-pagination feed, so this adds no new disclosure class — reviewed
        2026-07-11).

        Parameters
        ----------
        after : typing.Optional[int]

        limit : typing.Optional[int]

        summary : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Events
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
            await client.query.get_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_events(
            after=after, limit=limit, summary=summary, request_options=request_options
        )
        return _response.data

    async def get_events_projection(
        self,
        *,
        after: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        summary: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Events:
        """
        The feed WITHOUT the per-dataset filter, for a caller that observes the estate (§ G1).

        WHY A SECOND DOOR RATHER THAN A FLAG ON THE FIRST. `/events` is governed per dataset, which is
        right for a person: an event naming a table you cannot see must not disclose it. It is wrong for a
        SERVICE that has to reconcile the whole estate, and the wrongness is silent in both directions —
        measured on this estate 2026-09-09, a run that demonstrably exists answered **404** to a service
        principal, and its inputs answered **200 with an empty list**. A walker sees "nothing here", and an
        estate with no work looks identical to an estate it cannot see.

        THE SERVICE IS NOT THE DISCLOSURE BOUNDARY, and that is what makes this sound rather than a hole.
        A reconciler reads the feed to decide who to TELL; the telling is gated per subject at delivery
        (`can_be_notified`), which is the check that actually protects a person's inbox. Filtering the
        reconciler's own view protects nobody and only guarantees it cannot find the events it exists to
        catch. `can_be_notified` stays the sole disclosure gate; this door moves the estate-read decision
        to the rung that means "may observe the estate".

        `can_observe_events` ON THE ROOT OBJECT — the same rung `POST /v1/projects` and `POST /v1/stores`
        already gate on, so an estate privilege means one thing everywhere. It is `owner` on the root in
        `model.fga`, so nobody holds it by accident and granting it is a deliberate act.

        Identical shape to `/events` otherwise — same keyset cursor, same cap, same `summary` — so a caller
        can move between the two without a second client. `oldest_seq` is reported here too: a walker whose
        cursor falls below it lost a window to the prune, which is the one signal that distinguishes
        "caught up" from "rows went past me".

        Parameters
        ----------
        after : typing.Optional[int]

        limit : typing.Optional[int]

        summary : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Events
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
            await client.query.get_events_projection()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_events_projection(
            after=after, limit=limit, summary=summary, request_options=request_options
        )
        return _response.data

    async def get_runs(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Runs:
        """
        Live run-status board — each run's current state folded onto its ``(:Run)`` node in Apache AGE.

        **Durable** (survives restart / replica-shared) and **governed** like ``/events`` and the per-dataset
        reads: a run is shown only if the caller ``can_get_metadata`` on every dataset it wrote, so the board
        can't enumerate dataset names / creators / errors outside the caller's reach. Auth off → pass-through.

        **BOUNDED AT THE QUERY, newest first.** The board is polled every two seconds and the graph has no run
        retention, so an unbounded read grows without limit: measured live 2026-09-07 it answered 5,122 runs /
        2.65 MB, against 272 rows fifteen days earlier. A limit applied here rather than in the Cypher would
        change nothing — the cost is the READ, and asking for one run took 2.5 s while asking for a hundred
        took 1.4 s.

        The over-fetch window is ``/events``' answer, for the same reason: governance drops rows AFTER the
        read, so a page cut to size first comes back short — or empty — while visible runs sit below it. With
        auth off the filter is pass-through and the headroom is pure waste, so the fetch is exactly ``limit``.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Runs
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
            await client.query.get_runs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_runs(limit=limit, request_options=request_options)
        return _response.data

    async def get_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RunStatus:
        """
        ONE run's state — the point read the board is not.

        "Is this run in the graph?" was answered by downloading `/runs` and scanning it, which is
        O(estate) for a one-row question and became WRONG once the board was bounded: a run outside the
        newest page is missing from the response while present in the graph, so the caller concluded
        ABSENT and reported a provenance defect that did not exist.

        GOVERNED EXACTLY LIKE THE BOARD — visible only if the caller `can_get_metadata` on every dataset
        the run wrote — and an invisible run answers 404, the same as one that is not there. Deliberately
        the same answer: distinguishing them would let a caller enumerate runs it may not see by watching
        which ids give a different refusal.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunStatus
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
            await client.query.get_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_run(run_id, request_options=request_options)
        return _response.data

    async def get_run_inputs(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunInputs:
        """
        The inputs a run consumed, each with the version it PINNED — the per-run reproducibility answer.

        The pinned version rides the graph's ``READ`` edge (the Ray TRAIN job pins every feature — #115
        D1); this endpoint is its API surface (before, Cypher-only). Kept OFF the 2s-polled ``/runs`` board
        — it's a per-run drill-in, and adding a per-run READ-edge fetch to the board would be N+1 on the hot
        path. Governed like every read: an input the caller can't ``can_get_metadata`` is dropped (an empty
        list for a run the caller can't see into is itself non-disclosing). Auth off → pass-through.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunInputs
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
            await client.query.get_run_inputs(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_run_inputs(run_id, request_options=request_options)
        return _response.data
