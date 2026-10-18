

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.activate_vanity_subdomain_response_output import ActivateVanitySubdomainResponseOutput
from ..types.subdomain_availability_response_output import SubdomainAvailabilityResponseOutput
from ..types.update_custom_hostname_response_output import UpdateCustomHostnameResponseOutput
from ..types.vanity_subdomain_config_response_output import VanitySubdomainConfigResponseOutput
from .raw_client import AsyncRawDomainsClient, RawDomainsClient


OMIT = typing.cast(typing.Any, ...)


class DomainsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDomainsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDomainsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDomainsClient
        """
        return self._raw_client

    def v1get_hostname_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateCustomHostnameResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomHostnameResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.domains.v1get_hostname_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_hostname_config(ref, request_options=request_options)
        return _response.data

    def v1delete_hostname_config(
        self,
        ref: str,
        *,
        remove_addon: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        remove_addon : typing.Optional[str]
            If true, also removes the custom domain add-on from the project subscription.

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
        client.domains.v1delete_hostname_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1delete_hostname_config(
            ref, remove_addon=remove_addon, request_options=request_options
        )
        return _response.data

    def v1update_hostname_config(
        self, ref: str, *, custom_hostname: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateCustomHostnameResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        custom_hostname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomHostnameResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.domains.v1update_hostname_config(
            ref="abcdefghijklmnopqrst",
            custom_hostname="docs.example.com",
        )
        """
        _response = self._raw_client.v1update_hostname_config(
            ref, custom_hostname=custom_hostname, request_options=request_options
        )
        return _response.data

    def v1verify_dns_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateCustomHostnameResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomHostnameResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.domains.v1verify_dns_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1verify_dns_config(ref, request_options=request_options)
        return _response.data

    def v1activate_custom_hostname(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateCustomHostnameResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomHostnameResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.domains.v1activate_custom_hostname(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1activate_custom_hostname(ref, request_options=request_options)
        return _response.data

    def v1get_vanity_subdomain_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VanitySubdomainConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VanitySubdomainConfigResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.domains.v1get_vanity_subdomain_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_vanity_subdomain_config(ref, request_options=request_options)
        return _response.data

    def v1deactivate_vanity_subdomain_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
        client.domains.v1deactivate_vanity_subdomain_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1deactivate_vanity_subdomain_config(ref, request_options=request_options)
        return _response.data

    def v1check_vanity_subdomain_availability(
        self, ref: str, *, vanity_subdomain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SubdomainAvailabilityResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        vanity_subdomain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubdomainAvailabilityResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.domains.v1check_vanity_subdomain_availability(
            ref="abcdefghijklmnopqrst",
            vanity_subdomain="acme-prod",
        )
        """
        _response = self._raw_client.v1check_vanity_subdomain_availability(
            ref, vanity_subdomain=vanity_subdomain, request_options=request_options
        )
        return _response.data

    def v1activate_vanity_subdomain_config(
        self, ref: str, *, vanity_subdomain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ActivateVanitySubdomainResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        vanity_subdomain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActivateVanitySubdomainResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.domains.v1activate_vanity_subdomain_config(
            ref="abcdefghijklmnopqrst",
            vanity_subdomain="acme-prod",
        )
        """
        _response = self._raw_client.v1activate_vanity_subdomain_config(
            ref, vanity_subdomain=vanity_subdomain, request_options=request_options
        )
        return _response.data


class AsyncDomainsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDomainsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDomainsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDomainsClient
        """
        return self._raw_client

    async def v1get_hostname_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateCustomHostnameResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomHostnameResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.domains.v1get_hostname_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_hostname_config(ref, request_options=request_options)
        return _response.data

    async def v1delete_hostname_config(
        self,
        ref: str,
        *,
        remove_addon: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        remove_addon : typing.Optional[str]
            If true, also removes the custom domain add-on from the project subscription.

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
            await client.domains.v1delete_hostname_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1delete_hostname_config(
            ref, remove_addon=remove_addon, request_options=request_options
        )
        return _response.data

    async def v1update_hostname_config(
        self, ref: str, *, custom_hostname: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateCustomHostnameResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        custom_hostname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomHostnameResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.domains.v1update_hostname_config(
                ref="abcdefghijklmnopqrst",
                custom_hostname="docs.example.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_hostname_config(
            ref, custom_hostname=custom_hostname, request_options=request_options
        )
        return _response.data

    async def v1verify_dns_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateCustomHostnameResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomHostnameResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.domains.v1verify_dns_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1verify_dns_config(ref, request_options=request_options)
        return _response.data

    async def v1activate_custom_hostname(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateCustomHostnameResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomHostnameResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.domains.v1activate_custom_hostname(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1activate_custom_hostname(ref, request_options=request_options)
        return _response.data

    async def v1get_vanity_subdomain_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VanitySubdomainConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VanitySubdomainConfigResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.domains.v1get_vanity_subdomain_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_vanity_subdomain_config(ref, request_options=request_options)
        return _response.data

    async def v1deactivate_vanity_subdomain_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
            await client.domains.v1deactivate_vanity_subdomain_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1deactivate_vanity_subdomain_config(ref, request_options=request_options)
        return _response.data

    async def v1check_vanity_subdomain_availability(
        self, ref: str, *, vanity_subdomain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SubdomainAvailabilityResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        vanity_subdomain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubdomainAvailabilityResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.domains.v1check_vanity_subdomain_availability(
                ref="abcdefghijklmnopqrst",
                vanity_subdomain="acme-prod",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1check_vanity_subdomain_availability(
            ref, vanity_subdomain=vanity_subdomain, request_options=request_options
        )
        return _response.data

    async def v1activate_vanity_subdomain_config(
        self, ref: str, *, vanity_subdomain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ActivateVanitySubdomainResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        vanity_subdomain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActivateVanitySubdomainResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.domains.v1activate_vanity_subdomain_config(
                ref="abcdefghijklmnopqrst",
                vanity_subdomain="acme-prod",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1activate_vanity_subdomain_config(
            ref, vanity_subdomain=vanity_subdomain, request_options=request_options
        )
        return _response.data
