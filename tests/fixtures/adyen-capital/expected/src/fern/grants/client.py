

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.disbursement import Disbursement
from ..types.disbursement_repayment_info_update import DisbursementRepaymentInfoUpdate
from ..types.disbursements import Disbursements
from ..types.grant import Grant
from ..types.grant_info_counterparty import GrantInfoCounterparty
from ..types.grants import Grants
from .raw_client import AsyncRawGrantsClient, RawGrantsClient


OMIT = typing.cast(typing.Any, ...)


class GrantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGrantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGrantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGrantsClient
        """
        return self._raw_client

    def get_grants(
        self, *, counterparty_account_holder_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Grants:
        """
        Returns a list of all the grants of a specific account holder.

        Parameters
        ----------
        counterparty_account_holder_id : str
            The unique identifier of the account holder that received the grants.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Grants
            OK - The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.grants.get_grants(
            counterparty_account_holder_id="counterpartyAccountHolderId",
        )
        """
        _response = self._raw_client.get_grants(
            counterparty_account_holder_id=counterparty_account_holder_id, request_options=request_options
        )
        return _response.data

    def post_grants(
        self,
        *,
        grant_account_id: str,
        grant_offer_id: str,
        counterparty: typing.Optional[GrantInfoCounterparty] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Grant:
        """
        Make a request for a grant on behalf of an account holder.

        Parameters
        ----------
        grant_account_id : str
            The unique identifier of the grant account that tracks this grant.

        grant_offer_id : str
            The unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant.

        counterparty : typing.Optional[GrantInfoCounterparty]
            Contains the details of the party that receives the grant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Grant
            OK - The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.grants.post_grants(
            grant_account_id="grantAccountId",
            grant_offer_id="grantOfferId",
        )
        """
        _response = self._raw_client.post_grants(
            grant_account_id=grant_account_id,
            grant_offer_id=grant_offer_id,
            counterparty=counterparty,
            request_options=request_options,
        )
        return _response.data

    def get_grants_grant_id(self, grant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Grant:
        """
        Returns the details of the specified grant.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Grant
            OK - The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.grants.get_grants_grant_id(
            grant_id="grantId",
        )
        """
        _response = self._raw_client.get_grants_grant_id(grant_id, request_options=request_options)
        return _response.data

    def get_grants_grant_id_disbursements(
        self, grant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Disbursements:
        """
        Returns the disbursements of a specified grant.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Disbursements
            OK - The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.grants.get_grants_grant_id_disbursements(
            grant_id="grantId",
        )
        """
        _response = self._raw_client.get_grants_grant_id_disbursements(grant_id, request_options=request_options)
        return _response.data

    def get_grants_grant_id_disbursements_disbursement_id(
        self, grant_id: str, disbursement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Disbursement:
        """
        Returns the details of a disbursement specified in the path.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        disbursement_id : str
            The unique identifier of the disbursement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Disbursement
            OK - The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.grants.get_grants_grant_id_disbursements_disbursement_id(
            grant_id="grantId",
            disbursement_id="disbursementId",
        )
        """
        _response = self._raw_client.get_grants_grant_id_disbursements_disbursement_id(
            grant_id, disbursement_id, request_options=request_options
        )
        return _response.data

    def patch_grants_grant_id_disbursements_disbursement_id(
        self,
        grant_id: str,
        disbursement_id: str,
        *,
        repayment: typing.Optional[DisbursementRepaymentInfoUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Disbursement:
        """
        Update the percentage of your user's net income that is deducted for repaying the grant.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        disbursement_id : str
            The unique identifier of the disbursement.

        repayment : typing.Optional[DisbursementRepaymentInfoUpdate]
            Contains information about the basis points configured for repaying the disbursement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Disbursement
            OK - The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.grants.patch_grants_grant_id_disbursements_disbursement_id(
            grant_id="grantId",
            disbursement_id="disbursementId",
        )
        """
        _response = self._raw_client.patch_grants_grant_id_disbursements_disbursement_id(
            grant_id, disbursement_id, repayment=repayment, request_options=request_options
        )
        return _response.data


class AsyncGrantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGrantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGrantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGrantsClient
        """
        return self._raw_client

    async def get_grants(
        self, *, counterparty_account_holder_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Grants:
        """
        Returns a list of all the grants of a specific account holder.

        Parameters
        ----------
        counterparty_account_holder_id : str
            The unique identifier of the account holder that received the grants.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Grants
            OK - The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.grants.get_grants(
                counterparty_account_holder_id="counterpartyAccountHolderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_grants(
            counterparty_account_holder_id=counterparty_account_holder_id, request_options=request_options
        )
        return _response.data

    async def post_grants(
        self,
        *,
        grant_account_id: str,
        grant_offer_id: str,
        counterparty: typing.Optional[GrantInfoCounterparty] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Grant:
        """
        Make a request for a grant on behalf of an account holder.

        Parameters
        ----------
        grant_account_id : str
            The unique identifier of the grant account that tracks this grant.

        grant_offer_id : str
            The unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant.

        counterparty : typing.Optional[GrantInfoCounterparty]
            Contains the details of the party that receives the grant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Grant
            OK - The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.grants.post_grants(
                grant_account_id="grantAccountId",
                grant_offer_id="grantOfferId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_grants(
            grant_account_id=grant_account_id,
            grant_offer_id=grant_offer_id,
            counterparty=counterparty,
            request_options=request_options,
        )
        return _response.data

    async def get_grants_grant_id(
        self, grant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Grant:
        """
        Returns the details of the specified grant.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Grant
            OK - The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.grants.get_grants_grant_id(
                grant_id="grantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_grants_grant_id(grant_id, request_options=request_options)
        return _response.data

    async def get_grants_grant_id_disbursements(
        self, grant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Disbursements:
        """
        Returns the disbursements of a specified grant.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Disbursements
            OK - The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.grants.get_grants_grant_id_disbursements(
                grant_id="grantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_grants_grant_id_disbursements(grant_id, request_options=request_options)
        return _response.data

    async def get_grants_grant_id_disbursements_disbursement_id(
        self, grant_id: str, disbursement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Disbursement:
        """
        Returns the details of a disbursement specified in the path.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        disbursement_id : str
            The unique identifier of the disbursement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Disbursement
            OK - The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.grants.get_grants_grant_id_disbursements_disbursement_id(
                grant_id="grantId",
                disbursement_id="disbursementId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_grants_grant_id_disbursements_disbursement_id(
            grant_id, disbursement_id, request_options=request_options
        )
        return _response.data

    async def patch_grants_grant_id_disbursements_disbursement_id(
        self,
        grant_id: str,
        disbursement_id: str,
        *,
        repayment: typing.Optional[DisbursementRepaymentInfoUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Disbursement:
        """
        Update the percentage of your user's net income that is deducted for repaying the grant.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        disbursement_id : str
            The unique identifier of the disbursement.

        repayment : typing.Optional[DisbursementRepaymentInfoUpdate]
            Contains information about the basis points configured for repaying the disbursement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Disbursement
            OK - The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.grants.patch_grants_grant_id_disbursements_disbursement_id(
                grant_id="grantId",
                disbursement_id="disbursementId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_grants_grant_id_disbursements_disbursement_id(
            grant_id, disbursement_id, repayment=repayment, request_options=request_options
        )
        return _response.data
