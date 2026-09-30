

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
from ..types.dataset import Dataset
from ..types.substance_composition import SubstanceComposition
from .types.get_substance_composition_request_db import GetSubstanceCompositionRequestDb
from .types.get_substance_structures_request_db import GetSubstanceStructuresRequestDb
from .types.search_by_identifier_request_db import SearchByIdentifierRequestDb
from .types.search_by_identifier_request_representation import SearchByIdentifierRequestRepresentation
from .types.search_by_identifier_request_term import SearchByIdentifierRequestTerm
from .types.search_by_similarity_request_db import SearchBySimilarityRequestDb
from .types.search_by_similarity_request_type import SearchBySimilarityRequestType
from .types.search_by_smarts_request_db import SearchBySmartsRequestDb
from .types.search_by_smarts_request_type import SearchBySmartsRequestType
from pydantic import ValidationError


class RawStructuresClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[Dataset]:
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
        HttpResponse[Dataset]
            OK. Entries found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/query/compound/{encode_path_param(term)}/{encode_path_param(representation)}",
            method="GET",
            params={
                "search": search,
                "b64search": b64search,
                "casesens": casesens,
                "bundle_uri": bundle_uri,
                "sameas": sameas,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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
    ) -> HttpResponse[Dataset]:
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
        HttpResponse[Dataset]
            OK. Entries found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/query/similarity",
            method="GET",
            params={
                "search": search,
                "b64search": b64search,
                "type": type,
                "threshold": threshold,
                "dataset_uri": dataset_uri,
                "filterBySubstance": filter_by_substance,
                "bundle_uri": bundle_uri,
                "sameas": sameas,
                "mol": mol,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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
    ) -> HttpResponse[Dataset]:
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
        HttpResponse[Dataset]
            OK. Entries found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/query/smarts",
            method="GET",
            params={
                "search": search,
                "b64search": b64search,
                "type": type,
                "dataset_uri": dataset_uri,
                "filterBySubstance": filter_by_substance,
                "bundle_uri": bundle_uri,
                "sameas": sameas,
                "mol": mol,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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

    def get_substance_composition(
        self,
        db: GetSubstanceCompositionRequestDb,
        uuid_: str,
        *,
        all_: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubstanceComposition]:
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
        HttpResponse[SubstanceComposition]
            OK. compositions found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/substance/{encode_path_param(uuid_)}/composition",
            method="GET",
            params={
                "all": all_,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubstanceComposition,
                    parse_obj_as(
                        type_=SubstanceComposition,
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

    def get_substance_structures(
        self,
        db: GetSubstanceStructuresRequestDb,
        uuid_: str,
        *,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dataset]:
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
        HttpResponse[Dataset]
            OK. compositions found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/substance/{encode_path_param(uuid_)}/structures",
            method="GET",
            params={
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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


class AsyncRawStructuresClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[Dataset]:
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
        AsyncHttpResponse[Dataset]
            OK. Entries found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/query/compound/{encode_path_param(term)}/{encode_path_param(representation)}",
            method="GET",
            params={
                "search": search,
                "b64search": b64search,
                "casesens": casesens,
                "bundle_uri": bundle_uri,
                "sameas": sameas,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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
    ) -> AsyncHttpResponse[Dataset]:
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
        AsyncHttpResponse[Dataset]
            OK. Entries found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/query/similarity",
            method="GET",
            params={
                "search": search,
                "b64search": b64search,
                "type": type,
                "threshold": threshold,
                "dataset_uri": dataset_uri,
                "filterBySubstance": filter_by_substance,
                "bundle_uri": bundle_uri,
                "sameas": sameas,
                "mol": mol,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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
    ) -> AsyncHttpResponse[Dataset]:
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
        AsyncHttpResponse[Dataset]
            OK. Entries found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/query/smarts",
            method="GET",
            params={
                "search": search,
                "b64search": b64search,
                "type": type,
                "dataset_uri": dataset_uri,
                "filterBySubstance": filter_by_substance,
                "bundle_uri": bundle_uri,
                "sameas": sameas,
                "mol": mol,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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

    async def get_substance_composition(
        self,
        db: GetSubstanceCompositionRequestDb,
        uuid_: str,
        *,
        all_: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubstanceComposition]:
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
        AsyncHttpResponse[SubstanceComposition]
            OK. compositions found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/substance/{encode_path_param(uuid_)}/composition",
            method="GET",
            params={
                "all": all_,
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubstanceComposition,
                    parse_obj_as(
                        type_=SubstanceComposition,
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

    async def get_substance_structures(
        self,
        db: GetSubstanceStructuresRequestDb,
        uuid_: str,
        *,
        page: typing.Optional[int] = None,
        pagesize: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dataset]:
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
        AsyncHttpResponse[Dataset]
            OK. compositions found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"enm/{encode_path_param(db)}/substance/{encode_path_param(uuid_)}/structures",
            method="GET",
            params={
                "page": page,
                "pagesize": pagesize,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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
