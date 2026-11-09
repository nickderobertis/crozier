

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ats_create_or_update_offer_request import AtsCreateOrUpdateOfferRequest
from ..types.ats_create_or_update_offer_response import AtsCreateOrUpdateOfferResponse
from ..types.ats_delete_offer_response import AtsDeleteOfferResponse
from ..types.ats_get_offer_response import AtsGetOfferResponse
from ..types.ats_get_offers_response import AtsGetOffersResponse
from .raw_client import AsyncRawAtsOfferClient, RawAtsOfferClient


OMIT = typing.cast(typing.Any, ...)


class AtsOfferClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAtsOfferClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAtsOfferClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAtsOfferClient
        """
        return self._raw_client

    def ats_offer_get_offer(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsGetOfferResponse:
        """
        Get details of a offer.

        Parameters
        ----------
        id : str
            The unique `id` of the offer.

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetOfferResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_offer.ats_offer_get_offer(
            id="id",
        )
        """
        _response = self._raw_client.ats_offer_get_offer(id, fields=fields, request_options=request_options)
        return _response.data

    def ats_offer_delete_offer(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsDeleteOfferResponse:
        """
        Delete details of an Offer

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsDeleteOfferResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_offer.ats_offer_delete_offer(
            id="id",
        )
        """
        _response = self._raw_client.ats_offer_delete_offer(id, fields=fields, request_options=request_options)
        return _response.data

    def ats_offer_update_offer(
        self,
        id: str,
        *,
        request: AtsCreateOrUpdateOfferRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateOfferResponse:
        """
        Update a Offer

        Parameters
        ----------
        id : str

        request : AtsCreateOrUpdateOfferRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateOfferResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_offer.ats_offer_update_offer(
            id="id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.ats_offer_update_offer(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    def ats_offer_get_offers(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsGetOffersResponse:
        """
        Get all the offers.

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetOffersResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_offer.ats_offer_get_offers()
        """
        _response = self._raw_client.ats_offer_get_offers(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    def ats_offer_create_offer(
        self,
        *,
        request: AtsCreateOrUpdateOfferRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateOfferResponse:
        """
        Create a new Offer

        Parameters
        ----------
        request : AtsCreateOrUpdateOfferRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateOfferResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_offer.ats_offer_create_offer(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.ats_offer_create_offer(
            request=request, fields=fields, request_options=request_options
        )
        return _response.data


class AsyncAtsOfferClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAtsOfferClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAtsOfferClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAtsOfferClient
        """
        return self._raw_client

    async def ats_offer_get_offer(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsGetOfferResponse:
        """
        Get details of a offer.

        Parameters
        ----------
        id : str
            The unique `id` of the offer.

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetOfferResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_offer.ats_offer_get_offer(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_offer_get_offer(id, fields=fields, request_options=request_options)
        return _response.data

    async def ats_offer_delete_offer(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsDeleteOfferResponse:
        """
        Delete details of an Offer

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsDeleteOfferResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_offer.ats_offer_delete_offer(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_offer_delete_offer(id, fields=fields, request_options=request_options)
        return _response.data

    async def ats_offer_update_offer(
        self,
        id: str,
        *,
        request: AtsCreateOrUpdateOfferRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateOfferResponse:
        """
        Update a Offer

        Parameters
        ----------
        id : str

        request : AtsCreateOrUpdateOfferRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateOfferResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_offer.ats_offer_update_offer(
                id="id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_offer_update_offer(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    async def ats_offer_get_offers(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsGetOffersResponse:
        """
        Get all the offers.

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetOffersResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_offer.ats_offer_get_offers()


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_offer_get_offers(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def ats_offer_create_offer(
        self,
        *,
        request: AtsCreateOrUpdateOfferRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateOfferResponse:
        """
        Create a new Offer

        Parameters
        ----------
        request : AtsCreateOrUpdateOfferRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateOfferResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_offer.ats_offer_create_offer(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_offer_create_offer(
            request=request, fields=fields, request_options=request_options
        )
        return _response.data
