

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_entry import AccessEntry
from .raw_client import AsyncRawAccessClient, RawAccessClient


class AccessClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccessClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccessClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccessClient
        """
        return self._raw_client

    def add(self, user: str, agents: str, mask: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Adds/Overwrites the user entry in the access control database.

        Parameters
        ----------
        user : str
            Username of the simulator hosting system

        agents : str
            Agent range in minimal range representation

        mask : str
            Currently not used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access.add(
            user="user",
            agents="agents",
            mask="mask",
        )
        """
        _response = self._raw_client.add(user, agents, mask, request_options=request_options)
        return _response.data

    def del_(self, user: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Using '*' for user clears all the users.

        Parameters
        ----------
        user : str
            username of the simulator hosting system

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access.del_(
            user="user",
        )
        """
        _response = self._raw_client.del_(user, request_options=request_options)
        return _response.data

    def get_acldb(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        If nothing is specified then this returns "".

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access.get_acldb()
        """
        _response = self._raw_client.get_acldb(request_options=request_options)
        return _response.data

    def get_admindir(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        If nothing is specified in admin/settings.cfg then returns "". If no admin directory is specified then the shared area will be used where needed (e.g. for persistent info, access control data files etc. )

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access.get_admindir()
        """
        _response = self._raw_client.get_admindir(request_options=request_options)
        return _response.data

    def get_adminuser(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        If nothing is specified in admin/settings.cfg then returns "".

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access.get_adminuser()
        """
        _response = self._raw_client.get_adminuser(request_options=request_options)
        return _response.data

    def get_enabled(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        0 indicates that it is disabled, 1 indicates it is enabled.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access.get_enabled()
        """
        _response = self._raw_client.get_enabled(request_options=request_options)
        return _response.data

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[AccessEntry]:
        """
        Each entry consists of user, agents (in minimal range representation) and access mask (not used currently).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AccessEntry]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def load(self, filename: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        If filename is not specified then the currently set 'acldb' parameter is used.

        Parameters
        ----------
        filename : str
            Filename to load

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access.load(
            filename="filename",
        )
        """
        _response = self._raw_client.load(filename, request_options=request_options)
        return _response.data

    def save(self, filename: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        If filename is not specified then the currently set 'acldb' parameter is used.

        Parameters
        ----------
        filename : str
            Filename to save

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access.save(
            filename="filename",
        )
        """
        _response = self._raw_client.save(filename, request_options=request_options)
        return _response.data

    def set_acldb(self, database_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        This will be used for subsequent load and save operations.

        Parameters
        ----------
        database_name : str
            Database name to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access.set_acldb(
            database_name="databaseName",
        )
        """
        _response = self._raw_client.set_acldb(database_name, request_options=request_options)
        return _response.data

    def set_enabled(self, enabled_or_not: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        0 indicates disabled, 1 indicates enabled.

        Parameters
        ----------
        enabled_or_not : str
            indicator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.access.set_enabled(
            enabled_or_not="enabledOrNot",
        )
        """
        _response = self._raw_client.set_enabled(enabled_or_not, request_options=request_options)
        return _response.data


class AsyncAccessClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccessClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccessClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccessClient
        """
        return self._raw_client

    async def add(
        self, user: str, agents: str, mask: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Adds/Overwrites the user entry in the access control database.

        Parameters
        ----------
        user : str
            Username of the simulator hosting system

        agents : str
            Agent range in minimal range representation

        mask : str
            Currently not used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access.add(
                user="user",
                agents="agents",
                mask="mask",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(user, agents, mask, request_options=request_options)
        return _response.data

    async def del_(self, user: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Using '*' for user clears all the users.

        Parameters
        ----------
        user : str
            username of the simulator hosting system

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access.del_(
                user="user",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.del_(user, request_options=request_options)
        return _response.data

    async def get_acldb(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        If nothing is specified then this returns "".

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access.get_acldb()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_acldb(request_options=request_options)
        return _response.data

    async def get_admindir(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        If nothing is specified in admin/settings.cfg then returns "". If no admin directory is specified then the shared area will be used where needed (e.g. for persistent info, access control data files etc. )

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access.get_admindir()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_admindir(request_options=request_options)
        return _response.data

    async def get_adminuser(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        If nothing is specified in admin/settings.cfg then returns "".

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access.get_adminuser()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_adminuser(request_options=request_options)
        return _response.data

    async def get_enabled(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        0 indicates that it is disabled, 1 indicates it is enabled.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access.get_enabled()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_enabled(request_options=request_options)
        return _response.data

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[AccessEntry]:
        """
        Each entry consists of user, agents (in minimal range representation) and access mask (not used currently).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AccessEntry]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def load(self, filename: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        If filename is not specified then the currently set 'acldb' parameter is used.

        Parameters
        ----------
        filename : str
            Filename to load

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access.load(
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.load(filename, request_options=request_options)
        return _response.data

    async def save(self, filename: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        If filename is not specified then the currently set 'acldb' parameter is used.

        Parameters
        ----------
        filename : str
            Filename to save

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access.save(
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save(filename, request_options=request_options)
        return _response.data

    async def set_acldb(self, database_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        This will be used for subsequent load and save operations.

        Parameters
        ----------
        database_name : str
            Database name to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access.set_acldb(
                database_name="databaseName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_acldb(database_name, request_options=request_options)
        return _response.data

    async def set_enabled(self, enabled_or_not: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        0 indicates disabled, 1 indicates enabled.

        Parameters
        ----------
        enabled_or_not : str
            indicator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.access.set_enabled(
                enabled_or_not="enabledOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_enabled(enabled_or_not, request_options=request_options)
        return _response.data
