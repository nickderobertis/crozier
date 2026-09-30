

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.substance import Substance
from .raw_client import AsyncRawSubstancesClient, RawSubstancesClient
from .types.get_substance_by_uuid_request_db import GetSubstanceByUuidRequestDb
from .types.get_substances_request_db import GetSubstancesRequestDb
from .types.get_substances_request_type import GetSubstancesRequestType


class SubstancesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubstancesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubstancesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubstancesClient
        """
        return self._raw_client

    def get_substances(
        self,
        db: GetSubstancesRequestDb,
        *,
        search: typing.Optional[str] = None,
        type: typing.Optional[GetSubstancesRequestType] = None,
        compound_uri: typing.Optional[str] = None,
        bundle_uri: typing.Optional[str] = None,
        add_dummy_substance: typing.Optional[bool] = None,
        studysummary: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Substance:
        """
        Returns a list of substances, according to the search criteria

        Parameters
        ----------
        db : GetSubstancesRequestDb
            Database ID

        search : typing.Optional[str]
            Search parameter

        type : typing.Optional[GetSubstancesRequestType]

        compound_uri : typing.Optional[str]
            If type=related finds all substances containing this compound; if typ =reference - finds all substances with this compound as reference structure

        bundle_uri : typing.Optional[str]
            Retrieves if selected in this bundle

        add_dummy_substance : typing.Optional[bool]
            Adds a compound record as substance in JSON; only if type=related

        studysummary : typing.Optional[bool]
            If true retrieves study summary for each substance

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Substance
            OK. Substances found

        Examples
        --------
        from fern.substances import GetSubstancesRequestDb

        from fern import FernApi

        client = FernApi()
        client.substances.get_substances(
            db=GetSubstancesRequestDb.CALIBRATE,
        )
        """
        _response = self._raw_client.get_substances(
            db,
            search=search,
            type=type,
            compound_uri=compound_uri,
            bundle_uri=bundle_uri,
            add_dummy_substance=add_dummy_substance,
            studysummary=studysummary,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data

    def get_substance_by_uuid(
        self,
        db: GetSubstanceByUuidRequestDb,
        uuid_: str,
        *,
        property_uris: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Substance:
        """
        Returns substance representation

        Parameters
        ----------
        db : GetSubstanceByUuidRequestDb
            Database ID

        uuid_ : str
            Substance UUID

        property_uris : typing.Optional[str]
            Property URIs

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Substance
            OK. Substances found

        Examples
        --------
        from fern.substances import GetSubstanceByUuidRequestDb

        from fern import FernApi

        client = FernApi()
        client.substances.get_substance_by_uuid(
            db=GetSubstanceByUuidRequestDb.CALIBRATE,
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_substance_by_uuid(
            db, uuid_, property_uris=property_uris, page=page, pagesize=pagesize, request_options=request_options
        )
        return _response.data


class AsyncSubstancesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubstancesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubstancesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubstancesClient
        """
        return self._raw_client

    async def get_substances(
        self,
        db: GetSubstancesRequestDb,
        *,
        search: typing.Optional[str] = None,
        type: typing.Optional[GetSubstancesRequestType] = None,
        compound_uri: typing.Optional[str] = None,
        bundle_uri: typing.Optional[str] = None,
        add_dummy_substance: typing.Optional[bool] = None,
        studysummary: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Substance:
        """
        Returns a list of substances, according to the search criteria

        Parameters
        ----------
        db : GetSubstancesRequestDb
            Database ID

        search : typing.Optional[str]
            Search parameter

        type : typing.Optional[GetSubstancesRequestType]

        compound_uri : typing.Optional[str]
            If type=related finds all substances containing this compound; if typ =reference - finds all substances with this compound as reference structure

        bundle_uri : typing.Optional[str]
            Retrieves if selected in this bundle

        add_dummy_substance : typing.Optional[bool]
            Adds a compound record as substance in JSON; only if type=related

        studysummary : typing.Optional[bool]
            If true retrieves study summary for each substance

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Substance
            OK. Substances found

        Examples
        --------
        import asyncio

        from fern.substances import GetSubstancesRequestDb

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.substances.get_substances(
                db=GetSubstancesRequestDb.CALIBRATE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_substances(
            db,
            search=search,
            type=type,
            compound_uri=compound_uri,
            bundle_uri=bundle_uri,
            add_dummy_substance=add_dummy_substance,
            studysummary=studysummary,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data

    async def get_substance_by_uuid(
        self,
        db: GetSubstanceByUuidRequestDb,
        uuid_: str,
        *,
        property_uris: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Substance:
        """
        Returns substance representation

        Parameters
        ----------
        db : GetSubstanceByUuidRequestDb
            Database ID

        uuid_ : str
            Substance UUID

        property_uris : typing.Optional[str]
            Property URIs

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Substance
            OK. Substances found

        Examples
        --------
        import asyncio

        from fern.substances import GetSubstanceByUuidRequestDb

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.substances.get_substance_by_uuid(
                db=GetSubstanceByUuidRequestDb.CALIBRATE,
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_substance_by_uuid(
            db, uuid_, property_uris=property_uris, page=page, pagesize=pagesize, request_options=request_options
        )
        return _response.data
