

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.column_graph import ColumnGraph
from ..types.column_neighbors import ColumnNeighbors
from ..types.creator import Creator
from ..types.dataset_schema import DatasetSchema
from ..types.events import Events
from ..types.http_validation_error import HttpValidationError
from ..types.lineage_graph import LineageGraph
from ..types.neighbors import Neighbors
from ..types.producers import Producers
from ..types.readers import Readers
from ..types.reconcile_status import ReconcileStatus
from ..types.run_inputs import RunInputs
from ..types.run_status import RunStatus
from ..types.runs import Runs
from pydantic import ValidationError


class RawQueryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_dataset_columns(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ColumnGraph]:
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
        HttpResponse[ColumnGraph]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/columns",
            method="GET",
            params={
                "depth": depth,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ColumnGraph,
                    parse_obj_as(
                        type_=ColumnGraph,
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

    def get_column_downstream(
        self,
        name: str,
        field: str,
        *,
        depth: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ColumnNeighbors]:
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
        HttpResponse[ColumnNeighbors]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/columns/{encode_path_param(field)}/downstream",
            method="GET",
            params={
                "depth": depth,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ColumnNeighbors,
                    parse_obj_as(
                        type_=ColumnNeighbors,
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

    def get_column_upstream(
        self,
        name: str,
        field: str,
        *,
        depth: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ColumnNeighbors]:
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
        HttpResponse[ColumnNeighbors]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/columns/{encode_path_param(field)}/upstream",
            method="GET",
            params={
                "depth": depth,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ColumnNeighbors,
                    parse_obj_as(
                        type_=ColumnNeighbors,
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

    def get_creator(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Creator]:
        """
        Who created ``name`` (the verified catalog principal). Gated on ``can_get_metadata``.

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Creator]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/creator",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Creator,
                    parse_obj_as(
                        type_=Creator,
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

    def get_downstream(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Neighbors]:
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
        HttpResponse[Neighbors]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/downstream",
            method="GET",
            params={
                "depth": depth,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Neighbors,
                    parse_obj_as(
                        type_=Neighbors,
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

    def get_graph(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LineageGraph]:
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
        HttpResponse[LineageGraph]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/graph",
            method="GET",
            params={
                "depth": depth,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LineageGraph,
                    parse_obj_as(
                        type_=LineageGraph,
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

    def get_producers(
        self, name: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Producers]:
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
        HttpResponse[Producers]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/producers",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Producers,
                    parse_obj_as(
                        type_=Producers,
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

    def get_readers(
        self, name: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Readers]:
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
        HttpResponse[Readers]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/readers",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Readers,
                    parse_obj_as(
                        type_=Readers,
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

    def get_reconcile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ReconcileStatus]:
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
        HttpResponse[ReconcileStatus]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/reconcile",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReconcileStatus,
                    parse_obj_as(
                        type_=ReconcileStatus,
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

    def get_schema(
        self,
        name: str,
        *,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DatasetSchema]:
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
        HttpResponse[DatasetSchema]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/schema",
            method="GET",
            params={
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetSchema,
                    parse_obj_as(
                        type_=DatasetSchema,
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

    def get_upstream(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Neighbors]:
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
        HttpResponse[Neighbors]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/upstream",
            method="GET",
            params={
                "depth": depth,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Neighbors,
                    parse_obj_as(
                        type_=Neighbors,
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

    def get_events(
        self,
        *,
        after: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        summary: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Events]:
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
        HttpResponse[Events]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "events",
            method="GET",
            params={
                "after": after,
                "limit": limit,
                "summary": summary,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Events,
                    parse_obj_as(
                        type_=Events,
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

    def get_events_projection(
        self,
        *,
        after: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        summary: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Events]:
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
        HttpResponse[Events]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "events/projection",
            method="GET",
            params={
                "after": after,
                "limit": limit,
                "summary": summary,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Events,
                    parse_obj_as(
                        type_=Events,
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

    def get_runs(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Runs]:
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
        HttpResponse[Runs]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "runs",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Runs,
                    parse_obj_as(
                        type_=Runs,
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

    def get_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RunStatus]:
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
        HttpResponse[RunStatus]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunStatus,
                    parse_obj_as(
                        type_=RunStatus,
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

    def get_run_inputs(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RunInputs]:
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
        HttpResponse[RunInputs]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}/inputs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunInputs,
                    parse_obj_as(
                        type_=RunInputs,
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


class AsyncRawQueryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_dataset_columns(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ColumnGraph]:
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
        AsyncHttpResponse[ColumnGraph]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/columns",
            method="GET",
            params={
                "depth": depth,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ColumnGraph,
                    parse_obj_as(
                        type_=ColumnGraph,
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

    async def get_column_downstream(
        self,
        name: str,
        field: str,
        *,
        depth: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ColumnNeighbors]:
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
        AsyncHttpResponse[ColumnNeighbors]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/columns/{encode_path_param(field)}/downstream",
            method="GET",
            params={
                "depth": depth,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ColumnNeighbors,
                    parse_obj_as(
                        type_=ColumnNeighbors,
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

    async def get_column_upstream(
        self,
        name: str,
        field: str,
        *,
        depth: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ColumnNeighbors]:
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
        AsyncHttpResponse[ColumnNeighbors]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/columns/{encode_path_param(field)}/upstream",
            method="GET",
            params={
                "depth": depth,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ColumnNeighbors,
                    parse_obj_as(
                        type_=ColumnNeighbors,
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

    async def get_creator(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Creator]:
        """
        Who created ``name`` (the verified catalog principal). Gated on ``can_get_metadata``.

        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Creator]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/creator",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Creator,
                    parse_obj_as(
                        type_=Creator,
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

    async def get_downstream(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Neighbors]:
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
        AsyncHttpResponse[Neighbors]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/downstream",
            method="GET",
            params={
                "depth": depth,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Neighbors,
                    parse_obj_as(
                        type_=Neighbors,
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

    async def get_graph(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LineageGraph]:
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
        AsyncHttpResponse[LineageGraph]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/graph",
            method="GET",
            params={
                "depth": depth,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LineageGraph,
                    parse_obj_as(
                        type_=LineageGraph,
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

    async def get_producers(
        self, name: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Producers]:
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
        AsyncHttpResponse[Producers]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/producers",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Producers,
                    parse_obj_as(
                        type_=Producers,
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

    async def get_readers(
        self, name: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Readers]:
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
        AsyncHttpResponse[Readers]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/readers",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Readers,
                    parse_obj_as(
                        type_=Readers,
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

    async def get_reconcile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ReconcileStatus]:
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
        AsyncHttpResponse[ReconcileStatus]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/reconcile",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReconcileStatus,
                    parse_obj_as(
                        type_=ReconcileStatus,
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

    async def get_schema(
        self,
        name: str,
        *,
        version: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DatasetSchema]:
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
        AsyncHttpResponse[DatasetSchema]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/schema",
            method="GET",
            params={
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DatasetSchema,
                    parse_obj_as(
                        type_=DatasetSchema,
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

    async def get_upstream(
        self, name: str, *, depth: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Neighbors]:
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
        AsyncHttpResponse[Neighbors]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"datasets/{encode_path_param(name)}/upstream",
            method="GET",
            params={
                "depth": depth,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Neighbors,
                    parse_obj_as(
                        type_=Neighbors,
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

    async def get_events(
        self,
        *,
        after: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        summary: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Events]:
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
        AsyncHttpResponse[Events]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "events",
            method="GET",
            params={
                "after": after,
                "limit": limit,
                "summary": summary,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Events,
                    parse_obj_as(
                        type_=Events,
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

    async def get_events_projection(
        self,
        *,
        after: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        summary: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Events]:
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
        AsyncHttpResponse[Events]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "events/projection",
            method="GET",
            params={
                "after": after,
                "limit": limit,
                "summary": summary,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Events,
                    parse_obj_as(
                        type_=Events,
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

    async def get_runs(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Runs]:
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
        AsyncHttpResponse[Runs]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "runs",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Runs,
                    parse_obj_as(
                        type_=Runs,
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

    async def get_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RunStatus]:
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
        AsyncHttpResponse[RunStatus]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunStatus,
                    parse_obj_as(
                        type_=RunStatus,
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

    async def get_run_inputs(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RunInputs]:
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
        AsyncHttpResponse[RunInputs]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}/inputs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunInputs,
                    parse_obj_as(
                        type_=RunInputs,
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
