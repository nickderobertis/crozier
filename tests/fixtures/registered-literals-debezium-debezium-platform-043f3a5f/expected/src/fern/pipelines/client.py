

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.named_ref import NamedRef
from ..types.pipeline_response import PipelineResponse
from ..types.signal_response import SignalResponse
from .raw_client import AsyncRawPipelinesClient, RawPipelinesClient


OMIT = typing.cast(typing.Any, ...)


class PipelinesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPipelinesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPipelinesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPipelinesClient
        """
        return self._raw_client

    def returns_all_available_pipelines(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PipelineResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PipelineResponse]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.returns_all_available_pipelines()
        """
        _response = self._raw_client.returns_all_available_pipelines(request_options=request_options)
        return _response.data

    def creates_new_pipeline(
        self,
        *,
        name: str,
        source: NamedRef,
        destination: NamedRef,
        log_level: str,
        description: typing.Optional[str] = OMIT,
        transforms: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        log_levels: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        name : str

        source : NamedRef

        destination : NamedRef

        log_level : str

        description : typing.Optional[str]

        transforms : typing.Optional[typing.Sequence[NamedRef]]

        log_levels : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        from fern import FernApi, NamedRef

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.creates_new_pipeline(
            name="name",
            source=NamedRef(),
            destination=NamedRef(),
            log_level="logLevel",
        )
        """
        _response = self._raw_client.creates_new_pipeline(
            name=name,
            source=source,
            destination=destination,
            log_level=log_level,
            description=description,
            transforms=transforms,
            log_levels=log_levels,
            request_options=request_options,
        )
        return _response.data

    def returns_a_pipeline_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelineResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.returns_a_pipeline_with_given_id(
            id=1000000,
        )
        """
        _response = self._raw_client.returns_a_pipeline_with_given_id(id, request_options=request_options)
        return _response.data

    def updates_an_existing_pipeline(
        self,
        id: int,
        *,
        name: str,
        log_level: str,
        description: typing.Optional[str] = OMIT,
        transforms: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        log_levels: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        log_level : str

        description : typing.Optional[str]

        transforms : typing.Optional[typing.Sequence[NamedRef]]

        log_levels : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.updates_an_existing_pipeline(
            id=1000000,
            name="name",
            log_level="logLevel",
        )
        """
        _response = self._raw_client.updates_an_existing_pipeline(
            id,
            name=name,
            log_level=log_level,
            description=description,
            transforms=transforms,
            log_levels=log_levels,
            request_options=request_options,
        )
        return _response.data

    def deletes_an_existing_pipeline(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.deletes_an_existing_pipeline(
            id=1000000,
        )
        """
        _response = self._raw_client.deletes_an_existing_pipeline(id, request_options=request_options)
        return _response.data

    def returns_logs_for_pipeline_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.returns_logs_for_pipeline_with_given_id(
            id=1000000,
        )
        """
        _response = self._raw_client.returns_logs_for_pipeline_with_given_id(id, request_options=request_options)
        return _response.data

    def send_signal_to_pipeline_with_given_id(
        self,
        id_path_param: int,
        *,
        id: str,
        type: str,
        data: str,
        additional_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignalResponse:
        """
        Parameters
        ----------
        id_path_param : int

        id : str

        type : str

        data : str

        additional_data : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignalResponse
            Signal correctly sent to the pipeline

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.send_signal_to_pipeline_with_given_id(
            id_path_param=1000000,
            id="id",
            type="type",
            data="data",
        )
        """
        _response = self._raw_client.send_signal_to_pipeline_with_given_id(
            id_path_param, id=id, type=type, data=data, additional_data=additional_data, request_options=request_options
        )
        return _response.data


class AsyncPipelinesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPipelinesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPipelinesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPipelinesClient
        """
        return self._raw_client

    async def returns_all_available_pipelines(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PipelineResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PipelineResponse]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.returns_all_available_pipelines()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_available_pipelines(request_options=request_options)
        return _response.data

    async def creates_new_pipeline(
        self,
        *,
        name: str,
        source: NamedRef,
        destination: NamedRef,
        log_level: str,
        description: typing.Optional[str] = OMIT,
        transforms: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        log_levels: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        name : str

        source : NamedRef

        destination : NamedRef

        log_level : str

        description : typing.Optional[str]

        transforms : typing.Optional[typing.Sequence[NamedRef]]

        log_levels : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, NamedRef

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.creates_new_pipeline(
                name="name",
                source=NamedRef(),
                destination=NamedRef(),
                log_level="logLevel",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_new_pipeline(
            name=name,
            source=source,
            destination=destination,
            log_level=log_level,
            description=description,
            transforms=transforms,
            log_levels=log_levels,
            request_options=request_options,
        )
        return _response.data

    async def returns_a_pipeline_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelineResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.returns_a_pipeline_with_given_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_pipeline_with_given_id(id, request_options=request_options)
        return _response.data

    async def updates_an_existing_pipeline(
        self,
        id: int,
        *,
        name: str,
        log_level: str,
        description: typing.Optional[str] = OMIT,
        transforms: typing.Optional[typing.Sequence[NamedRef]] = OMIT,
        log_levels: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        log_level : str

        description : typing.Optional[str]

        transforms : typing.Optional[typing.Sequence[NamedRef]]

        log_levels : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.updates_an_existing_pipeline(
                id=1000000,
                name="name",
                log_level="logLevel",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_an_existing_pipeline(
            id,
            name=name,
            log_level=log_level,
            description=description,
            transforms=transforms,
            log_levels=log_levels,
            request_options=request_options,
        )
        return _response.data

    async def deletes_an_existing_pipeline(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.deletes_an_existing_pipeline(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_an_existing_pipeline(id, request_options=request_options)
        return _response.data

    async def returns_logs_for_pipeline_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        id : int

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

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.returns_logs_for_pipeline_with_given_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_logs_for_pipeline_with_given_id(id, request_options=request_options)
        return _response.data

    async def send_signal_to_pipeline_with_given_id(
        self,
        id_path_param: int,
        *,
        id: str,
        type: str,
        data: str,
        additional_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignalResponse:
        """
        Parameters
        ----------
        id_path_param : int

        id : str

        type : str

        data : str

        additional_data : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignalResponse
            Signal correctly sent to the pipeline

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.send_signal_to_pipeline_with_given_id(
                id_path_param=1000000,
                id="id",
                type="type",
                data="data",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_signal_to_pipeline_with_given_id(
            id_path_param, id=id, type=type, data=data, additional_data=additional_data, request_options=request_options
        )
        return _response.data
