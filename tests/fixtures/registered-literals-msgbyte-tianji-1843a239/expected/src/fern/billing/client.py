

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBillingClient, RawBillingClient
from .types.billing_credit_bills_response import BillingCreditBillsResponse
from .types.billing_credit_checkout_response import BillingCreditCheckoutResponse
from .types.billing_credit_packs_response_item import BillingCreditPacksResponseItem
from .types.billing_credit_response import BillingCreditResponse
from .types.billing_current_subscription_response import BillingCurrentSubscriptionResponse
from .types.billing_current_tier_response import BillingCurrentTierResponse
from .types.billing_limit_response import BillingLimitResponse
from .types.billing_usage_response import BillingUsageResponse


OMIT = typing.cast(typing.Any, ...)


class BillingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBillingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBillingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBillingClient
        """
        return self._raw_client

    def usage(
        self,
        *,
        workspace_id: str,
        start_at: float,
        end_at: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BillingUsageResponse:
        """
        get workspace usage

        Parameters
        ----------
        workspace_id : str

        start_at : float

        end_at : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingUsageResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.usage(
            workspace_id="workspaceId",
            start_at=1.1,
            end_at=1.1,
        )
        """
        _response = self._raw_client.usage(
            workspace_id=workspace_id, start_at=start_at, end_at=end_at, request_options=request_options
        )
        return _response.data

    def limit(
        self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BillingLimitResponse:
        """
        get workspace subscription limit

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingLimitResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.limit(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.limit(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    def currenttier(
        self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BillingCurrentTierResponse:
        """
        get workspace current tier

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingCurrentTierResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.currenttier(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.currenttier(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    def currentsubscription(
        self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[BillingCurrentSubscriptionResponse]:
        """
        get workspace current subscription

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[BillingCurrentSubscriptionResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.currentsubscription(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.currentsubscription(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    def credit(
        self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BillingCreditResponse:
        """
        get workspace credit balance

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingCreditResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.credit(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.credit(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    def creditbills(
        self,
        *,
        workspace_id: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BillingCreditBillsResponse:
        """
        list workspace credit bills

        Parameters
        ----------
        workspace_id : str

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingCreditBillsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.creditbills(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.creditbills(
            workspace_id=workspace_id, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def creditpacks(
        self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BillingCreditPacksResponseItem]:
        """
        list available credit packs

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BillingCreditPacksResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.creditpacks(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.creditpacks(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    def creditcheckout(
        self,
        *,
        workspace_id: str,
        pack_id: str,
        redirect_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BillingCreditCheckoutResponse:
        """
        create credit checkout session

        Parameters
        ----------
        workspace_id : str

        pack_id : str

        redirect_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingCreditCheckoutResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.creditcheckout(
            workspace_id="workspaceId",
            pack_id="packId",
        )
        """
        _response = self._raw_client.creditcheckout(
            workspace_id=workspace_id, pack_id=pack_id, redirect_url=redirect_url, request_options=request_options
        )
        return _response.data


class AsyncBillingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBillingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBillingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBillingClient
        """
        return self._raw_client

    async def usage(
        self,
        *,
        workspace_id: str,
        start_at: float,
        end_at: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BillingUsageResponse:
        """
        get workspace usage

        Parameters
        ----------
        workspace_id : str

        start_at : float

        end_at : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingUsageResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.usage(
                workspace_id="workspaceId",
                start_at=1.1,
                end_at=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.usage(
            workspace_id=workspace_id, start_at=start_at, end_at=end_at, request_options=request_options
        )
        return _response.data

    async def limit(
        self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BillingLimitResponse:
        """
        get workspace subscription limit

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingLimitResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.limit(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.limit(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    async def currenttier(
        self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BillingCurrentTierResponse:
        """
        get workspace current tier

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingCurrentTierResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.currenttier(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.currenttier(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    async def currentsubscription(
        self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[BillingCurrentSubscriptionResponse]:
        """
        get workspace current subscription

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[BillingCurrentSubscriptionResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.currentsubscription(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.currentsubscription(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def credit(
        self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BillingCreditResponse:
        """
        get workspace credit balance

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingCreditResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.credit(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.credit(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    async def creditbills(
        self,
        *,
        workspace_id: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BillingCreditBillsResponse:
        """
        list workspace credit bills

        Parameters
        ----------
        workspace_id : str

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingCreditBillsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.creditbills(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creditbills(
            workspace_id=workspace_id, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def creditpacks(
        self, *, workspace_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BillingCreditPacksResponseItem]:
        """
        list available credit packs

        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BillingCreditPacksResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.creditpacks(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creditpacks(workspace_id=workspace_id, request_options=request_options)
        return _response.data

    async def creditcheckout(
        self,
        *,
        workspace_id: str,
        pack_id: str,
        redirect_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BillingCreditCheckoutResponse:
        """
        create credit checkout session

        Parameters
        ----------
        workspace_id : str

        pack_id : str

        redirect_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillingCreditCheckoutResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.creditcheckout(
                workspace_id="workspaceId",
                pack_id="packId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creditcheckout(
            workspace_id=workspace_id, pack_id=pack_id, redirect_url=redirect_url, request_options=request_options
        )
        return _response.data
