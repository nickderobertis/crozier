

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.domain import Domain
from ..types.paginated_domains_response import PaginatedDomainsResponse
from ..types.success_response import SuccessResponse
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

    def get_domains(
        self,
        account_id: str,
        *,
        dns_valid: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDomainsResponse:
        """
        Returns a list of domains for the account

        Parameters
        ----------
        account_id : str
            Account ID

        dns_valid : typing.Optional[bool]
            Filter results by DNS validation status

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDomainsResponse
            List of domains

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.domains.get_domains(
            account_id="account_id",
        )
        """
        _response = self._raw_client.get_domains(
            account_id, dns_valid=dns_valid, limit=limit, after=after, before=before, request_options=request_options
        )
        return _response.data

    def create_domain(
        self,
        account_id: str,
        *,
        domain: str,
        idempotency_key: typing.Optional[str] = None,
        dkim_private_key: typing.Optional[str] = OMIT,
        tracking_subdomain: typing.Optional[str] = OMIT,
        return_path_subdomain: typing.Optional[str] = OMIT,
        subscription_subdomain: typing.Optional[str] = OMIT,
        media_subdomain: typing.Optional[str] = OMIT,
        dkim_rotation_interval_days: typing.Optional[int] = OMIT,
        dkim_selector: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Domain:
        """
        Creates a new domain

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Fully qualified domain name

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        dkim_private_key : typing.Optional[str]
            DKIM Private Key for the domain. Only RSA keys with a minimum key size of 1024 bits are supported.

            **Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.

            <Note>Key size of at least 1024 bits is supported; 2048 bit keys are strongly recommended for improved security.</Note>

        tracking_subdomain : typing.Optional[str]
            Optional custom tracking subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        return_path_subdomain : typing.Optional[str]
            Optional custom return-path subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        subscription_subdomain : typing.Optional[str]
            Optional custom subscription management subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        media_subdomain : typing.Optional[str]
            Optional custom media subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        dkim_rotation_interval_days : typing.Optional[int]
            Optional custom DKIM rotation interval in days. Only supported for managed DNS domains on eligible plans.

        dkim_selector : typing.Optional[str]
            Optional custom DKIM selector for the domain. Omit, send null, or send an empty or whitespace-only string to use the default selector (no per-domain override); the value is trimmed before it is interpreted, so whitespace-only input is treated as empty.

            When provided, it is normalized to lowercase and must be a single DNS label: 1-62 characters using lowercase letters, numbers, and hyphens only, without a leading or trailing hyphen.

            **Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Domain
            Domain created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.domains.create_domain(
            account_id="account_id",
            idempotency_key="user-12345-create-domain-20240101",
            domain="example.com",
            tracking_subdomain="click",
            return_path_subdomain="mail",
            subscription_subdomain="preferences",
            media_subdomain="media",
            dkim_rotation_interval_days=45,
        )
        """
        _response = self._raw_client.create_domain(
            account_id,
            domain=domain,
            idempotency_key=idempotency_key,
            dkim_private_key=dkim_private_key,
            tracking_subdomain=tracking_subdomain,
            return_path_subdomain=return_path_subdomain,
            subscription_subdomain=subscription_subdomain,
            media_subdomain=media_subdomain,
            dkim_rotation_interval_days=dkim_rotation_interval_days,
            dkim_selector=dkim_selector,
            request_options=request_options,
        )
        return _response.data

    def get_domain(
        self, account_id: str, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Domain:
        """
        Returns a specific domain by name

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Domain
            Domain details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.domains.get_domain(
            account_id="account_id",
            domain="domain",
        )
        """
        _response = self._raw_client.get_domain(account_id, domain, request_options=request_options)
        return _response.data

    def update_domain(
        self,
        account_id: str,
        domain: str,
        *,
        tracking_subdomain: typing.Optional[str] = OMIT,
        return_path_subdomain: typing.Optional[str] = OMIT,
        subscription_subdomain: typing.Optional[str] = OMIT,
        media_subdomain: typing.Optional[str] = OMIT,
        dkim_rotation_interval_days: typing.Optional[int] = OMIT,
        dkim_selector: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Domain:
        """
        Updates DNS domain settings such as custom subdomains and DKIM rotation interval.

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        tracking_subdomain : typing.Optional[str]
            Optional custom tracking subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        return_path_subdomain : typing.Optional[str]
            Optional custom return-path subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        subscription_subdomain : typing.Optional[str]
            Optional custom subscription management subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        media_subdomain : typing.Optional[str]
            Optional custom media subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        dkim_rotation_interval_days : typing.Optional[int]
            Optional custom DKIM rotation interval in days. Omit to leave the current value unchanged. Only supported for managed DNS domains on eligible plans.

        dkim_selector : typing.Optional[str]
            Optional custom DKIM selector for the domain. Omit or send null to leave the current value unchanged; send an empty or whitespace-only string to clear the override and revert to the default selector. The value is trimmed before it is interpreted, so whitespace-only input clears the override just like an empty string.

            When provided, it is normalized to lowercase and must be a single DNS label: 1-62 characters using lowercase letters, numbers, and hyphens only, without a leading or trailing hyphen. It cannot be changed once the selector locks after DNS verification or while a DKIM key rotation is in progress.

            **Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Domain
            Domain updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.domains.update_domain(
            account_id="account_id",
            domain="domain",
            tracking_subdomain="click",
            return_path_subdomain="mail",
            subscription_subdomain="preferences",
            media_subdomain="media",
            dkim_rotation_interval_days=45,
        )
        """
        _response = self._raw_client.update_domain(
            account_id,
            domain,
            tracking_subdomain=tracking_subdomain,
            return_path_subdomain=return_path_subdomain,
            subscription_subdomain=subscription_subdomain,
            media_subdomain=media_subdomain,
            dkim_rotation_interval_days=dkim_rotation_interval_days,
            dkim_selector=dkim_selector,
            request_options=request_options,
        )
        return _response.data

    def delete_domain(
        self, account_id: str, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Deletes a domain

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Domain deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.domains.delete_domain(
            account_id="account_id",
            domain="domain",
        )
        """
        _response = self._raw_client.delete_domain(account_id, domain, request_options=request_options)
        return _response.data

    def check_domain_dns(
        self, account_id: str, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Domain:
        """
        Triggers a DNS validation check for the domain. If the domain was checked within the last 60 seconds, the cached validation result is returned instead of performing a fresh lookup.

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Domain
            Domain DNS status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.domains.check_domain_dns(
            account_id="account_id",
            domain="domain",
        )
        """
        _response = self._raw_client.check_domain_dns(account_id, domain, request_options=request_options)
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

    async def get_domains(
        self,
        account_id: str,
        *,
        dns_valid: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDomainsResponse:
        """
        Returns a list of domains for the account

        Parameters
        ----------
        account_id : str
            Account ID

        dns_valid : typing.Optional[bool]
            Filter results by DNS validation status

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDomainsResponse
            List of domains

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.domains.get_domains(
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_domains(
            account_id, dns_valid=dns_valid, limit=limit, after=after, before=before, request_options=request_options
        )
        return _response.data

    async def create_domain(
        self,
        account_id: str,
        *,
        domain: str,
        idempotency_key: typing.Optional[str] = None,
        dkim_private_key: typing.Optional[str] = OMIT,
        tracking_subdomain: typing.Optional[str] = OMIT,
        return_path_subdomain: typing.Optional[str] = OMIT,
        subscription_subdomain: typing.Optional[str] = OMIT,
        media_subdomain: typing.Optional[str] = OMIT,
        dkim_rotation_interval_days: typing.Optional[int] = OMIT,
        dkim_selector: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Domain:
        """
        Creates a new domain

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Fully qualified domain name

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        dkim_private_key : typing.Optional[str]
            DKIM Private Key for the domain. Only RSA keys with a minimum key size of 1024 bits are supported.

            **Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.

            <Note>Key size of at least 1024 bits is supported; 2048 bit keys are strongly recommended for improved security.</Note>

        tracking_subdomain : typing.Optional[str]
            Optional custom tracking subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        return_path_subdomain : typing.Optional[str]
            Optional custom return-path subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        subscription_subdomain : typing.Optional[str]
            Optional custom subscription management subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        media_subdomain : typing.Optional[str]
            Optional custom media subdomain. Omit to use the default on create. Applies to both manual-DNS and managed-DNS domains.

        dkim_rotation_interval_days : typing.Optional[int]
            Optional custom DKIM rotation interval in days. Only supported for managed DNS domains on eligible plans.

        dkim_selector : typing.Optional[str]
            Optional custom DKIM selector for the domain. Omit, send null, or send an empty or whitespace-only string to use the default selector (no per-domain override); the value is trimmed before it is interpreted, so whitespace-only input is treated as empty.

            When provided, it is normalized to lowercase and must be a single DNS label: 1-62 characters using lowercase letters, numbers, and hyphens only, without a leading or trailing hyphen.

            **Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Domain
            Domain created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.domains.create_domain(
                account_id="account_id",
                idempotency_key="user-12345-create-domain-20240101",
                domain="example.com",
                tracking_subdomain="click",
                return_path_subdomain="mail",
                subscription_subdomain="preferences",
                media_subdomain="media",
                dkim_rotation_interval_days=45,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_domain(
            account_id,
            domain=domain,
            idempotency_key=idempotency_key,
            dkim_private_key=dkim_private_key,
            tracking_subdomain=tracking_subdomain,
            return_path_subdomain=return_path_subdomain,
            subscription_subdomain=subscription_subdomain,
            media_subdomain=media_subdomain,
            dkim_rotation_interval_days=dkim_rotation_interval_days,
            dkim_selector=dkim_selector,
            request_options=request_options,
        )
        return _response.data

    async def get_domain(
        self, account_id: str, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Domain:
        """
        Returns a specific domain by name

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Domain
            Domain details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.domains.get_domain(
                account_id="account_id",
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_domain(account_id, domain, request_options=request_options)
        return _response.data

    async def update_domain(
        self,
        account_id: str,
        domain: str,
        *,
        tracking_subdomain: typing.Optional[str] = OMIT,
        return_path_subdomain: typing.Optional[str] = OMIT,
        subscription_subdomain: typing.Optional[str] = OMIT,
        media_subdomain: typing.Optional[str] = OMIT,
        dkim_rotation_interval_days: typing.Optional[int] = OMIT,
        dkim_selector: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Domain:
        """
        Updates DNS domain settings such as custom subdomains and DKIM rotation interval.

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        tracking_subdomain : typing.Optional[str]
            Optional custom tracking subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        return_path_subdomain : typing.Optional[str]
            Optional custom return-path subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        subscription_subdomain : typing.Optional[str]
            Optional custom subscription management subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        media_subdomain : typing.Optional[str]
            Optional custom media subdomain. Omit to leave the current value unchanged. Applies to both manual-DNS and managed-DNS domains.

        dkim_rotation_interval_days : typing.Optional[int]
            Optional custom DKIM rotation interval in days. Omit to leave the current value unchanged. Only supported for managed DNS domains on eligible plans.

        dkim_selector : typing.Optional[str]
            Optional custom DKIM selector for the domain. Omit or send null to leave the current value unchanged; send an empty or whitespace-only string to clear the override and revert to the default selector. The value is trimmed before it is interpreted, so whitespace-only input clears the override just like an empty string.

            When provided, it is normalized to lowercase and must be a single DNS label: 1-62 characters using lowercase letters, numbers, and hyphens only, without a leading or trailing hyphen. It cannot be changed once the selector locks after DNS verification or while a DKIM key rotation is in progress.

            **Note:** This parameter is only supported on [Platform Partner](https://ahasend.com/partners) accounts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Domain
            Domain updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.domains.update_domain(
                account_id="account_id",
                domain="domain",
                tracking_subdomain="click",
                return_path_subdomain="mail",
                subscription_subdomain="preferences",
                media_subdomain="media",
                dkim_rotation_interval_days=45,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_domain(
            account_id,
            domain,
            tracking_subdomain=tracking_subdomain,
            return_path_subdomain=return_path_subdomain,
            subscription_subdomain=subscription_subdomain,
            media_subdomain=media_subdomain,
            dkim_rotation_interval_days=dkim_rotation_interval_days,
            dkim_selector=dkim_selector,
            request_options=request_options,
        )
        return _response.data

    async def delete_domain(
        self, account_id: str, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Deletes a domain

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Domain deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.domains.delete_domain(
                account_id="account_id",
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_domain(account_id, domain, request_options=request_options)
        return _response.data

    async def check_domain_dns(
        self, account_id: str, domain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Domain:
        """
        Triggers a DNS validation check for the domain. If the domain was checked within the last 60 seconds, the cached validation result is returned instead of performing a fresh lookup.

        Parameters
        ----------
        account_id : str
            Account ID

        domain : str
            Domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Domain
            Domain DNS status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.domains.check_domain_dns(
                account_id="account_id",
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_domain_dns(account_id, domain, request_options=request_options)
        return _response.data
