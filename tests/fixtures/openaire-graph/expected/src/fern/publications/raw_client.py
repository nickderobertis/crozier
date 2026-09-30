

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from .types.search7request_format import Search7RequestFormat
from pydantic import ValidationError


class RawPublicationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search7(
        self,
        *,
        format: typing.Optional[Search7RequestFormat] = None,
        keywords: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
        doi: typing.Optional[str] = None,
        orcid: typing.Optional[str] = None,
        from_date_accepted: typing.Optional[str] = None,
        to_date_accepted: typing.Optional[str] = None,
        openaire_provider_id: typing.Optional[str] = None,
        openaire_project_id: typing.Optional[str] = None,
        has_project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        funder: typing.Optional[str] = None,
        funding_stream: typing.Optional[str] = None,
        has_ec_funding: typing.Optional[str] = None,
        has_wt_funding: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        influence: typing.Optional[str] = None,
        popularity: typing.Optional[str] = None,
        impulse: typing.Optional[str] = None,
        citation_count: typing.Optional[str] = None,
        instancetype: typing.Optional[str] = None,
        original_id: typing.Optional[str] = None,
        sdg: typing.Optional[str] = None,
        fos: typing.Optional[str] = None,
        openaire_publication_id: typing.Optional[str] = None,
        peer_reviewed: typing.Optional[str] = None,
        diamond_journal: typing.Optional[str] = None,
        publicly_funded: typing.Optional[str] = None,
        green: typing.Optional[str] = None,
        open_access_color: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        size: typing.Optional[str] = None,
        cursor_mark: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Search and filter publications using the legacy XML API format.

        Parameters
        ----------
        format : typing.Optional[Search7RequestFormat]
            Response format

        keywords : typing.Optional[str]
            Keyword-based search in title, description, authors, etc.

        title : typing.Optional[str]
            Search in publication title

        author : typing.Optional[str]
            Search by author name/surname

        doi : typing.Optional[str]
            Filter by DOI(s)

        orcid : typing.Optional[str]
            Filter by author ORCID(s)

        from_date_accepted : typing.Optional[str]
            Filter from date of acceptance (YYYY-MM-DD)

        to_date_accepted : typing.Optional[str]
            Filter to date of acceptance (YYYY-MM-DD)

        openaire_provider_id : typing.Optional[str]
            Filter by OpenAIRE provider ID(s)

        openaire_project_id : typing.Optional[str]
            Filter by OpenAIRE project ID(s)

        has_project : typing.Optional[str]
            Filter research products that have a link to a project

        project_id : typing.Optional[str]
            Filter by project grant number

        funder : typing.Optional[str]
            Filter by funder shortname(s)

        funding_stream : typing.Optional[str]
            Filter by funding stream

        has_ec_funding : typing.Optional[str]
            Filter projects with EC funding

        has_wt_funding : typing.Optional[str]
            Filter projects with Wellcome Trust funding

        country : typing.Optional[str]
            Filter by country code

        influence : typing.Optional[str]
            Filter by influence class (C1-C5)

        popularity : typing.Optional[str]
            Filter by popularity class (C1-C5)

        impulse : typing.Optional[str]
            Filter by impulse class (C1-C5)

        citation_count : typing.Optional[str]
            Filter by citation count class (C1-C5)

        instancetype : typing.Optional[str]
            Filter by publication instance type

        original_id : typing.Optional[str]
            Filter by original identifier(s)

        sdg : typing.Optional[str]
            Filter by Sustainable Development Goal number (1-17)

        fos : typing.Optional[str]
            Filter by Field of Science classification value

        openaire_publication_id : typing.Optional[str]
            Filter by OpenAIRE publication ID(s)

        peer_reviewed : typing.Optional[str]
            Filter by peer review status

        diamond_journal : typing.Optional[str]
            Filter by diamond journal status

        publicly_funded : typing.Optional[str]
            Filter by publicly funded status

        green : typing.Optional[str]
            Filter by green open access status

        open_access_color : typing.Optional[str]
            Filter by open access color (gold, bronze, hybrid)

        sort_by : typing.Optional[str]
            sortBy=field,[ascending|descending] <br>
            'field' is one of: projectstartdate, projectstartyear, projectenddate, projectendyear, projectduration

        page : typing.Optional[str]
            Page number

        size : typing.Optional[str]
            Number of results per page (max 100)

        cursor_mark : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "search/publications",
            method="GET",
            params={
                "format": format,
                "keywords": keywords,
                "title": title,
                "author": author,
                "doi": doi,
                "orcid": orcid,
                "fromDateAccepted": from_date_accepted,
                "toDateAccepted": to_date_accepted,
                "openaireProviderID": openaire_provider_id,
                "openaireProjectID": openaire_project_id,
                "hasProject": has_project,
                "projectID": project_id,
                "funder": funder,
                "fundingStream": funding_stream,
                "hasECFunding": has_ec_funding,
                "hasWTFunding": has_wt_funding,
                "country": country,
                "influence": influence,
                "popularity": popularity,
                "impulse": impulse,
                "citationCount": citation_count,
                "instancetype": instancetype,
                "originalId": original_id,
                "sdg": sdg,
                "fos": fos,
                "openairePublicationID": openaire_publication_id,
                "peerReviewed": peer_reviewed,
                "diamondJournal": diamond_journal,
                "publiclyFunded": publicly_funded,
                "green": green,
                "openAccessColor": open_access_color,
                "sortBy": sort_by,
                "page": page,
                "size": size,
                "cursorMark": cursor_mark,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawPublicationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search7(
        self,
        *,
        format: typing.Optional[Search7RequestFormat] = None,
        keywords: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        author: typing.Optional[str] = None,
        doi: typing.Optional[str] = None,
        orcid: typing.Optional[str] = None,
        from_date_accepted: typing.Optional[str] = None,
        to_date_accepted: typing.Optional[str] = None,
        openaire_provider_id: typing.Optional[str] = None,
        openaire_project_id: typing.Optional[str] = None,
        has_project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        funder: typing.Optional[str] = None,
        funding_stream: typing.Optional[str] = None,
        has_ec_funding: typing.Optional[str] = None,
        has_wt_funding: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        influence: typing.Optional[str] = None,
        popularity: typing.Optional[str] = None,
        impulse: typing.Optional[str] = None,
        citation_count: typing.Optional[str] = None,
        instancetype: typing.Optional[str] = None,
        original_id: typing.Optional[str] = None,
        sdg: typing.Optional[str] = None,
        fos: typing.Optional[str] = None,
        openaire_publication_id: typing.Optional[str] = None,
        peer_reviewed: typing.Optional[str] = None,
        diamond_journal: typing.Optional[str] = None,
        publicly_funded: typing.Optional[str] = None,
        green: typing.Optional[str] = None,
        open_access_color: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        page: typing.Optional[str] = None,
        size: typing.Optional[str] = None,
        cursor_mark: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Search and filter publications using the legacy XML API format.

        Parameters
        ----------
        format : typing.Optional[Search7RequestFormat]
            Response format

        keywords : typing.Optional[str]
            Keyword-based search in title, description, authors, etc.

        title : typing.Optional[str]
            Search in publication title

        author : typing.Optional[str]
            Search by author name/surname

        doi : typing.Optional[str]
            Filter by DOI(s)

        orcid : typing.Optional[str]
            Filter by author ORCID(s)

        from_date_accepted : typing.Optional[str]
            Filter from date of acceptance (YYYY-MM-DD)

        to_date_accepted : typing.Optional[str]
            Filter to date of acceptance (YYYY-MM-DD)

        openaire_provider_id : typing.Optional[str]
            Filter by OpenAIRE provider ID(s)

        openaire_project_id : typing.Optional[str]
            Filter by OpenAIRE project ID(s)

        has_project : typing.Optional[str]
            Filter research products that have a link to a project

        project_id : typing.Optional[str]
            Filter by project grant number

        funder : typing.Optional[str]
            Filter by funder shortname(s)

        funding_stream : typing.Optional[str]
            Filter by funding stream

        has_ec_funding : typing.Optional[str]
            Filter projects with EC funding

        has_wt_funding : typing.Optional[str]
            Filter projects with Wellcome Trust funding

        country : typing.Optional[str]
            Filter by country code

        influence : typing.Optional[str]
            Filter by influence class (C1-C5)

        popularity : typing.Optional[str]
            Filter by popularity class (C1-C5)

        impulse : typing.Optional[str]
            Filter by impulse class (C1-C5)

        citation_count : typing.Optional[str]
            Filter by citation count class (C1-C5)

        instancetype : typing.Optional[str]
            Filter by publication instance type

        original_id : typing.Optional[str]
            Filter by original identifier(s)

        sdg : typing.Optional[str]
            Filter by Sustainable Development Goal number (1-17)

        fos : typing.Optional[str]
            Filter by Field of Science classification value

        openaire_publication_id : typing.Optional[str]
            Filter by OpenAIRE publication ID(s)

        peer_reviewed : typing.Optional[str]
            Filter by peer review status

        diamond_journal : typing.Optional[str]
            Filter by diamond journal status

        publicly_funded : typing.Optional[str]
            Filter by publicly funded status

        green : typing.Optional[str]
            Filter by green open access status

        open_access_color : typing.Optional[str]
            Filter by open access color (gold, bronze, hybrid)

        sort_by : typing.Optional[str]
            sortBy=field,[ascending|descending] <br>
            'field' is one of: projectstartdate, projectstartyear, projectenddate, projectendyear, projectduration

        page : typing.Optional[str]
            Page number

        size : typing.Optional[str]
            Number of results per page (max 100)

        cursor_mark : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "search/publications",
            method="GET",
            params={
                "format": format,
                "keywords": keywords,
                "title": title,
                "author": author,
                "doi": doi,
                "orcid": orcid,
                "fromDateAccepted": from_date_accepted,
                "toDateAccepted": to_date_accepted,
                "openaireProviderID": openaire_provider_id,
                "openaireProjectID": openaire_project_id,
                "hasProject": has_project,
                "projectID": project_id,
                "funder": funder,
                "fundingStream": funding_stream,
                "hasECFunding": has_ec_funding,
                "hasWTFunding": has_wt_funding,
                "country": country,
                "influence": influence,
                "popularity": popularity,
                "impulse": impulse,
                "citationCount": citation_count,
                "instancetype": instancetype,
                "originalId": original_id,
                "sdg": sdg,
                "fos": fos,
                "openairePublicationID": openaire_publication_id,
                "peerReviewed": peer_reviewed,
                "diamondJournal": diamond_journal,
                "publiclyFunded": publicly_funded,
                "green": green,
                "openAccessColor": open_access_color,
                "sortBy": sort_by,
                "page": page,
                "size": size,
                "cursorMark": cursor_mark,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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
