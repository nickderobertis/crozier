

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.flavours_default_quota import FlavoursDefaultQuota
from ..types.flavours_quota import FlavoursQuota
from ..types.project_flavour_total_kgs import ProjectFlavourTotalKgs
from ..types.project_flavours_quota import ProjectFlavoursQuota
from .raw_client import AsyncRawSystemQuotasClient, RawSystemQuotasClient


OMIT = typing.cast(typing.Any, ...)


class SystemQuotasClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemQuotasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemQuotasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemQuotasClient
        """
        return self._raw_client

    def get_flavours_default_quotas(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FlavoursDefaultQuota]:
        """
        Get flavours default values.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FlavoursDefaultQuota]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_quotas.get_flavours_default_quotas()
        """
        _response = self._raw_client.get_flavours_default_quotas(request_options=request_options)
        return _response.data

    def save_flavours_default_quotas(
        self, *, request: typing.Sequence[FlavoursDefaultQuota], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FlavoursDefaultQuota]:
        """
        Save flavours default quota.

        Parameters
        ----------
        request : typing.Sequence[FlavoursDefaultQuota]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FlavoursDefaultQuota]
            Successful Response

        Examples
        --------
        from fern import FernApi, FlavoursDefaultQuota

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_quotas.save_flavours_default_quotas(
            request=[
                FlavoursDefaultQuota(
                    display_name="display_name",
                    name="name",
                    default_quota=1,
                )
            ],
        )
        """
        _response = self._raw_client.save_flavours_default_quotas(request=request, request_options=request_options)
        return _response.data

    def get_projects_flavours_quota(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ProjectFlavoursQuota]:
        """
        Get projects flavours quotas.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProjectFlavoursQuota]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_quotas.get_projects_flavours_quota()
        """
        _response = self._raw_client.get_projects_flavours_quota(request_options=request_options)
        return _response.data

    def save_project_flavours_quota(
        self,
        *,
        name: str,
        proj_key: str,
        quotas: typing.Sequence[FlavoursQuota],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Save project flavours quota.

        Parameters
        ----------
        name : str

        proj_key : str

        quotas : typing.Sequence[FlavoursQuota]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, FlavoursQuota

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_quotas.save_project_flavours_quota(
            name="name",
            proj_key="proj_key",
            quotas=[
                FlavoursQuota(
                    display_name="display_name",
                    name="name",
                    quota=1,
                )
            ],
        )
        """
        _response = self._raw_client.save_project_flavours_quota(
            name=name, proj_key=proj_key, quotas=quotas, request_options=request_options
        )
        return _response.data

    def get_project_flavours_quota(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FlavoursQuota]:
        """
        Get project flavours quota.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FlavoursQuota]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_quotas.get_project_flavours_quota(
            proj_key="proj_key",
        )
        """
        _response = self._raw_client.get_project_flavours_quota(proj_key, request_options=request_options)
        return _response.data

    def get_project_flavour_total_kgs(
        self, proj_key: str, flavour_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectFlavourTotalKgs:
        """
        Gets kg total number by proj_key and flavour_key.

        Parameters
        ----------
        proj_key : str

        flavour_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectFlavourTotalKgs
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.system_quotas.get_project_flavour_total_kgs(
            proj_key="proj_key",
            flavour_name="flavour_name",
        )
        """
        _response = self._raw_client.get_project_flavour_total_kgs(
            proj_key, flavour_name, request_options=request_options
        )
        return _response.data


class AsyncSystemQuotasClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemQuotasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemQuotasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemQuotasClient
        """
        return self._raw_client

    async def get_flavours_default_quotas(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FlavoursDefaultQuota]:
        """
        Get flavours default values.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FlavoursDefaultQuota]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_quotas.get_flavours_default_quotas()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flavours_default_quotas(request_options=request_options)
        return _response.data

    async def save_flavours_default_quotas(
        self, *, request: typing.Sequence[FlavoursDefaultQuota], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FlavoursDefaultQuota]:
        """
        Save flavours default quota.

        Parameters
        ----------
        request : typing.Sequence[FlavoursDefaultQuota]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FlavoursDefaultQuota]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FlavoursDefaultQuota

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_quotas.save_flavours_default_quotas(
                request=[
                    FlavoursDefaultQuota(
                        display_name="display_name",
                        name="name",
                        default_quota=1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_flavours_default_quotas(
            request=request, request_options=request_options
        )
        return _response.data

    async def get_projects_flavours_quota(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ProjectFlavoursQuota]:
        """
        Get projects flavours quotas.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ProjectFlavoursQuota]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_quotas.get_projects_flavours_quota()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_projects_flavours_quota(request_options=request_options)
        return _response.data

    async def save_project_flavours_quota(
        self,
        *,
        name: str,
        proj_key: str,
        quotas: typing.Sequence[FlavoursQuota],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Save project flavours quota.

        Parameters
        ----------
        name : str

        proj_key : str

        quotas : typing.Sequence[FlavoursQuota]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FlavoursQuota

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_quotas.save_project_flavours_quota(
                name="name",
                proj_key="proj_key",
                quotas=[
                    FlavoursQuota(
                        display_name="display_name",
                        name="name",
                        quota=1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_project_flavours_quota(
            name=name, proj_key=proj_key, quotas=quotas, request_options=request_options
        )
        return _response.data

    async def get_project_flavours_quota(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FlavoursQuota]:
        """
        Get project flavours quota.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FlavoursQuota]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_quotas.get_project_flavours_quota(
                proj_key="proj_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_flavours_quota(proj_key, request_options=request_options)
        return _response.data

    async def get_project_flavour_total_kgs(
        self, proj_key: str, flavour_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectFlavourTotalKgs:
        """
        Gets kg total number by proj_key and flavour_key.

        Parameters
        ----------
        proj_key : str

        flavour_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectFlavourTotalKgs
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.system_quotas.get_project_flavour_total_kgs(
                proj_key="proj_key",
                flavour_name="flavour_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_flavour_total_kgs(
            proj_key, flavour_name, request_options=request_options
        )
        return _response.data
