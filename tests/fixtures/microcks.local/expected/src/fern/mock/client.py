

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.counter import Counter
from ..types.labels_map import LabelsMap
from ..types.parameter_constraint import ParameterConstraint
from ..types.service import Service
from .raw_client import AsyncRawMockClient, RawMockClient
from .types.get_service_response import GetServiceResponse


OMIT = typing.cast(typing.Any, ...)


class MockClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMockClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMockClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMockClient
        """
        return self._raw_client

    def export_snapshot(
        self,
        *,
        service_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Export a repostiory snapshot with requested services

        Parameters
        ----------
        service_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of service identifiers to export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Snapshot file representing the export of requested services
        """
        with self._raw_client.export_snapshot(service_ids=service_ids, request_options=request_options) as r:
            yield from r.data

    def import_snapshot(self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Import a repository snapshot previsouly exported into Microcks

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

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
        client.mock.import_snapshot()
        """
        _response = self._raw_client.import_snapshot(file=file, request_options=request_options)
        return _response.data

    def get_services(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page of Services to retrieve (starts at and defaults to 0)

        size : typing.Optional[int]
            Size of a page. Maximum number of Services to include in a response (defaults to 20)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            List of found Services

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mock.get_services()
        """
        _response = self._raw_client.get_services(page=page, size=size, request_options=request_options)
        return _response.data

    def get_services_counter(self, *, request_options: typing.Optional[RequestOptions] = None) -> Counter:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Counter
            Number of Services in datastore

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mock.get_services_counter()
        """
        _response = self._raw_client.get_services_counter(request_options=request_options)
        return _response.data

    def get_services_labels(self, *, request_options: typing.Optional[RequestOptions] = None) -> LabelsMap:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LabelsMap
            Already used labels: keys are label Keys, values are array of label Values

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mock.get_services_labels()
        """
        _response = self._raw_client.get_services_labels(request_options=request_options)
        return _response.data

    def search_services(
        self, *, query_map: typing.Dict[str, str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Service]:
        """
        Parameters
        ----------
        query_map : typing.Dict[str, str]
            Map of criterion. Key can be simply 'name' with value as the searched string. You can also search by label using keys like 'labels.x' where 'x' is the label and value the label value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Service]
            List of found Services (filtered according search criteria)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mock.search_services(
            query_map={"queryMap": "queryMap"},
        )
        """
        _response = self._raw_client.search_services(query_map=query_map, request_options=request_options)
        return _response.data

    def get_service(
        self,
        id: str,
        *,
        messages: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetServiceResponse:
        """
        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        messages : typing.Optional[bool]
            Whether to include details on services messages into result. Default is false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetServiceResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.mock.get_service(
            id="id",
        )
        """
        _response = self._raw_client.get_service(id, messages=messages, request_options=request_options)
        return _response.data

    def delete_service(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a Service

        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

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
        client.mock.delete_service(
            id="id",
        )
        """
        _response = self._raw_client.delete_service(id, request_options=request_options)
        return _response.data

    def update_service_metadata(
        self,
        id: str,
        *,
        created_on: int,
        last_update: int,
        annotations: typing.Optional[typing.Dict[str, str]] = OMIT,
        labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        created_on : int
            Creation date of attached object

        last_update : int
            Last update of attached object

        annotations : typing.Optional[typing.Dict[str, str]]
            Annotations of attached object

        labels : typing.Optional[typing.Dict[str, str]]
            Labels put on attached object

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
        client.mock.update_service_metadata(
            id="id",
            created_on=1,
            last_update=1,
        )
        """
        _response = self._raw_client.update_service_metadata(
            id,
            created_on=created_on,
            last_update=last_update,
            annotations=annotations,
            labels=labels,
            request_options=request_options,
        )
        return _response.data

    def override_service_operation(
        self,
        id: str,
        *,
        operation_name: str,
        default_delay: typing.Optional[int] = OMIT,
        dispatcher: typing.Optional[str] = OMIT,
        dispatcher_rules: typing.Optional[str] = OMIT,
        parameter_constraints: typing.Optional[typing.Sequence[ParameterConstraint]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        operation_name : str
            Name of operation to update

        default_delay : typing.Optional[int]
            Default delay in milliseconds to apply to mock responses on this operation

        dispatcher : typing.Optional[str]
            Type of dispatcher to apply for this operation

        dispatcher_rules : typing.Optional[str]
            Rules of dispatcher for this operation

        parameter_constraints : typing.Optional[typing.Sequence[ParameterConstraint]]
            Constraints that may apply to incoming parameters on this operation

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
        client.mock.override_service_operation(
            id="id",
            operation_name="operationName",
        )
        """
        _response = self._raw_client.override_service_operation(
            id,
            operation_name=operation_name,
            default_delay=default_delay,
            dispatcher=dispatcher,
            dispatcher_rules=dispatcher_rules,
            parameter_constraints=parameter_constraints,
            request_options=request_options,
        )
        return _response.data


class AsyncMockClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMockClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMockClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMockClient
        """
        return self._raw_client

    async def export_snapshot(
        self,
        *,
        service_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Export a repostiory snapshot with requested services

        Parameters
        ----------
        service_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of service identifiers to export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Snapshot file representing the export of requested services
        """
        async with self._raw_client.export_snapshot(service_ids=service_ids, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def import_snapshot(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Import a repository snapshot previsouly exported into Microcks

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

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
            await client.mock.import_snapshot()


        asyncio.run(main())
        """
        _response = await self._raw_client.import_snapshot(file=file, request_options=request_options)
        return _response.data

    async def get_services(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page of Services to retrieve (starts at and defaults to 0)

        size : typing.Optional[int]
            Size of a page. Maximum number of Services to include in a response (defaults to 20)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            List of found Services

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mock.get_services()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_services(page=page, size=size, request_options=request_options)
        return _response.data

    async def get_services_counter(self, *, request_options: typing.Optional[RequestOptions] = None) -> Counter:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Counter
            Number of Services in datastore

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mock.get_services_counter()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_services_counter(request_options=request_options)
        return _response.data

    async def get_services_labels(self, *, request_options: typing.Optional[RequestOptions] = None) -> LabelsMap:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LabelsMap
            Already used labels: keys are label Keys, values are array of label Values

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mock.get_services_labels()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_services_labels(request_options=request_options)
        return _response.data

    async def search_services(
        self, *, query_map: typing.Dict[str, str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Service]:
        """
        Parameters
        ----------
        query_map : typing.Dict[str, str]
            Map of criterion. Key can be simply 'name' with value as the searched string. You can also search by label using keys like 'labels.x' where 'x' is the label and value the label value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Service]
            List of found Services (filtered according search criteria)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mock.search_services(
                query_map={"queryMap": "queryMap"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_services(query_map=query_map, request_options=request_options)
        return _response.data

    async def get_service(
        self,
        id: str,
        *,
        messages: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetServiceResponse:
        """
        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        messages : typing.Optional[bool]
            Whether to include details on services messages into result. Default is false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetServiceResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.mock.get_service(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service(id, messages=messages, request_options=request_options)
        return _response.data

    async def delete_service(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a Service

        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

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
            await client.mock.delete_service(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_service(id, request_options=request_options)
        return _response.data

    async def update_service_metadata(
        self,
        id: str,
        *,
        created_on: int,
        last_update: int,
        annotations: typing.Optional[typing.Dict[str, str]] = OMIT,
        labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        created_on : int
            Creation date of attached object

        last_update : int
            Last update of attached object

        annotations : typing.Optional[typing.Dict[str, str]]
            Annotations of attached object

        labels : typing.Optional[typing.Dict[str, str]]
            Labels put on attached object

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
            await client.mock.update_service_metadata(
                id="id",
                created_on=1,
                last_update=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_service_metadata(
            id,
            created_on=created_on,
            last_update=last_update,
            annotations=annotations,
            labels=labels,
            request_options=request_options,
        )
        return _response.data

    async def override_service_operation(
        self,
        id: str,
        *,
        operation_name: str,
        default_delay: typing.Optional[int] = OMIT,
        dispatcher: typing.Optional[str] = OMIT,
        dispatcher_rules: typing.Optional[str] = OMIT,
        parameter_constraints: typing.Optional[typing.Sequence[ParameterConstraint]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique identifier of Service to managed

        operation_name : str
            Name of operation to update

        default_delay : typing.Optional[int]
            Default delay in milliseconds to apply to mock responses on this operation

        dispatcher : typing.Optional[str]
            Type of dispatcher to apply for this operation

        dispatcher_rules : typing.Optional[str]
            Rules of dispatcher for this operation

        parameter_constraints : typing.Optional[typing.Sequence[ParameterConstraint]]
            Constraints that may apply to incoming parameters on this operation

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
            await client.mock.override_service_operation(
                id="id",
                operation_name="operationName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.override_service_operation(
            id,
            operation_name=operation_name,
            default_delay=default_delay,
            dispatcher=dispatcher,
            dispatcher_rules=dispatcher_rules,
            parameter_constraints=parameter_constraints,
            request_options=request_options,
        )
        return _response.data
