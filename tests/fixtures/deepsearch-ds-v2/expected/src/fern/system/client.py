

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cps_package import CpsPackage
from ..types.modules_config import ModulesConfig
from ..types.system_info import SystemInfo
from .raw_client import AsyncRawSystemClient, RawSystemClient


class SystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemClient
        """
        return self._raw_client

    def get_system_information(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemInfo:
        """
        Get system info.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system.get_system_information()
        """
        _response = self._raw_client.get_system_information(request_options=request_options)
        return _response.data

    def get_system_modules_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ModulesConfig:
        """
        Get modules configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModulesConfig
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system.get_system_modules_configuration()
        """
        _response = self._raw_client.get_system_modules_configuration(request_options=request_options)
        return _response.data

    def get_system_modules_tasks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get modules configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system.get_system_modules_tasks()
        """
        _response = self._raw_client.get_system_modules_tasks(request_options=request_options)
        return _response.data

    def list_system_knowledge_graphs(
        self,
        *,
        proj_key: typing.Optional[str] = None,
        term: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        List all Knowledge Graphs in the system.

        Parameters
        ----------
        proj_key : typing.Optional[str]

        term : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system.list_system_knowledge_graphs()
        """
        _response = self._raw_client.list_system_knowledge_graphs(
            proj_key=proj_key, term=term, request_options=request_options
        )
        return _response.data

    def get_all_kgs_admin(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[typing.Any]:
        """
        Get all kgs (only bag_key) for admin use.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system.get_all_kgs_admin()
        """
        _response = self._raw_client.get_all_kgs_admin(request_options=request_options)
        return _response.data

    def list_packages(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[CpsPackage]:
        """
        Get packages available in this CPS installation for installing in a project.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CpsPackage]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system.list_packages()
        """
        _response = self._raw_client.list_packages(request_options=request_options)
        return _response.data

    def get_all_dcs_admin(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Get all data catalogs (only dc_key) for admin use.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system.get_all_dcs_admin()
        """
        _response = self._raw_client.get_all_dcs_admin(request_options=request_options)
        return _response.data


class AsyncSystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemClient
        """
        return self._raw_client

    async def get_system_information(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemInfo:
        """
        Get system info.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system.get_system_information()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_system_information(request_options=request_options)
        return _response.data

    async def get_system_modules_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ModulesConfig:
        """
        Get modules configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModulesConfig
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system.get_system_modules_configuration()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_system_modules_configuration(request_options=request_options)
        return _response.data

    async def get_system_modules_tasks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get modules configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system.get_system_modules_tasks()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_system_modules_tasks(request_options=request_options)
        return _response.data

    async def list_system_knowledge_graphs(
        self,
        *,
        proj_key: typing.Optional[str] = None,
        term: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        List all Knowledge Graphs in the system.

        Parameters
        ----------
        proj_key : typing.Optional[str]

        term : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system.list_system_knowledge_graphs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_system_knowledge_graphs(
            proj_key=proj_key, term=term, request_options=request_options
        )
        return _response.data

    async def get_all_kgs_admin(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Any]:
        """
        Get all kgs (only bag_key) for admin use.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system.get_all_kgs_admin()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_kgs_admin(request_options=request_options)
        return _response.data

    async def list_packages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CpsPackage]:
        """
        Get packages available in this CPS installation for installing in a project.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CpsPackage]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system.list_packages()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_packages(request_options=request_options)
        return _response.data

    async def get_all_dcs_admin(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Get all data catalogs (only dc_key) for admin use.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system.get_all_dcs_admin()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_dcs_admin(request_options=request_options)
        return _response.data
