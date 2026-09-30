

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPublicationsClient, RawPublicationsClient
from .types.search7request_format import Search7RequestFormat


class PublicationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPublicationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPublicationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPublicationsClient
        """
        return self._raw_client

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.publications.search7()
        """
        _response = self._raw_client.search7(
            format=format,
            keywords=keywords,
            title=title,
            author=author,
            doi=doi,
            orcid=orcid,
            from_date_accepted=from_date_accepted,
            to_date_accepted=to_date_accepted,
            openaire_provider_id=openaire_provider_id,
            openaire_project_id=openaire_project_id,
            has_project=has_project,
            project_id=project_id,
            funder=funder,
            funding_stream=funding_stream,
            has_ec_funding=has_ec_funding,
            has_wt_funding=has_wt_funding,
            country=country,
            influence=influence,
            popularity=popularity,
            impulse=impulse,
            citation_count=citation_count,
            instancetype=instancetype,
            original_id=original_id,
            sdg=sdg,
            fos=fos,
            openaire_publication_id=openaire_publication_id,
            peer_reviewed=peer_reviewed,
            diamond_journal=diamond_journal,
            publicly_funded=publicly_funded,
            green=green,
            open_access_color=open_access_color,
            sort_by=sort_by,
            page=page,
            size=size,
            cursor_mark=cursor_mark,
            request_options=request_options,
        )
        return _response.data


class AsyncPublicationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPublicationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPublicationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPublicationsClient
        """
        return self._raw_client

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
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.publications.search7()


        asyncio.run(main())
        """
        _response = await self._raw_client.search7(
            format=format,
            keywords=keywords,
            title=title,
            author=author,
            doi=doi,
            orcid=orcid,
            from_date_accepted=from_date_accepted,
            to_date_accepted=to_date_accepted,
            openaire_provider_id=openaire_provider_id,
            openaire_project_id=openaire_project_id,
            has_project=has_project,
            project_id=project_id,
            funder=funder,
            funding_stream=funding_stream,
            has_ec_funding=has_ec_funding,
            has_wt_funding=has_wt_funding,
            country=country,
            influence=influence,
            popularity=popularity,
            impulse=impulse,
            citation_count=citation_count,
            instancetype=instancetype,
            original_id=original_id,
            sdg=sdg,
            fos=fos,
            openaire_publication_id=openaire_publication_id,
            peer_reviewed=peer_reviewed,
            diamond_journal=diamond_journal,
            publicly_funded=publicly_funded,
            green=green,
            open_access_color=open_access_color,
            sort_by=sort_by,
            page=page,
            size=size,
            cursor_mark=cursor_mark,
            request_options=request_options,
        )
        return _response.data
