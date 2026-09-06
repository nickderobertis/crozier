

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawAnalyzeClient, RawAnalyzeClient

if typing.TYPE_CHECKING:
    from .reports.client import AsyncReportsClient, ReportsClient


class AnalyzeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAnalyzeClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._reports: typing.Optional[ReportsClient] = None

    @property
    def with_raw_response(self) -> RawAnalyzeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAnalyzeClient
        """
        return self._raw_client

    @property
    def reports(self):
        if self._reports is None:
            from .reports.client import ReportsClient

            self._reports = ReportsClient(client_wrapper=self._client_wrapper)
        return self._reports


class AsyncAnalyzeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAnalyzeClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._reports: typing.Optional[AsyncReportsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawAnalyzeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAnalyzeClient
        """
        return self._raw_client

    @property
    def reports(self):
        if self._reports is None:
            from .reports.client import AsyncReportsClient

            self._reports = AsyncReportsClient(client_wrapper=self._client_wrapper)
        return self._reports
