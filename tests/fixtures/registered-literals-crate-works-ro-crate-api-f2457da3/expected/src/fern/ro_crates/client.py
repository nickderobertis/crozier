

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.id import Id
from ..types.order import Order
from ..types.ro_crate import RoCrate
from .raw_client import AsyncRawRoCratesClient, RawRoCratesClient
from .types.list_ro_crates_request_sort import ListRoCratesRequestSort
from .types.list_ro_crates_response import ListRoCratesResponse


class RoCratesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoCratesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoCratesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoCratesClient
        """
        return self._raw_client

    def list_ro_crates(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[ListRoCratesRequestSort] = None,
        order: typing.Optional[Order] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListRoCratesResponse:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        List RO-Crates, paginated and sorted. The response contains whatever the caller is allowed to see under the implementation's visibility model: implementations choose whether RO-Crates are a public surface (listable by anyone, with per-object `access` governing metadata-document retrieval) or a depositor-only management surface (requiring the `write` scope).

        There are no content filters — catalog-side questions belong to `/entities` and `/search`.

        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of entities to return.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, useful for pagination.

        sort : typing.Optional[ListRoCratesRequestSort]
            Field to sort by.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRoCratesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ro_crates.list_ro_crates()
        """
        _response = self._raw_client.list_ro_crates(
            limit=limit, offset=offset, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_ro_crate(self, id: Id, *, request_options: typing.Optional[RequestOptions] = None) -> RoCrate:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve an RO-Crate. The body is deliberately lean: identity, the entities materialised from the current version, timestamps, and access. The deposited metadata document — `GET /ro-crate/{id}/metadata` — is the single source of truth for the RO-Crate's content inventory; the RO-Crate carries no file list of its own.

        `entityIds` is the authoritative answer to "what did my deposit create". It is the inverse of the entity's `roCrateIds` and can change when later deposits (of this or other RO-Crates) alter the materialisation.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoCrate
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ro_crates.get_ro_crate(
            id="https://catalog.paradisec.org.au/repository/NT1/001",
        )
        """
        _response = self._raw_client.get_ro_crate(id, request_options=request_options)
        return _response.data

    def delete_ro_crate(self, id: Id, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Delete an RO-Crate — its metadata document and files. Deletion is not a deposit session; it is already atomic. Implementations needing slow teardown MAY return `202 Accepted`.

        The spec mandates no preconditions; implementations MAY refuse per their own policy (curatorial holds, cross-references) with `409` and a reason. The effect on materialised entities is implementation-defined, mirroring re-deposit pruning: an entity no other RO-Crate contributes to MAY be removed, and deliberate retention is legitimate. An entity with other contributors survives — the deleted RO-Crate simply drops out of its `roCrateIds`.

        Open deposits do not block deletion: delete wins, and a subsequent finalise of such a deposit fails back to `open` with the failure recorded. Implementations MAY auto-abort open deposits against the deleted RO-Crate.

        After deletion, the RO-Crate's URIs (including `/ro-crate/{id}/metadata`) follow the implementation's declared `tombstonePolicy`.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ro_crates.delete_ro_crate(
            id="https://catalog.paradisec.org.au/repository/NT1/001",
        )
        """
        _response = self._raw_client.delete_ro_crate(id, request_options=request_options)
        return _response.data

    def get_ro_crate_metadata(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve the RO-Crate's current RO-Crate metadata document, verbatim as deposited. Unlike `GET /entity/{id}/metadata`, which may return a derived view, this endpoint always returns the original deposited metadata document.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Returns the deposited RO-Crate JSON-LD metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ro_crates.get_ro_crate_metadata(
            id="https://catalog.paradisec.org.au/repository/NT1/001",
        )
        """
        _response = self._raw_client.get_ro_crate_metadata(id, request_options=request_options)
        return _response.data

    def head_ro_crate_metadata(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve the deposited metadata document's headers without downloading the content. Returns the same headers as GET but with no response body, useful for checking availability and caching information.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ro_crates.head_ro_crate_metadata(
            id="https://catalog.paradisec.org.au/repository/NT1/001",
        )
        """
        _response = self._raw_client.head_ro_crate_metadata(id, request_options=request_options)
        return _response.headers


class AsyncRoCratesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoCratesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoCratesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoCratesClient
        """
        return self._raw_client

    async def list_ro_crates(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[ListRoCratesRequestSort] = None,
        order: typing.Optional[Order] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListRoCratesResponse:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        List RO-Crates, paginated and sorted. The response contains whatever the caller is allowed to see under the implementation's visibility model: implementations choose whether RO-Crates are a public surface (listable by anyone, with per-object `access` governing metadata-document retrieval) or a depositor-only management surface (requiring the `write` scope).

        There are no content filters — catalog-side questions belong to `/entities` and `/search`.

        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of entities to return.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, useful for pagination.

        sort : typing.Optional[ListRoCratesRequestSort]
            Field to sort by.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRoCratesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ro_crates.list_ro_crates()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_ro_crates(
            limit=limit, offset=offset, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_ro_crate(self, id: Id, *, request_options: typing.Optional[RequestOptions] = None) -> RoCrate:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve an RO-Crate. The body is deliberately lean: identity, the entities materialised from the current version, timestamps, and access. The deposited metadata document — `GET /ro-crate/{id}/metadata` — is the single source of truth for the RO-Crate's content inventory; the RO-Crate carries no file list of its own.

        `entityIds` is the authoritative answer to "what did my deposit create". It is the inverse of the entity's `roCrateIds` and can change when later deposits (of this or other RO-Crates) alter the materialisation.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoCrate
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ro_crates.get_ro_crate(
                id="https://catalog.paradisec.org.au/repository/NT1/001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ro_crate(id, request_options=request_options)
        return _response.data

    async def delete_ro_crate(self, id: Id, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Delete an RO-Crate — its metadata document and files. Deletion is not a deposit session; it is already atomic. Implementations needing slow teardown MAY return `202 Accepted`.

        The spec mandates no preconditions; implementations MAY refuse per their own policy (curatorial holds, cross-references) with `409` and a reason. The effect on materialised entities is implementation-defined, mirroring re-deposit pruning: an entity no other RO-Crate contributes to MAY be removed, and deliberate retention is legitimate. An entity with other contributors survives — the deleted RO-Crate simply drops out of its `roCrateIds`.

        Open deposits do not block deletion: delete wins, and a subsequent finalise of such a deposit fails back to `open` with the failure recorded. Implementations MAY auto-abort open deposits against the deleted RO-Crate.

        After deletion, the RO-Crate's URIs (including `/ro-crate/{id}/metadata`) follow the implementation's declared `tombstonePolicy`.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ro_crates.delete_ro_crate(
                id="https://catalog.paradisec.org.au/repository/NT1/001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_ro_crate(id, request_options=request_options)
        return _response.data

    async def get_ro_crate_metadata(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve the RO-Crate's current RO-Crate metadata document, verbatim as deposited. Unlike `GET /entity/{id}/metadata`, which may return a derived view, this endpoint always returns the original deposited metadata document.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Returns the deposited RO-Crate JSON-LD metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ro_crates.get_ro_crate_metadata(
                id="https://catalog.paradisec.org.au/repository/NT1/001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ro_crate_metadata(id, request_options=request_options)
        return _response.data

    async def head_ro_crate_metadata(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve the deposited metadata document's headers without downloading the content. Returns the same headers as GET but with no response body, useful for checking availability and caching information.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ro_crates.head_ro_crate_metadata(
                id="https://catalog.paradisec.org.au/repository/NT1/001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_ro_crate_metadata(id, request_options=request_options)
        return _response.headers
