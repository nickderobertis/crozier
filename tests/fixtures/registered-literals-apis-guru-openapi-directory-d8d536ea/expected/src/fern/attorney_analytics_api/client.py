

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.associated_norm_judge_response import AssociatedNormJudgeResponse
from ..types.associated_norm_law_firm_response import AssociatedNormLawFirmResponse
from ..types.associated_norm_party_response import AssociatedNormPartyResponse
from ..types.norm_attorney import NormAttorney
from ..types.norm_attorney_search_response import NormAttorneySearchResponse
from .raw_client import AsyncRawAttorneyAnalyticsApiClient, RawAttorneyAnalyticsApiClient


class AttorneyAnalyticsApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAttorneyAnalyticsApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAttorneyAnalyticsApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAttorneyAnalyticsApiClient
        """
        return self._raw_client

    def get_norm_attorney_by_id(
        self, norm_attorney_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NormAttorney:
        """
        This endpoint retrieves information on the attorney in our normalized attorney database which matches the normAttorneyId specified in the request.

        Parameters
        ----------
        norm_attorney_id : str
            Norm ID of Attorney.
              - minimum: 18
              - maximum: 18

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NormAttorney
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.attorney_analytics_api.get_norm_attorney_by_id(
            norm_attorney_id="NATYs4P6kDBkhKL8CF",
        )
        """
        _response = self._raw_client.get_norm_attorney_by_id(norm_attorney_id, request_options=request_options)
        return _response.data

    def get_norm_judges_associated_with_norm_attorney(
        self,
        norm_attorney_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssociatedNormJudgeResponse:
        """
        This endpoint returns information on all judges which have appeared in cases with the attorney specified by the normAttorneyId. The returned judges are ordered in descending order of number of cases shared with the relevant attorney.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz"  AND  courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz", "CORTKQiA4LJuv54tEj")**|
        | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all judges associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_attorney_id : str
            Norm ID of Attorney.
              - minimum: 18
              - maximum: 18

        page_number : int
            Page number.
            - minimum: 1

        q : typing.Optional[str]
            The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssociatedNormJudgeResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.attorney_analytics_api.get_norm_judges_associated_with_norm_attorney(
            norm_attorney_id="NATYfwmXwRHS279WPY",
            page_number=1,
        )
        """
        _response = self._raw_client.get_norm_judges_associated_with_norm_attorney(
            norm_attorney_id, page_number=page_number, q=q, request_options=request_options
        )
        return _response.data

    def get_norm_law_firms_associated_with_norm_attorney(
        self,
        norm_attorney_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssociatedNormLawFirmResponse:
        """
        Returns a list of Law Firms the norm Attorney has worked for.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz"  AND  courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz", "CORTKQiA4LJuv54tEj")**|
        | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **partyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **partyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **attorneyPartyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **attorneyPartyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all LawFirms associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_attorney_id : str
            Norm ID of Attorney.
              - minimum: 18
              - maximum: 18

        page_number : int
            Page number.
            - minimum: 1

        q : typing.Optional[str]
            The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssociatedNormLawFirmResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.attorney_analytics_api.get_norm_law_firms_associated_with_norm_attorney(
            norm_attorney_id="NATYfwmXwRHS279WPY",
            page_number=1,
        )
        """
        _response = self._raw_client.get_norm_law_firms_associated_with_norm_attorney(
            norm_attorney_id, page_number=page_number, q=q, request_options=request_options
        )
        return _response.data

    def get_norm_parties_associated_with_norm_attorney(
        self,
        norm_attorney_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssociatedNormPartyResponse:
        """
        Returns a list of Parties the Attorney has represented.
        <br><br>
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz"  AND  courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz", "CORTKQiA4LJuv54tEj")**|
        | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **partyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **partyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **attorneyPartyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **attorneyPartyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Group Object.. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all parties associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_attorney_id : str
            Norm ID of Attorney.
              - minimum: 18
              - maximum: 18

        page_number : int
            Page number.
            - minimum: 1

        q : typing.Optional[str]
            The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssociatedNormPartyResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.attorney_analytics_api.get_norm_parties_associated_with_norm_attorney(
            norm_attorney_id="NATYfwmXwRHS279WPY",
            page_number=1,
        )
        """
        _response = self._raw_client.get_norm_parties_associated_with_norm_attorney(
            norm_attorney_id, page_number=page_number, q=q, request_options=request_options
        )
        return _response.data

    def search_normalized_attorneys(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NormAttorneySearchResponse:
        """
        ### This endpoint retrieves information, including the normAttorneyId, on all attorneys in our normalized attorney database which match the request parameters. All query parameters supported by this API can be found in the schema section below.

        Parameters
        ----------
        q : typing.Optional[str]
            The URL encoded query you are searching for.
            The query can be as simple as a keyword, but supports many additional options and filters.</a>

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.
            - Minimum: 1
            - Maximum: 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NormAttorneySearchResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.attorney_analytics_api.search_normalized_attorneys(
            q='normAttorneyId:"NATYhUvNaef3b2iP8D"',
            page_number=1,
        )
        """
        _response = self._raw_client.search_normalized_attorneys(
            q=q, page_number=page_number, request_options=request_options
        )
        return _response.data

    def search_normalized_attorneys_by_id(
        self,
        norm_attorney_search_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NormAttorneySearchResponse:
        """
        ### All query parameters supported for this API can be found in below schema section. Schema --> NormAttorneySearchQueryObject

        Parameters
        ----------
        norm_attorney_search_id : str
            Norm Attorney Search information for the given normAttorneySearchId.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.
            - Minimum: 1
            - Maximum: 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NormAttorneySearchResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.attorney_analytics_api.search_normalized_attorneys_by_id(
            norm_attorney_search_id="ASRCJxUHYsgddr4Hc5",
            page_number=1,
        )
        """
        _response = self._raw_client.search_normalized_attorneys_by_id(
            norm_attorney_search_id, page_number=page_number, request_options=request_options
        )
        return _response.data


class AsyncAttorneyAnalyticsApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAttorneyAnalyticsApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAttorneyAnalyticsApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAttorneyAnalyticsApiClient
        """
        return self._raw_client

    async def get_norm_attorney_by_id(
        self, norm_attorney_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NormAttorney:
        """
        This endpoint retrieves information on the attorney in our normalized attorney database which matches the normAttorneyId specified in the request.

        Parameters
        ----------
        norm_attorney_id : str
            Norm ID of Attorney.
              - minimum: 18
              - maximum: 18

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NormAttorney
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.attorney_analytics_api.get_norm_attorney_by_id(
                norm_attorney_id="NATYs4P6kDBkhKL8CF",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_norm_attorney_by_id(norm_attorney_id, request_options=request_options)
        return _response.data

    async def get_norm_judges_associated_with_norm_attorney(
        self,
        norm_attorney_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssociatedNormJudgeResponse:
        """
        This endpoint returns information on all judges which have appeared in cases with the attorney specified by the normAttorneyId. The returned judges are ordered in descending order of number of cases shared with the relevant attorney.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz"  AND  courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz", "CORTKQiA4LJuv54tEj")**|
        | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all judges associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_attorney_id : str
            Norm ID of Attorney.
              - minimum: 18
              - maximum: 18

        page_number : int
            Page number.
            - minimum: 1

        q : typing.Optional[str]
            The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssociatedNormJudgeResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.attorney_analytics_api.get_norm_judges_associated_with_norm_attorney(
                norm_attorney_id="NATYfwmXwRHS279WPY",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_norm_judges_associated_with_norm_attorney(
            norm_attorney_id, page_number=page_number, q=q, request_options=request_options
        )
        return _response.data

    async def get_norm_law_firms_associated_with_norm_attorney(
        self,
        norm_attorney_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssociatedNormLawFirmResponse:
        """
        Returns a list of Law Firms the norm Attorney has worked for.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz"  AND  courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz", "CORTKQiA4LJuv54tEj")**|
        | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **partyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **partyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **attorneyPartyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **attorneyPartyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all LawFirms associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_attorney_id : str
            Norm ID of Attorney.
              - minimum: 18
              - maximum: 18

        page_number : int
            Page number.
            - minimum: 1

        q : typing.Optional[str]
            The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssociatedNormLawFirmResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.attorney_analytics_api.get_norm_law_firms_associated_with_norm_attorney(
                norm_attorney_id="NATYfwmXwRHS279WPY",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_norm_law_firms_associated_with_norm_attorney(
            norm_attorney_id, page_number=page_number, q=q, request_options=request_options
        )
        return _response.data

    async def get_norm_parties_associated_with_norm_attorney(
        self,
        norm_attorney_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssociatedNormPartyResponse:
        """
        Returns a list of Parties the Attorney has represented.
        <br><br>
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz"  AND  courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz", "CORTKQiA4LJuv54tEj")**|
        | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **partyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **partyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **attorneyPartyRoleId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **attorneyPartyRoleGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Attorney Party Type Group Object.. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **caseFiledDate** | Single Allowed   |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all parties associated with attorney with norm id NATYfwmXwRHS279WPY of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_attorney_id : str
            Norm ID of Attorney.
              - minimum: 18
              - maximum: 18

        page_number : int
            Page number.
            - minimum: 1

        q : typing.Optional[str]
            The URL encoded query you are searching for. The query can be as simple as a keyword, but supports many additional options and filters. All options are documented above.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssociatedNormPartyResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.attorney_analytics_api.get_norm_parties_associated_with_norm_attorney(
                norm_attorney_id="NATYfwmXwRHS279WPY",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_norm_parties_associated_with_norm_attorney(
            norm_attorney_id, page_number=page_number, q=q, request_options=request_options
        )
        return _response.data

    async def search_normalized_attorneys(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NormAttorneySearchResponse:
        """
        ### This endpoint retrieves information, including the normAttorneyId, on all attorneys in our normalized attorney database which match the request parameters. All query parameters supported by this API can be found in the schema section below.

        Parameters
        ----------
        q : typing.Optional[str]
            The URL encoded query you are searching for.
            The query can be as simple as a keyword, but supports many additional options and filters.</a>

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.
            - Minimum: 1
            - Maximum: 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NormAttorneySearchResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.attorney_analytics_api.search_normalized_attorneys(
                q='normAttorneyId:"NATYhUvNaef3b2iP8D"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_normalized_attorneys(
            q=q, page_number=page_number, request_options=request_options
        )
        return _response.data

    async def search_normalized_attorneys_by_id(
        self,
        norm_attorney_search_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NormAttorneySearchResponse:
        """
        ### All query parameters supported for this API can be found in below schema section. Schema --> NormAttorneySearchQueryObject

        Parameters
        ----------
        norm_attorney_search_id : str
            Norm Attorney Search information for the given normAttorneySearchId.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.
            - Minimum: 1
            - Maximum: 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NormAttorneySearchResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.attorney_analytics_api.search_normalized_attorneys_by_id(
                norm_attorney_search_id="ASRCJxUHYsgddr4Hc5",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_normalized_attorneys_by_id(
            norm_attorney_search_id, page_number=page_number, request_options=request_options
        )
        return _response.data
