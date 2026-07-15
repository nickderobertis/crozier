

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSimilarClient, RawSimilarClient
from .types.get_similar_response import GetSimilarResponse


class SimilarClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSimilarClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSimilarClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSimilarClient
        """
        return self._raw_client

    def send_a_company_website_to_receive_a_list_of_companies_related_to_them(
        self, *, link: str, page: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSimilarResponse:
        """
        Parameters
        ----------
        link : str
            We'll provide information about related companies based on the site you provide. If a LinkedIn page is sent, we will try to identify the company related to the page. Ex. https://api.byautomata.io/similar?link=ibm.com

        page : typing.Optional[str]
            Page number of search results. Ex. https://api.byautomata.io/similar?link=ibm.com&page=1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSimilarResponse
            A successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.similar.send_a_company_website_to_receive_a_list_of_companies_related_to_them(
            link="link",
        )
        """
        _response = self._raw_client.send_a_company_website_to_receive_a_list_of_companies_related_to_them(
            link=link, page=page, request_options=request_options
        )
        return _response.data


class AsyncSimilarClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSimilarClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSimilarClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSimilarClient
        """
        return self._raw_client

    async def send_a_company_website_to_receive_a_list_of_companies_related_to_them(
        self, *, link: str, page: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSimilarResponse:
        """
        Parameters
        ----------
        link : str
            We'll provide information about related companies based on the site you provide. If a LinkedIn page is sent, we will try to identify the company related to the page. Ex. https://api.byautomata.io/similar?link=ibm.com

        page : typing.Optional[str]
            Page number of search results. Ex. https://api.byautomata.io/similar?link=ibm.com&page=1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSimilarResponse
            A successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.similar.send_a_company_website_to_receive_a_list_of_companies_related_to_them(
                link="link",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_a_company_website_to_receive_a_list_of_companies_related_to_them(
            link=link, page=page, request_options=request_options
        )
        return _response.data
