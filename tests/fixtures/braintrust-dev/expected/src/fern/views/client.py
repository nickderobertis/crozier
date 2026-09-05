

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.acl_object_id import AclObjectId
from ..types.acl_object_type import AclObjectType
from ..types.app_limit_param import AppLimitParam
from ..types.create_view_view_type import CreateViewViewType
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.starting_after import StartingAfter
from ..types.view import View
from ..types.view_data import ViewData
from ..types.view_id_param import ViewIdParam
from ..types.view_name import ViewName
from ..types.view_options import ViewOptions
from ..types.view_type import ViewType
from .raw_client import AsyncRawViewsClient, RawViewsClient
from .types.get_view_response import GetViewResponse
from .types.patch_view_view_type import PatchViewViewType


OMIT = typing.cast(typing.Any, ...)


class ViewsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawViewsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawViewsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawViewsClient
        """
        return self._raw_client

    def get_view(
        self,
        *,
        object_type: AclObjectType,
        object_id: AclObjectId,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        view_name: typing.Optional[ViewName] = None,
        view_type: typing.Optional[ViewType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetViewResponse:
        """
        List out all views. The views are sorted by creation date, with the most recently-created views coming first

        Parameters
        ----------
        object_type : AclObjectType
            The object type that the ACL applies to

        object_id : AclObjectId
            The id of the object the ACL applies to

        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        view_name : typing.Optional[ViewName]
            Name of the view to search for

        view_type : typing.Optional[ViewType]
            Type of object that the view corresponds to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetViewResponse
            Returns a list of view objects

        Examples
        --------
        from fern import AclObjectType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.views.get_view(
            object_type=AclObjectType.ORGANIZATION,
            object_id="object_id",
        )
        """
        _response = self._raw_client.get_view(
            object_type=object_type,
            object_id=object_id,
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            view_name=view_name,
            view_type=view_type,
            request_options=request_options,
        )
        return _response.data

    def post_view(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        view_type: CreateViewViewType,
        name: str,
        view_data: typing.Optional[ViewData] = OMIT,
        options: typing.Optional[ViewOptions] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        deleted_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> View:
        """
        Create a new view. If there is an existing view with the same name as the one specified in the request, will return the existing view unmodified

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        view_type : CreateViewViewType
            Type of object that the view corresponds to.

        name : str
            Name of the view

        view_data : typing.Optional[ViewData]

        options : typing.Optional[ViewOptions]

        user_id : typing.Optional[str]
            Identifies the user who created the view

        deleted_at : typing.Optional[dt.datetime]
            Date of role deletion, or null if the role is still active

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        View
            Returns the new view object

        Examples
        --------
        from fern import AclObjectType, CreateViewViewType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.views.post_view(
            object_type=AclObjectType.ORGANIZATION,
            object_id="object_id",
            view_type=CreateViewViewType.PROJECTS,
            name="name",
        )
        """
        _response = self._raw_client.post_view(
            object_type=object_type,
            object_id=object_id,
            view_type=view_type,
            name=name,
            view_data=view_data,
            options=options,
            user_id=user_id,
            deleted_at=deleted_at,
            request_options=request_options,
        )
        return _response.data

    def put_view(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        view_type: CreateViewViewType,
        name: str,
        view_data: typing.Optional[ViewData] = OMIT,
        options: typing.Optional[ViewOptions] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        deleted_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> View:
        """
        Create or replace view. If there is an existing view with the same name as the one specified in the request, will replace the existing view with the provided fields

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        view_type : CreateViewViewType
            Type of object that the view corresponds to.

        name : str
            Name of the view

        view_data : typing.Optional[ViewData]

        options : typing.Optional[ViewOptions]

        user_id : typing.Optional[str]
            Identifies the user who created the view

        deleted_at : typing.Optional[dt.datetime]
            Date of role deletion, or null if the role is still active

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        View
            Returns the new view object

        Examples
        --------
        from fern import AclObjectType, CreateViewViewType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.views.put_view(
            object_type=AclObjectType.ORGANIZATION,
            object_id="object_id",
            view_type=CreateViewViewType.PROJECTS,
            name="name",
        )
        """
        _response = self._raw_client.put_view(
            object_type=object_type,
            object_id=object_id,
            view_type=view_type,
            name=name,
            view_data=view_data,
            options=options,
            user_id=user_id,
            deleted_at=deleted_at,
            request_options=request_options,
        )
        return _response.data

    def get_view_id(
        self,
        view_id: ViewIdParam,
        *,
        object_type: AclObjectType,
        object_id: AclObjectId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> View:
        """
        Get a view object by its id

        Parameters
        ----------
        view_id : ViewIdParam
            View id

        object_type : AclObjectType
            The object type that the ACL applies to

        object_id : AclObjectId
            The id of the object the ACL applies to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        View
            Returns the view object

        Examples
        --------
        from fern import AclObjectType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.views.get_view_id(
            view_id="view_id",
            object_type=AclObjectType.ORGANIZATION,
            object_id="object_id",
        )
        """
        _response = self._raw_client.get_view_id(
            view_id, object_type=object_type, object_id=object_id, request_options=request_options
        )
        return _response.data

    def delete_view_id(
        self,
        view_id: ViewIdParam,
        *,
        object_type: AclObjectType,
        object_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> View:
        """
        Delete a view object by its id

        Parameters
        ----------
        view_id : ViewIdParam
            View id

        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        View
            Returns the deleted view object

        Examples
        --------
        from fern import AclObjectType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.views.delete_view_id(
            view_id="view_id",
            object_type=AclObjectType.ORGANIZATION,
            object_id="object_id",
        )
        """
        _response = self._raw_client.delete_view_id(
            view_id, object_type=object_type, object_id=object_id, request_options=request_options
        )
        return _response.data

    def patch_view_id(
        self,
        view_id: ViewIdParam,
        *,
        object_type: AclObjectType,
        object_id: str,
        view_type: typing.Optional[PatchViewViewType] = OMIT,
        name: typing.Optional[str] = OMIT,
        view_data: typing.Optional[ViewData] = OMIT,
        options: typing.Optional[ViewOptions] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> View:
        """
        Partially update a view object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        view_id : ViewIdParam
            View id

        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        view_type : typing.Optional[PatchViewViewType]
            Type of object that the view corresponds to.

        name : typing.Optional[str]
            Name of the view

        view_data : typing.Optional[ViewData]

        options : typing.Optional[ViewOptions]

        user_id : typing.Optional[str]
            Identifies the user who created the view

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        View
            Returns the view object

        Examples
        --------
        from fern import AclObjectType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.views.patch_view_id(
            view_id="view_id",
            object_type=AclObjectType.ORGANIZATION,
            object_id="object_id",
        )
        """
        _response = self._raw_client.patch_view_id(
            view_id,
            object_type=object_type,
            object_id=object_id,
            view_type=view_type,
            name=name,
            view_data=view_data,
            options=options,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data


class AsyncViewsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawViewsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawViewsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawViewsClient
        """
        return self._raw_client

    async def get_view(
        self,
        *,
        object_type: AclObjectType,
        object_id: AclObjectId,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        view_name: typing.Optional[ViewName] = None,
        view_type: typing.Optional[ViewType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetViewResponse:
        """
        List out all views. The views are sorted by creation date, with the most recently-created views coming first

        Parameters
        ----------
        object_type : AclObjectType
            The object type that the ACL applies to

        object_id : AclObjectId
            The id of the object the ACL applies to

        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        view_name : typing.Optional[ViewName]
            Name of the view to search for

        view_type : typing.Optional[ViewType]
            Type of object that the view corresponds to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetViewResponse
            Returns a list of view objects

        Examples
        --------
        import asyncio

        from fern import AclObjectType, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.views.get_view(
                object_type=AclObjectType.ORGANIZATION,
                object_id="object_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_view(
            object_type=object_type,
            object_id=object_id,
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            view_name=view_name,
            view_type=view_type,
            request_options=request_options,
        )
        return _response.data

    async def post_view(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        view_type: CreateViewViewType,
        name: str,
        view_data: typing.Optional[ViewData] = OMIT,
        options: typing.Optional[ViewOptions] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        deleted_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> View:
        """
        Create a new view. If there is an existing view with the same name as the one specified in the request, will return the existing view unmodified

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        view_type : CreateViewViewType
            Type of object that the view corresponds to.

        name : str
            Name of the view

        view_data : typing.Optional[ViewData]

        options : typing.Optional[ViewOptions]

        user_id : typing.Optional[str]
            Identifies the user who created the view

        deleted_at : typing.Optional[dt.datetime]
            Date of role deletion, or null if the role is still active

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        View
            Returns the new view object

        Examples
        --------
        import asyncio

        from fern import AclObjectType, AsyncFernApi, CreateViewViewType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.views.post_view(
                object_type=AclObjectType.ORGANIZATION,
                object_id="object_id",
                view_type=CreateViewViewType.PROJECTS,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_view(
            object_type=object_type,
            object_id=object_id,
            view_type=view_type,
            name=name,
            view_data=view_data,
            options=options,
            user_id=user_id,
            deleted_at=deleted_at,
            request_options=request_options,
        )
        return _response.data

    async def put_view(
        self,
        *,
        object_type: AclObjectType,
        object_id: str,
        view_type: CreateViewViewType,
        name: str,
        view_data: typing.Optional[ViewData] = OMIT,
        options: typing.Optional[ViewOptions] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        deleted_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> View:
        """
        Create or replace view. If there is an existing view with the same name as the one specified in the request, will replace the existing view with the provided fields

        Parameters
        ----------
        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        view_type : CreateViewViewType
            Type of object that the view corresponds to.

        name : str
            Name of the view

        view_data : typing.Optional[ViewData]

        options : typing.Optional[ViewOptions]

        user_id : typing.Optional[str]
            Identifies the user who created the view

        deleted_at : typing.Optional[dt.datetime]
            Date of role deletion, or null if the role is still active

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        View
            Returns the new view object

        Examples
        --------
        import asyncio

        from fern import AclObjectType, AsyncFernApi, CreateViewViewType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.views.put_view(
                object_type=AclObjectType.ORGANIZATION,
                object_id="object_id",
                view_type=CreateViewViewType.PROJECTS,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_view(
            object_type=object_type,
            object_id=object_id,
            view_type=view_type,
            name=name,
            view_data=view_data,
            options=options,
            user_id=user_id,
            deleted_at=deleted_at,
            request_options=request_options,
        )
        return _response.data

    async def get_view_id(
        self,
        view_id: ViewIdParam,
        *,
        object_type: AclObjectType,
        object_id: AclObjectId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> View:
        """
        Get a view object by its id

        Parameters
        ----------
        view_id : ViewIdParam
            View id

        object_type : AclObjectType
            The object type that the ACL applies to

        object_id : AclObjectId
            The id of the object the ACL applies to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        View
            Returns the view object

        Examples
        --------
        import asyncio

        from fern import AclObjectType, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.views.get_view_id(
                view_id="view_id",
                object_type=AclObjectType.ORGANIZATION,
                object_id="object_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_view_id(
            view_id, object_type=object_type, object_id=object_id, request_options=request_options
        )
        return _response.data

    async def delete_view_id(
        self,
        view_id: ViewIdParam,
        *,
        object_type: AclObjectType,
        object_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> View:
        """
        Delete a view object by its id

        Parameters
        ----------
        view_id : ViewIdParam
            View id

        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        View
            Returns the deleted view object

        Examples
        --------
        import asyncio

        from fern import AclObjectType, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.views.delete_view_id(
                view_id="view_id",
                object_type=AclObjectType.ORGANIZATION,
                object_id="object_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_view_id(
            view_id, object_type=object_type, object_id=object_id, request_options=request_options
        )
        return _response.data

    async def patch_view_id(
        self,
        view_id: ViewIdParam,
        *,
        object_type: AclObjectType,
        object_id: str,
        view_type: typing.Optional[PatchViewViewType] = OMIT,
        name: typing.Optional[str] = OMIT,
        view_data: typing.Optional[ViewData] = OMIT,
        options: typing.Optional[ViewOptions] = OMIT,
        user_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> View:
        """
        Partially update a view object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        view_id : ViewIdParam
            View id

        object_type : AclObjectType

        object_id : str
            The id of the object the view applies to

        view_type : typing.Optional[PatchViewViewType]
            Type of object that the view corresponds to.

        name : typing.Optional[str]
            Name of the view

        view_data : typing.Optional[ViewData]

        options : typing.Optional[ViewOptions]

        user_id : typing.Optional[str]
            Identifies the user who created the view

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        View
            Returns the view object

        Examples
        --------
        import asyncio

        from fern import AclObjectType, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.views.patch_view_id(
                view_id="view_id",
                object_type=AclObjectType.ORGANIZATION,
                object_id="object_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_view_id(
            view_id,
            object_type=object_type,
            object_id=object_id,
            view_type=view_type,
            name=name,
            view_data=view_data,
            options=options,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data
