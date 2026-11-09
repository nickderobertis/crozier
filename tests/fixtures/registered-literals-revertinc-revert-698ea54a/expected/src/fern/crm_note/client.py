

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.common_deal_association import CommonDealAssociation
from ..types.crm_create_or_update_note_response import CrmCreateOrUpdateNoteResponse
from ..types.crm_get_note_response import CrmGetNoteResponse
from ..types.crm_get_notes_response import CrmGetNotesResponse
from ..types.crm_search_notes_response import CrmSearchNotesResponse
from .raw_client import AsyncRawCrmNoteClient, RawCrmNoteClient


OMIT = typing.cast(typing.Any, ...)


class CrmNoteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrmNoteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrmNoteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrmNoteClient
        """
        return self._raw_client

    def crm_note_get_note(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetNoteResponse:
        """
        Get details of a note

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetNoteResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_note.crm_note_get_note(
            id="id",
        )
        """
        _response = self._raw_client.crm_note_get_note(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    def crm_note_update_note(
        self,
        id: str,
        *,
        additional: typing.Any,
        content: str,
        associations: typing.Optional[CommonDealAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateNoteResponse:
        """
        Update a note

        Parameters
        ----------
        id : str

        additional : typing.Any

        content : str
            The contents of the note in plain text or HTML.

        associations : typing.Optional[CommonDealAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateNoteResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_note.crm_note_update_note(
            id="id",
            additional={"key": "value"},
            content="content",
        )
        """
        _response = self._raw_client.crm_note_update_note(
            id, additional=additional, content=content, associations=associations, request_options=request_options
        )
        return _response.data

    def crm_note_get_notes(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetNotesResponse:
        """
        Get all the notes

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetNotesResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_note.crm_note_get_notes()
        """
        _response = self._raw_client.crm_note_get_notes(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    def crm_note_create_note(
        self,
        *,
        additional: typing.Any,
        content: str,
        associations: typing.Optional[CommonDealAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateNoteResponse:
        """
        Create a new note

        Parameters
        ----------
        additional : typing.Any

        content : str
            The contents of the note in plain text or HTML.

        associations : typing.Optional[CommonDealAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateNoteResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_note.crm_note_create_note(
            additional={"key": "value"},
            content="content",
        )
        """
        _response = self._raw_client.crm_note_create_note(
            additional=additional, content=content, associations=associations, request_options=request_options
        )
        return _response.data

    def crm_note_search_notes(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchNotesResponse:
        """
        Search for notes

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmSearchNotesResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_note.crm_note_search_notes(
            search_criteria={"key": "value"},
        )
        """
        _response = self._raw_client.crm_note_search_notes(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data


class AsyncCrmNoteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrmNoteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrmNoteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrmNoteClient
        """
        return self._raw_client

    async def crm_note_get_note(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetNoteResponse:
        """
        Get details of a note

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetNoteResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_note.crm_note_get_note(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_note_get_note(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    async def crm_note_update_note(
        self,
        id: str,
        *,
        additional: typing.Any,
        content: str,
        associations: typing.Optional[CommonDealAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateNoteResponse:
        """
        Update a note

        Parameters
        ----------
        id : str

        additional : typing.Any

        content : str
            The contents of the note in plain text or HTML.

        associations : typing.Optional[CommonDealAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateNoteResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_note.crm_note_update_note(
                id="id",
                additional={"key": "value"},
                content="content",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_note_update_note(
            id, additional=additional, content=content, associations=associations, request_options=request_options
        )
        return _response.data

    async def crm_note_get_notes(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetNotesResponse:
        """
        Get all the notes

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetNotesResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_note.crm_note_get_notes()


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_note_get_notes(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    async def crm_note_create_note(
        self,
        *,
        additional: typing.Any,
        content: str,
        associations: typing.Optional[CommonDealAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateNoteResponse:
        """
        Create a new note

        Parameters
        ----------
        additional : typing.Any

        content : str
            The contents of the note in plain text or HTML.

        associations : typing.Optional[CommonDealAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateNoteResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_note.crm_note_create_note(
                additional={"key": "value"},
                content="content",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_note_create_note(
            additional=additional, content=content, associations=associations, request_options=request_options
        )
        return _response.data

    async def crm_note_search_notes(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchNotesResponse:
        """
        Search for notes

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmSearchNotesResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_note.crm_note_search_notes(
                search_criteria={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_note_search_notes(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data
