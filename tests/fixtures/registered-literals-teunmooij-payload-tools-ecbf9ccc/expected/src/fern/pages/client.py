

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.pages import Pages
from ..types.pages_upsert_confirmation import PagesUpsertConfirmation
from ..types.pagess import Pagess
from ..types.where import Where
from .raw_client import AsyncRawPagesClient, RawPagesClient
from .types.delete_pages_response import DeletePagesResponse
from .types.patch_pages_response import PatchPagesResponse


OMIT = typing.cast(typing.Any, ...)


class PagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPagesClient
        """
        return self._raw_client

    def find_paginated_pages(
        self,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pagess:
        """
        Find paginated Pages

        Parameters
        ----------
        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pagess
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.find_paginated_pages()
        """
        _response = self._raw_client.find_paginated_pages(
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            sort=sort,
            where=where,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    def create_a_new_page(
        self,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagesUpsertConfirmation:
        """
        Create a new Page

        Parameters
        ----------
        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagesUpsertConfirmation
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.create_a_new_page(
            id="id",
            updated_at="updatedAt",
            created_at="createdAt",
        )
        """
        _response = self._raw_client.create_a_new_page(
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            title=title,
            request_options=request_options,
        )
        return _response.data

    def delete_multiple_pages(
        self,
        *,
        where: Where,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeletePagesResponse:
        """
        Delete all Pages matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePagesResponse
            ok

        Examples
        --------
        from fern import FernApi, Where

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.delete_multiple_pages(
            where=Where(),
        )
        """
        _response = self._raw_client.delete_multiple_pages(
            where=where,
            sort=sort,
            limit=limit,
            page=page,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            request_options=request_options,
        )
        return _response.data

    def update_multiple_pages(
        self,
        *,
        where: Where,
        id: str,
        updated_at: str,
        created_at: str,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchPagesResponse:
        """
        Update all Pages matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        id : str

        updated_at : str

        created_at : str

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchPagesResponse
            ok

        Examples
        --------
        from fern import FernApi, Where

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.update_multiple_pages(
            where=Where(),
            id="id",
            updated_at="updatedAt",
            created_at="createdAt",
        )
        """
        _response = self._raw_client.update_multiple_pages(
            where=where,
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            sort=sort,
            limit=limit,
            page=page,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            title=title,
            request_options=request_options,
        )
        return _response.data

    def get_a_single_page_by_its_id(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pages:
        """
        Get a single Page by its id

        Parameters
        ----------
        id : str
            id of the Page

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pages
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.get_a_single_page_by_its_id(
            id="id",
        )
        """
        _response = self._raw_client.get_a_single_page_by_its_id(
            id,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            sort=sort,
            where=where,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    def deletes_an_existing_page(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagesUpsertConfirmation:
        """
        Deletes an existing Page

        Parameters
        ----------
        id : str
            id of the Page

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagesUpsertConfirmation
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.deletes_an_existing_page(
            id="id",
        )
        """
        _response = self._raw_client.deletes_an_existing_page(
            id, depth=depth, locale=locale, fallback_locale=fallback_locale, request_options=request_options
        )
        return _response.data

    def updates_a_page(
        self,
        id_: str,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagesUpsertConfirmation:
        """
        Updates a Page

        Parameters
        ----------
        id_ : str
            id of the Page

        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagesUpsertConfirmation
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.updates_a_page(
            id_="id",
            id="id",
            updated_at="updatedAt",
            created_at="createdAt",
        )
        """
        _response = self._raw_client.updates_a_page(
            id_,
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            title=title,
            request_options=request_options,
        )
        return _response.data

    def custom_operation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        custom operation

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            succesful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.custom_operation()
        """
        _response = self._raw_client.custom_operation(request_options=request_options)
        return _response.data


class AsyncPagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPagesClient
        """
        return self._raw_client

    async def find_paginated_pages(
        self,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pagess:
        """
        Find paginated Pages

        Parameters
        ----------
        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pagess
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.find_paginated_pages()


        asyncio.run(main())
        """
        _response = await self._raw_client.find_paginated_pages(
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            sort=sort,
            where=where,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    async def create_a_new_page(
        self,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagesUpsertConfirmation:
        """
        Create a new Page

        Parameters
        ----------
        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagesUpsertConfirmation
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.create_a_new_page(
                id="id",
                updated_at="updatedAt",
                created_at="createdAt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_page(
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            title=title,
            request_options=request_options,
        )
        return _response.data

    async def delete_multiple_pages(
        self,
        *,
        where: Where,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeletePagesResponse:
        """
        Delete all Pages matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePagesResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Where

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.delete_multiple_pages(
                where=Where(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_multiple_pages(
            where=where,
            sort=sort,
            limit=limit,
            page=page,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            request_options=request_options,
        )
        return _response.data

    async def update_multiple_pages(
        self,
        *,
        where: Where,
        id: str,
        updated_at: str,
        created_at: str,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchPagesResponse:
        """
        Update all Pages matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        id : str

        updated_at : str

        created_at : str

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchPagesResponse
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Where

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.update_multiple_pages(
                where=Where(),
                id="id",
                updated_at="updatedAt",
                created_at="createdAt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_multiple_pages(
            where=where,
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            sort=sort,
            limit=limit,
            page=page,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            title=title,
            request_options=request_options,
        )
        return _response.data

    async def get_a_single_page_by_its_id(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pages:
        """
        Get a single Page by its id

        Parameters
        ----------
        id : str
            id of the Page

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pages
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.get_a_single_page_by_its_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_single_page_by_its_id(
            id,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            sort=sort,
            where=where,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    async def deletes_an_existing_page(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagesUpsertConfirmation:
        """
        Deletes an existing Page

        Parameters
        ----------
        id : str
            id of the Page

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagesUpsertConfirmation
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.deletes_an_existing_page(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_an_existing_page(
            id, depth=depth, locale=locale, fallback_locale=fallback_locale, request_options=request_options
        )
        return _response.data

    async def updates_a_page(
        self,
        id_: str,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagesUpsertConfirmation:
        """
        Updates a Page

        Parameters
        ----------
        id_ : str
            id of the Page

        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagesUpsertConfirmation
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.updates_a_page(
                id_="id",
                id="id",
                updated_at="updatedAt",
                created_at="createdAt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_a_page(
            id_,
            id=id,
            updated_at=updated_at,
            created_at=created_at,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            title=title,
            request_options=request_options,
        )
        return _response.data

    async def custom_operation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        custom operation

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            succesful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.custom_operation()


        asyncio.run(main())
        """
        _response = await self._raw_client.custom_operation(request_options=request_options)
        return _response.data
