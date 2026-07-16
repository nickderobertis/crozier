

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deleted import Deleted
from ..types.patch import Patch
from ..types.script import Script
from ..types.script_compilation_result import ScriptCompilationResult
from .raw_client import AsyncRawScriptsClient, RawScriptsClient


OMIT = typing.cast(typing.Any, ...)


class ScriptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScriptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScriptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScriptsClient
        """
        return self._raw_client

    def find_all_scripts(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Script]:
        """
        Get all scripts

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Script]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.find_all_scripts()
        """
        _response = self._raw_client.find_all_scripts(request_options=request_options)
        return _response.data

    def create_script(
        self,
        *,
        code: typing.Dict[str, str],
        desc: typing.Dict[str, str],
        id: str,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Script:
        """
        Create a new script

        Parameters
        ----------
        code : typing.Dict[str, str]
            The code of the script

        desc : typing.Dict[str, str]
            The description of the script

        id : str
            The id of the script

        name : str
            The name of the script

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Script
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.create_script(
            code={"key": "value"},
            desc={"key": "value"},
            id="a string value",
            name="a string value",
        )
        """
        _response = self._raw_client.create_script(
            code=code, desc=desc, id=id, name=name, request_options=request_options
        )
        return _response.data

    def compile_script(
        self,
        *,
        code: typing.Dict[str, str],
        desc: typing.Dict[str, str],
        id: str,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScriptCompilationResult:
        """
        Compile a script

        Parameters
        ----------
        code : typing.Dict[str, str]
            The code of the script

        desc : typing.Dict[str, str]
            The description of the script

        id : str
            The id of the script

        name : str
            The name of the script

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScriptCompilationResult
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.compile_script(
            code={"key": "value"},
            desc={"key": "value"},
            id="a string value",
            name="a string value",
        )
        """
        _response = self._raw_client.compile_script(
            code=code, desc=desc, id=id, name=name, request_options=request_options
        )
        return _response.data

    def find_script_by_id(self, script_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Script:
        """
        Get a script

        Parameters
        ----------
        script_id : str
            The script id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Script
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.find_script_by_id(
            script_id="scriptId",
        )
        """
        _response = self._raw_client.find_script_by_id(script_id, request_options=request_options)
        return _response.data

    def update_script(
        self,
        script_id: str,
        *,
        code: typing.Dict[str, str],
        desc: typing.Dict[str, str],
        id: str,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Script:
        """
        Update a script

        Parameters
        ----------
        script_id : str
            The script id

        code : typing.Dict[str, str]
            The code of the script

        desc : typing.Dict[str, str]
            The description of the script

        id : str
            The id of the script

        name : str
            The name of the script

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Script
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.update_script(
            script_id="scriptId",
            code={"key": "value"},
            desc={"key": "value"},
            id="a string value",
            name="a string value",
        )
        """
        _response = self._raw_client.update_script(
            script_id, code=code, desc=desc, id=id, name=name, request_options=request_options
        )
        return _response.data

    def delete_script(self, script_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Deleted:
        """
        Delete a script

        Parameters
        ----------
        script_id : str
            The script id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.delete_script(
            script_id="scriptId",
        )
        """
        _response = self._raw_client.delete_script(script_id, request_options=request_options)
        return _response.data

    def patch_script(
        self, script_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> Script:
        """
        Update a script with a diff

        Parameters
        ----------
        script_id : str
            The script id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Script
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.scripts.patch_script(
            script_id="scriptId",
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.patch_script(script_id, request=request, request_options=request_options)
        return _response.data


class AsyncScriptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScriptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScriptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScriptsClient
        """
        return self._raw_client

    async def find_all_scripts(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Script]:
        """
        Get all scripts

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Script]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.scripts.find_all_scripts()


        asyncio.run(main())
        """
        _response = await self._raw_client.find_all_scripts(request_options=request_options)
        return _response.data

    async def create_script(
        self,
        *,
        code: typing.Dict[str, str],
        desc: typing.Dict[str, str],
        id: str,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Script:
        """
        Create a new script

        Parameters
        ----------
        code : typing.Dict[str, str]
            The code of the script

        desc : typing.Dict[str, str]
            The description of the script

        id : str
            The id of the script

        name : str
            The name of the script

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Script
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.scripts.create_script(
                code={"key": "value"},
                desc={"key": "value"},
                id="a string value",
                name="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_script(
            code=code, desc=desc, id=id, name=name, request_options=request_options
        )
        return _response.data

    async def compile_script(
        self,
        *,
        code: typing.Dict[str, str],
        desc: typing.Dict[str, str],
        id: str,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ScriptCompilationResult:
        """
        Compile a script

        Parameters
        ----------
        code : typing.Dict[str, str]
            The code of the script

        desc : typing.Dict[str, str]
            The description of the script

        id : str
            The id of the script

        name : str
            The name of the script

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScriptCompilationResult
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.scripts.compile_script(
                code={"key": "value"},
                desc={"key": "value"},
                id="a string value",
                name="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.compile_script(
            code=code, desc=desc, id=id, name=name, request_options=request_options
        )
        return _response.data

    async def find_script_by_id(
        self, script_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Script:
        """
        Get a script

        Parameters
        ----------
        script_id : str
            The script id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Script
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.scripts.find_script_by_id(
                script_id="scriptId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_script_by_id(script_id, request_options=request_options)
        return _response.data

    async def update_script(
        self,
        script_id: str,
        *,
        code: typing.Dict[str, str],
        desc: typing.Dict[str, str],
        id: str,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Script:
        """
        Update a script

        Parameters
        ----------
        script_id : str
            The script id

        code : typing.Dict[str, str]
            The code of the script

        desc : typing.Dict[str, str]
            The description of the script

        id : str
            The id of the script

        name : str
            The name of the script

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Script
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.scripts.update_script(
                script_id="scriptId",
                code={"key": "value"},
                desc={"key": "value"},
                id="a string value",
                name="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_script(
            script_id, code=code, desc=desc, id=id, name=name, request_options=request_options
        )
        return _response.data

    async def delete_script(
        self, script_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete a script

        Parameters
        ----------
        script_id : str
            The script id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.scripts.delete_script(
                script_id="scriptId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_script(script_id, request_options=request_options)
        return _response.data

    async def patch_script(
        self, script_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> Script:
        """
        Update a script with a diff

        Parameters
        ----------
        script_id : str
            The script id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Script
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PatchItem, PatchItemOp

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.scripts.patch_script(
                script_id="scriptId",
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_script(script_id, request=request, request_options=request_options)
        return _response.data
