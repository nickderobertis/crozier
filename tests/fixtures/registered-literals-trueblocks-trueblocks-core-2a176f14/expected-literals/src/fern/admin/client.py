

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAdminClient, RawAdminClient
from .types.admin_chunks_request_mode import AdminChunksRequestMode
from .types.admin_chunks_response import AdminChunksResponse
from .types.admin_config_request_mode import AdminConfigRequestMode
from .types.admin_config_response import AdminConfigResponse
from .types.admin_init_response import AdminInitResponse
from .types.admin_status_request_modes_item import AdminStatusRequestModesItem
from .types.admin_status_response import AdminStatusResponse


class AdminClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdminClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdminClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdminClient
        """
        return self._raw_client

    def config(
        self,
        *,
        mode: typing.Optional[AdminConfigRequestMode] = None,
        paths: typing.Optional[bool] = None,
        dump: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdminConfigResponse:
        """
        Report on and edit the configuration of the TrueBlocks system. Corresponds to the <a href="/chifra/admin/#chifra-config">chifra config</a> command line.

        Parameters
        ----------
        mode : typing.Optional[AdminConfigRequestMode]
            either show or edit the configuration

        paths : typing.Optional[bool]
            show the configuration paths for the system

        dump : typing.Optional[bool]
            dump the configuration to stdout

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminConfigResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.config()
        """
        _response = self._raw_client.config(
            mode=mode,
            paths=paths,
            dump=dump,
            chain=chain,
            no_header=no_header,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    def status(
        self,
        *,
        modes: typing.Optional[
            typing.Union[AdminStatusRequestModesItem, typing.Sequence[AdminStatusRequestModesItem]]
        ] = None,
        diagnose: typing.Optional[bool] = None,
        first_record: typing.Optional[int] = None,
        max_records: typing.Optional[int] = None,
        chains: typing.Optional[bool] = None,
        caches: typing.Optional[bool] = None,
        healthcheck: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdminStatusResponse:
        """
        Report on the state of the internal binary caches. Corresponds to the <a href="/chifra/admin/#chifra-status">chifra status</a> command line.

        Parameters
        ----------
        modes : typing.Optional[typing.Union[AdminStatusRequestModesItem, typing.Sequence[AdminStatusRequestModesItem]]]
            the (optional) name of the binary cache to report on, terse otherwise

        diagnose : typing.Optional[bool]
            same as the default but with additional diagnostics

        first_record : typing.Optional[int]
            the first record to process

        max_records : typing.Optional[int]
            the maximum number of records to process

        chains : typing.Optional[bool]
            include a list of chain configurations in the output

        caches : typing.Optional[bool]
            include a list of cache items in the output

        healthcheck : typing.Optional[bool]
            an alias for the diagnose endpoint

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminStatusResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.status()
        """
        _response = self._raw_client.status(
            modes=modes,
            diagnose=diagnose,
            first_record=first_record,
            max_records=max_records,
            chains=chains,
            caches=caches,
            healthcheck=healthcheck,
            chain=chain,
            no_header=no_header,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    def chunks(
        self,
        *,
        mode: AdminChunksRequestMode,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        check: typing.Optional[bool] = None,
        belongs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        first_block: typing.Optional[float] = None,
        last_block: typing.Optional[float] = None,
        max_addrs: typing.Optional[int] = None,
        deep: typing.Optional[bool] = None,
        rewrite: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        metadata: typing.Optional[bool] = None,
        sleep: typing.Optional[float] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdminChunksResponse:
        """
        Manage, investigate, and display the Unchained Index. Corresponds to the <a href="/chifra/admin/#chifra-chunks">chifra chunks</a> command line.

        Parameters
        ----------
        mode : AdminChunksRequestMode
            the type of data to process

        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            an optional list of blocks to intersect with chunk ranges

        check : typing.Optional[bool]
            check the manifest, index, or blooms for internal consistency

        belongs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            in index mode only, checks the address(es) for inclusion in the given index chunk

        first_block : typing.Optional[float]
            first block to process (inclusive)

        last_block : typing.Optional[float]
            last block to process (inclusive)

        max_addrs : typing.Optional[int]
            the max number of addresses to process in a given chunk

        deep : typing.Optional[bool]
            if true, dig more deeply during checking (manifest only)

        rewrite : typing.Optional[bool]
            for the --pin --deep mode only, writes the manifest back to the index folder (see notes)

        count : typing.Optional[bool]
            for certain modes only, display the count of records

        metadata : typing.Optional[bool]
            for --pin only, pin only metadata files (ts.bin and manifest.json)

        sleep : typing.Optional[float]
            for --remote pinning only, seconds to sleep between API calls

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminChunksResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.chunks(
            mode="manifest",
        )
        """
        _response = self._raw_client.chunks(
            mode=mode,
            blocks=blocks,
            check=check,
            belongs=belongs,
            first_block=first_block,
            last_block=last_block,
            max_addrs=max_addrs,
            deep=deep,
            rewrite=rewrite,
            count=count,
            metadata=metadata,
            sleep=sleep,
            chain=chain,
            no_header=no_header,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    def init(
        self,
        *,
        all_: typing.Optional[bool] = None,
        example: typing.Optional[str] = None,
        dry_run: typing.Optional[bool] = None,
        first_block: typing.Optional[float] = None,
        sleep: typing.Optional[float] = None,
        chain: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdminInitResponse:
        """
        Initialize the TrueBlocks system by downloading the Unchained Index from IPFS. Corresponds to the <a href="/chifra/admin/#chifra-init">chifra init</a> command line.

        Parameters
        ----------
        all_ : typing.Optional[bool]
            in addition to Bloom filters, download full index chunks (recommended)

        example : typing.Optional[str]
            create an example for the SDK with the given name

        dry_run : typing.Optional[bool]
            display the results of the download without actually downloading

        first_block : typing.Optional[float]
            do not download any chunks earlier than this block

        sleep : typing.Optional[float]
            seconds to sleep between downloads

        chain : typing.Optional[str]
            the chain to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminInitResponse
            returns the requested data

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.init()
        """
        _response = self._raw_client.init(
            all_=all_,
            example=example,
            dry_run=dry_run,
            first_block=first_block,
            sleep=sleep,
            chain=chain,
            request_options=request_options,
        )
        return _response.data


class AsyncAdminClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdminClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdminClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdminClient
        """
        return self._raw_client

    async def config(
        self,
        *,
        mode: typing.Optional[AdminConfigRequestMode] = None,
        paths: typing.Optional[bool] = None,
        dump: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdminConfigResponse:
        """
        Report on and edit the configuration of the TrueBlocks system. Corresponds to the <a href="/chifra/admin/#chifra-config">chifra config</a> command line.

        Parameters
        ----------
        mode : typing.Optional[AdminConfigRequestMode]
            either show or edit the configuration

        paths : typing.Optional[bool]
            show the configuration paths for the system

        dump : typing.Optional[bool]
            dump the configuration to stdout

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminConfigResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.config()


        asyncio.run(main())
        """
        _response = await self._raw_client.config(
            mode=mode,
            paths=paths,
            dump=dump,
            chain=chain,
            no_header=no_header,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    async def status(
        self,
        *,
        modes: typing.Optional[
            typing.Union[AdminStatusRequestModesItem, typing.Sequence[AdminStatusRequestModesItem]]
        ] = None,
        diagnose: typing.Optional[bool] = None,
        first_record: typing.Optional[int] = None,
        max_records: typing.Optional[int] = None,
        chains: typing.Optional[bool] = None,
        caches: typing.Optional[bool] = None,
        healthcheck: typing.Optional[bool] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdminStatusResponse:
        """
        Report on the state of the internal binary caches. Corresponds to the <a href="/chifra/admin/#chifra-status">chifra status</a> command line.

        Parameters
        ----------
        modes : typing.Optional[typing.Union[AdminStatusRequestModesItem, typing.Sequence[AdminStatusRequestModesItem]]]
            the (optional) name of the binary cache to report on, terse otherwise

        diagnose : typing.Optional[bool]
            same as the default but with additional diagnostics

        first_record : typing.Optional[int]
            the first record to process

        max_records : typing.Optional[int]
            the maximum number of records to process

        chains : typing.Optional[bool]
            include a list of chain configurations in the output

        caches : typing.Optional[bool]
            include a list of cache items in the output

        healthcheck : typing.Optional[bool]
            an alias for the diagnose endpoint

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminStatusResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.status()


        asyncio.run(main())
        """
        _response = await self._raw_client.status(
            modes=modes,
            diagnose=diagnose,
            first_record=first_record,
            max_records=max_records,
            chains=chains,
            caches=caches,
            healthcheck=healthcheck,
            chain=chain,
            no_header=no_header,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    async def chunks(
        self,
        *,
        mode: AdminChunksRequestMode,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        check: typing.Optional[bool] = None,
        belongs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        first_block: typing.Optional[float] = None,
        last_block: typing.Optional[float] = None,
        max_addrs: typing.Optional[int] = None,
        deep: typing.Optional[bool] = None,
        rewrite: typing.Optional[bool] = None,
        count: typing.Optional[bool] = None,
        metadata: typing.Optional[bool] = None,
        sleep: typing.Optional[float] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdminChunksResponse:
        """
        Manage, investigate, and display the Unchained Index. Corresponds to the <a href="/chifra/admin/#chifra-chunks">chifra chunks</a> command line.

        Parameters
        ----------
        mode : AdminChunksRequestMode
            the type of data to process

        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            an optional list of blocks to intersect with chunk ranges

        check : typing.Optional[bool]
            check the manifest, index, or blooms for internal consistency

        belongs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            in index mode only, checks the address(es) for inclusion in the given index chunk

        first_block : typing.Optional[float]
            first block to process (inclusive)

        last_block : typing.Optional[float]
            last block to process (inclusive)

        max_addrs : typing.Optional[int]
            the max number of addresses to process in a given chunk

        deep : typing.Optional[bool]
            if true, dig more deeply during checking (manifest only)

        rewrite : typing.Optional[bool]
            for the --pin --deep mode only, writes the manifest back to the index folder (see notes)

        count : typing.Optional[bool]
            for certain modes only, display the count of records

        metadata : typing.Optional[bool]
            for --pin only, pin only metadata files (ts.bin and manifest.json)

        sleep : typing.Optional[float]
            for --remote pinning only, seconds to sleep between API calls

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminChunksResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.chunks(
                mode="manifest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.chunks(
            mode=mode,
            blocks=blocks,
            check=check,
            belongs=belongs,
            first_block=first_block,
            last_block=last_block,
            max_addrs=max_addrs,
            deep=deep,
            rewrite=rewrite,
            count=count,
            metadata=metadata,
            sleep=sleep,
            chain=chain,
            no_header=no_header,
            fmt=fmt,
            request_options=request_options,
        )
        return _response.data

    async def init(
        self,
        *,
        all_: typing.Optional[bool] = None,
        example: typing.Optional[str] = None,
        dry_run: typing.Optional[bool] = None,
        first_block: typing.Optional[float] = None,
        sleep: typing.Optional[float] = None,
        chain: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdminInitResponse:
        """
        Initialize the TrueBlocks system by downloading the Unchained Index from IPFS. Corresponds to the <a href="/chifra/admin/#chifra-init">chifra init</a> command line.

        Parameters
        ----------
        all_ : typing.Optional[bool]
            in addition to Bloom filters, download full index chunks (recommended)

        example : typing.Optional[str]
            create an example for the SDK with the given name

        dry_run : typing.Optional[bool]
            display the results of the download without actually downloading

        first_block : typing.Optional[float]
            do not download any chunks earlier than this block

        sleep : typing.Optional[float]
            seconds to sleep between downloads

        chain : typing.Optional[str]
            the chain to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdminInitResponse
            returns the requested data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.init()


        asyncio.run(main())
        """
        _response = await self._raw_client.init(
            all_=all_,
            example=example,
            dry_run=dry_run,
            first_block=first_block,
            sleep=sleep,
            chain=chain,
            request_options=request_options,
        )
        return _response.data
