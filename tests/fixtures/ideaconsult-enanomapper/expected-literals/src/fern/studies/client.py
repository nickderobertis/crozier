

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.facet import Facet
from ..types.investigation import Investigation
from ..types.substance_study import SubstanceStudy
from ..types.substance_study_summary import SubstanceStudySummary
from .raw_client import AsyncRawStudiesClient, RawStudiesClient
from .types.get_endpoint_summary_request_db import GetEndpointSummaryRequestDb
from .types.get_endpoint_summary_request_top import GetEndpointSummaryRequestTop
from .types.get_investigation_results_request_db import GetInvestigationResultsRequestDb
from .types.get_investigation_results_request_type import GetInvestigationResultsRequestType
from .types.get_substance_study_request_db import GetSubstanceStudyRequestDb
from .types.get_substance_study_request_top import GetSubstanceStudyRequestTop
from .types.get_substance_study_summary_request_db import GetSubstanceStudySummaryRequestDb
from .types.get_substance_study_summary_request_top import GetSubstanceStudySummaryRequestTop


class StudiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStudiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStudiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStudiesClient
        """
        return self._raw_client

    def get_investigation_results(
        self,
        db: GetInvestigationResultsRequestDb,
        *,
        type: GetInvestigationResultsRequestType,
        search: str,
        inchikey: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Investigation:
        """
        Multiple studies in tabular form

        Parameters
        ----------
        db : GetInvestigationResultsRequestDb
            Database ID

        type : GetInvestigationResultsRequestType
            query type

        search : str
            Search parameter, UUID of the investigation or a substance

        inchikey : typing.Optional[str]
            Search parameter, InChI key(s) of the substance component(s), comma delimited

        id : typing.Optional[str]
            Search parameter, chemical structure or substance identifier(s), comma delimited

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Investigation
            OK. Entries found

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.studies.get_investigation_results(
            db="calibrate",
            type="byinvestigation",
            search="PC_GRANULOMETRY_SECTION",
            inchikey="YUYCVXFAYWRXLS-UHFFFAOYSA-N",
        )
        """
        _response = self._raw_client.get_investigation_results(
            db,
            type=type,
            search=search,
            inchikey=inchikey,
            id=id,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data

    def get_endpoint_summary(
        self,
        db: GetEndpointSummaryRequestDb,
        *,
        top: typing.Optional[GetEndpointSummaryRequestTop] = None,
        category: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Facet:
        """
        Returns endpoint summary

        Parameters
        ----------
        db : GetEndpointSummaryRequestDb
            Database ID

        top : typing.Optional[GetEndpointSummaryRequestTop]
            Top endpoint category

        category : typing.Optional[str]
            Endpoint category (The value in the protocol.category.code field)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Facet
            OK.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.studies.get_endpoint_summary(
            db="calibrate",
        )
        """
        _response = self._raw_client.get_endpoint_summary(
            db, top=top, category=category, request_options=request_options
        )
        return _response.data

    def get_substance_study(
        self,
        db: GetSubstanceStudyRequestDb,
        uuid_: str,
        *,
        top: typing.Optional[GetSubstanceStudyRequestTop] = None,
        category: typing.Optional[str] = None,
        property_uri: typing.Optional[str] = None,
        property: typing.Optional[str] = None,
        investigation_uuid: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubstanceStudy:
        """
        Returns substance study representation

        Parameters
        ----------
        db : GetSubstanceStudyRequestDb
            Database ID

        uuid_ : str
            Substance UUID

        top : typing.Optional[GetSubstanceStudyRequestTop]
            Top endpoint category

        category : typing.Optional[str]
            Endpoint category (The value in the protocol.category.code field)

        property_uri : typing.Optional[str]
            Property URI https://data.enanomapper.net/property/{UUID} , see Property service

        property : typing.Optional[str]
            Property UUID

        investigation_uuid : typing.Optional[str]
            Investigation UUID, a code to link different studies

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubstanceStudy
            OK. Substances found

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.studies.get_substance_study(
            db="calibrate",
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_substance_study(
            db,
            uuid_,
            top=top,
            category=category,
            property_uri=property_uri,
            property=property,
            investigation_uuid=investigation_uuid,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data

    def get_substance_study_summary(
        self,
        db: GetSubstanceStudySummaryRequestDb,
        uuid_: str,
        *,
        top: typing.Optional[GetSubstanceStudySummaryRequestTop] = None,
        category: typing.Optional[str] = None,
        property_uri: typing.Optional[str] = None,
        property: typing.Optional[str] = None,
        result: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubstanceStudySummary:
        """
        Study summary

        Parameters
        ----------
        db : GetSubstanceStudySummaryRequestDb
            Database ID

        uuid_ : str
            Substance UUID

        top : typing.Optional[GetSubstanceStudySummaryRequestTop]
            Top endpoint category

        category : typing.Optional[str]
            Endpoint category (The value in the protocol.category.code field)

        property_uri : typing.Optional[str]
            Property URI https://data.enanomapper.net/property/{UUID} , see Property service

        property : typing.Optional[str]
            Property UUID, see Property service

        result : typing.Optional[bool]
            If true will group by topcategory,endpointcategory,interpretation result

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubstanceStudySummary
            OK.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.studies.get_substance_study_summary(
            db="calibrate",
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_substance_study_summary(
            db,
            uuid_,
            top=top,
            category=category,
            property_uri=property_uri,
            property=property,
            result=result,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data


class AsyncStudiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStudiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStudiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStudiesClient
        """
        return self._raw_client

    async def get_investigation_results(
        self,
        db: GetInvestigationResultsRequestDb,
        *,
        type: GetInvestigationResultsRequestType,
        search: str,
        inchikey: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Investigation:
        """
        Multiple studies in tabular form

        Parameters
        ----------
        db : GetInvestigationResultsRequestDb
            Database ID

        type : GetInvestigationResultsRequestType
            query type

        search : str
            Search parameter, UUID of the investigation or a substance

        inchikey : typing.Optional[str]
            Search parameter, InChI key(s) of the substance component(s), comma delimited

        id : typing.Optional[str]
            Search parameter, chemical structure or substance identifier(s), comma delimited

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Investigation
            OK. Entries found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.studies.get_investigation_results(
                db="calibrate",
                type="byinvestigation",
                search="PC_GRANULOMETRY_SECTION",
                inchikey="YUYCVXFAYWRXLS-UHFFFAOYSA-N",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_investigation_results(
            db,
            type=type,
            search=search,
            inchikey=inchikey,
            id=id,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data

    async def get_endpoint_summary(
        self,
        db: GetEndpointSummaryRequestDb,
        *,
        top: typing.Optional[GetEndpointSummaryRequestTop] = None,
        category: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Facet:
        """
        Returns endpoint summary

        Parameters
        ----------
        db : GetEndpointSummaryRequestDb
            Database ID

        top : typing.Optional[GetEndpointSummaryRequestTop]
            Top endpoint category

        category : typing.Optional[str]
            Endpoint category (The value in the protocol.category.code field)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Facet
            OK.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.studies.get_endpoint_summary(
                db="calibrate",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_endpoint_summary(
            db, top=top, category=category, request_options=request_options
        )
        return _response.data

    async def get_substance_study(
        self,
        db: GetSubstanceStudyRequestDb,
        uuid_: str,
        *,
        top: typing.Optional[GetSubstanceStudyRequestTop] = None,
        category: typing.Optional[str] = None,
        property_uri: typing.Optional[str] = None,
        property: typing.Optional[str] = None,
        investigation_uuid: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubstanceStudy:
        """
        Returns substance study representation

        Parameters
        ----------
        db : GetSubstanceStudyRequestDb
            Database ID

        uuid_ : str
            Substance UUID

        top : typing.Optional[GetSubstanceStudyRequestTop]
            Top endpoint category

        category : typing.Optional[str]
            Endpoint category (The value in the protocol.category.code field)

        property_uri : typing.Optional[str]
            Property URI https://data.enanomapper.net/property/{UUID} , see Property service

        property : typing.Optional[str]
            Property UUID

        investigation_uuid : typing.Optional[str]
            Investigation UUID, a code to link different studies

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubstanceStudy
            OK. Substances found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.studies.get_substance_study(
                db="calibrate",
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_substance_study(
            db,
            uuid_,
            top=top,
            category=category,
            property_uri=property_uri,
            property=property,
            investigation_uuid=investigation_uuid,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data

    async def get_substance_study_summary(
        self,
        db: GetSubstanceStudySummaryRequestDb,
        uuid_: str,
        *,
        top: typing.Optional[GetSubstanceStudySummaryRequestTop] = None,
        category: typing.Optional[str] = None,
        property_uri: typing.Optional[str] = None,
        property: typing.Optional[str] = None,
        result: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubstanceStudySummary:
        """
        Study summary

        Parameters
        ----------
        db : GetSubstanceStudySummaryRequestDb
            Database ID

        uuid_ : str
            Substance UUID

        top : typing.Optional[GetSubstanceStudySummaryRequestTop]
            Top endpoint category

        category : typing.Optional[str]
            Endpoint category (The value in the protocol.category.code field)

        property_uri : typing.Optional[str]
            Property URI https://data.enanomapper.net/property/{UUID} , see Property service

        property : typing.Optional[str]
            Property UUID, see Property service

        result : typing.Optional[bool]
            If true will group by topcategory,endpointcategory,interpretation result

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubstanceStudySummary
            OK.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.studies.get_substance_study_summary(
                db="calibrate",
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_substance_study_summary(
            db,
            uuid_,
            top=top,
            category=category,
            property_uri=property_uri,
            property=property,
            result=result,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data
