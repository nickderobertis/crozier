

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_authorization_codes_shared_models_category import (
    ApiIPagedResponseAuthorizationCodesSharedModelsCategory,
)
from ..types.api_i_paged_response_authorization_codes_shared_models_category_user_report import (
    ApiIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport,
)
from .raw_client import AsyncRawAuthorizationcategoriesClient, RawAuthorizationcategoriesClient


OMIT = typing.cast(typing.Any, ...)


class AuthorizationcategoriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthorizationcategoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthorizationcategoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthorizationcategoriesClient
        """
        return self._raw_client

    def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        definition_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseAuthorizationCodesSharedModelsCategory:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by categories visible to the provided user with the provided userID.

        definition_id : typing.Optional[str]
            Optional. Filter by categories containing a definition with the provided ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseAuthorizationCodesSharedModelsCategory
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcategories.get()
        """
        _response = self._raw_client.get(
            limit=limit, offset=offset, user_id=user_id, definition_id=definition_id, request_options=request_options
        )
        return _response.data

    def post(
        self,
        *,
        description: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        description : typing.Optional[str]
            A description of the Category.

        id : typing.Optional[str]
            The ID of the Category.

        name : typing.Optional[str]
            The Name of the Category.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcategories.post()
        """
        _response = self._raw_client.post(description=description, id=id, name=name, request_options=request_options)
        return _response.data

    def getusers(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_i_ds: typing.Optional[str] = None,
        category_i_ds: typing.Optional[str] = None,
        include_categories: typing.Optional[bool] = None,
        include_users: typing.Optional[bool] = None,
        user_search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. Defaults to 10.

        offset : typing.Optional[int]
            Optional. Defaults to 0.

        user_i_ds : typing.Optional[str]
            Optional. Includes only users with IDs on the provided comma-separated list.

        category_i_ds : typing.Optional[str]
            Optional. Includes only users with categories with IDs on the provided comma-separated list.

        include_categories : typing.Optional[bool]
            If true, include full Authorization Category detail. Defaults to false.

        include_users : typing.Optional[bool]
            If true, include full User detail. Defaults to false.

        user_search : typing.Optional[str]
            Optional. Includes only users with a Name, Username, or Email containing the provided value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcategories.getusers()
        """
        _response = self._raw_client.getusers(
            limit=limit,
            offset=offset,
            user_i_ds=user_i_ds,
            category_i_ds=category_i_ds,
            include_categories=include_categories,
            include_users=include_users,
            user_search=user_search,
            request_options=request_options,
        )
        return _response.data

    def put(
        self,
        id_: str,
        *,
        description: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : str

        description : typing.Optional[str]
            A description of the Category.

        id : typing.Optional[str]
            The ID of the Category.

        name : typing.Optional[str]
            The Name of the Category.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcategories.put(
            id_="id",
        )
        """
        _response = self._raw_client.put(
            id_, description=description, id=id, name=name, request_options=request_options
        )
        return _response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the authorization category.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcategories.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def adduser(self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str


        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcategories.adduser(
            id="id",
            user_id=1,
        )
        """
        _response = self._raw_client.adduser(id, user_id, request_options=request_options)
        return _response.data

    def removeuser(self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str


        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcategories.removeuser(
            id="id",
            user_id=1,
        )
        """
        _response = self._raw_client.removeuser(id, user_id, request_options=request_options)
        return _response.data


class AsyncAuthorizationcategoriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthorizationcategoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthorizationcategoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthorizationcategoriesClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        definition_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseAuthorizationCodesSharedModelsCategory:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        user_id : typing.Optional[int]
            Optional. Filter by categories visible to the provided user with the provided userID.

        definition_id : typing.Optional[str]
            Optional. Filter by categories containing a definition with the provided ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseAuthorizationCodesSharedModelsCategory
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authorizationcategories.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            limit=limit, offset=offset, user_id=user_id, definition_id=definition_id, request_options=request_options
        )
        return _response.data

    async def post(
        self,
        *,
        description: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        description : typing.Optional[str]
            A description of the Category.

        id : typing.Optional[str]
            The ID of the Category.

        name : typing.Optional[str]
            The Name of the Category.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authorizationcategories.post()


        asyncio.run(main())
        """
        _response = await self._raw_client.post(
            description=description, id=id, name=name, request_options=request_options
        )
        return _response.data

    async def getusers(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_i_ds: typing.Optional[str] = None,
        category_i_ds: typing.Optional[str] = None,
        include_categories: typing.Optional[bool] = None,
        include_users: typing.Optional[bool] = None,
        user_search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. Defaults to 10.

        offset : typing.Optional[int]
            Optional. Defaults to 0.

        user_i_ds : typing.Optional[str]
            Optional. Includes only users with IDs on the provided comma-separated list.

        category_i_ds : typing.Optional[str]
            Optional. Includes only users with categories with IDs on the provided comma-separated list.

        include_categories : typing.Optional[bool]
            If true, include full Authorization Category detail. Defaults to false.

        include_users : typing.Optional[bool]
            If true, include full User detail. Defaults to false.

        user_search : typing.Optional[str]
            Optional. Includes only users with a Name, Username, or Email containing the provided value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authorizationcategories.getusers()


        asyncio.run(main())
        """
        _response = await self._raw_client.getusers(
            limit=limit,
            offset=offset,
            user_i_ds=user_i_ds,
            category_i_ds=category_i_ds,
            include_categories=include_categories,
            include_users=include_users,
            user_search=user_search,
            request_options=request_options,
        )
        return _response.data

    async def put(
        self,
        id_: str,
        *,
        description: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : str

        description : typing.Optional[str]
            A description of the Category.

        id : typing.Optional[str]
            The ID of the Category.

        name : typing.Optional[str]
            The Name of the Category.

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
            await client.authorizationcategories.put(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put(
            id_, description=description, id=id, name=name, request_options=request_options
        )
        return _response.data

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the authorization category.

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
            await client.authorizationcategories.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data

    async def adduser(self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str


        user_id : int


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
            await client.authorizationcategories.adduser(
                id="id",
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.adduser(id, user_id, request_options=request_options)
        return _response.data

    async def removeuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str


        user_id : int


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
            await client.authorizationcategories.removeuser(
                id="id",
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.removeuser(id, user_id, request_options=request_options)
        return _response.data
