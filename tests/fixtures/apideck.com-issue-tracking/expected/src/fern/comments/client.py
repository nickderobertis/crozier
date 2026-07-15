

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.comments_sort import CommentsSort
from ..types.create_comment_response import CreateCommentResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.delete_comment_response import DeleteCommentResponse
from ..types.get_comment_response import GetCommentResponse
from ..types.get_comments_response import GetCommentsResponse
from ..types.id import Id
from ..types.update_comment_response import UpdateCommentResponse
from ..types.updated_at import UpdatedAt
from .raw_client import AsyncRawCommentsClient, RawCommentsClient


OMIT = typing.cast(typing.Any, ...)


class CommentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCommentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCommentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCommentsClient
        """
        return self._raw_client

    def collection_ticket_comments_all(
        self,
        collection_id: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[CommentsSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCommentsResponse:
        """
        List Comments

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        sort : typing.Optional[CommentsSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCommentsResponse
            List Comments

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.comments.collection_ticket_comments_all(
            collection_id="apideck-io",
            ticket_id="ticket_id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.collection_ticket_comments_all(
            collection_id,
            ticket_id,
            raw=raw,
            cursor=cursor,
            limit=limit,
            sort=sort,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    def collection_ticket_comments_add(
        self,
        collection_id: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        body: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        id: typing.Optional[Id] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCommentResponse:
        """
        Create Comment

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        body : typing.Optional[str]
            Body of the comment

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        id : typing.Optional[Id]

        updated_at : typing.Optional[UpdatedAt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCommentResponse
            Create a Comment

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.comments.collection_ticket_comments_add(
            collection_id="apideck-io",
            ticket_id="ticket_id",
        )
        """
        _response = self._raw_client.collection_ticket_comments_add(
            collection_id,
            ticket_id,
            raw=raw,
            body=body,
            created_at=created_at,
            created_by=created_by,
            id=id,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    def collection_ticket_comments_one(
        self,
        collection_id: str,
        ticket_id: str,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCommentResponse:
        """
        Get Comment

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        id : str
            ID of the record you are acting upon.

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
        GetCommentResponse
            Get a Comment

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.comments.collection_ticket_comments_one(
            collection_id="apideck-io",
            ticket_id="ticket_id",
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.collection_ticket_comments_one(
            collection_id,
            ticket_id,
            id,
            raw=raw,
            cursor=cursor,
            limit=limit,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    def collection_ticket_comments_delete(
        self,
        collection_id: str,
        ticket_id: str,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteCommentResponse:
        """
        Delete Comment

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCommentResponse
            Delete a Comment

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.comments.collection_ticket_comments_delete(
            collection_id="apideck-io",
            ticket_id="ticket_id",
            id="id",
        )
        """
        _response = self._raw_client.collection_ticket_comments_delete(
            collection_id, ticket_id, id, raw=raw, request_options=request_options
        )
        return _response.data

    def collection_ticket_comments_update(
        self,
        collection_id: str,
        ticket_id: str,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        body: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        id: typing.Optional[Id] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCommentResponse:
        """
        Update Comment

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        body : typing.Optional[str]
            Body of the comment

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        id : typing.Optional[Id]

        updated_at : typing.Optional[UpdatedAt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCommentResponse
            Update a Comment

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.comments.collection_ticket_comments_update(
            collection_id="apideck-io",
            ticket_id="ticket_id",
            id_="id",
        )
        """
        _response = self._raw_client.collection_ticket_comments_update(
            collection_id,
            ticket_id,
            id_,
            raw=raw,
            body=body,
            created_at=created_at,
            created_by=created_by,
            id=id,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data


class AsyncCommentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCommentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCommentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCommentsClient
        """
        return self._raw_client

    async def collection_ticket_comments_all(
        self,
        collection_id: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[CommentsSort] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCommentsResponse:
        """
        List Comments

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        sort : typing.Optional[CommentsSort]
            Apply sorting

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCommentsResponse
            List Comments

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.comments.collection_ticket_comments_all(
                collection_id="apideck-io",
                ticket_id="ticket_id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_ticket_comments_all(
            collection_id,
            ticket_id,
            raw=raw,
            cursor=cursor,
            limit=limit,
            sort=sort,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    async def collection_ticket_comments_add(
        self,
        collection_id: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        body: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        id: typing.Optional[Id] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCommentResponse:
        """
        Create Comment

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        body : typing.Optional[str]
            Body of the comment

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        id : typing.Optional[Id]

        updated_at : typing.Optional[UpdatedAt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCommentResponse
            Create a Comment

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.comments.collection_ticket_comments_add(
                collection_id="apideck-io",
                ticket_id="ticket_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_ticket_comments_add(
            collection_id,
            ticket_id,
            raw=raw,
            body=body,
            created_at=created_at,
            created_by=created_by,
            id=id,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    async def collection_ticket_comments_one(
        self,
        collection_id: str,
        ticket_id: str,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCommentResponse:
        """
        Get Comment

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        id : str
            ID of the record you are acting upon.

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
        GetCommentResponse
            Get a Comment

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.comments.collection_ticket_comments_one(
                collection_id="apideck-io",
                ticket_id="ticket_id",
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_ticket_comments_one(
            collection_id,
            ticket_id,
            id,
            raw=raw,
            cursor=cursor,
            limit=limit,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    async def collection_ticket_comments_delete(
        self,
        collection_id: str,
        ticket_id: str,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteCommentResponse:
        """
        Delete Comment

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCommentResponse
            Delete a Comment

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.comments.collection_ticket_comments_delete(
                collection_id="apideck-io",
                ticket_id="ticket_id",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_ticket_comments_delete(
            collection_id, ticket_id, id, raw=raw, request_options=request_options
        )
        return _response.data

    async def collection_ticket_comments_update(
        self,
        collection_id: str,
        ticket_id: str,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        body: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        id: typing.Optional[Id] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCommentResponse:
        """
        Update Comment

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        body : typing.Optional[str]
            Body of the comment

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        id : typing.Optional[Id]

        updated_at : typing.Optional[UpdatedAt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCommentResponse
            Update a Comment

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.comments.collection_ticket_comments_update(
                collection_id="apideck-io",
                ticket_id="ticket_id",
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_ticket_comments_update(
            collection_id,
            ticket_id,
            id_,
            raw=raw,
            body=body,
            created_at=created_at,
            created_by=created_by,
            id=id,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data
