

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.event_type_out import EventTypeOut
from ..types.list_response_event_type_out import ListResponseEventTypeOut
from ..types.ordering import Ordering
from .raw_client import AsyncRawEventTypeClient, RawEventTypeClient


OMIT = typing.cast(typing.Any, ...)


class EventTypeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventTypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventTypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventTypeClient
        """
        return self._raw_client

    def v1event_type_list(
        self,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        order: typing.Optional[Ordering] = None,
        include_archived: typing.Optional[bool] = None,
        with_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseEventTypeOut:
        """
        Return the list of event types.

        Parameters
        ----------
        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        order : typing.Optional[Ordering]
            The sorting order of the returned items

        include_archived : typing.Optional[bool]
            When `true` archived (deleted but not expunged) items are included in the response

        with_content : typing.Optional[bool]
            When `true` the full item (including the schema) is included in the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseEventTypeOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.event_type.v1event_type_list(
            iterator="user.signup",
        )
        """
        _response = self._raw_client.v1event_type_list(
            limit=limit,
            iterator=iterator,
            order=order,
            include_archived=include_archived,
            with_content=with_content,
            request_options=request_options,
        )
        return _response.data

    def v1event_type_create(
        self,
        *,
        description: str,
        name: str,
        idempotency_key: typing.Optional[str] = None,
        archived: typing.Optional[bool] = OMIT,
        deprecated: typing.Optional[bool] = OMIT,
        feature_flag: typing.Optional[str] = OMIT,
        schemas: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventTypeOut:
        """
        Create new or unarchive existing event type.

        Unarchiving an event type will allow endpoints to filter on it and messages to be sent with it.
        Endpoints filtering on the event type before archival will continue to filter on it.
        This operation does not preserve the description and schemas.

        Parameters
        ----------
        description : str

        name : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        archived : typing.Optional[bool]

        deprecated : typing.Optional[bool]

        feature_flag : typing.Optional[str]

        schemas : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]
            The schema for the event type for a specific version as a JSON schema.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventTypeOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.event_type.v1event_type_create(
            description="A user has signed up",
            name="user.signup",
        )
        """
        _response = self._raw_client.v1event_type_create(
            description=description,
            name=name,
            idempotency_key=idempotency_key,
            archived=archived,
            deprecated=deprecated,
            feature_flag=feature_flag,
            schemas=schemas,
            request_options=request_options,
        )
        return _response.data

    def v1event_type_get(
        self, event_type_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EventTypeOut:
        """
        Get an event type.

        Parameters
        ----------
        event_type_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventTypeOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.event_type.v1event_type_get(
            event_type_name="user.signup",
        )
        """
        _response = self._raw_client.v1event_type_get(event_type_name, request_options=request_options)
        return _response.data

    def v1event_type_update(
        self,
        event_type_name: str,
        *,
        description: str,
        archived: typing.Optional[bool] = OMIT,
        deprecated: typing.Optional[bool] = OMIT,
        feature_flag: typing.Optional[str] = OMIT,
        schemas: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventTypeOut:
        """
        Update an event type.

        Parameters
        ----------
        event_type_name : str

        description : str

        archived : typing.Optional[bool]

        deprecated : typing.Optional[bool]

        feature_flag : typing.Optional[str]

        schemas : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]
            The schema for the event type for a specific version as a JSON schema.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventTypeOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.event_type.v1event_type_update(
            event_type_name="user.signup",
            description="A user has signed up",
        )
        """
        _response = self._raw_client.v1event_type_update(
            event_type_name,
            description=description,
            archived=archived,
            deprecated=deprecated,
            feature_flag=feature_flag,
            schemas=schemas,
            request_options=request_options,
        )
        return _response.data

    def v1event_type_delete(
        self,
        event_type_name: str,
        *,
        expunge: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Archive an event type.

        Endpoints already configured to filter on an event type will continue to do so after archival.
        However, new messages can not be sent with it and endpoints can not filter on it.
        An event type can be unarchived with the
        [create operation](#operation/create_event_type_api_v1_event_type__post).

        Parameters
        ----------
        event_type_name : str

        expunge : typing.Optional[bool]
            By default event types are archived when "deleted". Passing this to `true` deletes them entirely.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.event_type.v1event_type_delete(
            event_type_name="user.signup",
        )
        """
        _response = self._raw_client.v1event_type_delete(
            event_type_name, expunge=expunge, request_options=request_options
        )
        return _response.data

    def patch_event_type(
        self,
        event_type_name: str,
        *,
        archived: typing.Optional[bool] = OMIT,
        deprecated: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        feature_flag: typing.Optional[str] = OMIT,
        schemas: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventTypeOut:
        """
        Partially update an event type.

        Parameters
        ----------
        event_type_name : str

        archived : typing.Optional[bool]

        deprecated : typing.Optional[bool]

        description : typing.Optional[str]

        feature_flag : typing.Optional[str]

        schemas : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventTypeOut


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.event_type.patch_event_type(
            event_type_name="user.signup",
        )
        """
        _response = self._raw_client.patch_event_type(
            event_type_name,
            archived=archived,
            deprecated=deprecated,
            description=description,
            feature_flag=feature_flag,
            schemas=schemas,
            request_options=request_options,
        )
        return _response.data


class AsyncEventTypeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventTypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventTypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventTypeClient
        """
        return self._raw_client

    async def v1event_type_list(
        self,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        order: typing.Optional[Ordering] = None,
        include_archived: typing.Optional[bool] = None,
        with_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListResponseEventTypeOut:
        """
        Return the list of event types.

        Parameters
        ----------
        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        order : typing.Optional[Ordering]
            The sorting order of the returned items

        include_archived : typing.Optional[bool]
            When `true` archived (deleted but not expunged) items are included in the response

        with_content : typing.Optional[bool]
            When `true` the full item (including the schema) is included in the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseEventTypeOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.event_type.v1event_type_list(
                iterator="user.signup",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1event_type_list(
            limit=limit,
            iterator=iterator,
            order=order,
            include_archived=include_archived,
            with_content=with_content,
            request_options=request_options,
        )
        return _response.data

    async def v1event_type_create(
        self,
        *,
        description: str,
        name: str,
        idempotency_key: typing.Optional[str] = None,
        archived: typing.Optional[bool] = OMIT,
        deprecated: typing.Optional[bool] = OMIT,
        feature_flag: typing.Optional[str] = OMIT,
        schemas: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventTypeOut:
        """
        Create new or unarchive existing event type.

        Unarchiving an event type will allow endpoints to filter on it and messages to be sent with it.
        Endpoints filtering on the event type before archival will continue to filter on it.
        This operation does not preserve the description and schemas.

        Parameters
        ----------
        description : str

        name : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        archived : typing.Optional[bool]

        deprecated : typing.Optional[bool]

        feature_flag : typing.Optional[str]

        schemas : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]
            The schema for the event type for a specific version as a JSON schema.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventTypeOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.event_type.v1event_type_create(
                description="A user has signed up",
                name="user.signup",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1event_type_create(
            description=description,
            name=name,
            idempotency_key=idempotency_key,
            archived=archived,
            deprecated=deprecated,
            feature_flag=feature_flag,
            schemas=schemas,
            request_options=request_options,
        )
        return _response.data

    async def v1event_type_get(
        self, event_type_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EventTypeOut:
        """
        Get an event type.

        Parameters
        ----------
        event_type_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventTypeOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.event_type.v1event_type_get(
                event_type_name="user.signup",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1event_type_get(event_type_name, request_options=request_options)
        return _response.data

    async def v1event_type_update(
        self,
        event_type_name: str,
        *,
        description: str,
        archived: typing.Optional[bool] = OMIT,
        deprecated: typing.Optional[bool] = OMIT,
        feature_flag: typing.Optional[str] = OMIT,
        schemas: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventTypeOut:
        """
        Update an event type.

        Parameters
        ----------
        event_type_name : str

        description : str

        archived : typing.Optional[bool]

        deprecated : typing.Optional[bool]

        feature_flag : typing.Optional[str]

        schemas : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]
            The schema for the event type for a specific version as a JSON schema.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventTypeOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.event_type.v1event_type_update(
                event_type_name="user.signup",
                description="A user has signed up",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1event_type_update(
            event_type_name,
            description=description,
            archived=archived,
            deprecated=deprecated,
            feature_flag=feature_flag,
            schemas=schemas,
            request_options=request_options,
        )
        return _response.data

    async def v1event_type_delete(
        self,
        event_type_name: str,
        *,
        expunge: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Archive an event type.

        Endpoints already configured to filter on an event type will continue to do so after archival.
        However, new messages can not be sent with it and endpoints can not filter on it.
        An event type can be unarchived with the
        [create operation](#operation/create_event_type_api_v1_event_type__post).

        Parameters
        ----------
        event_type_name : str

        expunge : typing.Optional[bool]
            By default event types are archived when "deleted". Passing this to `true` deletes them entirely.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.event_type.v1event_type_delete(
                event_type_name="user.signup",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1event_type_delete(
            event_type_name, expunge=expunge, request_options=request_options
        )
        return _response.data

    async def patch_event_type(
        self,
        event_type_name: str,
        *,
        archived: typing.Optional[bool] = OMIT,
        deprecated: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        feature_flag: typing.Optional[str] = OMIT,
        schemas: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventTypeOut:
        """
        Partially update an event type.

        Parameters
        ----------
        event_type_name : str

        archived : typing.Optional[bool]

        deprecated : typing.Optional[bool]

        description : typing.Optional[str]

        feature_flag : typing.Optional[str]

        schemas : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventTypeOut


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.event_type.patch_event_type(
                event_type_name="user.signup",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_event_type(
            event_type_name,
            archived=archived,
            deprecated=deprecated,
            description=description,
            feature_flag=feature_flag,
            schemas=schemas,
            request_options=request_options,
        )
        return _response.data
