

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.task_dto import TaskDto
from ..types.tool_dto import ToolDto
from .raw_client import AsyncRawToolsClient, RawToolsClient


OMIT = typing.cast(typing.Any, ...)


class ToolsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawToolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawToolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawToolsClient
        """
        return self._raw_client

    def tools_api_get_tools(
        self,
        *,
        page_size: typing.Optional[float] = None,
        page_index: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolDto:
        """
        Returns all tools. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        page_size : typing.Optional[float]
            The numbers of items to return

        page_index : typing.Optional[float]
            The number of pages to skip before starting to collect the result set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_get_tools()
        """
        _response = self._raw_client.tools_api_get_tools(
            page_size=page_size, page_index=page_index, request_options=request_options
        )
        return _response.data

    def tools_api_create_new_tool(self, *, request_options: typing.Optional[RequestOptions] = None) -> ToolDto:
        """
        Creates a new tool. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_create_new_tool()
        """
        _response = self._raw_client.tools_api_create_new_tool(request_options=request_options)
        return _response.data

    def tools_api_create_new_tool_async(self, *, request_options: typing.Optional[RequestOptions] = None) -> TaskDto:
        """
        Creates a new tool. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_create_new_tool_async()
        """
        _response = self._raw_client.tools_api_create_new_tool_async(request_options=request_options)
        return _response.data

    def tools_api_get_tool_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ToolDto:
        """
        Retrieves tool configuration for the specified tool ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str
            Tool ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_get_tool_by_id(
            id="id",
        )
        """
        _response = self._raw_client.tools_api_get_tool_by_id(id, request_options=request_options)
        return _response.data

    def tools_api_update_tool(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ToolDto:
        """
        Updates tool configuration for the specified tool ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str
            Tool ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_update_tool(
            id="id",
        )
        """
        _response = self._raw_client.tools_api_update_tool(id, request_options=request_options)
        return _response.data

    def tools_api_delete_tool(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the tool.

        Parameters
        ----------
        id : str
            Tool ID

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
        client.tools.tools_api_delete_tool(
            id="id",
        )
        """
        _response = self._raw_client.tools_api_delete_tool(id, request_options=request_options)
        return _response.data

    def tools_api_publish_tool(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ToolDto:
        """
        Publishes the tool with the specified (internal) tool ID onto IPFS, sends a message featuring its IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str
            Tool ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_publish_tool(
            id="id",
        )
        """
        _response = self._raw_client.tools_api_publish_tool(id, request_options=request_options)
        return _response.data

    def tools_api_publish_tool_async(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskDto:
        """
        Publishes the tool with the specified (internal) tool ID onto IPFS, sends a message featuring its IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str
            Tool ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_publish_tool_async(
            id="id",
        )
        """
        _response = self._raw_client.tools_api_publish_tool_async(id, request_options=request_options)
        return _response.data

    def tools_api_validate_tool(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Validates selected tool. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_validate_tool()
        """
        _response = self._raw_client.tools_api_validate_tool(request_options=request_options)
        return _response.data

    def tools_api_tool_export_file(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns a zip file containing the published tool and all associated artifacts, i.e. schemas and VCs. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str
            Tool ID

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
        client.tools.tools_api_tool_export_file(
            id="id",
        )
        """
        _response = self._raw_client.tools_api_tool_export_file(id, request_options=request_options)
        return _response.data

    def tools_api_tool_export_message(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the Hedera message ID for the specified tool published onto IPFS. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str
            Tool ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_tool_export_message(
            id="id",
        )
        """
        _response = self._raw_client.tools_api_tool_export_message(id, request_options=request_options)
        return _response.data

    def tools_api_tool_import_message_preview(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new tool and all associated artifacts from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_tool_import_message_preview()
        """
        _response = self._raw_client.tools_api_tool_import_message_preview(request_options=request_options)
        return _response.data

    def tools_api_tool_import_message(self, *, request_options: typing.Optional[RequestOptions] = None) -> ToolDto:
        """
        Imports new tool and all associated artifacts from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_tool_import_message()
        """
        _response = self._raw_client.tools_api_tool_import_message(request_options=request_options)
        return _response.data

    def tools_api_tool_import_file_preview(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new tool and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_tool_import_file_preview()
        """
        _response = self._raw_client.tools_api_tool_import_file_preview(request_options=request_options)
        return _response.data

    def tools_api_tool_import_file(self, *, request_options: typing.Optional[RequestOptions] = None) -> ToolDto:
        """
        Imports new tool and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_tool_import_file()
        """
        _response = self._raw_client.tools_api_tool_import_file(request_options=request_options)
        return _response.data

    def tools_api_tool_import_file_with_metadata(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolDto:
        """
        Imports new tool and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        metadata : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_tool_import_file_with_metadata()
        """
        _response = self._raw_client.tools_api_tool_import_file_with_metadata(
            file=file, metadata=metadata, request_options=request_options
        )
        return _response.data

    def tools_api_tool_import_file_async(self, *, request_options: typing.Optional[RequestOptions] = None) -> TaskDto:
        """
        Imports new tool and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_tool_import_file_async()
        """
        _response = self._raw_client.tools_api_tool_import_file_async(request_options=request_options)
        return _response.data

    def tools_api_tool_import_file_with_metadata_async(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskDto:
        """
        Imports new tool and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        metadata : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_tool_import_file_with_metadata_async()
        """
        _response = self._raw_client.tools_api_tool_import_file_with_metadata_async(
            file=file, metadata=metadata, request_options=request_options
        )
        return _response.data

    def tools_api_tool_import_message_async(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskDto:
        """
        Imports new tool and all associated artifacts from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_tool_import_message_async()
        """
        _response = self._raw_client.tools_api_tool_import_message_async(request_options=request_options)
        return _response.data

    def tools_api_get_menu(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Returns tools menu. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.tools_api_get_menu()
        """
        _response = self._raw_client.tools_api_get_menu(request_options=request_options)
        return _response.data


class AsyncToolsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawToolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawToolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawToolsClient
        """
        return self._raw_client

    async def tools_api_get_tools(
        self,
        *,
        page_size: typing.Optional[float] = None,
        page_index: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolDto:
        """
        Returns all tools. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        page_size : typing.Optional[float]
            The numbers of items to return

        page_index : typing.Optional[float]
            The number of pages to skip before starting to collect the result set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_get_tools()


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_get_tools(
            page_size=page_size, page_index=page_index, request_options=request_options
        )
        return _response.data

    async def tools_api_create_new_tool(self, *, request_options: typing.Optional[RequestOptions] = None) -> ToolDto:
        """
        Creates a new tool. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_create_new_tool()


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_create_new_tool(request_options=request_options)
        return _response.data

    async def tools_api_create_new_tool_async(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskDto:
        """
        Creates a new tool. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_create_new_tool_async()


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_create_new_tool_async(request_options=request_options)
        return _response.data

    async def tools_api_get_tool_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ToolDto:
        """
        Retrieves tool configuration for the specified tool ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str
            Tool ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_get_tool_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_get_tool_by_id(id, request_options=request_options)
        return _response.data

    async def tools_api_update_tool(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ToolDto:
        """
        Updates tool configuration for the specified tool ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str
            Tool ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_update_tool(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_update_tool(id, request_options=request_options)
        return _response.data

    async def tools_api_delete_tool(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the tool.

        Parameters
        ----------
        id : str
            Tool ID

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
            await client.tools.tools_api_delete_tool(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_delete_tool(id, request_options=request_options)
        return _response.data

    async def tools_api_publish_tool(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ToolDto:
        """
        Publishes the tool with the specified (internal) tool ID onto IPFS, sends a message featuring its IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str
            Tool ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_publish_tool(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_publish_tool(id, request_options=request_options)
        return _response.data

    async def tools_api_publish_tool_async(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskDto:
        """
        Publishes the tool with the specified (internal) tool ID onto IPFS, sends a message featuring its IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str
            Tool ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_publish_tool_async(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_publish_tool_async(id, request_options=request_options)
        return _response.data

    async def tools_api_validate_tool(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Validates selected tool. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_validate_tool()


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_validate_tool(request_options=request_options)
        return _response.data

    async def tools_api_tool_export_file(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns a zip file containing the published tool and all associated artifacts, i.e. schemas and VCs. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str
            Tool ID

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
            await client.tools.tools_api_tool_export_file(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_tool_export_file(id, request_options=request_options)
        return _response.data

    async def tools_api_tool_export_message(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the Hedera message ID for the specified tool published onto IPFS. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        id : str
            Tool ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_tool_export_message(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_tool_export_message(id, request_options=request_options)
        return _response.data

    async def tools_api_tool_import_message_preview(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new tool and all associated artifacts from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_tool_import_message_preview()


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_tool_import_message_preview(request_options=request_options)
        return _response.data

    async def tools_api_tool_import_message(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ToolDto:
        """
        Imports new tool and all associated artifacts from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_tool_import_message()


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_tool_import_message(request_options=request_options)
        return _response.data

    async def tools_api_tool_import_file_preview(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new tool and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_tool_import_file_preview()


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_tool_import_file_preview(request_options=request_options)
        return _response.data

    async def tools_api_tool_import_file(self, *, request_options: typing.Optional[RequestOptions] = None) -> ToolDto:
        """
        Imports new tool and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_tool_import_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_tool_import_file(request_options=request_options)
        return _response.data

    async def tools_api_tool_import_file_with_metadata(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolDto:
        """
        Imports new tool and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        metadata : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_tool_import_file_with_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_tool_import_file_with_metadata(
            file=file, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def tools_api_tool_import_file_async(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskDto:
        """
        Imports new tool and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_tool_import_file_async()


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_tool_import_file_async(request_options=request_options)
        return _response.data

    async def tools_api_tool_import_file_with_metadata_async(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskDto:
        """
        Imports new tool and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        metadata : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_tool_import_file_with_metadata_async()


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_tool_import_file_with_metadata_async(
            file=file, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def tools_api_tool_import_message_async(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskDto:
        """
        Imports new tool and all associated artifacts from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_tool_import_message_async()


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_tool_import_message_async(request_options=request_options)
        return _response.data

    async def tools_api_get_menu(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Returns tools menu. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.tools_api_get_menu()


        asyncio.run(main())
        """
        _response = await self._raw_client.tools_api_get_menu(request_options=request_options)
        return _response.data
