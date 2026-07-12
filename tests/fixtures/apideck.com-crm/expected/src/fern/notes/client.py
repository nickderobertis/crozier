

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_note_response import CreateNoteResponse
from ..types.delete_note_response import DeleteNoteResponse
from ..types.get_note_response import GetNoteResponse
from ..types.get_notes_response import GetNotesResponse
from ..types.update_note_response import UpdateNoteResponse
from .raw_client import AsyncRawNotesClient, RawNotesClient


OMIT = typing.cast(typing.Any, ...)


class NotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotesClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetNotesResponse:
        """
        List notes

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNotesResponse
            Notes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.notes.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

    def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        opportunity_id: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateNoteResponse:
        """
        Create note

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        company_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        content : typing.Optional[str]

        created_at : typing.Optional[str]

        created_by : typing.Optional[str]

        id : typing.Optional[str]

        lead_id : typing.Optional[str]

        opportunity_id : typing.Optional[str]

        owner_id : typing.Optional[str]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        updated_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateNoteResponse
            Note created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.notes.add()
        """
        _response = self._raw_client.add(
            raw=raw,
            active=active,
            company_id=company_id,
            contact_id=contact_id,
            content=content,
            created_at=created_at,
            created_by=created_by,
            id=id,
            lead_id=lead_id,
            opportunity_id=opportunity_id,
            owner_id=owner_id,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetNoteResponse:
        """
        Get note

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNoteResponse
            Note

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.notes.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteNoteResponse:
        """
        Delete note

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteNoteResponse
            Note deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.notes.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        opportunity_id: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateNoteResponse:
        """
        Update note

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        company_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        content : typing.Optional[str]

        created_at : typing.Optional[str]

        created_by : typing.Optional[str]

        id : typing.Optional[str]

        lead_id : typing.Optional[str]

        opportunity_id : typing.Optional[str]

        owner_id : typing.Optional[str]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        updated_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateNoteResponse
            Note updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )
        client.notes.update(
            id_="id",
        )
        """
        _response = self._raw_client.update(
            id_,
            raw=raw,
            active=active,
            company_id=company_id,
            contact_id=contact_id,
            content=content,
            created_at=created_at,
            created_by=created_by,
            id=id,
            lead_id=lead_id,
            opportunity_id=opportunity_id,
            owner_id=owner_id,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data


class AsyncNotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotesClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetNotesResponse:
        """
        List notes

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNotesResponse
            Notes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.notes.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw, cursor=cursor, limit=limit, fields=fields, request_options=request_options
        )
        return _response.data

    async def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        opportunity_id: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateNoteResponse:
        """
        Create note

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        company_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        content : typing.Optional[str]

        created_at : typing.Optional[str]

        created_by : typing.Optional[str]

        id : typing.Optional[str]

        lead_id : typing.Optional[str]

        opportunity_id : typing.Optional[str]

        owner_id : typing.Optional[str]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        updated_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateNoteResponse
            Note created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.notes.add()


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            raw=raw,
            active=active,
            company_id=company_id,
            contact_id=contact_id,
            content=content,
            created_at=created_at,
            created_by=created_by,
            id=id,
            lead_id=lead_id,
            opportunity_id=opportunity_id,
            owner_id=owner_id,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetNoteResponse:
        """
        Get note

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetNoteResponse
            Note

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.notes.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteNoteResponse:
        """
        Delete note

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteNoteResponse
            Note deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.notes.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    async def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        company_id: typing.Optional[str] = OMIT,
        contact_id: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        lead_id: typing.Optional[str] = OMIT,
        opportunity_id: typing.Optional[str] = OMIT,
        owner_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        updated_by: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateNoteResponse:
        """
        Update note

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]

        company_id : typing.Optional[str]

        contact_id : typing.Optional[str]

        content : typing.Optional[str]

        created_at : typing.Optional[str]

        created_by : typing.Optional[str]

        id : typing.Optional[str]

        lead_id : typing.Optional[str]

        opportunity_id : typing.Optional[str]

        owner_id : typing.Optional[str]

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        updated_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateNoteResponse
            Note updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.notes.update(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            raw=raw,
            active=active,
            company_id=company_id,
            contact_id=contact_id,
            content=content,
            created_at=created_at,
            created_by=created_by,
            id=id,
            lead_id=lead_id,
            opportunity_id=opportunity_id,
            owner_id=owner_id,
            title=title,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data
