

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.assignment import Assignment
from ..types.media_usage import MediaUsage
from ..types.tag import Tag
from .raw_client import AsyncRawAssignmentClient, RawAssignmentClient


OMIT = typing.cast(typing.Any, ...)


class AssignmentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssignmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssignmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssignmentClient
        """
        return self._raw_client

    def list_assignments(
        self,
        *,
        owned_by: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        open: typing.Optional[bool] = None,
        always_open: typing.Optional[bool] = None,
        tag: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Assignment]:
        """
        Parameters
        ----------
        owned_by : typing.Optional[str]
            Restrict results to assignments owned by this user.

        page : typing.Optional[int]
            Pagination page

        page_size : typing.Optional[int]
            Pagination page size

        q : typing.Optional[str]
            Restrict results to assignments whose name or description matches this keyword.

        url_words : typing.Optional[str]
            Select an assignment by urlWords.

        open : typing.Optional[bool]
            Select open or closed assignments

        always_open : typing.Optional[bool]
            Select assignments with no closing date.

        tag : typing.Optional[str]
            Restrict results to assignments which are tagged with this tag.

        name : typing.Optional[str]
            Restrict results to the assignment (or potentially assignments) with this exact name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Assignment]
            A list of assignments

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assignment.list_assignments()
        """
        _response = self._raw_client.list_assignments(
            owned_by=owned_by,
            page=page,
            page_size=page_size,
            q=q,
            url_words=url_words,
            open=open,
            always_open=always_open,
            tag=tag,
            name=name,
            request_options=request_options,
        )
        return _response.data

    def create_a_new_assignment(
        self,
        *,
        name: str,
        allows_anonymous_contributions: typing.Optional[bool] = OMIT,
        cover: typing.Optional[MediaUsage] = OMIT,
        description: typing.Optional[str] = OMIT,
        embargo: typing.Optional[dt.datetime] = OMIT,
        ends: typing.Optional[dt.datetime] = OMIT,
        featured: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        media_required: typing.Optional[bool] = OMIT,
        moderator: typing.Optional[str] = OMIT,
        receipt_message: typing.Optional[str] = OMIT,
        starts: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        url_words: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Assignment:
        """
        Parameters
        ----------
        name : str

        allows_anonymous_contributions : typing.Optional[bool]

        cover : typing.Optional[MediaUsage]

        description : typing.Optional[str]

        embargo : typing.Optional[dt.datetime]

        ends : typing.Optional[dt.datetime]

        featured : typing.Optional[bool]

        id : typing.Optional[str]

        media_required : typing.Optional[bool]

        moderator : typing.Optional[str]
            Optional credential id of the login which will moderator this assignment.

        receipt_message : typing.Optional[str]
            An optional assignment specific message to be displayed on successful contribution submission. For example, this might be used to inform contributors of assignment specific moderation time frames.

        starts : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[Tag]]

        url_words : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assignment
            Assignment created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assignment.create_a_new_assignment(
            name="name",
        )
        """
        _response = self._raw_client.create_a_new_assignment(
            name=name,
            allows_anonymous_contributions=allows_anonymous_contributions,
            cover=cover,
            description=description,
            embargo=embargo,
            ends=ends,
            featured=featured,
            id=id,
            media_required=media_required,
            moderator=moderator,
            receipt_message=receipt_message,
            starts=starts,
            tags=tags,
            url_words=url_words,
            request_options=request_options,
        )
        return _response.data

    def get_a_single_assigment_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Assignment:
        """
        Parameters
        ----------
        id : str
            Id of the assignment to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assignment
            Assignment found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assignment.get_a_single_assigment_by_id(
            id="id",
        )
        """
        _response = self._raw_client.get_a_single_assigment_by_id(id, request_options=request_options)
        return _response.data

    def delete_this_assignment_and_all_of_its_contributions(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Id of the assignment to return

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
        )
        client.assignment.delete_this_assignment_and_all_of_its_contributions(
            id="id",
        )
        """
        _response = self._raw_client.delete_this_assignment_and_all_of_its_contributions(
            id, request_options=request_options
        )
        return _response.data


class AsyncAssignmentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssignmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssignmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssignmentClient
        """
        return self._raw_client

    async def list_assignments(
        self,
        *,
        owned_by: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        open: typing.Optional[bool] = None,
        always_open: typing.Optional[bool] = None,
        tag: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Assignment]:
        """
        Parameters
        ----------
        owned_by : typing.Optional[str]
            Restrict results to assignments owned by this user.

        page : typing.Optional[int]
            Pagination page

        page_size : typing.Optional[int]
            Pagination page size

        q : typing.Optional[str]
            Restrict results to assignments whose name or description matches this keyword.

        url_words : typing.Optional[str]
            Select an assignment by urlWords.

        open : typing.Optional[bool]
            Select open or closed assignments

        always_open : typing.Optional[bool]
            Select assignments with no closing date.

        tag : typing.Optional[str]
            Restrict results to assignments which are tagged with this tag.

        name : typing.Optional[str]
            Restrict results to the assignment (or potentially assignments) with this exact name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Assignment]
            A list of assignments

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assignment.list_assignments()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_assignments(
            owned_by=owned_by,
            page=page,
            page_size=page_size,
            q=q,
            url_words=url_words,
            open=open,
            always_open=always_open,
            tag=tag,
            name=name,
            request_options=request_options,
        )
        return _response.data

    async def create_a_new_assignment(
        self,
        *,
        name: str,
        allows_anonymous_contributions: typing.Optional[bool] = OMIT,
        cover: typing.Optional[MediaUsage] = OMIT,
        description: typing.Optional[str] = OMIT,
        embargo: typing.Optional[dt.datetime] = OMIT,
        ends: typing.Optional[dt.datetime] = OMIT,
        featured: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        media_required: typing.Optional[bool] = OMIT,
        moderator: typing.Optional[str] = OMIT,
        receipt_message: typing.Optional[str] = OMIT,
        starts: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        url_words: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Assignment:
        """
        Parameters
        ----------
        name : str

        allows_anonymous_contributions : typing.Optional[bool]

        cover : typing.Optional[MediaUsage]

        description : typing.Optional[str]

        embargo : typing.Optional[dt.datetime]

        ends : typing.Optional[dt.datetime]

        featured : typing.Optional[bool]

        id : typing.Optional[str]

        media_required : typing.Optional[bool]

        moderator : typing.Optional[str]
            Optional credential id of the login which will moderator this assignment.

        receipt_message : typing.Optional[str]
            An optional assignment specific message to be displayed on successful contribution submission. For example, this might be used to inform contributors of assignment specific moderation time frames.

        starts : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[Tag]]

        url_words : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assignment
            Assignment created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assignment.create_a_new_assignment(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_assignment(
            name=name,
            allows_anonymous_contributions=allows_anonymous_contributions,
            cover=cover,
            description=description,
            embargo=embargo,
            ends=ends,
            featured=featured,
            id=id,
            media_required=media_required,
            moderator=moderator,
            receipt_message=receipt_message,
            starts=starts,
            tags=tags,
            url_words=url_words,
            request_options=request_options,
        )
        return _response.data

    async def get_a_single_assigment_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Assignment:
        """
        Parameters
        ----------
        id : str
            Id of the assignment to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assignment
            Assignment found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assignment.get_a_single_assigment_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_single_assigment_by_id(id, request_options=request_options)
        return _response.data

    async def delete_this_assignment_and_all_of_its_contributions(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Id of the assignment to return

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
        )


        async def main() -> None:
            await client.assignment.delete_this_assignment_and_all_of_its_contributions(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_this_assignment_and_all_of_its_contributions(
            id, request_options=request_options
        )
        return _response.data
