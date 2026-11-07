

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bill_summary import BillSummary
from ..types.cloud_environment_state import CloudEnvironmentState
from ..types.environment_state_change import EnvironmentStateChange
from .raw_client import AsyncRawBillingClient, RawBillingClient


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

    def post_api_v1geneva_actions_billing_resend(
        self,
        *,
        end_time: typing.Optional[dt.datetime] = OMIT,
        start_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BillSummary:
        """
        Parameters
        ----------
        end_time : typing.Optional[dt.datetime]

        start_time : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillSummary
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.post_api_v1geneva_actions_billing_resend()
        """
        _response = self._raw_client.post_api_v1geneva_actions_billing_resend(
            end_time=end_time, start_time=start_time, request_options=request_options
        )
        return _response.data

    def get_api_v1geneva_actions_billing_environment_id(
        self,
        environment_id: str,
        *,
        start_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BillSummary:
        """
        Parameters
        ----------
        environment_id : str

        start_time : typing.Optional[str]

        end_time : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillSummary
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.get_api_v1geneva_actions_billing_environment_id(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.get_api_v1geneva_actions_billing_environment_id(
            environment_id, start_time=start_time, end_time=end_time, request_options=request_options
        )
        return _response.data

    def get_api_v1geneva_actions_billing_environment_id_state_changes(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvironmentStateChange:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentStateChange
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.get_api_v1geneva_actions_billing_environment_id_state_changes(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.get_api_v1geneva_actions_billing_environment_id_state_changes(
            environment_id, request_options=request_options
        )
        return _response.data

    def post_api_v1geneva_actions_billing_environment_id_state_changes(
        self,
        environment_id: str,
        *,
        new_value: typing.Optional[CloudEnvironmentState] = OMIT,
        old_value: typing.Optional[CloudEnvironmentState] = OMIT,
        time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentStateChange:
        """
        Parameters
        ----------
        environment_id : str

        new_value : typing.Optional[CloudEnvironmentState]

        old_value : typing.Optional[CloudEnvironmentState]

        time : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentStateChange
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.post_api_v1geneva_actions_billing_environment_id_state_changes(
            environment_id="environmentId",
        )
        """
        _response = self._raw_client.post_api_v1geneva_actions_billing_environment_id_state_changes(
            environment_id, new_value=new_value, old_value=old_value, time=time, request_options=request_options
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

    async def post_api_v1geneva_actions_billing_resend(
        self,
        *,
        end_time: typing.Optional[dt.datetime] = OMIT,
        start_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BillSummary:
        """
        Parameters
        ----------
        end_time : typing.Optional[dt.datetime]

        start_time : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillSummary
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.post_api_v1geneva_actions_billing_resend()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1geneva_actions_billing_resend(
            end_time=end_time, start_time=start_time, request_options=request_options
        )
        return _response.data

    async def get_api_v1geneva_actions_billing_environment_id(
        self,
        environment_id: str,
        *,
        start_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BillSummary:
        """
        Parameters
        ----------
        environment_id : str

        start_time : typing.Optional[str]

        end_time : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BillSummary
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.get_api_v1geneva_actions_billing_environment_id(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1geneva_actions_billing_environment_id(
            environment_id, start_time=start_time, end_time=end_time, request_options=request_options
        )
        return _response.data

    async def get_api_v1geneva_actions_billing_environment_id_state_changes(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvironmentStateChange:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentStateChange
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.get_api_v1geneva_actions_billing_environment_id_state_changes(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1geneva_actions_billing_environment_id_state_changes(
            environment_id, request_options=request_options
        )
        return _response.data

    async def post_api_v1geneva_actions_billing_environment_id_state_changes(
        self,
        environment_id: str,
        *,
        new_value: typing.Optional[CloudEnvironmentState] = OMIT,
        old_value: typing.Optional[CloudEnvironmentState] = OMIT,
        time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvironmentStateChange:
        """
        Parameters
        ----------
        environment_id : str

        new_value : typing.Optional[CloudEnvironmentState]

        old_value : typing.Optional[CloudEnvironmentState]

        time : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentStateChange
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.post_api_v1geneva_actions_billing_environment_id_state_changes(
                environment_id="environmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1geneva_actions_billing_environment_id_state_changes(
            environment_id, new_value=new_value, old_value=old_value, time=time, request_options=request_options
        )
        return _response.data
