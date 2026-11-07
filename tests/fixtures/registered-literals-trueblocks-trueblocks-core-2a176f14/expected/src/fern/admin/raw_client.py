

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from .types.admin_chunks_request_mode import AdminChunksRequestMode
from .types.admin_chunks_response import AdminChunksResponse
from .types.admin_config_request_mode import AdminConfigRequestMode
from .types.admin_config_response import AdminConfigResponse
from .types.admin_init_response import AdminInitResponse
from .types.admin_status_request_modes_item import AdminStatusRequestModesItem
from .types.admin_status_response import AdminStatusResponse
from pydantic import ValidationError


class RawAdminClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[AdminConfigResponse]:
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
        HttpResponse[AdminConfigResponse]
            returns the requested data
        """
        _response = self._client_wrapper.httpx_client.request(
            "config",
            method="GET",
            params={
                "mode": mode,
                "paths": paths,
                "dump": dump,
                "chain": chain,
                "noHeader": no_header,
                "fmt": fmt,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdminConfigResponse,
                    parse_obj_as(
                        type_=AdminConfigResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[AdminStatusResponse]:
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
        HttpResponse[AdminStatusResponse]
            returns the requested data
        """
        _response = self._client_wrapper.httpx_client.request(
            "status",
            method="GET",
            params={
                "modes": modes,
                "diagnose": diagnose,
                "firstRecord": first_record,
                "maxRecords": max_records,
                "chains": chains,
                "caches": caches,
                "healthcheck": healthcheck,
                "chain": chain,
                "noHeader": no_header,
                "fmt": fmt,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdminStatusResponse,
                    parse_obj_as(
                        type_=AdminStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[AdminChunksResponse]:
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
        HttpResponse[AdminChunksResponse]
            returns the requested data
        """
        _response = self._client_wrapper.httpx_client.request(
            "chunks",
            method="GET",
            params={
                "mode": mode,
                "blocks": blocks,
                "check": check,
                "belongs": belongs,
                "firstBlock": first_block,
                "lastBlock": last_block,
                "maxAddrs": max_addrs,
                "deep": deep,
                "rewrite": rewrite,
                "count": count,
                "metadata": metadata,
                "sleep": sleep,
                "chain": chain,
                "noHeader": no_header,
                "fmt": fmt,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdminChunksResponse,
                    parse_obj_as(
                        type_=AdminChunksResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[AdminInitResponse]:
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
        HttpResponse[AdminInitResponse]
            returns the requested data
        """
        _response = self._client_wrapper.httpx_client.request(
            "init",
            method="GET",
            params={
                "all": all_,
                "example": example,
                "dryRun": dry_run,
                "firstBlock": first_block,
                "sleep": sleep,
                "chain": chain,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdminInitResponse,
                    parse_obj_as(
                        type_=AdminInitResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAdminClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[AdminConfigResponse]:
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
        AsyncHttpResponse[AdminConfigResponse]
            returns the requested data
        """
        _response = await self._client_wrapper.httpx_client.request(
            "config",
            method="GET",
            params={
                "mode": mode,
                "paths": paths,
                "dump": dump,
                "chain": chain,
                "noHeader": no_header,
                "fmt": fmt,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdminConfigResponse,
                    parse_obj_as(
                        type_=AdminConfigResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[AdminStatusResponse]:
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
        AsyncHttpResponse[AdminStatusResponse]
            returns the requested data
        """
        _response = await self._client_wrapper.httpx_client.request(
            "status",
            method="GET",
            params={
                "modes": modes,
                "diagnose": diagnose,
                "firstRecord": first_record,
                "maxRecords": max_records,
                "chains": chains,
                "caches": caches,
                "healthcheck": healthcheck,
                "chain": chain,
                "noHeader": no_header,
                "fmt": fmt,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdminStatusResponse,
                    parse_obj_as(
                        type_=AdminStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[AdminChunksResponse]:
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
        AsyncHttpResponse[AdminChunksResponse]
            returns the requested data
        """
        _response = await self._client_wrapper.httpx_client.request(
            "chunks",
            method="GET",
            params={
                "mode": mode,
                "blocks": blocks,
                "check": check,
                "belongs": belongs,
                "firstBlock": first_block,
                "lastBlock": last_block,
                "maxAddrs": max_addrs,
                "deep": deep,
                "rewrite": rewrite,
                "count": count,
                "metadata": metadata,
                "sleep": sleep,
                "chain": chain,
                "noHeader": no_header,
                "fmt": fmt,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdminChunksResponse,
                    parse_obj_as(
                        type_=AdminChunksResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[AdminInitResponse]:
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
        AsyncHttpResponse[AdminInitResponse]
            returns the requested data
        """
        _response = await self._client_wrapper.httpx_client.request(
            "init",
            method="GET",
            params={
                "all": all_,
                "example": example,
                "dryRun": dry_run,
                "firstBlock": first_block,
                "sleep": sleep,
                "chain": chain,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdminInitResponse,
                    parse_obj_as(
                        type_=AdminInitResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
