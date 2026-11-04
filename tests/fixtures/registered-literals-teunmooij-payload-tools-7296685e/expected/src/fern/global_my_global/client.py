

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.my_global import MyGlobal
from ..types.my_global_upsert_confirmation import MyGlobalUpsertConfirmation
from ..types.shared_meta import SharedMeta
from .raw_client import AsyncRawGlobalMyGlobalClient, RawGlobalMyGlobalClient


OMIT = typing.cast(typing.Any, ...)


class GlobalMyGlobalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGlobalMyGlobalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGlobalMyGlobalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGlobalMyGlobalClient
        """
        return self._raw_client

    def get_the_my_global(
        self,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MyGlobal:
        """
        Get the My Global

        Parameters
        ----------
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
        MyGlobal
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.global_my_global.get_the_my_global()
        """
        _response = self._raw_client.get_the_my_global(
            depth=depth, locale=locale, fallback_locale=fallback_locale, request_options=request_options
        )
        return _response.data

    def updates_the_my_global(
        self,
        *,
        id: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        meta: typing.Optional[SharedMeta] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MyGlobalUpsertConfirmation:
        """
        Updates the My Global

        Parameters
        ----------
        id : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        meta : typing.Optional[SharedMeta]

        updated_at : typing.Optional[str]

        created_at : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MyGlobalUpsertConfirmation
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.global_my_global.updates_the_my_global(
            id="id",
        )
        """
        _response = self._raw_client.updates_the_my_global(
            id=id,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            title=title,
            meta=meta,
            updated_at=updated_at,
            created_at=created_at,
            request_options=request_options,
        )
        return _response.data


class AsyncGlobalMyGlobalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGlobalMyGlobalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGlobalMyGlobalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGlobalMyGlobalClient
        """
        return self._raw_client

    async def get_the_my_global(
        self,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MyGlobal:
        """
        Get the My Global

        Parameters
        ----------
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
        MyGlobal
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.global_my_global.get_the_my_global()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_my_global(
            depth=depth, locale=locale, fallback_locale=fallback_locale, request_options=request_options
        )
        return _response.data

    async def updates_the_my_global(
        self,
        *,
        id: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        meta: typing.Optional[SharedMeta] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MyGlobalUpsertConfirmation:
        """
        Updates the My Global

        Parameters
        ----------
        id : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        meta : typing.Optional[SharedMeta]

        updated_at : typing.Optional[str]

        created_at : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MyGlobalUpsertConfirmation
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.global_my_global.updates_the_my_global(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_the_my_global(
            id=id,
            depth=depth,
            locale=locale,
            fallback_locale=fallback_locale,
            title=title,
            meta=meta,
            updated_at=updated_at,
            created_at=created_at,
            request_options=request_options,
        )
        return _response.data
