

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_content_submission_shared_business_entities_user_content_definition import (
    ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition,
)
from ..types.content_submission_shared_business_entities_user_content_definition import (
    ContentSubmissionSharedBusinessEntitiesUserContentDefinition,
)
from .raw_client import AsyncRawUsercontentdefinitionsClient, RawUsercontentdefinitionsClient


OMIT = typing.cast(typing.Any, ...)


class UsercontentdefinitionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsercontentdefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsercontentdefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsercontentdefinitionsClient
        """
        return self._raw_client

    def getusercontentdefinitions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        content_definition_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition:
        """
        Gets a collection of UserContentDefinitions. When successful, the response is a PagedResponse of UserContentDefinitions.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by UserID.

        content_definition_id : typing.Optional[int]
            Optional. Filter by ContentDefinitionID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.usercontentdefinitions.getusercontentdefinitions()
        """
        _response = self._raw_client.getusercontentdefinitions(
            limit=limit,
            offset=offset,
            user_id=user_id,
            content_definition_id=content_definition_id,
            request_options=request_options,
        )
        return _response.data

    def postusercontentdefinition(
        self,
        *,
        content_definition_id: typing.Optional[int] = OMIT,
        user_content_definition_id: typing.Optional[int] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a UserContentDefinition.  The body of the POST is the UserContentDefinition to create.
                    The UserContentDefinitionID will be assigned on creation of the Job.  When successful, the response
                    is the UserContentDefinitionID.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id : typing.Optional[int]
            The ID of the ContentDefinition.

        user_content_definition_id : typing.Optional[int]
            Read Only. The ID of the User to ContentDefinition relationship.

        user_id : typing.Optional[int]
            The ID of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.usercontentdefinitions.postusercontentdefinition()
        """
        _response = self._raw_client.postusercontentdefinition(
            content_definition_id=content_definition_id,
            user_content_definition_id=user_content_definition_id,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    def getusercontentdefinition(
        self, user_content_definition_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentSubmissionSharedBusinessEntitiesUserContentDefinition:
        """
        Gets a UserContentDefinition by ID. When successful, the response is the requested UserContentDefinition.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        user_content_definition_id : int
            The ID of the UserContentDefinition to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSubmissionSharedBusinessEntitiesUserContentDefinition
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.usercontentdefinitions.getusercontentdefinition(
            user_content_definition_id=1,
        )
        """
        _response = self._raw_client.getusercontentdefinition(
            user_content_definition_id, request_options=request_options
        )
        return _response.data

    def deleteusercontentdefinition(
        self, user_content_definition_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an UserContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        user_content_definition_id : int
            The ID of the UserContentDefinition to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.usercontentdefinitions.deleteusercontentdefinition(
            user_content_definition_id=1,
        )
        """
        _response = self._raw_client.deleteusercontentdefinition(
            user_content_definition_id, request_options=request_options
        )
        return _response.data


class AsyncUsercontentdefinitionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsercontentdefinitionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsercontentdefinitionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsercontentdefinitionsClient
        """
        return self._raw_client

    async def getusercontentdefinitions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        content_definition_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition:
        """
        Gets a collection of UserContentDefinitions. When successful, the response is a PagedResponse of UserContentDefinitions.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by UserID.

        content_definition_id : typing.Optional[int]
            Optional. Filter by ContentDefinitionID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.usercontentdefinitions.getusercontentdefinitions()


        asyncio.run(main())
        """
        _response = await self._raw_client.getusercontentdefinitions(
            limit=limit,
            offset=offset,
            user_id=user_id,
            content_definition_id=content_definition_id,
            request_options=request_options,
        )
        return _response.data

    async def postusercontentdefinition(
        self,
        *,
        content_definition_id: typing.Optional[int] = OMIT,
        user_content_definition_id: typing.Optional[int] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a UserContentDefinition.  The body of the POST is the UserContentDefinition to create.
                    The UserContentDefinitionID will be assigned on creation of the Job.  When successful, the response
                    is the UserContentDefinitionID.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id : typing.Optional[int]
            The ID of the ContentDefinition.

        user_content_definition_id : typing.Optional[int]
            Read Only. The ID of the User to ContentDefinition relationship.

        user_id : typing.Optional[int]
            The ID of the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.usercontentdefinitions.postusercontentdefinition()


        asyncio.run(main())
        """
        _response = await self._raw_client.postusercontentdefinition(
            content_definition_id=content_definition_id,
            user_content_definition_id=user_content_definition_id,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    async def getusercontentdefinition(
        self, user_content_definition_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentSubmissionSharedBusinessEntitiesUserContentDefinition:
        """
        Gets a UserContentDefinition by ID. When successful, the response is the requested UserContentDefinition.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        user_content_definition_id : int
            The ID of the UserContentDefinition to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSubmissionSharedBusinessEntitiesUserContentDefinition
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.usercontentdefinitions.getusercontentdefinition(
                user_content_definition_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getusercontentdefinition(
            user_content_definition_id, request_options=request_options
        )
        return _response.data

    async def deleteusercontentdefinition(
        self, user_content_definition_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an UserContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        user_content_definition_id : int
            The ID of the UserContentDefinition to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.usercontentdefinitions.deleteusercontentdefinition(
                user_content_definition_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteusercontentdefinition(
            user_content_definition_id, request_options=request_options
        )
        return _response.data
