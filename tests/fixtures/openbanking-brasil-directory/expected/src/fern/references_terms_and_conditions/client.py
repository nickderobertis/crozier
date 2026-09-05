

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.terms_and_conditions_page import TermsAndConditionsPage
from .raw_client import AsyncRawReferencesTermsAndConditionsClient, RawReferencesTermsAndConditionsClient


class ReferencesTermsAndConditionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReferencesTermsAndConditionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReferencesTermsAndConditionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReferencesTermsAndConditionsClient
        """
        return self._raw_client

    def all_terms_and_conditions(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TermsAndConditionsPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            The page number to return of the result set

        size : typing.Optional[int]
            The size of the pages to return

        sort : typing.Optional[str]
            The field name to sort

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TermsAndConditionsPage
            Paged data of TnC items

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.references_terms_and_conditions.all_terms_and_conditions()
        """
        _response = self._raw_client.all_terms_and_conditions(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data


class AsyncReferencesTermsAndConditionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReferencesTermsAndConditionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReferencesTermsAndConditionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReferencesTermsAndConditionsClient
        """
        return self._raw_client

    async def all_terms_and_conditions(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TermsAndConditionsPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            The page number to return of the result set

        size : typing.Optional[int]
            The size of the pages to return

        sort : typing.Optional[str]
            The field name to sort

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TermsAndConditionsPage
            Paged data of TnC items

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.references_terms_and_conditions.all_terms_and_conditions()


        asyncio.run(main())
        """
        _response = await self._raw_client.all_terms_and_conditions(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data
