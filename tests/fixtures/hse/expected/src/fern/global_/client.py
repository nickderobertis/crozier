

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.events import Events
from ..types.performance_counters import PerformanceCounters
from .raw_client import AsyncRawGlobalClient, RawGlobalClient
from .types.kmc_vmstat_get_response_item import KmcVmstatGetResponseItem
from .types.param_get_response import ParamGetResponse
from .types.param_set_request_body import ParamSetRequestBody
from .types.params_get_response import ParamsGetResponse
from .types.workqueues_get_response_item import WorkqueuesGetResponseItem


OMIT = typing.cast(typing.Any, ...)


class GlobalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGlobalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGlobalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGlobalClient
        """
        return self._raw_client

    def events_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Events:
        """
        Get all event counter information.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Events
            Successfully retrieved event counter information.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_.events_get()
        """
        _response = self._raw_client.events_get(pretty=pretty, request_options=request_options)
        return _response.data

    def events_in_file_get(
        self,
        file: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Events:
        """
        Get all event counter information for file.

        Parameters
        ----------
        file : str
            Basename of file.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Events
            Successfully retrieved event counter information.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_.events_in_file_get(
            file="cn.c",
        )
        """
        _response = self._raw_client.events_in_file_get(file, pretty=pretty, request_options=request_options)
        return _response.data

    def events_in_file_in_function_get(
        self,
        file: str,
        function: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Events:
        """
        Get all event counter information for function in file.

        Parameters
        ----------
        file : str
            Basename of file.

        function : str
            Function name.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Events
            Successfully retrieved event counter information.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_.events_in_file_in_function_get(
            file="cn.c",
            function="table_create",
        )
        """
        _response = self._raw_client.events_in_file_in_function_get(
            file, function, pretty=pretty, request_options=request_options
        )
        return _response.data

    def events_in_file_in_function_on_lineno_get(
        self,
        file: str,
        function: str,
        lineno: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Events:
        """
        Get all event counter information for function on line number of file.

        Parameters
        ----------
        file : str
            Basename of file.

        function : str
            Function name.

        lineno : str
            Line number.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Events
            Successfully retrieved event counter information.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_.events_in_file_in_function_on_lineno_get(
            file="cn.c",
            function="table_create",
            lineno="420",
        )
        """
        _response = self._raw_client.events_in_file_in_function_on_lineno_get(
            file, function, lineno, pretty=pretty, request_options=request_options
        )
        return _response.data

    def kmc_vmstat_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[KmcVmstatGetResponseItem]:
        """
        Get virtual memory statistics.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[KmcVmstatGetResponseItem]
            Successfully retrieved virtual memory statistics.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_.kmc_vmstat_get()
        """
        _response = self._raw_client.kmc_vmstat_get(pretty=pretty, request_options=request_options)
        return _response.data

    def params_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ParamsGetResponse:
        """
        Get all global parameters.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParamsGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_.params_get()
        """
        _response = self._raw_client.params_get(pretty=pretty, request_options=request_options)
        return _response.data

    def param_get(
        self,
        param: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParamGetResponse:
        """
        Get the value of the global parameter.

        Parameters
        ----------
        param : str
            Parameter to interact with.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParamGetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_.param_get(
            param="logging.enabled",
        )
        """
        _response = self._raw_client.param_get(param, pretty=pretty, request_options=request_options)
        return _response.data

    def param_set(
        self, param: str, *, request: ParamSetRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Set the value of the global parameter.

        Parameters
        ----------
        param : str
            Parameter to interact with.

        request : ParamSetRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_.param_set(
            param="logging.enabled",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.param_set(param, request=request, request_options=request_options)
        return _response.data

    def perfc_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> PerformanceCounters:
        """
        Get all performance counter information.

        Parameters
        ----------
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
        client.global_.perfc_get()
        """
        _response = self._raw_client.perfc_get(pretty=pretty, request_options=request_options)
        return _response.data

    def perfc_in_group_get(
        self,
        group: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformanceCounters:
        """
        Get all performance counter information for group.

        Parameters
        ----------
        group : str
            Performance counter group.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PerformanceCounters
            Successfully retrieved event counter information for group.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_.perfc_in_group_get(
            group="global",
        )
        """
        _response = self._raw_client.perfc_in_group_get(group, pretty=pretty, request_options=request_options)
        return _response.data

    def perfc_in_group_in_set_get(
        self,
        group: str,
        set_: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformanceCounters:
        """
        Get all performance counter information for group in set.

        Parameters
        ----------
        group : str
            Performance counter group.

        set_ : str
            Performance counter set.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PerformanceCounters
            Successfully retrieved event counter information for group in set.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_.perfc_in_group_in_set_get(
            group="global",
            set_="CNCOMP",
        )
        """
        _response = self._raw_client.perfc_in_group_in_set_get(
            group, set_, pretty=pretty, request_options=request_options
        )
        return _response.data

    def perfc_in_group_in_set_with_name_get(
        self,
        group: str,
        set_: str,
        counter_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformanceCounters:
        """
        Get all performance counter information for group in set with name.

        Parameters
        ----------
        group : str
            Performance counter group.

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
            Successfully retrieved event counter information for group in set with name.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_.perfc_in_group_in_set_with_name_get(
            group="global",
            set_="CNCOMP",
            counter_name="kcompact",
        )
        """
        _response = self._raw_client.perfc_in_group_in_set_with_name_get(
            group, set_, counter_name, pretty=pretty, request_options=request_options
        )
        return _response.data

    def workqueues_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WorkqueuesGetResponseItem]:
        """
        Get the process' `/proc/self/task/[tid]/stat` information.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkqueuesGetResponseItem]
            Successfully retrieved all workqueue information.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_.workqueues_get()
        """
        _response = self._raw_client.workqueues_get(pretty=pretty, request_options=request_options)
        return _response.data


class AsyncGlobalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGlobalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGlobalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGlobalClient
        """
        return self._raw_client

    async def events_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> Events:
        """
        Get all event counter information.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Events
            Successfully retrieved event counter information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_.events_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.events_get(pretty=pretty, request_options=request_options)
        return _response.data

    async def events_in_file_get(
        self,
        file: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Events:
        """
        Get all event counter information for file.

        Parameters
        ----------
        file : str
            Basename of file.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Events
            Successfully retrieved event counter information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_.events_in_file_get(
                file="cn.c",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.events_in_file_get(file, pretty=pretty, request_options=request_options)
        return _response.data

    async def events_in_file_in_function_get(
        self,
        file: str,
        function: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Events:
        """
        Get all event counter information for function in file.

        Parameters
        ----------
        file : str
            Basename of file.

        function : str
            Function name.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Events
            Successfully retrieved event counter information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_.events_in_file_in_function_get(
                file="cn.c",
                function="table_create",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.events_in_file_in_function_get(
            file, function, pretty=pretty, request_options=request_options
        )
        return _response.data

    async def events_in_file_in_function_on_lineno_get(
        self,
        file: str,
        function: str,
        lineno: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Events:
        """
        Get all event counter information for function on line number of file.

        Parameters
        ----------
        file : str
            Basename of file.

        function : str
            Function name.

        lineno : str
            Line number.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Events
            Successfully retrieved event counter information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_.events_in_file_in_function_on_lineno_get(
                file="cn.c",
                function="table_create",
                lineno="420",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.events_in_file_in_function_on_lineno_get(
            file, function, lineno, pretty=pretty, request_options=request_options
        )
        return _response.data

    async def kmc_vmstat_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[KmcVmstatGetResponseItem]:
        """
        Get virtual memory statistics.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[KmcVmstatGetResponseItem]
            Successfully retrieved virtual memory statistics.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_.kmc_vmstat_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.kmc_vmstat_get(pretty=pretty, request_options=request_options)
        return _response.data

    async def params_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ParamsGetResponse:
        """
        Get all global parameters.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParamsGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_.params_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.params_get(pretty=pretty, request_options=request_options)
        return _response.data

    async def param_get(
        self,
        param: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParamGetResponse:
        """
        Get the value of the global parameter.

        Parameters
        ----------
        param : str
            Parameter to interact with.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParamGetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_.param_get(
                param="logging.enabled",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.param_get(param, pretty=pretty, request_options=request_options)
        return _response.data

    async def param_set(
        self, param: str, *, request: ParamSetRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Set the value of the global parameter.

        Parameters
        ----------
        param : str
            Parameter to interact with.

        request : ParamSetRequestBody

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
            await client.global_.param_set(
                param="logging.enabled",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.param_set(param, request=request, request_options=request_options)
        return _response.data

    async def perfc_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> PerformanceCounters:
        """
        Get all performance counter information.

        Parameters
        ----------
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
            await client.global_.perfc_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.perfc_get(pretty=pretty, request_options=request_options)
        return _response.data

    async def perfc_in_group_get(
        self,
        group: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformanceCounters:
        """
        Get all performance counter information for group.

        Parameters
        ----------
        group : str
            Performance counter group.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PerformanceCounters
            Successfully retrieved event counter information for group.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_.perfc_in_group_get(
                group="global",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perfc_in_group_get(group, pretty=pretty, request_options=request_options)
        return _response.data

    async def perfc_in_group_in_set_get(
        self,
        group: str,
        set_: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformanceCounters:
        """
        Get all performance counter information for group in set.

        Parameters
        ----------
        group : str
            Performance counter group.

        set_ : str
            Performance counter set.

        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PerformanceCounters
            Successfully retrieved event counter information for group in set.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_.perfc_in_group_in_set_get(
                group="global",
                set_="CNCOMP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perfc_in_group_in_set_get(
            group, set_, pretty=pretty, request_options=request_options
        )
        return _response.data

    async def perfc_in_group_in_set_with_name_get(
        self,
        group: str,
        set_: str,
        counter_name: str,
        *,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PerformanceCounters:
        """
        Get all performance counter information for group in set with name.

        Parameters
        ----------
        group : str
            Performance counter group.

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
            Successfully retrieved event counter information for group in set with name.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_.perfc_in_group_in_set_with_name_get(
                group="global",
                set_="CNCOMP",
                counter_name="kcompact",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perfc_in_group_in_set_with_name_get(
            group, set_, counter_name, pretty=pretty, request_options=request_options
        )
        return _response.data

    async def workqueues_get(
        self, *, pretty: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WorkqueuesGetResponseItem]:
        """
        Get the process' `/proc/self/task/[tid]/stat` information.

        Parameters
        ----------
        pretty : typing.Optional[bool]
            Pretty print the response body.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkqueuesGetResponseItem]
            Successfully retrieved all workqueue information.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_.workqueues_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.workqueues_get(pretty=pretty, request_options=request_options)
        return _response.data
