

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.performance_counters import PerformanceCounters
from .raw_client import AsyncRawKvsClient, RawKvsClient
from .types.kvs_cn_tree_get_response import KvsCnTreeGetResponse
from .types.kvs_param_get_response import KvsParamGetResponse
from .types.kvs_param_set_request_body import KvsParamSetRequestBody
from .types.kvs_params_get_response import KvsParamsGetResponse


OMIT = typing.cast(typing.Any, ...)


class KvsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKvsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKvsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKvsClient
        """
        return self._raw_client

    def cn_tree_get(
        self,
        alias: str,
        kvs_name: str,
        *,
        human: typing.Optional[bool] = None,
        kvsets: typing.Optional[bool] = None,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvsCnTreeGetResponse:
        """
        Get information about the KVS's cN tree.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        human : typing.Optional[bool]
            Humanize certain values.

        kvsets : typing.Optional[bool]
            Include kvset details in output.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvsCnTreeGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvs.cn_tree_get(
            alias="0",
            kvs_name="kvs1",
        )
        """
        _response = self._raw_client.cn_tree_get(
            alias, kvs_name, human=human, kvsets=kvsets, pretty=pretty, request_options=request_options
        )
        return _response.data

    def params_get(
        self,
        alias: str,
        kvs_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvsParamsGetResponse:
        """
        Get all KVS parameters.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvsParamsGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvs.params_get(
            alias="0",
            kvs_name="kvs1",
        )
        """
        _response = self._raw_client.params_get(alias, kvs_name, pretty=pretty, request_options=request_options)
        return _response.data

    def param_get(
        self,
        alias: str,
        kvs_name: str,
        param: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvsParamGetResponse:
        """
        Get the value of the KVS parameter.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        param : str
            Parameter to interact with.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvsParamGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvs.param_get(
            alias="0",
            kvs_name="kvs1",
            param="logging.enabled",
        )
        """
        _response = self._raw_client.param_get(alias, kvs_name, param, pretty=pretty, request_options=request_options)
        return _response.data

    def param_set(
        self,
        alias: str,
        kvs_name: str,
        param: str,
        *,
        request: KvsParamSetRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Set the value of the KVS parameter.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        param : str
            Parameter to interact with.

        request : KvsParamSetRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.kvs.param_set(
            alias="0",
            kvs_name="kvs1",
            param="logging.enabled",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.param_set(alias, kvs_name, param, request=request, request_options=request_options)
        return _response.data

    def perfc_get(
        self,
        alias: str,
        kvs_name: str,
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

        kvs_name : str
            Name of the KVS.

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
        client.kvs.perfc_get(
            alias="0",
            kvs_name="kvs1",
        )
        """
        _response = self._raw_client.perfc_get(alias, kvs_name, pretty=pretty, request_options=request_options)
        return _response.data

    def perfc_in_set_get(
        self,
        alias: str,
        kvs_name: str,
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

        kvs_name : str
            Name of the KVS.

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
        client.kvs.perfc_in_set_get(
            alias="0",
            kvs_name="kvs1",
            set_="CNCOMP",
        )
        """
        _response = self._raw_client.perfc_in_set_get(
            alias, kvs_name, set_, pretty=pretty, request_options=request_options
        )
        return _response.data

    def perfc_in_set_with_name_get(
        self,
        alias: str,
        kvs_name: str,
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

        kvs_name : str
            Name of the KVS.

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
        client.kvs.perfc_in_set_with_name_get(
            alias="0",
            kvs_name="kvs1",
            set_="CNCOMP",
            counter_name="kcompact",
        )
        """
        _response = self._raw_client.perfc_in_set_with_name_get(
            alias, kvs_name, set_, counter_name, pretty=pretty, request_options=request_options
        )
        return _response.data


class AsyncKvsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKvsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKvsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKvsClient
        """
        return self._raw_client

    async def cn_tree_get(
        self,
        alias: str,
        kvs_name: str,
        *,
        human: typing.Optional[bool] = None,
        kvsets: typing.Optional[bool] = None,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvsCnTreeGetResponse:
        """
        Get information about the KVS's cN tree.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        human : typing.Optional[bool]
            Humanize certain values.

        kvsets : typing.Optional[bool]
            Include kvset details in output.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvsCnTreeGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kvs.cn_tree_get(
                alias="0",
                kvs_name="kvs1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cn_tree_get(
            alias, kvs_name, human=human, kvsets=kvsets, pretty=pretty, request_options=request_options
        )
        return _response.data

    async def params_get(
        self,
        alias: str,
        kvs_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvsParamsGetResponse:
        """
        Get all KVS parameters.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvsParamsGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kvs.params_get(
                alias="0",
                kvs_name="kvs1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.params_get(alias, kvs_name, pretty=pretty, request_options=request_options)
        return _response.data

    async def param_get(
        self,
        alias: str,
        kvs_name: str,
        param: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KvsParamGetResponse:
        """
        Get the value of the KVS parameter.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        param : str
            Parameter to interact with.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KvsParamGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.kvs.param_get(
                alias="0",
                kvs_name="kvs1",
                param="logging.enabled",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.param_get(
            alias, kvs_name, param, pretty=pretty, request_options=request_options
        )
        return _response.data

    async def param_set(
        self,
        alias: str,
        kvs_name: str,
        param: str,
        *,
        request: KvsParamSetRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Set the value of the KVS parameter.

        Parameters
        ----------
        alias : str
            Alias for a KVDB.

        kvs_name : str
            Name of the KVS.

        param : str
            Parameter to interact with.

        request : KvsParamSetRequestBody

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
            await client.kvs.param_set(
                alias="0",
                kvs_name="kvs1",
                param="logging.enabled",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.param_set(
            alias, kvs_name, param, request=request, request_options=request_options
        )
        return _response.data

    async def perfc_get(
        self,
        alias: str,
        kvs_name: str,
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

        kvs_name : str
            Name of the KVS.

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
            await client.kvs.perfc_get(
                alias="0",
                kvs_name="kvs1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perfc_get(alias, kvs_name, pretty=pretty, request_options=request_options)
        return _response.data

    async def perfc_in_set_get(
        self,
        alias: str,
        kvs_name: str,
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

        kvs_name : str
            Name of the KVS.

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
            await client.kvs.perfc_in_set_get(
                alias="0",
                kvs_name="kvs1",
                set_="CNCOMP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perfc_in_set_get(
            alias, kvs_name, set_, pretty=pretty, request_options=request_options
        )
        return _response.data

    async def perfc_in_set_with_name_get(
        self,
        alias: str,
        kvs_name: str,
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

        kvs_name : str
            Name of the KVS.

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
            await client.kvs.perfc_in_set_with_name_get(
                alias="0",
                kvs_name="kvs1",
                set_="CNCOMP",
                counter_name="kcompact",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perfc_in_set_with_name_get(
            alias, kvs_name, set_, counter_name, pretty=pretty, request_options=request_options
        )
        return _response.data
