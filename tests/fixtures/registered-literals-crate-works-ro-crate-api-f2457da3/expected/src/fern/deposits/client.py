

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deposit import Deposit
from ..types.file_upload_target import FileUploadTarget
from ..types.id import Id
from .raw_client import AsyncRawDepositsClient, RawDepositsClient


OMIT = typing.cast(typing.Any, ...)


class DepositsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDepositsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDepositsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDepositsClient
        """
        return self._raw_client

    def create_deposit(
        self, *, ro_crate_id: typing.Optional[Id] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Deposit:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Open a deposit session that will create a new RO-Crate. The RO-Crate comes into existence only at the deposit's first successful finalise — until then nothing is readable and no entities exist.

        The request body MAY propose a `roCrateId` where the implementation's `idMinting` capability is `client` or `both`; when the body or the field is absent the server mints one (`server` or `both`). Proposing an ID that is not supported by the declared `idMinting` mode is rejected with `422`; proposing an ID that already exists is rejected with `409`. The RO-Crate ID is returned immediately so the client can reference it from the deposited metadata document; whether the metadata document MUST reference it is implementation-defined and enforced at finalise.

        A previously deleted RO-Crate ID MAY be reused; implementations MAY refuse with `409`. Recreation is a new RO-Crate, not a continuation — no relationship to the deleted RO-Crate's history or entities is implied.

        To update an existing RO-Crate, use `POST /ro-crate/{id}/deposits` instead.

        Parameters
        ----------
        ro_crate_id : typing.Optional[Id]
            A client-proposed ID for the new RO-Crate. Only valid when the implementation's `idMinting` capability is `client` or `both`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deposit
            Deposit created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deposits.create_deposit()
        """
        _response = self._raw_client.create_deposit(ro_crate_id=ro_crate_id, request_options=request_options)
        return _response.data

    def get_deposit(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Deposit:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve the deposit, including its lifecycle state, the files staged so far with per-file upload status, and the violations recorded by the most recent failed finalise. This is the polling resource for asynchronous finalisation: after a `202` from finalise, poll here until the state leaves `finalising`.

        Parameters
        ----------
        id : str
            The deposit ID, as returned when the deposit was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deposit
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deposits.get_deposit(
            id="dep_8f14e45f",
        )
        """
        _response = self._raw_client.get_deposit(id, request_options=request_options)
        return _response.data

    def abort_deposit(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Abort an `open` deposit, discarding its staged metadata document and files. Aborting is terminal; the RO-Crate is left at its prior version (or never comes into existence for a create deposit).

        Deposits are also subject to implementation-defined expiry — an expired deposit behaves as aborted, and subsequent access MAY return `404`. Where the implementation declares `depositTtlSeconds` in `/capabilities`, that is the expiry horizon.

        Parameters
        ----------
        id : str
            The deposit ID, as returned when the deposit was created.

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
        client.deposits.abort_deposit(
            id="dep_8f14e45f",
        )
        """
        _response = self._raw_client.abort_deposit(id, request_options=request_options)
        return _response.data

    def stage_deposit_metadata(
        self, id: str, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Stage the RO-Crate metadata document for this deposit. This is a full replace — staging a new metadata document discards the previously staged one; there is no metadata PATCH and no metadata DELETE. The metadata document and files may be staged in any order; metadata–file association is checked at finalise.

        At finalise the staged metadata document becomes the RO-Crate's authoritative file manifest: each file entity in the metadata document resolves to bytes staged in this deposit, else (for update deposits) to the file carried forward by `@id` from the baseline version, else remains an unresolved reference. Unresolved references are not protocol errors — they simply `404` when followed — but implementations MAY reject them at finalise via validation. Files present in the baseline but absent from the new metadata document drop out of the new version.

        Parameters
        ----------
        id : str
            The deposit ID, as returned when the deposit was created.

        request : typing.Dict[str, typing.Any]

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
        client.deposits.stage_deposit_metadata(
            id="dep_8f14e45f",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.stage_deposit_metadata(id, request=request, request_options=request_options)
        return _response.data

    def stage_deposit_file(
        self,
        id: str,
        file_id: str,
        *,
        size: int,
        checksum: typing.Optional[str] = OMIT,
        media_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[FileUploadTarget]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Stage a file in this deposit. `{fileId}` is the file entity's `@id` in the deposited metadata document, percent-encoded — for attached files, its crate-relative path. The metadata document and files may be staged in any order.

        Two upload modes share this endpoint, discriminated by the request `Content-Type`; the implementation declares which it supports in the `fileUpload` capability:

        - **Inline** (`fileUpload` contains `inline`): the request body is the file's bytes, sent with the file's own media type. Responds `204`.
        - **Presigned** (`fileUpload` contains `presigned`): the request body is `application/json` transport metadata (size, checksum, media type) and the response is `200` with an upload target the client sends the bytes to directly. There is no per-file completion call — finalise verifies that the bytes landed and match the declared size and checksum.

        Only transport metadata is carried here; descriptive metadata about the file lives in the metadata document. Staging the same `{fileId}` again replaces the earlier staging. Using a mode the implementation does not declare is rejected with `400`.

        Parameters
        ----------
        id : str
            The deposit ID, as returned when the deposit was created.

        file_id : str
            The file entity's `@id` in the deposited metadata document, percent-encoded. For attached files this is the crate-relative path.

        size : int
            The file's size in bytes. Verified at finalise.

        checksum : typing.Optional[str]
            The file's checksum, prefixed with the algorithm (e.g. `sha256:`). Verified at finalise when supplied.

        media_type : typing.Optional[str]
            The MIME type of the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[FileUploadTarget]
            Transport metadata staged (presigned mode) - upload the bytes to the returned target

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deposits.stage_deposit_file(
            id="dep_8f14e45f",
            file_id="NT1-001-001A.mp3",
            size=2048576,
        )
        """
        _response = self._raw_client.stage_deposit_file(
            id, file_id, size=size, checksum=checksum, media_type=media_type, request_options=request_options
        )
        return _response.data

    def unstage_deposit_file(
        self, id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Remove a file staged in this deposit. Valid while the deposit is `open`. This only affects the deposit's staging area — to drop a file from an existing RO-Crate, stage a metadata document that no longer references it.

        Parameters
        ----------
        id : str
            The deposit ID, as returned when the deposit was created.

        file_id : str
            The file entity's `@id` in the deposited metadata document, percent-encoded. For attached files this is the crate-relative path.

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
        client.deposits.unstage_deposit_file(
            id="dep_8f14e45f",
            file_id="NT1-001-001A.mp3",
        )
        """
        _response = self._raw_client.unstage_deposit_file(id, file_id, request_options=request_options)
        return _response.data

    def finalise_deposit(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Deposit:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Finalise the deposit: validate the staged content, publish it as the RO-Crate's new current version (replacing the prior version wholesale), and materialise catalog entities from it. Validation depth and materialisation rules are implementation-defined.

        Finalisation MAY complete synchronously or asynchronously, at the server's discretion per request — there is no capability flag. A `200` returns the deposit in state `complete`; a `202` returns it in state `finalising`, and the client polls `GET /deposit/{id}` until the state leaves `finalising`. One client code path handles both.

        For every file staged in presigned mode, finalise verifies the bytes landed and match the declared size and checksum; missing or mismatched files are validation violations.

        **Failure atomicity is guaranteed**: a finalise that does not reach `complete` leaves no observable change. On validation failure the deposit returns to `open` with the violations recorded — as a `422` on the synchronous path, and in the deposit's `errors` field on the asynchronous path. Non-validation failures (including the target RO-Crate having been deleted mid-deposit) also return the deposit to `open` with the failure recorded; retry is safe, and abort covers walking away. Once `complete`, the new metadata document and all materialised entities are readable; readers are not guaranteed to observe the transition as a single atomic flip.

        For update deposits, carry-forward resolves against the baseline version pinned when the deposit was opened; the last finalise wins as a unit. Implementations MAY reject a finalise whose baseline has been superseded with `409`.

        Parameters
        ----------
        id : str
            The deposit ID, as returned when the deposit was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deposit
            Finalised synchronously - the deposit is `complete` and the RO-Crate's new version is published

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deposits.finalise_deposit(
            id="dep_8f14e45f",
        )
        """
        _response = self._raw_client.finalise_deposit(id, request_options=request_options)
        return _response.data

    def create_update_deposit(self, id: Id, *, request_options: typing.Optional[RequestOptions] = None) -> Deposit:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Open a deposit session against an existing RO-Crate. The deposit starts logically empty; the client stages a new metadata document plus only the files that changed. At finalise the new metadata document is the authoritative file manifest — unchanged files are carried forward from the baseline by `@id`, and files absent from the new metadata document drop out. A metadata-only fix is therefore just `PUT /deposit/{id}/metadata` followed by finalise.

        The baseline for carry-forward is the RO-Crate's current version at the moment this deposit is created. Concurrent open deposits against one RO-Crate are allowed; each finalise replaces the RO-Crate wholesale, so the last finalise wins as a unit.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deposit
            Deposit created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.deposits.create_update_deposit(
            id="https://catalog.paradisec.org.au/repository/NT1/001",
        )
        """
        _response = self._raw_client.create_update_deposit(id, request_options=request_options)
        return _response.data


class AsyncDepositsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDepositsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDepositsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDepositsClient
        """
        return self._raw_client

    async def create_deposit(
        self, *, ro_crate_id: typing.Optional[Id] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Deposit:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Open a deposit session that will create a new RO-Crate. The RO-Crate comes into existence only at the deposit's first successful finalise — until then nothing is readable and no entities exist.

        The request body MAY propose a `roCrateId` where the implementation's `idMinting` capability is `client` or `both`; when the body or the field is absent the server mints one (`server` or `both`). Proposing an ID that is not supported by the declared `idMinting` mode is rejected with `422`; proposing an ID that already exists is rejected with `409`. The RO-Crate ID is returned immediately so the client can reference it from the deposited metadata document; whether the metadata document MUST reference it is implementation-defined and enforced at finalise.

        A previously deleted RO-Crate ID MAY be reused; implementations MAY refuse with `409`. Recreation is a new RO-Crate, not a continuation — no relationship to the deleted RO-Crate's history or entities is implied.

        To update an existing RO-Crate, use `POST /ro-crate/{id}/deposits` instead.

        Parameters
        ----------
        ro_crate_id : typing.Optional[Id]
            A client-proposed ID for the new RO-Crate. Only valid when the implementation's `idMinting` capability is `client` or `both`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deposit
            Deposit created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deposits.create_deposit()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_deposit(ro_crate_id=ro_crate_id, request_options=request_options)
        return _response.data

    async def get_deposit(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Deposit:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Retrieve the deposit, including its lifecycle state, the files staged so far with per-file upload status, and the violations recorded by the most recent failed finalise. This is the polling resource for asynchronous finalisation: after a `202` from finalise, poll here until the state leaves `finalising`.

        Parameters
        ----------
        id : str
            The deposit ID, as returned when the deposit was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deposit
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deposits.get_deposit(
                id="dep_8f14e45f",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_deposit(id, request_options=request_options)
        return _response.data

    async def abort_deposit(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Abort an `open` deposit, discarding its staged metadata document and files. Aborting is terminal; the RO-Crate is left at its prior version (or never comes into existence for a create deposit).

        Deposits are also subject to implementation-defined expiry — an expired deposit behaves as aborted, and subsequent access MAY return `404`. Where the implementation declares `depositTtlSeconds` in `/capabilities`, that is the expiry horizon.

        Parameters
        ----------
        id : str
            The deposit ID, as returned when the deposit was created.

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
            await client.deposits.abort_deposit(
                id="dep_8f14e45f",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.abort_deposit(id, request_options=request_options)
        return _response.data

    async def stage_deposit_metadata(
        self, id: str, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Stage the RO-Crate metadata document for this deposit. This is a full replace — staging a new metadata document discards the previously staged one; there is no metadata PATCH and no metadata DELETE. The metadata document and files may be staged in any order; metadata–file association is checked at finalise.

        At finalise the staged metadata document becomes the RO-Crate's authoritative file manifest: each file entity in the metadata document resolves to bytes staged in this deposit, else (for update deposits) to the file carried forward by `@id` from the baseline version, else remains an unresolved reference. Unresolved references are not protocol errors — they simply `404` when followed — but implementations MAY reject them at finalise via validation. Files present in the baseline but absent from the new metadata document drop out of the new version.

        Parameters
        ----------
        id : str
            The deposit ID, as returned when the deposit was created.

        request : typing.Dict[str, typing.Any]

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
            await client.deposits.stage_deposit_metadata(
                id="dep_8f14e45f",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stage_deposit_metadata(id, request=request, request_options=request_options)
        return _response.data

    async def stage_deposit_file(
        self,
        id: str,
        file_id: str,
        *,
        size: int,
        checksum: typing.Optional[str] = OMIT,
        media_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[FileUploadTarget]:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Stage a file in this deposit. `{fileId}` is the file entity's `@id` in the deposited metadata document, percent-encoded — for attached files, its crate-relative path. The metadata document and files may be staged in any order.

        Two upload modes share this endpoint, discriminated by the request `Content-Type`; the implementation declares which it supports in the `fileUpload` capability:

        - **Inline** (`fileUpload` contains `inline`): the request body is the file's bytes, sent with the file's own media type. Responds `204`.
        - **Presigned** (`fileUpload` contains `presigned`): the request body is `application/json` transport metadata (size, checksum, media type) and the response is `200` with an upload target the client sends the bytes to directly. There is no per-file completion call — finalise verifies that the bytes landed and match the declared size and checksum.

        Only transport metadata is carried here; descriptive metadata about the file lives in the metadata document. Staging the same `{fileId}` again replaces the earlier staging. Using a mode the implementation does not declare is rejected with `400`.

        Parameters
        ----------
        id : str
            The deposit ID, as returned when the deposit was created.

        file_id : str
            The file entity's `@id` in the deposited metadata document, percent-encoded. For attached files this is the crate-relative path.

        size : int
            The file's size in bytes. Verified at finalise.

        checksum : typing.Optional[str]
            The file's checksum, prefixed with the algorithm (e.g. `sha256:`). Verified at finalise when supplied.

        media_type : typing.Optional[str]
            The MIME type of the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[FileUploadTarget]
            Transport metadata staged (presigned mode) - upload the bytes to the returned target

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deposits.stage_deposit_file(
                id="dep_8f14e45f",
                file_id="NT1-001-001A.mp3",
                size=2048576,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stage_deposit_file(
            id, file_id, size=size, checksum=checksum, media_type=media_type, request_options=request_options
        )
        return _response.data

    async def unstage_deposit_file(
        self, id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Remove a file staged in this deposit. Valid while the deposit is `open`. This only affects the deposit's staging area — to drop a file from an existing RO-Crate, stage a metadata document that no longer references it.

        Parameters
        ----------
        id : str
            The deposit ID, as returned when the deposit was created.

        file_id : str
            The file entity's `@id` in the deposited metadata document, percent-encoded. For attached files this is the crate-relative path.

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
            await client.deposits.unstage_deposit_file(
                id="dep_8f14e45f",
                file_id="NT1-001-001A.mp3",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unstage_deposit_file(id, file_id, request_options=request_options)
        return _response.data

    async def finalise_deposit(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Deposit:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Finalise the deposit: validate the staged content, publish it as the RO-Crate's new current version (replacing the prior version wholesale), and materialise catalog entities from it. Validation depth and materialisation rules are implementation-defined.

        Finalisation MAY complete synchronously or asynchronously, at the server's discretion per request — there is no capability flag. A `200` returns the deposit in state `complete`; a `202` returns it in state `finalising`, and the client polls `GET /deposit/{id}` until the state leaves `finalising`. One client code path handles both.

        For every file staged in presigned mode, finalise verifies the bytes landed and match the declared size and checksum; missing or mismatched files are validation violations.

        **Failure atomicity is guaranteed**: a finalise that does not reach `complete` leaves no observable change. On validation failure the deposit returns to `open` with the violations recorded — as a `422` on the synchronous path, and in the deposit's `errors` field on the asynchronous path. Non-validation failures (including the target RO-Crate having been deleted mid-deposit) also return the deposit to `open` with the failure recorded; retry is safe, and abort covers walking away. Once `complete`, the new metadata document and all materialised entities are readable; readers are not guaranteed to observe the transition as a single atomic flip.

        For update deposits, carry-forward resolves against the baseline version pinned when the deposit was opened; the last finalise wins as a unit. Implementations MAY reject a finalise whose baseline has been superseded with `409`.

        Parameters
        ----------
        id : str
            The deposit ID, as returned when the deposit was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deposit
            Finalised synchronously - the deposit is `complete` and the RO-Crate's new version is published

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deposits.finalise_deposit(
                id="dep_8f14e45f",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.finalise_deposit(id, request_options=request_options)
        return _response.data

    async def create_update_deposit(
        self, id: Id, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deposit:
        """
        Optional core — provided when `deposit.supported` is `true`. See the [Deposits guide](https://ro-crate-api.crate-works.org/docs/deposit).

        Open a deposit session against an existing RO-Crate. The deposit starts logically empty; the client stages a new metadata document plus only the files that changed. At finalise the new metadata document is the authoritative file manifest — unchanged files are carried forward from the baseline by `@id`, and files absent from the new metadata document drop out. A metadata-only fix is therefore just `PUT /deposit/{id}/metadata` followed by finalise.

        The baseline for carry-forward is the RO-Crate's current version at the moment this deposit is created. Concurrent open deposits against one RO-Crate are allowed; each finalise replaces the RO-Crate wholesale, so the last finalise wins as a unit.

        Parameters
        ----------
        id : Id
            The RO-Crate ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deposit
            Deposit created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.deposits.create_update_deposit(
                id="https://catalog.paradisec.org.au/repository/NT1/001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_update_deposit(id, request_options=request_options)
        return _response.data
