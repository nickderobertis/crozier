

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.mclass import Mclass
from ..types.performance_counters import PerformanceCounters
from .raw_client import AsyncRawKvdbClient, RawKvdbClient
from .types.kvdb_compact_status_get_response import KvdbCompactStatusGetResponse
from .types.kvdb_csched_get_response_item import KvdbCschedGetResponseItem
from .types.kvdb_media_class_get_response import KvdbMediaClassGetResponse
from .types.kvdb_param_get_response import KvdbParamGetResponse
from .types.kvdb_param_set_request_body import KvdbParamSetRequestBody
from .types.kvdb_params_get_response import KvdbParamsGetResponse


OMIT = typing.cast(typing.Any, ...)


class KvdbClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKvdbClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKvdbClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKvdbClient
        """
        return self._raw_client

    def compact_status_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvdbCompactStatusGetResponse:
        """
        Get the current KVDB compaction status.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvdbCompactStatusGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvdb.compact_status_get(
            alias="0",
        )
        """
        _response = self._raw_client.compact_status_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    def compact_request(self, alias: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Create a KVDB compaction request.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvdb.compact_request(
            alias="0",
        )
        """
        _response = self._raw_client.compact_request(alias, request_options=request_options)
        return _response.data

    def compact_cancel(self, alias: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Cancel a KVDB compaction request.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvdb.compact_cancel(
            alias="0",
        )
        """
        _response = self._raw_client.compact_cancel(alias, request_options=request_options)
        return _response.data

    def csched_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[KvdbCschedGetResponseItem]:
        """
        Get information about all current KVDB compaction jobs.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[KvdbCschedGetResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvdb.csched_get(
            alias="0",
        )
        """
        _response = self._raw_client.csched_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    def home_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Get KVDB home.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

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
        client.kvdb.home_get(
            alias="0",
        )
        """
        _response = self._raw_client.home_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    def params_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvdbParamsGetResponse:
        """
        Get all KVDB parameters.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvdbParamsGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvdb.params_get(
            alias="0",
        )
        """
        _response = self._raw_client.params_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    def param_get(
        self,
        alias: str,
        param: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvdbParamGetResponse:
        """
        Get the value of the KVDB parameter.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        param : str
            Parameter to interact with.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvdbParamGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvdb.param_get(
            alias="0",
            param="logging.enabled",
        )
        """
        _response = self._raw_client.param_get(alias, param, pretty=pretty, request_options=request_options)
        return _response.data

    def param_set(
        self,
        alias: str,
        param: str,
        *,
        request: KvdbParamSetRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Set the value of the KVDB parameter.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        param : str
            Parameter to interact with.

        request : KvdbParamSetRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvdb.param_set(
            alias="0",
            param="logging.enabled",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.param_set(alias, param, request=request, request_options=request_options)
        return _response.data

    def media_classes_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Mclass]:
        """
        Get list of configured media classes and their paths.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Mclass]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvdb.media_classes_get(
            alias="0",
        )
        """
        _response = self._raw_client.media_classes_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    def media_class_get(
        self,
        alias: str,
        mclass: Mclass,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvdbMediaClassGetResponse:
        """
        Get information about a media class.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        mclass : Mclass
            Media class name.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvdbMediaClassGetResponse
            OK

        Examples
        --------
        from fern import FernApi, Mclass

        client = FernApi()
        client.kvdb.media_class_get(
            alias="0",
            mclass=Mclass.CAPACITY,
        )
        """
        _response = self._raw_client.media_class_get(alias, mclass, pretty=pretty, request_options=request_options)
        return _response.data

    def kvs_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Get all KVS names.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvdb.kvs_get(
            alias="0",
        )
        """
        _response = self._raw_client.kvs_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    def perfc_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformanceCounters:
        """
        Get all performance counter information.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PerformanceCounters
            Successfully retrieved performance counter information.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvdb.perfc_get(
            alias="0",
        )
        """
        _response = self._raw_client.perfc_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    def perfc_in_set_get(
        self,
        alias: str,
        set_: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformanceCounters:
        """
        Get all performance counter information.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        set_ : str
            Performance counter set.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PerformanceCounters
            Successfully retrieved performance counter information.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvdb.perfc_in_set_get(
            alias="0",
            set_="CNCOMP",
        )
        """
        _response = self._raw_client.perfc_in_set_get(alias, set_, pretty=pretty, request_options=request_options)
        return _response.data

    def perfc_in_set_with_name_get(
        self,
        alias: str,
        set_: str,
        counter_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformanceCounters:
        """
        Get all performance counter information.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        set_ : str
            Performance counter set.

        counter_name : str
            Performance counter name.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PerformanceCounters
            Successfully retrieved performance counter information.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvdb.perfc_in_set_with_name_get(
            alias="0",
            set_="CNCOMP",
            counter_name="kcompact",
        )
        """
        _response = self._raw_client.perfc_in_set_with_name_get(
            alias, set_, counter_name, pretty=pretty, request_options=request_options
        )
        return _response.data


class AsyncKvdbClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKvdbClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKvdbClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKvdbClient
        """
        return self._raw_client

    async def compact_status_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvdbCompactStatusGetResponse:
        """
        Get the current KVDB compaction status.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvdbCompactStatusGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kvdb.compact_status_get(
                alias="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.compact_status_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    async def compact_request(self, alias: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Create a KVDB compaction request.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

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
            await client.kvdb.compact_request(
                alias="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.compact_request(alias, request_options=request_options)
        return _response.data

    async def compact_cancel(self, alias: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Cancel a KVDB compaction request.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

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
            await client.kvdb.compact_cancel(
                alias="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.compact_cancel(alias, request_options=request_options)
        return _response.data

    async def csched_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[KvdbCschedGetResponseItem]:
        """
        Get information about all current KVDB compaction jobs.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[KvdbCschedGetResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kvdb.csched_get(
                alias="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.csched_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    async def home_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Get KVDB home.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

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
            await client.kvdb.home_get(
                alias="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.home_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    async def params_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvdbParamsGetResponse:
        """
        Get all KVDB parameters.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvdbParamsGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kvdb.params_get(
                alias="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.params_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    async def param_get(
        self,
        alias: str,
        param: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvdbParamGetResponse:
        """
        Get the value of the KVDB parameter.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        param : str
            Parameter to interact with.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvdbParamGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kvdb.param_get(
                alias="0",
                param="logging.enabled",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.param_get(alias, param, pretty=pretty, request_options=request_options)
        return _response.data

    async def param_set(
        self,
        alias: str,
        param: str,
        *,
        request: KvdbParamSetRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Set the value of the KVDB parameter.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        param : str
            Parameter to interact with.

        request : KvdbParamSetRequestBody

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
            await client.kvdb.param_set(
                alias="0",
                param="logging.enabled",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.param_set(alias, param, request=request, request_options=request_options)
        return _response.data

    async def media_classes_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Mclass]:
        """
        Get list of configured media classes and their paths.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Mclass]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kvdb.media_classes_get(
                alias="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.media_classes_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    async def media_class_get(
        self,
        alias: str,
        mclass: Mclass,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvdbMediaClassGetResponse:
        """
        Get information about a media class.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        mclass : Mclass
            Media class name.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvdbMediaClassGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Mclass

        client = AsyncFernApi()


        async def main() -> None:
            await client.kvdb.media_class_get(
                alias="0",
                mclass=Mclass.CAPACITY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.media_class_get(
            alias, mclass, pretty=pretty, request_options=request_options
        )
        return _response.data

    async def kvs_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Get all KVS names.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kvdb.kvs_get(
                alias="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.kvs_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    async def perfc_get(
        self,
        alias: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformanceCounters:
        """
        Get all performance counter information.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PerformanceCounters
            Successfully retrieved performance counter information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kvdb.perfc_get(
                alias="0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perfc_get(alias, pretty=pretty, request_options=request_options)
        return _response.data

    async def perfc_in_set_get(
        self,
        alias: str,
        set_: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformanceCounters:
        """
        Get all performance counter information.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        set_ : str
            Performance counter set.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PerformanceCounters
            Successfully retrieved performance counter information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kvdb.perfc_in_set_get(
                alias="0",
                set_="CNCOMP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perfc_in_set_get(alias, set_, pretty=pretty, request_options=request_options)
        return _response.data

    async def perfc_in_set_with_name_get(
        self,
        alias: str,
        set_: str,
        counter_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformanceCounters:
        """
        Get all performance counter information.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        set_ : str
            Performance counter set.

        counter_name : str
            Performance counter name.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PerformanceCounters
            Successfully retrieved performance counter information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kvdb.perfc_in_set_with_name_get(
                alias="0",
                set_="CNCOMP",
                counter_name="kcompact",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perfc_in_set_with_name_get(
            alias, set_, counter_name, pretty=pretty, request_options=request_options
        )
        return _response.data
