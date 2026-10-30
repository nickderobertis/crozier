

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawMaintenanceClient, RawMaintenanceClient

if typing.TYPE_CHECKING:
    from .checkpoints.client import AsyncCheckpointsClient, CheckpointsClient
    from .diagnostics.client import AsyncDiagnosticsClient, DiagnosticsClient
    from .grep_index.client import AsyncGrepIndexClient, GrepIndexClient
    from .runs.client import AsyncRunsClient, RunsClient
    from .store.client import AsyncStoreClient, StoreClient


class MaintenanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMaintenanceClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._checkpoints: typing.Optional[CheckpointsClient] = None
        self._diagnostics: typing.Optional[DiagnosticsClient] = None
        self._grep_index: typing.Optional[GrepIndexClient] = None
        self._runs: typing.Optional[RunsClient] = None
        self._store: typing.Optional[StoreClient] = None

    @property
    def with_raw_response(self) -> RawMaintenanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMaintenanceClient
        """
        return self._raw_client

    @property
    def checkpoints(self):
        if self._checkpoints is None:
            from .checkpoints.client import CheckpointsClient

            self._checkpoints = CheckpointsClient(client_wrapper=self._client_wrapper)
        return self._checkpoints

    @property
    def diagnostics(self):
        if self._diagnostics is None:
            from .diagnostics.client import DiagnosticsClient

            self._diagnostics = DiagnosticsClient(client_wrapper=self._client_wrapper)
        return self._diagnostics

    @property
    def grep_index(self):
        if self._grep_index is None:
            from .grep_index.client import GrepIndexClient

            self._grep_index = GrepIndexClient(client_wrapper=self._client_wrapper)
        return self._grep_index

    @property
    def runs(self):
        if self._runs is None:
            from .runs.client import RunsClient

            self._runs = RunsClient(client_wrapper=self._client_wrapper)
        return self._runs

    @property
    def store(self):
        if self._store is None:
            from .store.client import StoreClient

            self._store = StoreClient(client_wrapper=self._client_wrapper)
        return self._store


class AsyncMaintenanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMaintenanceClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._checkpoints: typing.Optional[AsyncCheckpointsClient] = None
        self._diagnostics: typing.Optional[AsyncDiagnosticsClient] = None
        self._grep_index: typing.Optional[AsyncGrepIndexClient] = None
        self._runs: typing.Optional[AsyncRunsClient] = None
        self._store: typing.Optional[AsyncStoreClient] = None

    @property
    def with_raw_response(self) -> AsyncRawMaintenanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMaintenanceClient
        """
        return self._raw_client

    @property
    def checkpoints(self):
        if self._checkpoints is None:
            from .checkpoints.client import AsyncCheckpointsClient

            self._checkpoints = AsyncCheckpointsClient(client_wrapper=self._client_wrapper)
        return self._checkpoints

    @property
    def diagnostics(self):
        if self._diagnostics is None:
            from .diagnostics.client import AsyncDiagnosticsClient

            self._diagnostics = AsyncDiagnosticsClient(client_wrapper=self._client_wrapper)
        return self._diagnostics

    @property
    def grep_index(self):
        if self._grep_index is None:
            from .grep_index.client import AsyncGrepIndexClient

            self._grep_index = AsyncGrepIndexClient(client_wrapper=self._client_wrapper)
        return self._grep_index

    @property
    def runs(self):
        if self._runs is None:
            from .runs.client import AsyncRunsClient

            self._runs = AsyncRunsClient(client_wrapper=self._client_wrapper)
        return self._runs

    @property
    def store(self):
        if self._store is None:
            from .store.client import AsyncStoreClient

            self._store = AsyncStoreClient(client_wrapper=self._client_wrapper)
        return self._store
