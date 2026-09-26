

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.apis_v1components_observation_scope import ApisV1ComponentsObservationScope
from ..types.profiling_capabilities_response import ProfilingCapabilitiesResponse
from ..types.profiling_job_list_response import ProfilingJobListResponse
from ..types.profiling_job_response import ProfilingJobResponse
from ..types.profiling_language import ProfilingLanguage
from ..types.profiling_mode import ProfilingMode
from ..types.profiling_type import ProfilingType
from ..types.raw_profile_page_response import RawProfilePageResponse
from .raw_client import AsyncRawProfilingClient, RawProfilingClient


OMIT = typing.cast(typing.Any, ...)


class ProfilingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProfilingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProfilingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProfilingClient
        """
        return self._raw_client

    def list_profiling_jobs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProfilingJobListResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfilingJobListResponse
            Profiling Jobs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.profiling.list_profiling_jobs()
        """
        _response = self._raw_client.list_profiling_jobs(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def create_profiling_job(
        self,
        *,
        duration_seconds: int,
        hostname: str,
        language: ProfilingLanguage,
        mode: ProfilingMode,
        scope: ApisV1ComponentsObservationScope,
        type: ProfilingType,
        binary_match_path: typing.Optional[str] = OMIT,
        container_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProfilingJobResponse:
        """
        Parameters
        ----------
        duration_seconds : int

        hostname : str

        language : ProfilingLanguage

        mode : ProfilingMode

        scope : ApisV1ComponentsObservationScope

        type : ProfilingType

        binary_match_path : typing.Optional[str]

        container_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfilingJobResponse
            Profiling Job created.

        Examples
        --------
        from fern import (
            ApisV1ComponentsObservationScope,
            FernApi,
            ProfilingLanguage,
            ProfilingMode,
            ProfilingType,
        )

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.profiling.create_profiling_job(
            duration_seconds=1000000,
            hostname="hostname",
            language=ProfilingLanguage.C,
            mode=ProfilingMode.ON_CPU,
            scope=ApisV1ComponentsObservationScope.HOST,
            type=ProfilingType.CPU,
        )
        """
        _response = self._raw_client.create_profiling_job(
            duration_seconds=duration_seconds,
            hostname=hostname,
            language=language,
            mode=mode,
            scope=scope,
            type=type,
            binary_match_path=binary_match_path,
            container_id=container_id,
            request_options=request_options,
        )
        return _response.data

    def get_profiling_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProfilingCapabilitiesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfilingCapabilitiesResponse
            Static profiling capabilities.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.profiling.get_profiling_capabilities()
        """
        _response = self._raw_client.get_profiling_capabilities(request_options=request_options)
        return _response.data

    def get_profile_label_names(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Pyroscope-compatible protobuf response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.profiling.get_profile_label_names()
        """
        with self._raw_client.get_profile_label_names(request_options=request_options) as r:
            yield from r.data

    def get_profile_label_values(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Pyroscope-compatible protobuf response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.profiling.get_profile_label_values()
        """
        with self._raw_client.get_profile_label_values(request_options=request_options) as r:
            yield from r.data

    def get_profile_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Pyroscope-compatible protobuf response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.profiling.get_profile_types()
        """
        with self._raw_client.get_profile_types(request_options=request_options) as r:
            yield from r.data

    def select_merge_stacktraces(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Pyroscope-compatible protobuf response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.profiling.select_merge_stacktraces()
        """
        with self._raw_client.select_merge_stacktraces(request_options=request_options) as r:
            yield from r.data

    def get_profiling_job(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProfilingJobResponse:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfilingJobResponse
            Profiling Job.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.profiling.get_profiling_job(
            request_id="request_id",
        )
        """
        _response = self._raw_client.get_profiling_job(request_id, request_options=request_options)
        return _response.data

    def get_raw_profiles(
        self,
        request_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RawProfilePageResponse:
        """
        Parameters
        ----------
        request_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RawProfilePageResponse
            Raw profile page.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.profiling.get_raw_profiles(
            request_id="request_id",
        )
        """
        _response = self._raw_client.get_raw_profiles(
            request_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def stop_profiling_job(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProfilingJobResponse:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfilingJobResponse
            Current Profiling Job after applying the stop intent.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.profiling.stop_profiling_job(
            request_id="request_id",
        )
        """
        _response = self._raw_client.stop_profiling_job(request_id, request_options=request_options)
        return _response.data


class AsyncProfilingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProfilingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProfilingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProfilingClient
        """
        return self._raw_client

    async def list_profiling_jobs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProfilingJobListResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfilingJobListResponse
            Profiling Jobs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.profiling.list_profiling_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_profiling_jobs(
            limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def create_profiling_job(
        self,
        *,
        duration_seconds: int,
        hostname: str,
        language: ProfilingLanguage,
        mode: ProfilingMode,
        scope: ApisV1ComponentsObservationScope,
        type: ProfilingType,
        binary_match_path: typing.Optional[str] = OMIT,
        container_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProfilingJobResponse:
        """
        Parameters
        ----------
        duration_seconds : int

        hostname : str

        language : ProfilingLanguage

        mode : ProfilingMode

        scope : ApisV1ComponentsObservationScope

        type : ProfilingType

        binary_match_path : typing.Optional[str]

        container_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfilingJobResponse
            Profiling Job created.

        Examples
        --------
        import asyncio

        from fern import (
            ApisV1ComponentsObservationScope,
            AsyncFernApi,
            ProfilingLanguage,
            ProfilingMode,
            ProfilingType,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.profiling.create_profiling_job(
                duration_seconds=1000000,
                hostname="hostname",
                language=ProfilingLanguage.C,
                mode=ProfilingMode.ON_CPU,
                scope=ApisV1ComponentsObservationScope.HOST,
                type=ProfilingType.CPU,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_profiling_job(
            duration_seconds=duration_seconds,
            hostname=hostname,
            language=language,
            mode=mode,
            scope=scope,
            type=type,
            binary_match_path=binary_match_path,
            container_id=container_id,
            request_options=request_options,
        )
        return _response.data

    async def get_profiling_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProfilingCapabilitiesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfilingCapabilitiesResponse
            Static profiling capabilities.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.profiling.get_profiling_capabilities()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_profiling_capabilities(request_options=request_options)
        return _response.data

    async def get_profile_label_names(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Pyroscope-compatible protobuf response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.profiling.get_profile_label_names()


        asyncio.run(main())
        """
        async with self._raw_client.get_profile_label_names(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_profile_label_values(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Pyroscope-compatible protobuf response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.profiling.get_profile_label_values()


        asyncio.run(main())
        """
        async with self._raw_client.get_profile_label_values(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_profile_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Pyroscope-compatible protobuf response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.profiling.get_profile_types()


        asyncio.run(main())
        """
        async with self._raw_client.get_profile_types(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def select_merge_stacktraces(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Pyroscope-compatible protobuf response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.profiling.select_merge_stacktraces()


        asyncio.run(main())
        """
        async with self._raw_client.select_merge_stacktraces(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_profiling_job(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProfilingJobResponse:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfilingJobResponse
            Profiling Job.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.profiling.get_profiling_job(
                request_id="request_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_profiling_job(request_id, request_options=request_options)
        return _response.data

    async def get_raw_profiles(
        self,
        request_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RawProfilePageResponse:
        """
        Parameters
        ----------
        request_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RawProfilePageResponse
            Raw profile page.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.profiling.get_raw_profiles(
                request_id="request_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_raw_profiles(
            request_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def stop_profiling_job(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProfilingJobResponse:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfilingJobResponse
            Current Profiling Job after applying the stop intent.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.profiling.stop_profiling_job(
                request_id="request_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_profiling_job(request_id, request_options=request_options)
        return _response.data
