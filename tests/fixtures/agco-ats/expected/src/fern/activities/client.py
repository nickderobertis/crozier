

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_build_system_shared_dto_activity import ApiPagedResponseBuildSystemSharedDtoActivity
from ..types.build_system_shared_dto_activity import BuildSystemSharedDtoActivity
from ..types.build_system_shared_dto_activity_step import BuildSystemSharedDtoActivityStep
from ..types.build_system_shared_dto_parameter import BuildSystemSharedDtoParameter
from .raw_client import AsyncRawActivitiesClient, RawActivitiesClient


OMIT = typing.cast(typing.Any, ...)


class ActivitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawActivitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawActivitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawActivitiesClient
        """
        return self._raw_client

    def getactivities(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseBuildSystemSharedDtoActivity:
        """
        Gets a collection of Activities. When successful, the response is a PagedResponse of Activities.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted activity, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseBuildSystemSharedDtoActivity
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.activities.getactivities()
        """
        _response = self._raw_client.getactivities(
            limit=limit, offset=offset, is_include_deleted=is_include_deleted, request_options=request_options
        )
        return _response.data

    def postactivity(
        self,
        *,
        activity_id: typing.Optional[int] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        steps: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates an Activity.  The body of the POST is the Activity to create.  The ActivityID will be assigned
                    on creation of the Activity.  When successful, the response is the ActivityID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        activity_id : typing.Optional[int]
            The ID of the activity

        deleted : typing.Optional[bool]


        name : typing.Optional[str]
            The name of the activity

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this activity

        steps : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]]
            The steps which are performed for this activity

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
        client.activities.postactivity()
        """
        _response = self._raw_client.postactivity(
            activity_id=activity_id,
            deleted=deleted,
            name=name,
            parameters=parameters,
            steps=steps,
            request_options=request_options,
        )
        return _response.data

    def getactivity(
        self,
        activity_id: int,
        *,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuildSystemSharedDtoActivity:
        """
        Gets an Activity by ID. When successful, the response is the requested Activity.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        activity_id : int
            The ID of the Activity to get.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted activity, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoActivity
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.activities.getactivity(
            activity_id=1,
        )
        """
        _response = self._raw_client.getactivity(
            activity_id, is_include_deleted=is_include_deleted, request_options=request_options
        )
        return _response.data

    def putactivity(
        self,
        activity_id_: int,
        *,
        activity_id: typing.Optional[int] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        steps: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates an Activity.  The body of the PUT is the updated Activity.  When successful, the response is empty.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_id_ : int
            The id of the activity to update

        activity_id : typing.Optional[int]
            The ID of the activity

        deleted : typing.Optional[bool]


        name : typing.Optional[str]
            The name of the activity

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this activity

        steps : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]]
            The steps which are performed for this activity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.activities.putactivity(
            activity_id_=1,
        )
        """
        _response = self._raw_client.putactivity(
            activity_id_,
            activity_id=activity_id,
            deleted=deleted,
            name=name,
            parameters=parameters,
            steps=steps,
            request_options=request_options,
        )
        return _response.data

    def deleteactivity(self, activity_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes an Activity. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        activity_id : int
            The id of the activity to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.activities.deleteactivity(
            activity_id=1,
        )
        """
        _response = self._raw_client.deleteactivity(activity_id, request_options=request_options)
        return _response.data


class AsyncActivitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawActivitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawActivitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawActivitiesClient
        """
        return self._raw_client

    async def getactivities(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseBuildSystemSharedDtoActivity:
        """
        Gets a collection of Activities. When successful, the response is a PagedResponse of Activities.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted activity, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseBuildSystemSharedDtoActivity
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.activities.getactivities()


        asyncio.run(main())
        """
        _response = await self._raw_client.getactivities(
            limit=limit, offset=offset, is_include_deleted=is_include_deleted, request_options=request_options
        )
        return _response.data

    async def postactivity(
        self,
        *,
        activity_id: typing.Optional[int] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        steps: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates an Activity.  The body of the POST is the Activity to create.  The ActivityID will be assigned
                    on creation of the Activity.  When successful, the response is the ActivityID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        activity_id : typing.Optional[int]
            The ID of the activity

        deleted : typing.Optional[bool]


        name : typing.Optional[str]
            The name of the activity

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this activity

        steps : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]]
            The steps which are performed for this activity

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
            await client.activities.postactivity()


        asyncio.run(main())
        """
        _response = await self._raw_client.postactivity(
            activity_id=activity_id,
            deleted=deleted,
            name=name,
            parameters=parameters,
            steps=steps,
            request_options=request_options,
        )
        return _response.data

    async def getactivity(
        self,
        activity_id: int,
        *,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuildSystemSharedDtoActivity:
        """
        Gets an Activity by ID. When successful, the response is the requested Activity.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        activity_id : int
            The ID of the Activity to get.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted activity, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoActivity
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.activities.getactivity(
                activity_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getactivity(
            activity_id, is_include_deleted=is_include_deleted, request_options=request_options
        )
        return _response.data

    async def putactivity(
        self,
        activity_id_: int,
        *,
        activity_id: typing.Optional[int] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        steps: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates an Activity.  The body of the PUT is the updated Activity.  When successful, the response is empty.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_id_ : int
            The id of the activity to update

        activity_id : typing.Optional[int]
            The ID of the activity

        deleted : typing.Optional[bool]


        name : typing.Optional[str]
            The name of the activity

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this activity

        steps : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]]
            The steps which are performed for this activity

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
            await client.activities.putactivity(
                activity_id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putactivity(
            activity_id_,
            activity_id=activity_id,
            deleted=deleted,
            name=name,
            parameters=parameters,
            steps=steps,
            request_options=request_options,
        )
        return _response.data

    async def deleteactivity(
        self, activity_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an Activity. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        activity_id : int
            The id of the activity to delete

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
            await client.activities.deleteactivity(
                activity_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteactivity(activity_id, request_options=request_options)
        return _response.data
