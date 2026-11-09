

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.associated_norm_attorney_response import AssociatedNormAttorneyResponse
from ..types.associated_norm_judge_response import AssociatedNormJudgeResponse
from ..types.associated_norm_law_firm_response import AssociatedNormLawFirmResponse
from ..types.exception import Exception
from ..types.norm_party import NormParty
from ..types.norm_party_search_response import NormPartySearchResponse
from pydantic import ValidationError


class RawPartyAnalyticsApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_norm_party_by_id(
        self, norm_party_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NormParty]:
        """
        The Party Details API allows you to look up Parties by normPartyId.

        Parameters
        ----------
        norm_party_id : str
            Norm ID of the Party.
              - minimum: 18
              - maximum: 18

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NormParty]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"normParty/{encode_path_param(norm_party_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NormParty,
                    parse_obj_as(
                        type_=NormParty,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_norm_attorneys_associated_with_norm_party(
        self,
        norm_party_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AssociatedNormAttorneyResponse]:
        """
        Returns a list of  Attorneys the Party has been represented by.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz","CORTYsomR6GiiiPovp")**|
        | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all attorneys associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_party_id : str
            Norm ID of the Party.
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
        HttpResponse[AssociatedNormAttorneyResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"normParty/{encode_path_param(norm_party_id)}/associatedNormAttorneys",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AssociatedNormAttorneyResponse,
                    parse_obj_as(
                        type_=AssociatedNormAttorneyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_norm_judges_associated_with_norm_party(
        self,
        norm_party_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AssociatedNormJudgeResponse]:
        """
        Returns a list of Judges the party has faced.
        <br><br>
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz","CORTYsomR6GiiiPovp")**|
        | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all judges associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_party_id : str
            Norm ID of the Party.
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
        HttpResponse[AssociatedNormJudgeResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"normParty/{encode_path_param(norm_party_id)}/associatedNormJudges",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AssociatedNormJudgeResponse,
                    parse_obj_as(
                        type_=AssociatedNormJudgeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_norm_law_firms_associated_with_norm_party(
        self,
        norm_party_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AssociatedNormLawFirmResponse]:
        """
        Returns a list of Law Firms the Party has been represented by.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz","CORTYsomR6GiiiPovp")**|
        | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all lawfirms associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]

        Parameters
        ----------
        norm_party_id : str
            Norm ID of the Party.
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
        HttpResponse[AssociatedNormLawFirmResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"normParty/{encode_path_param(norm_party_id)}/associatedNormLawFirms",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AssociatedNormLawFirmResponse,
                    parse_obj_as(
                        type_=AssociatedNormLawFirmResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_normalized_parties(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NormPartySearchResponse]:
        """
        ### All query parameters supported for this API can be found in below schema section. Schema --> NormPartySearchQueryObject

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
        HttpResponse[NormPartySearchResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "normPartySearch",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NormPartySearchResponse,
                    parse_obj_as(
                        type_=NormPartySearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_normalized_parties_by_id(
        self,
        norm_party_search_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NormPartySearchResponse]:
        """
        ### All query parameters supported for this API can be found in below schema section. Schema --> NormPartySearchQueryObject

        Parameters
        ----------
        norm_party_search_id : str
            Norm Party Search information for the given normPartySearchId.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.
            - Minimum: 1
            - Maximum: 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NormPartySearchResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"normPartySearch/{encode_path_param(norm_party_search_id)}",
            method="GET",
            params={
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NormPartySearchResponse,
                    parse_obj_as(
                        type_=NormPartySearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPartyAnalyticsApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_norm_party_by_id(
        self, norm_party_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NormParty]:
        """
        The Party Details API allows you to look up Parties by normPartyId.

        Parameters
        ----------
        norm_party_id : str
            Norm ID of the Party.
              - minimum: 18
              - maximum: 18

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NormParty]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"normParty/{encode_path_param(norm_party_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NormParty,
                    parse_obj_as(
                        type_=NormParty,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_norm_attorneys_associated_with_norm_party(
        self,
        norm_party_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AssociatedNormAttorneyResponse]:
        """
        Returns a list of  Attorneys the Party has been represented by.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz","CORTYsomR6GiiiPovp")**|
        | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all attorneys associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_party_id : str
            Norm ID of the Party.
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
        AsyncHttpResponse[AssociatedNormAttorneyResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"normParty/{encode_path_param(norm_party_id)}/associatedNormAttorneys",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AssociatedNormAttorneyResponse,
                    parse_obj_as(
                        type_=AssociatedNormAttorneyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_norm_judges_associated_with_norm_party(
        self,
        norm_party_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AssociatedNormJudgeResponse]:
        """
        Returns a list of Judges the party has faced.
        <br><br>
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz","CORTYsomR6GiiiPovp")**|
        | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **caseFiledDate** | Single Allowed  |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all judges associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]
        <br><br>

        Parameters
        ----------
        norm_party_id : str
            Norm ID of the Party.
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
        AsyncHttpResponse[AssociatedNormJudgeResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"normParty/{encode_path_param(norm_party_id)}/associatedNormJudges",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AssociatedNormJudgeResponse,
                    parse_obj_as(
                        type_=AssociatedNormJudgeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_norm_law_firms_associated_with_norm_party(
        self,
        norm_party_id: str,
        *,
        page_number: int,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AssociatedNormLawFirmResponse]:
        """
        Returns a list of Law Firms the Party has been represented by.
        ## Terms and Connectors
        | Connector | Schema   | Description  | Example |
        | ------| ------| ------|------|
        | **AND** ||Find analytics containing all connected terms. The word AND does not have to be capitalized.|**courtId:"CORTV4vCEaKrhystBz" AND courtLocationId:"COLO6b82CkRqS846hx"**|
        | **IN()** || Allows you to specify multiple values, for a limit of up to 10.| **courtId IN ("CORTV4vCEaKrhystBz","CORTYsomR6GiiiPovp")**|
        | **courtId** | Multiple Ids Allowed |Find Analytics for a particular Court Object. | **courtId:"CORTV4vCEaKrhystBz"** |
        | **courtSystemId** | Multiple Ids Allowed |Find Analytics for a particular Court System Object. | **courtSystemId:"COSYACHBdMewtaG5DY"** |
        | **courtTypeId** | Multiple Ids Allowed |Find Analytics for a particular Court Type Object. | **courtTypeId:"COTPm8jjc2PAydpFhq"** |
        | **courtLocationId** | Multiple Ids Allowed |Find Analytics for a particular Court Location Object. | **courtLocationId:"COLO6b82CkRqS846hx"** |
        | **caseTypeId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Object. | **caseTypeId:"CTYPATMYyaJekdgj2c"** |
        | **caseTypeGroupId** | Multiple Ids Allowed |Find Analytics for a particular Case Type Group Object. | **caseTypeGroupId:"CTYG8gZ6hPRKhhYi4Y"** |
        | **areaOfLawId** | Multiple Ids Allowed |Find Analytics for a particular Area Of Law Object. | **areaOfLawId:"AOFL2UxEWfVmTPMyqf"** |
        | **caseClassId** | Multiple Ids Allowed |Find Analytics for a particular Case Class Category Object. | **caseClassId:"CSCLNjbKTN7Yfo2wdb"** |
        | **partyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Object. | **partyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **partyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Party Type Group Object. | **partyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **attorneyPartyRoleId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Object. | **attorneyPartyRoleId:"PTYRiP8nMgPxBsPc5i"** |
        | **attorneyPartyRoleGroupId** | Multiple Ids Allowed |Find Analytics for a particular Attorney Party Type Group Object. | **attorneyPartyRoleGroupId:"PTYGBnjxbx6tKNfVEP"** |
        | **caseFiledDate** | Single Allowed |Find Analytics within a particular date range. | **caseFiledDate:[2018-05-08T00:00:00+00:00TO2019-05-08T00:00:00+00:00]** |
        | **JurisdictionGeo** | Multiple filters Allowed |Find Analytics within a particular Jurisdiction Geo. | **(JurisdictionGeo:(state:"California"))** |
        | **confidenceScore** | Single Allowed |Find Analytics for a given ConfidenceScore  | **confidenceScore:[0.5 TO \\*]** |
        | **bestMatch** | Single Allowed |True if the normEntity has the highest Confidence Score of all possible normEntities | **bestMatch:true** |
        <br>
        ## Example Query
        Query to get all lawfirms associated with Party with norm id NORGrPmQyLdx9NGHcT of all cases with case type id CTYPATMYyaJekdgj2c and  case filed date between Jan 1st, 2017 to Nov 30th,2021<br>
        q=caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]

        Parameters
        ----------
        norm_party_id : str
            Norm ID of the Party.
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
        AsyncHttpResponse[AssociatedNormLawFirmResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"normParty/{encode_path_param(norm_party_id)}/associatedNormLawFirms",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AssociatedNormLawFirmResponse,
                    parse_obj_as(
                        type_=AssociatedNormLawFirmResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_normalized_parties(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NormPartySearchResponse]:
        """
        ### All query parameters supported for this API can be found in below schema section. Schema --> NormPartySearchQueryObject

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
        AsyncHttpResponse[NormPartySearchResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "normPartySearch",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NormPartySearchResponse,
                    parse_obj_as(
                        type_=NormPartySearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_normalized_parties_by_id(
        self,
        norm_party_search_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NormPartySearchResponse]:
        """
        ### All query parameters supported for this API can be found in below schema section. Schema --> NormPartySearchQueryObject

        Parameters
        ----------
        norm_party_search_id : str
            Norm Party Search information for the given normPartySearchId.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.
            - Minimum: 1
            - Maximum: 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NormPartySearchResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"normPartySearch/{encode_path_param(norm_party_search_id)}",
            method="GET",
            params={
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NormPartySearchResponse,
                    parse_obj_as(
                        type_=NormPartySearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
