

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dataset import Dataset
from ..types.substance_composition import SubstanceComposition
from .raw_client import AsyncRawStructuresClient, RawStructuresClient
from .types.get_substance_composition_request_db import GetSubstanceCompositionRequestDb
from .types.get_substance_structures_request_db import GetSubstanceStructuresRequestDb
from .types.search_by_identifier_request_db import SearchByIdentifierRequestDb
from .types.search_by_identifier_request_representation import SearchByIdentifierRequestRepresentation
from .types.search_by_identifier_request_term import SearchByIdentifierRequestTerm
from .types.search_by_similarity_request_db import SearchBySimilarityRequestDb
from .types.search_by_similarity_request_type import SearchBySimilarityRequestType
from .types.search_by_smarts_request_db import SearchBySmartsRequestDb
from .types.search_by_smarts_request_type import SearchBySmartsRequestType


class StructuresClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStructuresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStructuresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStructuresClient
        """
        return self._raw_client

    def search_by_identifier(
        self,
        db: SearchByIdentifierRequestDb,
        term: SearchByIdentifierRequestTerm,
        representation: SearchByIdentifierRequestRepresentation,
        *,
        search: typing.Optional[str] = None,
        b64search: typing.Optional[str] = None,
        casesens: typing.Optional[bool] = None,
        bundle_uri: typing.Optional[str] = None,
        sameas: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Returns compounds found

        Parameters
        ----------
        db : SearchByIdentifierRequestDb
            Database ID

        term : SearchByIdentifierRequestTerm
            search term type

        representation : SearchByIdentifierRequestRepresentation

        search : typing.Optional[str]
            Compound identifier (SMILES, InChI, name, registry identifiers)

        b64search : typing.Optional[str]
            Base64 encoded mol file; if included, will be used instead of the 'search' parameter

        casesens : typing.Optional[bool]
            Case sensitive search if yes

        bundle_uri : typing.Optional[str]
            Bundle URI

        sameas : typing.Optional[str]
            Ontology URI to define groups of columns

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            OK. Entries found

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.structures.search_by_identifier(
            db="calibrate",
            term="search",
            representation="all",
        )
        """
        _response = self._raw_client.search_by_identifier(
            db,
            term,
            representation,
            search=search,
            b64search=b64search,
            casesens=casesens,
            bundle_uri=bundle_uri,
            sameas=sameas,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data

    def search_by_similarity(
        self,
        db: SearchBySimilarityRequestDb,
        *,
        search: typing.Optional[str] = None,
        b64search: typing.Optional[str] = None,
        type: typing.Optional[SearchBySimilarityRequestType] = None,
        threshold: typing.Optional[float] = None,
        dataset_uri: typing.Optional[str] = None,
        filter_by_substance: typing.Optional[bool] = None,
        bundle_uri: typing.Optional[str] = None,
        sameas: typing.Optional[str] = None,
        mol: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Returns similar compounds

        Parameters
        ----------
        db : SearchBySimilarityRequestDb
            Database ID

        search : typing.Optional[str]
            Compound identifier (SMILES, InChI, name, registry identifiers)

        b64search : typing.Optional[str]
            Base64 encoded mol file; if included, will be used instead of the 'search' parameter

        type : typing.Optional[SearchBySimilarityRequestType]
            Defines the expected content of the search parameter

        threshold : typing.Optional[float]
            Similarity threshold

        dataset_uri : typing.Optional[str]
            Restrict the search within the AMBIT dataset specified with the URI

        filter_by_substance : typing.Optional[bool]
            Restrict the search within the set of structures with assigned substances

        bundle_uri : typing.Optional[str]
            If the structure is used in the specified bundle URI, the selection tag will be returned

        sameas : typing.Optional[str]
            Ontology URI to define groups of columns

        mol : typing.Optional[bool]
            Only for application/json; to include mol as JSON field

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            OK. Entries found

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.structures.search_by_similarity(
            db="calibrate",
        )
        """
        _response = self._raw_client.search_by_similarity(
            db,
            search=search,
            b64search=b64search,
            type=type,
            threshold=threshold,
            dataset_uri=dataset_uri,
            filter_by_substance=filter_by_substance,
            bundle_uri=bundle_uri,
            sameas=sameas,
            mol=mol,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data

    def search_by_smarts(
        self,
        db: SearchBySmartsRequestDb,
        *,
        search: typing.Optional[str] = None,
        b64search: typing.Optional[str] = None,
        type: typing.Optional[SearchBySmartsRequestType] = None,
        dataset_uri: typing.Optional[str] = None,
        filter_by_substance: typing.Optional[bool] = None,
        bundle_uri: typing.Optional[str] = None,
        sameas: typing.Optional[str] = None,
        mol: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Returns compounds with the specified substructure

        Parameters
        ----------
        db : SearchBySmartsRequestDb
            Database ID

        search : typing.Optional[str]
            Compound identifier (SMILES, InChI, name, registry identifiers)

        b64search : typing.Optional[str]
            Base64 encoded mol file; if included, will be used instead of the 'search' parameter

        type : typing.Optional[SearchBySmartsRequestType]
            Defines the expected content of the search parameter

        dataset_uri : typing.Optional[str]
            Restrict the search within the AMBIT dataset specified with the URI

        filter_by_substance : typing.Optional[bool]
            Restrict the search within the set of structures with assigned substances

        bundle_uri : typing.Optional[str]
            If the structure is used in the specified bundle URI, the selection tag will be returned

        sameas : typing.Optional[str]
            Ontology URI to define groups of columns

        mol : typing.Optional[bool]
            Only for application/json; to include mol as JSON field

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            OK. Entries found

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.structures.search_by_smarts(
            db="calibrate",
        )
        """
        _response = self._raw_client.search_by_smarts(
            db,
            search=search,
            b64search=b64search,
            type=type,
            dataset_uri=dataset_uri,
            filter_by_substance=filter_by_substance,
            bundle_uri=bundle_uri,
            sameas=sameas,
            mol=mol,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data

    def get_substance_composition(
        self,
        db: GetSubstanceCompositionRequestDb,
        uuid_: str,
        *,
        all_: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubstanceComposition:
        """
        Returns substance composition

        Parameters
        ----------
        db : GetSubstanceCompositionRequestDb
            Database ID

        uuid_ : str
            Substance UUID

        all_ : typing.Optional[bool]
            true (Show all compositions) false (do not show hidden compositions)

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubstanceComposition
            OK. compositions found

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.structures.get_substance_composition(
            db="calibrate",
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_substance_composition(
            db, uuid_, all_=all_, page=page, pagesize=pagesize, request_options=request_options
        )
        return _response.data

    def get_substance_structures(
        self,
        db: GetSubstanceStructuresRequestDb,
        uuid_: str,
        *,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Returns substance composition

        Parameters
        ----------
        db : GetSubstanceStructuresRequestDb
            Database ID

        uuid_ : str
            Substance UUID

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            OK. compositions found

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.structures.get_substance_structures(
            db="calibrate",
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_substance_structures(
            db, uuid_, page=page, pagesize=pagesize, request_options=request_options
        )
        return _response.data


class AsyncStructuresClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStructuresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStructuresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStructuresClient
        """
        return self._raw_client

    async def search_by_identifier(
        self,
        db: SearchByIdentifierRequestDb,
        term: SearchByIdentifierRequestTerm,
        representation: SearchByIdentifierRequestRepresentation,
        *,
        search: typing.Optional[str] = None,
        b64search: typing.Optional[str] = None,
        casesens: typing.Optional[bool] = None,
        bundle_uri: typing.Optional[str] = None,
        sameas: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Returns compounds found

        Parameters
        ----------
        db : SearchByIdentifierRequestDb
            Database ID

        term : SearchByIdentifierRequestTerm
            search term type

        representation : SearchByIdentifierRequestRepresentation

        search : typing.Optional[str]
            Compound identifier (SMILES, InChI, name, registry identifiers)

        b64search : typing.Optional[str]
            Base64 encoded mol file; if included, will be used instead of the 'search' parameter

        casesens : typing.Optional[bool]
            Case sensitive search if yes

        bundle_uri : typing.Optional[str]
            Bundle URI

        sameas : typing.Optional[str]
            Ontology URI to define groups of columns

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            OK. Entries found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.structures.search_by_identifier(
                db="calibrate",
                term="search",
                representation="all",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_by_identifier(
            db,
            term,
            representation,
            search=search,
            b64search=b64search,
            casesens=casesens,
            bundle_uri=bundle_uri,
            sameas=sameas,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data

    async def search_by_similarity(
        self,
        db: SearchBySimilarityRequestDb,
        *,
        search: typing.Optional[str] = None,
        b64search: typing.Optional[str] = None,
        type: typing.Optional[SearchBySimilarityRequestType] = None,
        threshold: typing.Optional[float] = None,
        dataset_uri: typing.Optional[str] = None,
        filter_by_substance: typing.Optional[bool] = None,
        bundle_uri: typing.Optional[str] = None,
        sameas: typing.Optional[str] = None,
        mol: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Returns similar compounds

        Parameters
        ----------
        db : SearchBySimilarityRequestDb
            Database ID

        search : typing.Optional[str]
            Compound identifier (SMILES, InChI, name, registry identifiers)

        b64search : typing.Optional[str]
            Base64 encoded mol file; if included, will be used instead of the 'search' parameter

        type : typing.Optional[SearchBySimilarityRequestType]
            Defines the expected content of the search parameter

        threshold : typing.Optional[float]
            Similarity threshold

        dataset_uri : typing.Optional[str]
            Restrict the search within the AMBIT dataset specified with the URI

        filter_by_substance : typing.Optional[bool]
            Restrict the search within the set of structures with assigned substances

        bundle_uri : typing.Optional[str]
            If the structure is used in the specified bundle URI, the selection tag will be returned

        sameas : typing.Optional[str]
            Ontology URI to define groups of columns

        mol : typing.Optional[bool]
            Only for application/json; to include mol as JSON field

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            OK. Entries found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.structures.search_by_similarity(
                db="calibrate",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_by_similarity(
            db,
            search=search,
            b64search=b64search,
            type=type,
            threshold=threshold,
            dataset_uri=dataset_uri,
            filter_by_substance=filter_by_substance,
            bundle_uri=bundle_uri,
            sameas=sameas,
            mol=mol,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data

    async def search_by_smarts(
        self,
        db: SearchBySmartsRequestDb,
        *,
        search: typing.Optional[str] = None,
        b64search: typing.Optional[str] = None,
        type: typing.Optional[SearchBySmartsRequestType] = None,
        dataset_uri: typing.Optional[str] = None,
        filter_by_substance: typing.Optional[bool] = None,
        bundle_uri: typing.Optional[str] = None,
        sameas: typing.Optional[str] = None,
        mol: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Returns compounds with the specified substructure

        Parameters
        ----------
        db : SearchBySmartsRequestDb
            Database ID

        search : typing.Optional[str]
            Compound identifier (SMILES, InChI, name, registry identifiers)

        b64search : typing.Optional[str]
            Base64 encoded mol file; if included, will be used instead of the 'search' parameter

        type : typing.Optional[SearchBySmartsRequestType]
            Defines the expected content of the search parameter

        dataset_uri : typing.Optional[str]
            Restrict the search within the AMBIT dataset specified with the URI

        filter_by_substance : typing.Optional[bool]
            Restrict the search within the set of structures with assigned substances

        bundle_uri : typing.Optional[str]
            If the structure is used in the specified bundle URI, the selection tag will be returned

        sameas : typing.Optional[str]
            Ontology URI to define groups of columns

        mol : typing.Optional[bool]
            Only for application/json; to include mol as JSON field

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            OK. Entries found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.structures.search_by_smarts(
                db="calibrate",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_by_smarts(
            db,
            search=search,
            b64search=b64search,
            type=type,
            dataset_uri=dataset_uri,
            filter_by_substance=filter_by_substance,
            bundle_uri=bundle_uri,
            sameas=sameas,
            mol=mol,
            page=page,
            pagesize=pagesize,
            request_options=request_options,
        )
        return _response.data

    async def get_substance_composition(
        self,
        db: GetSubstanceCompositionRequestDb,
        uuid_: str,
        *,
        all_: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubstanceComposition:
        """
        Returns substance composition

        Parameters
        ----------
        db : GetSubstanceCompositionRequestDb
            Database ID

        uuid_ : str
            Substance UUID

        all_ : typing.Optional[bool]
            true (Show all compositions) false (do not show hidden compositions)

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubstanceComposition
            OK. compositions found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.structures.get_substance_composition(
                db="calibrate",
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_substance_composition(
            db, uuid_, all_=all_, page=page, pagesize=pagesize, request_options=request_options
        )
        return _response.data

    async def get_substance_structures(
        self,
        db: GetSubstanceStructuresRequestDb,
        uuid_: str,
        *,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Returns substance composition

        Parameters
        ----------
        db : GetSubstanceStructuresRequestDb
            Database ID

        uuid_ : str
            Substance UUID

        page : typing.Optional[int]
            Starting page

        pagesize : typing.Optional[int]
            Page size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            OK. compositions found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.structures.get_substance_structures(
                db="calibrate",
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_substance_structures(
            db, uuid_, page=page, pagesize=pagesize, request_options=request_options
        )
        return _response.data
