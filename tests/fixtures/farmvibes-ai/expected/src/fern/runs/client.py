

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRunsClient, RawRunsClient


class RunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRunsClient
        """
        return self._raw_client

    def terravibes_list_runs(
        self,
        *,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        items: typing.Optional[int] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        List all the workflow runs currently in the system.

        Parameters
        ----------
        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The list of run IDs to retrieve. If not provided, all runs are returned.

        page : typing.Optional[int]
            The page number to retrieve.

        items : typing.Optional[int]
            The number of items per page.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Fields to return alongside each run id. If not provided, only run ids are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.runs.terravibes_list_runs()
        """
        _response = self._raw_client.terravibes_list_runs(
            ids=ids, page=page, items=items, fields=fields, request_options=request_options
        )
        return _response.data

    def terravibes_describe_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get information of a specific run.

        Parameters
        ----------
        run_id : str
            The ID of the workflow execution to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.runs.terravibes_describe_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.terravibes_describe_run(run_id, request_options=request_options)
        return _response.data

    def terravibes_delete_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete data associated with a workflow run (if not shared by other runs).

        For a detailed overview on how data is managed in FarmVibes.AI, please refer to the
        [documentation](https://microsoft.github.io/farmvibes-ai/docfiles/markdown/CACHE.html).

        Parameters
        ----------
        run_id : str
            The ID of the workflow run to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.runs.terravibes_delete_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.terravibes_delete_run(run_id, request_options=request_options)
        return _response.data

    def terravibes_cancel_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Cancel a workflow run.

        Parameters
        ----------
        run_id : str
            The ID of the workflow run to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.runs.terravibes_cancel_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.terravibes_cancel_run(run_id, request_options=request_options)
        return _response.data

    def terravibes_resubmit_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Resubmit a workflow run.

        Parameters
        ----------
        run_id : str
            The ID of the workflow run to resubmit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.runs.terravibes_resubmit_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.terravibes_resubmit_run(run_id, request_options=request_options)
        return _response.data


class AsyncRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRunsClient
        """
        return self._raw_client

    async def terravibes_list_runs(
        self,
        *,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        page: typing.Optional[int] = None,
        items: typing.Optional[int] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        List all the workflow runs currently in the system.

        Parameters
        ----------
        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The list of run IDs to retrieve. If not provided, all runs are returned.

        page : typing.Optional[int]
            The page number to retrieve.

        items : typing.Optional[int]
            The number of items per page.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Fields to return alongside each run id. If not provided, only run ids are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.runs.terravibes_list_runs()


        asyncio.run(main())
        """
        _response = await self._raw_client.terravibes_list_runs(
            ids=ids, page=page, items=items, fields=fields, request_options=request_options
        )
        return _response.data

    async def terravibes_describe_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get information of a specific run.

        Parameters
        ----------
        run_id : str
            The ID of the workflow execution to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.runs.terravibes_describe_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.terravibes_describe_run(run_id, request_options=request_options)
        return _response.data

    async def terravibes_delete_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete data associated with a workflow run (if not shared by other runs).

        For a detailed overview on how data is managed in FarmVibes.AI, please refer to the
        [documentation](https://microsoft.github.io/farmvibes-ai/docfiles/markdown/CACHE.html).

        Parameters
        ----------
        run_id : str
            The ID of the workflow run to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.runs.terravibes_delete_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.terravibes_delete_run(run_id, request_options=request_options)
        return _response.data

    async def terravibes_cancel_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Cancel a workflow run.

        Parameters
        ----------
        run_id : str
            The ID of the workflow run to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.runs.terravibes_cancel_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.terravibes_cancel_run(run_id, request_options=request_options)
        return _response.data

    async def terravibes_resubmit_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Resubmit a workflow run.

        Parameters
        ----------
        run_id : str
            The ID of the workflow run to resubmit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.runs.terravibes_resubmit_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.terravibes_resubmit_run(run_id, request_options=request_options)
        return _response.data
