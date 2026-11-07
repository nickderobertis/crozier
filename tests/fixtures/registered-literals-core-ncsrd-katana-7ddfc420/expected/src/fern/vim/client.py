

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sbi_ls import SbiLs
from ..types.vim import Vim
from ..types.vim_config import VimConfig
from .raw_client import AsyncRawVimClient, RawVimClient


OMIT = typing.cast(typing.Any, ...)


class VimClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVimClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVimClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVimClient
        """
        return self._raw_client

    def returns_a_list_of_registered_vi_ms(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SbiLs]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SbiLs]
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.vim.returns_a_list_of_registered_vi_ms()
        """
        _response = self._raw_client.returns_a_list_of_registered_vi_ms(request_options=request_options)
        return _response.data

    def adds_a_new_vim(
        self,
        *,
        id: str,
        auth_url: str,
        username: str,
        password: str,
        admin_project_name: str,
        name: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        infrastructure_monitoring: typing.Optional[str] = OMIT,
        config: typing.Optional[VimConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique id

        auth_url : str
            VIM's authentication URL - example: http://10.200.64.2:5000/v3/

        username : str
            The admin username

        password : str
            The admin password

        admin_project_name : str
            The admin project

        name : typing.Optional[str]
            The name for the new VIM

        location : typing.Optional[str]
            VIM's location

        type : typing.Optional[str]
            VIM's type

        version : typing.Optional[str]
            The version of the VIM's OS

        description : typing.Optional[str]
            A description for the VIM

        infrastructure_monitoring : typing.Optional[str]
            Optional - The URL of the Prometheus system that is responsible for monitoring the VIM

        config : typing.Optional[VimConfig]
            Optional parameters regarding the VIM operation - example: Security group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.vim.adds_a_new_vim(
            id="id",
            auth_url="auth_url",
            username="username",
            password="password",
            admin_project_name="admin_project_name",
        )
        """
        _response = self._raw_client.adds_a_new_vim(
            id=id,
            auth_url=auth_url,
            username=username,
            password=password,
            admin_project_name=admin_project_name,
            name=name,
            location=location,
            type=type,
            version=version,
            description=description,
            infrastructure_monitoring=infrastructure_monitoring,
            config=config,
            request_options=request_options,
        )
        return _response.data

    def returns_information_about_the_given_vim_id(
        self, vim_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Vim:
        """
        Parameters
        ----------
        vim_id : str
            ID of VIM to be inspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vim
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.vim.returns_information_about_the_given_vim_id(
            vim_id="vim_id",
        )
        """
        _response = self._raw_client.returns_information_about_the_given_vim_id(vim_id, request_options=request_options)
        return _response.data

    def updates_the_given_vim(self, vim_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        vim_id : str
            ID of VIM to be updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.vim.updates_the_given_vim(
            vim_id="vim_id",
        )
        """
        _response = self._raw_client.updates_the_given_vim(vim_id, request_options=request_options)
        return _response.data

    def deletes_the_given_vim(self, vim_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        vim_id : str
            ID of VIM to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.vim.deletes_the_given_vim(
            vim_id="vim_id",
        )
        """
        _response = self._raw_client.deletes_the_given_vim(vim_id, request_options=request_options)
        return _response.data


class AsyncVimClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVimClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVimClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVimClient
        """
        return self._raw_client

    async def returns_a_list_of_registered_vi_ms(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SbiLs]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SbiLs]
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.vim.returns_a_list_of_registered_vi_ms()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_registered_vi_ms(request_options=request_options)
        return _response.data

    async def adds_a_new_vim(
        self,
        *,
        id: str,
        auth_url: str,
        username: str,
        password: str,
        admin_project_name: str,
        name: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        infrastructure_monitoring: typing.Optional[str] = OMIT,
        config: typing.Optional[VimConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Unique id

        auth_url : str
            VIM's authentication URL - example: http://10.200.64.2:5000/v3/

        username : str
            The admin username

        password : str
            The admin password

        admin_project_name : str
            The admin project

        name : typing.Optional[str]
            The name for the new VIM

        location : typing.Optional[str]
            VIM's location

        type : typing.Optional[str]
            VIM's type

        version : typing.Optional[str]
            The version of the VIM's OS

        description : typing.Optional[str]
            A description for the VIM

        infrastructure_monitoring : typing.Optional[str]
            Optional - The URL of the Prometheus system that is responsible for monitoring the VIM

        config : typing.Optional[VimConfig]
            Optional parameters regarding the VIM operation - example: Security group

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
            await client.vim.adds_a_new_vim(
                id="id",
                auth_url="auth_url",
                username="username",
                password="password",
                admin_project_name="admin_project_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.adds_a_new_vim(
            id=id,
            auth_url=auth_url,
            username=username,
            password=password,
            admin_project_name=admin_project_name,
            name=name,
            location=location,
            type=type,
            version=version,
            description=description,
            infrastructure_monitoring=infrastructure_monitoring,
            config=config,
            request_options=request_options,
        )
        return _response.data

    async def returns_information_about_the_given_vim_id(
        self, vim_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Vim:
        """
        Parameters
        ----------
        vim_id : str
            ID of VIM to be inspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vim
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.vim.returns_information_about_the_given_vim_id(
                vim_id="vim_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_information_about_the_given_vim_id(
            vim_id, request_options=request_options
        )
        return _response.data

    async def updates_the_given_vim(
        self, vim_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        vim_id : str
            ID of VIM to be updated

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
            await client.vim.updates_the_given_vim(
                vim_id="vim_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_the_given_vim(vim_id, request_options=request_options)
        return _response.data

    async def deletes_the_given_vim(
        self, vim_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        vim_id : str
            ID of VIM to be deleted

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
            await client.vim.deletes_the_given_vim(
                vim_id="vim_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_the_given_vim(vim_id, request_options=request_options)
        return _response.data
