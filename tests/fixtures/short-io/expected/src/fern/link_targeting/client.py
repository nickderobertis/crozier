

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLinkTargetingClient, RawLinkTargetingClient
from .types.delete_link_country_link_id_country_request_country import DeleteLinkCountryLinkIdCountryRequestCountry
from .types.delete_link_region_link_id_country_region_request_country import (
    DeleteLinkRegionLinkIdCountryRegionRequestCountry,
)
from .types.get_link_region_list_country_request_country import GetLinkRegionListCountryRequestCountry
from .types.post_link_country_bulk_link_id_request_body_item import PostLinkCountryBulkLinkIdRequestBodyItem
from .types.post_link_country_link_id_request_country import PostLinkCountryLinkIdRequestCountry
from .types.post_link_region_bulk_link_id_request_body_item import PostLinkRegionBulkLinkIdRequestBodyItem
from .types.post_link_region_link_id_request_country import PostLinkRegionLinkIdRequestCountry


OMIT = typing.cast(typing.Any, ...)


class LinkTargetingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLinkTargetingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLinkTargetingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLinkTargetingClient
        """
        return self._raw_client

    def get_link_countries(
        self,
        link_id: str,
        *,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_targeting.get_link_countries(
            link_id="linkId",
        )
        """
        _response = self._raw_client.get_link_countries(link_id, domain_id=domain_id, request_options=request_options)
        return _response.data

    def create_link_country(
        self,
        link_id: str,
        *,
        country: PostLinkCountryLinkIdRequestCountry,
        original_url: str,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        country : PostLinkCountryLinkIdRequestCountry
            Country code

        original_url : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.link_targeting import PostLinkCountryLinkIdRequestCountry

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_targeting.create_link_country(
            link_id="linkId",
            country=PostLinkCountryLinkIdRequestCountry.AD,
            original_url="originalURL",
        )
        """
        _response = self._raw_client.create_link_country(
            link_id, country=country, original_url=original_url, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    def create_link_countries_in_bulk(
        self,
        link_id: str,
        *,
        request: typing.Sequence[PostLinkCountryBulkLinkIdRequestBodyItem],
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        request : typing.Sequence[PostLinkCountryBulkLinkIdRequestBodyItem]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.link_targeting import (
            PostLinkCountryBulkLinkIdRequestBodyItem,
            PostLinkCountryBulkLinkIdRequestBodyItemCountry,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_targeting.create_link_countries_in_bulk(
            link_id="linkId",
            request=[
                PostLinkCountryBulkLinkIdRequestBodyItem(
                    country=PostLinkCountryBulkLinkIdRequestBodyItemCountry.AD,
                    original_url="originalURL",
                )
            ],
        )
        """
        _response = self._raw_client.create_link_countries_in_bulk(
            link_id, request=request, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    def delete_link_country(
        self,
        link_id: str,
        country: DeleteLinkCountryLinkIdCountryRequestCountry,
        *,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        country : DeleteLinkCountryLinkIdCountryRequestCountry
            Country code

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.link_targeting import DeleteLinkCountryLinkIdCountryRequestCountry

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_targeting.delete_link_country(
            link_id="linkId",
            country=DeleteLinkCountryLinkIdCountryRequestCountry.AD,
        )
        """
        _response = self._raw_client.delete_link_country(
            link_id, country, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    def get_link_regions(
        self,
        link_id: str,
        *,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_targeting.get_link_regions(
            link_id="linkId",
        )
        """
        _response = self._raw_client.get_link_regions(link_id, domain_id=domain_id, request_options=request_options)
        return _response.data

    def add_region_targeting_to_link(
        self,
        link_id: str,
        *,
        country: PostLinkRegionLinkIdRequestCountry,
        region: str,
        original_url: str,
        domain_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add region targeting to link

        Parameters
        ----------
        link_id : str

        country : PostLinkRegionLinkIdRequestCountry
            Country code

        region : str
            ISO 3166-2 region code

        original_url : str

        domain_id : typing.Optional[int]
            Domain ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.link_targeting import PostLinkRegionLinkIdRequestCountry

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_targeting.add_region_targeting_to_link(
            link_id="linkId",
            country=PostLinkRegionLinkIdRequestCountry.AD,
            region="region",
            original_url="https://example.com",
        )
        """
        _response = self._raw_client.add_region_targeting_to_link(
            link_id,
            country=country,
            region=region,
            original_url=original_url,
            domain_id=domain_id,
            request_options=request_options,
        )
        return _response.data

    def get_all_regions_by_country(
        self,
        country: GetLinkRegionListCountryRequestCountry,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        country : GetLinkRegionListCountryRequestCountry
            Country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.link_targeting import GetLinkRegionListCountryRequestCountry

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_targeting.get_all_regions_by_country(
            country=GetLinkRegionListCountryRequestCountry.AD,
        )
        """
        _response = self._raw_client.get_all_regions_by_country(country, request_options=request_options)
        return _response.data

    def create_link_regions_in_bulk(
        self,
        link_id: str,
        *,
        request: typing.Sequence[PostLinkRegionBulkLinkIdRequestBodyItem],
        domain_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        request : typing.Sequence[PostLinkRegionBulkLinkIdRequestBodyItem]

        domain_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.link_targeting import (
            PostLinkRegionBulkLinkIdRequestBodyItem,
            PostLinkRegionBulkLinkIdRequestBodyItemCountry,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_targeting.create_link_regions_in_bulk(
            link_id="linkId",
            request=[
                PostLinkRegionBulkLinkIdRequestBodyItem(
                    country=PostLinkRegionBulkLinkIdRequestBodyItemCountry.AD,
                    region="region",
                    original_url="https://example.com",
                )
            ],
        )
        """
        _response = self._raw_client.create_link_regions_in_bulk(
            link_id, request=request, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    def delete_link_region_by_country(
        self,
        link_id: str,
        country: DeleteLinkRegionLinkIdCountryRegionRequestCountry,
        region: str,
        *,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        country : DeleteLinkRegionLinkIdCountryRegionRequestCountry
            Country code

        region : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.link_targeting import (
            DeleteLinkRegionLinkIdCountryRegionRequestCountry,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.link_targeting.delete_link_region_by_country(
            link_id="linkId",
            country=DeleteLinkRegionLinkIdCountryRegionRequestCountry.AD,
            region="region",
        )
        """
        _response = self._raw_client.delete_link_region_by_country(
            link_id, country, region, domain_id=domain_id, request_options=request_options
        )
        return _response.data


class AsyncLinkTargetingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLinkTargetingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLinkTargetingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLinkTargetingClient
        """
        return self._raw_client

    async def get_link_countries(
        self,
        link_id: str,
        *,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_targeting.get_link_countries(
                link_id="linkId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_link_countries(
            link_id, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    async def create_link_country(
        self,
        link_id: str,
        *,
        country: PostLinkCountryLinkIdRequestCountry,
        original_url: str,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        country : PostLinkCountryLinkIdRequestCountry
            Country code

        original_url : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.link_targeting import PostLinkCountryLinkIdRequestCountry

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_targeting.create_link_country(
                link_id="linkId",
                country=PostLinkCountryLinkIdRequestCountry.AD,
                original_url="originalURL",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_link_country(
            link_id, country=country, original_url=original_url, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    async def create_link_countries_in_bulk(
        self,
        link_id: str,
        *,
        request: typing.Sequence[PostLinkCountryBulkLinkIdRequestBodyItem],
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        request : typing.Sequence[PostLinkCountryBulkLinkIdRequestBodyItem]

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.link_targeting import (
            PostLinkCountryBulkLinkIdRequestBodyItem,
            PostLinkCountryBulkLinkIdRequestBodyItemCountry,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_targeting.create_link_countries_in_bulk(
                link_id="linkId",
                request=[
                    PostLinkCountryBulkLinkIdRequestBodyItem(
                        country=PostLinkCountryBulkLinkIdRequestBodyItemCountry.AD,
                        original_url="originalURL",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_link_countries_in_bulk(
            link_id, request=request, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    async def delete_link_country(
        self,
        link_id: str,
        country: DeleteLinkCountryLinkIdCountryRequestCountry,
        *,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        country : DeleteLinkCountryLinkIdCountryRequestCountry
            Country code

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.link_targeting import DeleteLinkCountryLinkIdCountryRequestCountry

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_targeting.delete_link_country(
                link_id="linkId",
                country=DeleteLinkCountryLinkIdCountryRequestCountry.AD,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_link_country(
            link_id, country, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    async def get_link_regions(
        self,
        link_id: str,
        *,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_targeting.get_link_regions(
                link_id="linkId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_link_regions(
            link_id, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    async def add_region_targeting_to_link(
        self,
        link_id: str,
        *,
        country: PostLinkRegionLinkIdRequestCountry,
        region: str,
        original_url: str,
        domain_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Add region targeting to link

        Parameters
        ----------
        link_id : str

        country : PostLinkRegionLinkIdRequestCountry
            Country code

        region : str
            ISO 3166-2 region code

        original_url : str

        domain_id : typing.Optional[int]
            Domain ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.link_targeting import PostLinkRegionLinkIdRequestCountry

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_targeting.add_region_targeting_to_link(
                link_id="linkId",
                country=PostLinkRegionLinkIdRequestCountry.AD,
                region="region",
                original_url="https://example.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_region_targeting_to_link(
            link_id,
            country=country,
            region=region,
            original_url=original_url,
            domain_id=domain_id,
            request_options=request_options,
        )
        return _response.data

    async def get_all_regions_by_country(
        self,
        country: GetLinkRegionListCountryRequestCountry,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        country : GetLinkRegionListCountryRequestCountry
            Country code

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.link_targeting import GetLinkRegionListCountryRequestCountry

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_targeting.get_all_regions_by_country(
                country=GetLinkRegionListCountryRequestCountry.AD,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_regions_by_country(country, request_options=request_options)
        return _response.data

    async def create_link_regions_in_bulk(
        self,
        link_id: str,
        *,
        request: typing.Sequence[PostLinkRegionBulkLinkIdRequestBodyItem],
        domain_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        request : typing.Sequence[PostLinkRegionBulkLinkIdRequestBodyItem]

        domain_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.link_targeting import (
            PostLinkRegionBulkLinkIdRequestBodyItem,
            PostLinkRegionBulkLinkIdRequestBodyItemCountry,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_targeting.create_link_regions_in_bulk(
                link_id="linkId",
                request=[
                    PostLinkRegionBulkLinkIdRequestBodyItem(
                        country=PostLinkRegionBulkLinkIdRequestBodyItemCountry.AD,
                        region="region",
                        original_url="https://example.com",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_link_regions_in_bulk(
            link_id, request=request, domain_id=domain_id, request_options=request_options
        )
        return _response.data

    async def delete_link_region_by_country(
        self,
        link_id: str,
        country: DeleteLinkRegionLinkIdCountryRegionRequestCountry,
        region: str,
        *,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        link_id : str

        country : DeleteLinkRegionLinkIdCountryRegionRequestCountry
            Country code

        region : str

        domain_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.link_targeting import (
            DeleteLinkRegionLinkIdCountryRegionRequestCountry,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.link_targeting.delete_link_region_by_country(
                link_id="linkId",
                country=DeleteLinkRegionLinkIdCountryRegionRequestCountry.AD,
                region="region",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_link_region_by_country(
            link_id, country, region, domain_id=domain_id, request_options=request_options
        )
        return _response.data
