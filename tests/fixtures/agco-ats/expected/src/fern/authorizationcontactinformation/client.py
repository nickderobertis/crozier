

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_authorization_codes_shared_models_authorization_contact_information import (
    ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation,
)
from .raw_client import AsyncRawAuthorizationcontactinformationClient, RawAuthorizationcontactinformationClient


OMIT = typing.cast(typing.Any, ...)


class AuthorizationcontactinformationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthorizationcontactinformationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthorizationcontactinformationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthorizationcontactinformationClient
        """
        return self._raw_client

    def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        authorization_code: typing.Optional[str] = None,
        after_date: typing.Optional[dt.datetime] = None,
        before_date: typing.Optional[dt.datetime] = None,
        dealer_code: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        authorization_code : typing.Optional[str]
            Optional. Search by authorization code.

        after_date : typing.Optional[dt.datetime]
            Optional. Include only data for authorization codes created after a provided date.

        before_date : typing.Optional[dt.datetime]
            Optional. Include only data for authorization codes created before a provided date.

        dealer_code : typing.Optional[str]
            Optional. Search by dealer code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcontactinformation.get()
        """
        _response = self._raw_client.get(
            limit=limit,
            offset=offset,
            authorization_code=authorization_code,
            after_date=after_date,
            before_date=before_date,
            dealer_code=dealer_code,
            request_options=request_options,
        )
        return _response.data

    def post(
        self,
        *,
        authorization_code_id: int,
        contact: str,
        dealer_code: str,
        dealership: str,
        phone: str,
        code: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        definition_name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        authorization_code_id : int
            AuthorizationCode ID that the contact information ties into.

        contact : str
            Name of contact requesting an authorization code. Minimum length of 3 characters.

        dealer_code : str
            Dealer code that relates to the dealership. Minimum length of 3 characters.

        dealership : str
            Name of dealership. Minimum length of 3 characters.

        phone : str
            Phone number of contact.

        code : typing.Optional[str]
            The authorization code. Read Only.

        created_by : typing.Optional[str]
            The name of the user that created this code. Read Only.

        created_date : typing.Optional[dt.datetime]
            The date the authorization code was created.

        definition_name : typing.Optional[str]
            The name of the definition used for generating this authorization code. Read Only.

        email : typing.Optional[str]
            Email of contact.

        id : typing.Optional[int]
            ID of authorizationContactInformation

        notes : typing.Optional[str]
            Optional notes used for internal use.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.authorizationcontactinformation.post(
            authorization_code_id=1,
            contact="Contact",
            dealer_code="DealerCode",
            dealership="Dealership",
            phone="Phone",
        )
        """
        _response = self._raw_client.post(
            authorization_code_id=authorization_code_id,
            contact=contact,
            dealer_code=dealer_code,
            dealership=dealership,
            phone=phone,
            code=code,
            created_by=created_by,
            created_date=created_date,
            definition_name=definition_name,
            email=email,
            id=id,
            notes=notes,
            request_options=request_options,
        )
        return _response.data


class AsyncAuthorizationcontactinformationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthorizationcontactinformationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthorizationcontactinformationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthorizationcontactinformationClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        authorization_code: typing.Optional[str] = None,
        after_date: typing.Optional[dt.datetime] = None,
        before_date: typing.Optional[dt.datetime] = None,
        dealer_code: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        authorization_code : typing.Optional[str]
            Optional. Search by authorization code.

        after_date : typing.Optional[dt.datetime]
            Optional. Include only data for authorization codes created after a provided date.

        before_date : typing.Optional[dt.datetime]
            Optional. Include only data for authorization codes created before a provided date.

        dealer_code : typing.Optional[str]
            Optional. Search by dealer code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authorizationcontactinformation.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            limit=limit,
            offset=offset,
            authorization_code=authorization_code,
            after_date=after_date,
            before_date=before_date,
            dealer_code=dealer_code,
            request_options=request_options,
        )
        return _response.data

    async def post(
        self,
        *,
        authorization_code_id: int,
        contact: str,
        dealer_code: str,
        dealership: str,
        phone: str,
        code: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        definition_name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        authorization_code_id : int
            AuthorizationCode ID that the contact information ties into.

        contact : str
            Name of contact requesting an authorization code. Minimum length of 3 characters.

        dealer_code : str
            Dealer code that relates to the dealership. Minimum length of 3 characters.

        dealership : str
            Name of dealership. Minimum length of 3 characters.

        phone : str
            Phone number of contact.

        code : typing.Optional[str]
            The authorization code. Read Only.

        created_by : typing.Optional[str]
            The name of the user that created this code. Read Only.

        created_date : typing.Optional[dt.datetime]
            The date the authorization code was created.

        definition_name : typing.Optional[str]
            The name of the definition used for generating this authorization code. Read Only.

        email : typing.Optional[str]
            Email of contact.

        id : typing.Optional[int]
            ID of authorizationContactInformation

        notes : typing.Optional[str]
            Optional notes used for internal use.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.authorizationcontactinformation.post(
                authorization_code_id=1,
                contact="Contact",
                dealer_code="DealerCode",
                dealership="Dealership",
                phone="Phone",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post(
            authorization_code_id=authorization_code_id,
            contact=contact,
            dealer_code=dealer_code,
            dealership=dealership,
            phone=phone,
            code=code,
            created_by=created_by,
            created_date=created_date,
            definition_name=definition_name,
            email=email,
            id=id,
            notes=notes,
            request_options=request_options,
        )
        return _response.data
