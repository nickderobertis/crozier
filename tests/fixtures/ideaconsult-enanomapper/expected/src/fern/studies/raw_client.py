

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.facet import Facet
from ..types.investigation import Investigation
from ..types.substance_study import SubstanceStudy
from ..types.substance_study_summary import SubstanceStudySummary
from .types.get_endpoint_summary_request_db import GetEndpointSummaryRequestDb
from .types.get_endpoint_summary_request_top import GetEndpointSummaryRequestTop
from .types.get_investigation_results_request_db import GetInvestigationResultsRequestDb
from .types.get_investigation_results_request_type import GetInvestigationResultsRequestType
from .types.get_substance_study_request_db import GetSubstanceStudyRequestDb
from .types.get_substance_study_request_top import GetSubstanceStudyRequestTop
from .types.get_substance_study_summary_request_db import GetSubstanceStudySummaryRequestDb
from .types.get_substance_study_summary_request_top import GetSubstanceStudySummaryRequestTop
from pydantic import ValidationError


class RawStudiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[Investigation]:
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
        HttpResponse[Investigation]
            OK. Entries found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/investigation",
            method="GET",
            params={
                "type": type,
                "search": search,
                "inchikey": inchikey,
                "id": id,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Investigation,
                    parse_obj_as(
                        type_=Investigation,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_endpoint_summary(
        self,
        db: GetEndpointSummaryRequestDb,
        *,
        top: typing.Optional[GetEndpointSummaryRequestTop] = None,
        category: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Facet]:
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
        HttpResponse[Facet]
            OK.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/query/study",
            method="GET",
            params={
                "top": top,
                "category": category,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Facet,
                    parse_obj_as(
                        type_=Facet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
    ) -> HttpResponse[SubstanceStudy]:
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
        HttpResponse[SubstanceStudy]
            OK. Substances found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/substance/{encode_path_param(uuid_)}/study",
            method="GET",
            params={
                "top": top,
                "category": category,
                "property_uri": property_uri,
                "property": property,
                "investigation_uuid": investigation_uuid,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubstanceStudy,
                    parse_obj_as(
                        type_=SubstanceStudy,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
    ) -> HttpResponse[SubstanceStudySummary]:
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
        HttpResponse[SubstanceStudySummary]
            OK.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/substance/{encode_path_param(uuid_)}/studySummary",
            method="GET",
            params={
                "top": top,
                "category": category,
                "property_uri": property_uri,
                "property": property,
                "result": result,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubstanceStudySummary,
                    parse_obj_as(
                        type_=SubstanceStudySummary,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawStudiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[Investigation]:
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
        AsyncHttpResponse[Investigation]
            OK. Entries found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/investigation",
            method="GET",
            params={
                "type": type,
                "search": search,
                "inchikey": inchikey,
                "id": id,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Investigation,
                    parse_obj_as(
                        type_=Investigation,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_endpoint_summary(
        self,
        db: GetEndpointSummaryRequestDb,
        *,
        top: typing.Optional[GetEndpointSummaryRequestTop] = None,
        category: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Facet]:
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
        AsyncHttpResponse[Facet]
            OK.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/query/study",
            method="GET",
            params={
                "top": top,
                "category": category,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Facet,
                    parse_obj_as(
                        type_=Facet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
    ) -> AsyncHttpResponse[SubstanceStudy]:
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
        AsyncHttpResponse[SubstanceStudy]
            OK. Substances found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/substance/{encode_path_param(uuid_)}/study",
            method="GET",
            params={
                "top": top,
                "category": category,
                "property_uri": property_uri,
                "property": property,
                "investigation_uuid": investigation_uuid,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubstanceStudy,
                    parse_obj_as(
                        type_=SubstanceStudy,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
    ) -> AsyncHttpResponse[SubstanceStudySummary]:
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
        AsyncHttpResponse[SubstanceStudySummary]
            OK.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/substance/{encode_path_param(uuid_)}/studySummary",
            method="GET",
            params={
                "top": top,
                "category": category,
                "property_uri": property_uri,
                "property": property,
                "result": result,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubstanceStudySummary,
                    parse_obj_as(
                        type_=SubstanceStudySummary,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
