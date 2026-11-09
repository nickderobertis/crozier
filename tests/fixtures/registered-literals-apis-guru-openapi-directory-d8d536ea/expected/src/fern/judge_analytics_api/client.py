

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.associated_norm_attorney_response import AssociatedNormAttorneyResponse
from ..types.associated_norm_law_firm_response import AssociatedNormLawFirmResponse
from ..types.associated_norm_party_response import AssociatedNormPartyResponse
from ..types.norm_judge import NormJudge
from ..types.norm_judge_search_response import NormJudgeSearchResponse
from .raw_client import AsyncRawJudgeAnalyticsApiClient, RawJudgeAnalyticsApiClient


class JudgeAnalyticsApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJudgeAnalyticsApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJudgeAnalyticsApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJudgeAnalyticsApiClient
        """
        return self._raw_client

    def get_norm_judge_by_id(
        self, norm_judge_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NormJudge:
        """
        The Judge API allows you to look up Judge Details by normJudgeId.

        Parameters
        ----------
        norm_judge_id : str
            Norm  ID of the Judge.
              - minimum: 18
              - maximum: 18

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NormJudge
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.judge_analytics_api.get_norm_judge_by_id(
            norm_judge_id="NJUDT7jCZyFNeLGpRq",
        )
        """
        _response = self._raw_client.get_norm_judge_by_id(norm_judge_id, request_options=request_options)
        return _response.data

    def get_norm_attorneys_associated_with_norm_judge(
        self,
        norm_judge_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssociatedNormAttorneyResponse:
        """
        Returns a list of attorneys associated with a judge.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN ("COLODj4BBVTho3pKpz","COLOPUfJRhw5yPxgRi")**|
        | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all attorneys associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPATMYyaJekdgj2c and case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_judge_id : str
            Norm  ID of the Judge.
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
        AssociatedNormAttorneyResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.judge_analytics_api.get_norm_attorneys_associated_with_norm_judge(
            norm_judge_id="NJUDT7jCZyFNeLGpRq",
            page_number=1,
        )
        """
        _response = self._raw_client.get_norm_attorneys_associated_with_norm_judge(
            norm_judge_id, page_number=page_number, q=q, request_options=request_options
        )
        return _response.data

    def get_norm_law_firms_associated_with_norm_judge(
        self,
        norm_judge_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssociatedNormLawFirmResponse:
        """
        Returns a list of Law Firms a Judge has heard.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLOPUfJRhw5yPxgRi"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN ("COLODj4BBVTho3pKpz","COLOPUfJRhw5yPxgRi")**|
        | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo**  | Multiple Ids Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all Law Firms associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPATMYyaJekdgj2c and case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_judge_id : str
            Norm  ID of the Judge.
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
        client.judge_analytics_api.get_norm_law_firms_associated_with_norm_judge(
            norm_judge_id="NJUDT7jCZyFNeLGpRq",
            page_number=1,
        )
        """
        _response = self._raw_client.get_norm_law_firms_associated_with_norm_judge(
            norm_judge_id, page_number=page_number, q=q, request_options=request_options
        )
        return _response.data

    def get_norm_parties_associated_with_norm_judge(
        self,
        norm_judge_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssociatedNormPartyResponse:
        """
        Returns a list of Parties A Judge has seen.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN ("COLODj4BBVTho3pKpz","COLOPUfJRhw5yPxgRi")**|
        | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all Parties associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPATMYyaJekdgj2c and case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_judge_id : str
            Norm  ID of the Judge.
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
        client.judge_analytics_api.get_norm_parties_associated_with_norm_judge(
            norm_judge_id="NJUDT7jCZyFNeLGpRq",
            page_number=1,
        )
        """
        _response = self._raw_client.get_norm_parties_associated_with_norm_judge(
            norm_judge_id, page_number=page_number, q=q, request_options=request_options
        )
        return _response.data

    def search_normalized_judges(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NormJudgeSearchResponse:
        """
        ### All query parameters supported for this API can be found in below schema section. Schema --> NormJudgeSearchQueryObject

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
        NormJudgeSearchResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.judge_analytics_api.search_normalized_judges(
            q='normJudgeId:"NJUD5STmDbUZGukfQm"',
            page_number=1,
        )
        """
        _response = self._raw_client.search_normalized_judges(
            q=q, page_number=page_number, request_options=request_options
        )
        return _response.data

    def search_normalized_judges_by_id(
        self,
        norm_judge_search_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NormJudgeSearchResponse:
        """
        ### All query parameters supported for this API can be found in below schema section. Schema --> NormJudgeSearchQueryObject

        Parameters
        ----------
        norm_judge_search_id : str
            Norm judge Search information for the given normJudgeSearchId.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.
            - Minimum: 1
            - Maximum: 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NormJudgeSearchResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.judge_analytics_api.search_normalized_judges_by_id(
            norm_judge_search_id="JSRCNUSK3pLGe48QcU",
            page_number=1,
        )
        """
        _response = self._raw_client.search_normalized_judges_by_id(
            norm_judge_search_id, page_number=page_number, request_options=request_options
        )
        return _response.data


class AsyncJudgeAnalyticsApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJudgeAnalyticsApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJudgeAnalyticsApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJudgeAnalyticsApiClient
        """
        return self._raw_client

    async def get_norm_judge_by_id(
        self, norm_judge_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NormJudge:
        """
        The Judge API allows you to look up Judge Details by normJudgeId.

        Parameters
        ----------
        norm_judge_id : str
            Norm  ID of the Judge.
              - minimum: 18
              - maximum: 18

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NormJudge
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.judge_analytics_api.get_norm_judge_by_id(
                norm_judge_id="NJUDT7jCZyFNeLGpRq",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_norm_judge_by_id(norm_judge_id, request_options=request_options)
        return _response.data

    async def get_norm_attorneys_associated_with_norm_judge(
        self,
        norm_judge_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssociatedNormAttorneyResponse:
        """
        Returns a list of attorneys associated with a judge.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN ("COLODj4BBVTho3pKpz","COLOPUfJRhw5yPxgRi")**|
        | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all attorneys associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPATMYyaJekdgj2c and case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_judge_id : str
            Norm  ID of the Judge.
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
        AssociatedNormAttorneyResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.judge_analytics_api.get_norm_attorneys_associated_with_norm_judge(
                norm_judge_id="NJUDT7jCZyFNeLGpRq",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_norm_attorneys_associated_with_norm_judge(
            norm_judge_id, page_number=page_number, q=q, request_options=request_options
        )
        return _response.data

    async def get_norm_law_firms_associated_with_norm_judge(
        self,
        norm_judge_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssociatedNormLawFirmResponse:
        """
        Returns a list of Law Firms a Judge has heard.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLOPUfJRhw5yPxgRi"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN ("COLODj4BBVTho3pKpz","COLOPUfJRhw5yPxgRi")**|
        | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo**  | Multiple Ids Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all Law Firms associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPATMYyaJekdgj2c and case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_judge_id : str
            Norm  ID of the Judge.
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
            await client.judge_analytics_api.get_norm_law_firms_associated_with_norm_judge(
                norm_judge_id="NJUDT7jCZyFNeLGpRq",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_norm_law_firms_associated_with_norm_judge(
            norm_judge_id, page_number=page_number, q=q, request_options=request_options
        )
        return _response.data

    async def get_norm_parties_associated_with_norm_judge(
        self,
        norm_judge_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AssociatedNormPartyResponse:
        """
        Returns a list of Parties A Judge has seen.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtLocationId IN ("COLODj4BBVTho3pKpz","COLOPUfJRhw5yPxgRi")**|
        | **courtId** | Multiple Ids Allowed  |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed  |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed  |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed  |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed  |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed  |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple Ids Allowed  |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all Parties associated with judge with norm id NJUDT7jCZyFNeLGpRq of all cases with case type id CTYPATMYyaJekdgj2c and case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_judge_id : str
            Norm  ID of the Judge.
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
            await client.judge_analytics_api.get_norm_parties_associated_with_norm_judge(
                norm_judge_id="NJUDT7jCZyFNeLGpRq",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_norm_parties_associated_with_norm_judge(
            norm_judge_id, page_number=page_number, q=q, request_options=request_options
        )
        return _response.data

    async def search_normalized_judges(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NormJudgeSearchResponse:
        """
        ### All query parameters supported for this API can be found in below schema section. Schema --> NormJudgeSearchQueryObject

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
        NormJudgeSearchResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.judge_analytics_api.search_normalized_judges(
                q='normJudgeId:"NJUD5STmDbUZGukfQm"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_normalized_judges(
            q=q, page_number=page_number, request_options=request_options
        )
        return _response.data

    async def search_normalized_judges_by_id(
        self,
        norm_judge_search_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NormJudgeSearchResponse:
        """
        ### All query parameters supported for this API can be found in below schema section. Schema --> NormJudgeSearchQueryObject

        Parameters
        ----------
        norm_judge_search_id : str
            Norm judge Search information for the given normJudgeSearchId.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.
            - Minimum: 1
            - Maximum: 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NormJudgeSearchResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.judge_analytics_api.search_normalized_judges_by_id(
                norm_judge_search_id="JSRCNUSK3pLGe48QcU",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_normalized_judges_by_id(
            norm_judge_search_id, page_number=page_number, request_options=request_options
        )
        return _response.data
