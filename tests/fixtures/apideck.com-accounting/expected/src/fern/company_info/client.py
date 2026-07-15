

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_company_info_response import GetCompanyInfoResponse
from .raw_client import AsyncRawCompanyInfoClient, RawCompanyInfoClient


class CompanyInfoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCompanyInfoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCompanyInfoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCompanyInfoClient
        """
        return self._raw_client

    def one(
        self,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCompanyInfoResponse:
        """
        Get company info

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCompanyInfoResponse
            CompanyInfo

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.company_info.one(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(raw=raw, fields=fields, request_options=request_options)
        return _response.data


class AsyncCompanyInfoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCompanyInfoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCompanyInfoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCompanyInfoClient
        """
        return self._raw_client

    async def one(
        self,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCompanyInfoResponse:
        """
        Get company info

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCompanyInfoResponse
            CompanyInfo

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.company_info.one(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(raw=raw, fields=fields, request_options=request_options)
        return _response.data
