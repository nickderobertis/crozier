

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawLibraryClient, RawLibraryClient

if typing.TYPE_CHECKING:
    from .archive.client import ArchiveClient, AsyncArchiveClient
    from .loans.client import AsyncLoansClient, LoansClient
    from .members.client import AsyncMembersClient, MembersClient


class LibraryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLibraryClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._members: typing.Optional[MembersClient] = None
        self._loans: typing.Optional[LoansClient] = None
        self._archive: typing.Optional[ArchiveClient] = None

    @property
    def with_raw_response(self) -> RawLibraryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLibraryClient
        """
        return self._raw_client

    @property
    def members(self):
        if self._members is None:
            from .members.client import MembersClient

            self._members = MembersClient(client_wrapper=self._client_wrapper)
        return self._members

    @property
    def loans(self):
        if self._loans is None:
            from .loans.client import LoansClient

            self._loans = LoansClient(client_wrapper=self._client_wrapper)
        return self._loans

    @property
    def archive(self):
        if self._archive is None:
            from .archive.client import ArchiveClient

            self._archive = ArchiveClient(client_wrapper=self._client_wrapper)
        return self._archive


class AsyncLibraryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLibraryClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._members: typing.Optional[AsyncMembersClient] = None
        self._loans: typing.Optional[AsyncLoansClient] = None
        self._archive: typing.Optional[AsyncArchiveClient] = None

    @property
    def with_raw_response(self) -> AsyncRawLibraryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLibraryClient
        """
        return self._raw_client

    @property
    def members(self):
        if self._members is None:
            from .members.client import AsyncMembersClient

            self._members = AsyncMembersClient(client_wrapper=self._client_wrapper)
        return self._members

    @property
    def loans(self):
        if self._loans is None:
            from .loans.client import AsyncLoansClient

            self._loans = AsyncLoansClient(client_wrapper=self._client_wrapper)
        return self._loans

    @property
    def archive(self):
        if self._archive is None:
            from .archive.client import AsyncArchiveClient

            self._archive = AsyncArchiveClient(client_wrapper=self._client_wrapper)
        return self._archive
