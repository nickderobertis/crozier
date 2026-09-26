

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bag_flavour_full_data import BagFlavourFullData
from ..types.flavour import Flavour
from ..types.list_project_flavours import ListProjectFlavours
from ..types.projects_flavours import ProjectsFlavours
from .raw_client import AsyncRawSystemFlavoursClient, RawSystemFlavoursClient


OMIT = typing.cast(typing.Any, ...)


class SystemFlavoursClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemFlavoursClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemFlavoursClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemFlavoursClient
        """
        return self._raw_client

    def list_all_flavours(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BagFlavourFullData]:
        """
        Get all KG flavours storage on db.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BagFlavourFullData]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_flavours.list_all_flavours()
        """
        _response = self._raw_client.list_all_flavours(request_options=request_options)
        return _response.data

    def get_flavour(
        self, flavour_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BagFlavourFullData:
        """
        Get flavour from db.

        Parameters
        ----------
        flavour_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BagFlavourFullData
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_flavours.get_flavour(
            flavour_name="flavour_name",
        )
        """
        _response = self._raw_client.get_flavour(flavour_name, request_options=request_options)
        return _response.data

    def save_flavour(
        self,
        *,
        new_flavour: bool,
        backend: str,
        config: typing.Dict[str, typing.Any],
        description: str,
        display_name: str,
        name: str,
        project_specific: bool,
        default_quota: typing.Optional[int] = OMIT,
        is_from_deployment: typing.Optional[bool] = OMIT,
        order: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Save flavour on db.

        Parameters
        ----------
        new_flavour : bool

        backend : str

        config : typing.Dict[str, typing.Any]

        description : str

        display_name : str

        name : str

        project_specific : bool

        default_quota : typing.Optional[int]

        is_from_deployment : typing.Optional[bool]

        order : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_flavours.save_flavour(
            new_flavour=True,
            backend="backend",
            config={"key": "value"},
            description="description",
            display_name="display_name",
            name="name",
            project_specific=True,
        )
        """
        _response = self._raw_client.save_flavour(
            new_flavour=new_flavour,
            backend=backend,
            config=config,
            description=description,
            display_name=display_name,
            name=name,
            project_specific=project_specific,
            default_quota=default_quota,
            is_from_deployment=is_from_deployment,
            order=order,
            request_options=request_options,
        )
        return _response.data

    def delete_flavour(
        self, flavour_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete flavour from db.

        Parameters
        ----------
        flavour_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_flavours.delete_flavour(
            flavour_name="flavour_name",
        )
        """
        _response = self._raw_client.delete_flavour(flavour_name, request_options=request_options)
        return _response.data

    def list_projects_flavours(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ProjectsFlavours]:
        """
        Get all projects and their flavours.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProjectsFlavours]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_flavours.list_projects_flavours()
        """
        _response = self._raw_client.list_projects_flavours(request_options=request_options)
        return _response.data

    def save_project_flavours(
        self,
        *,
        proj_key: str,
        name: str,
        flavours: typing.Sequence[Flavour],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Save project flavours assignment on db.

        Parameters
        ----------
        proj_key : str

        name : str

        flavours : typing.Sequence[Flavour]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, Flavour

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_flavours.save_project_flavours(
            proj_key="proj_key",
            name="name",
            flavours=[
                Flavour(
                    name="name",
                )
            ],
        )
        """
        _response = self._raw_client.save_project_flavours(
            proj_key=proj_key, name=name, flavours=flavours, request_options=request_options
        )
        return _response.data

    def list_flavours_by_project(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListProjectFlavours:
        """
        Get project assignment flavours.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProjectFlavours
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_flavours.list_flavours_by_project(
            proj_key="proj_key",
        )
        """
        _response = self._raw_client.list_flavours_by_project(proj_key, request_options=request_options)
        return _response.data


class AsyncSystemFlavoursClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemFlavoursClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemFlavoursClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemFlavoursClient
        """
        return self._raw_client

    async def list_all_flavours(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BagFlavourFullData]:
        """
        Get all KG flavours storage on db.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BagFlavourFullData]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_flavours.list_all_flavours()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_flavours(request_options=request_options)
        return _response.data

    async def get_flavour(
        self, flavour_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BagFlavourFullData:
        """
        Get flavour from db.

        Parameters
        ----------
        flavour_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BagFlavourFullData
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_flavours.get_flavour(
                flavour_name="flavour_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flavour(flavour_name, request_options=request_options)
        return _response.data

    async def save_flavour(
        self,
        *,
        new_flavour: bool,
        backend: str,
        config: typing.Dict[str, typing.Any],
        description: str,
        display_name: str,
        name: str,
        project_specific: bool,
        default_quota: typing.Optional[int] = OMIT,
        is_from_deployment: typing.Optional[bool] = OMIT,
        order: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Save flavour on db.

        Parameters
        ----------
        new_flavour : bool

        backend : str

        config : typing.Dict[str, typing.Any]

        description : str

        display_name : str

        name : str

        project_specific : bool

        default_quota : typing.Optional[int]

        is_from_deployment : typing.Optional[bool]

        order : typing.Optional[int]

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

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_flavours.save_flavour(
                new_flavour=True,
                backend="backend",
                config={"key": "value"},
                description="description",
                display_name="display_name",
                name="name",
                project_specific=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_flavour(
            new_flavour=new_flavour,
            backend=backend,
            config=config,
            description=description,
            display_name=display_name,
            name=name,
            project_specific=project_specific,
            default_quota=default_quota,
            is_from_deployment=is_from_deployment,
            order=order,
            request_options=request_options,
        )
        return _response.data

    async def delete_flavour(
        self, flavour_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete flavour from db.

        Parameters
        ----------
        flavour_name : str

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

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_flavours.delete_flavour(
                flavour_name="flavour_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_flavour(flavour_name, request_options=request_options)
        return _response.data

    async def list_projects_flavours(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ProjectsFlavours]:
        """
        Get all projects and their flavours.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProjectsFlavours]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_flavours.list_projects_flavours()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_projects_flavours(request_options=request_options)
        return _response.data

    async def save_project_flavours(
        self,
        *,
        proj_key: str,
        name: str,
        flavours: typing.Sequence[Flavour],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Save project flavours assignment on db.

        Parameters
        ----------
        proj_key : str

        name : str

        flavours : typing.Sequence[Flavour]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Flavour

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_flavours.save_project_flavours(
                proj_key="proj_key",
                name="name",
                flavours=[
                    Flavour(
                        name="name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_project_flavours(
            proj_key=proj_key, name=name, flavours=flavours, request_options=request_options
        )
        return _response.data

    async def list_flavours_by_project(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListProjectFlavours:
        """
        Get project assignment flavours.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProjectFlavours
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_flavours.list_flavours_by_project(
                proj_key="proj_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_flavours_by_project(proj_key, request_options=request_options)
        return _response.data
