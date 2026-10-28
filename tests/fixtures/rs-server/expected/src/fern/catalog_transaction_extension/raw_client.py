

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.asset import Asset
from ..types.collection_input_summaries_value import CollectionInputSummariesValue
from ..types.collection_input_type import CollectionInputType
from ..types.extent import Extent
from ..types.http_validation_error import HttpValidationError
from ..types.item_input_geometry import ItemInputGeometry
from ..types.item_input_type import ItemInputType
from ..types.item_properties import ItemProperties
from ..types.links_input import LinksInput
from ..types.provider import Provider
from ..types.stac_pydantic_collection_collection_output import StacPydanticCollectionCollectionOutput
from ..types.stac_pydantic_item_item_output import StacPydanticItemItemOutput
from .types.create_item_catalog_collections_collection_id_items_post_request_body import (
    CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody,
)
from .types.patch_collection_catalog_collections_collection_id_patch_request_body import (
    PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody,
)
from .types.patch_item_catalog_collections_collection_id_items_item_id_patch_request_body import (
    PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCatalogTransactionExtensionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def update_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        type: ItemInputType,
        properties: ItemProperties,
        id: str,
        assets: typing.Dict[str, Asset],
        links: LinksInput,
        bbox: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        geometry: typing.Optional[ItemInputGeometry] = OMIT,
        stac_version: typing.Optional[str] = OMIT,
        stac_extensions: typing.Optional[typing.Sequence[str]] = OMIT,
        collection: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StacPydanticItemItemOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        type : ItemInputType

        properties : ItemProperties

        id : str

        assets : typing.Dict[str, Asset]

        links : LinksInput

        bbox : typing.Optional[typing.Sequence[typing.Any]]

        geometry : typing.Optional[ItemInputGeometry]

        stac_version : typing.Optional[str]

        stac_extensions : typing.Optional[typing.Sequence[str]]

        collection : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StacPydanticItemItemOutput]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}/items/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "bbox": bbox,
                "type": type,
                "geometry": convert_and_respect_annotation_metadata(
                    object_=geometry, annotation=typing.Optional[ItemInputGeometry], direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=ItemProperties, direction="write"
                ),
                "id": id,
                "stac_version": stac_version,
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets, annotation=typing.Dict[str, Asset], direction="write"
                ),
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=LinksInput, direction="write"
                ),
                "stac_extensions": stac_extensions,
                "collection": collection,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticItemItemOutput,
                    parse_obj_as(
                        type_=StacPydanticItemItemOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def delete_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StacPydanticItemItemOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StacPydanticItemItemOutput]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}/items/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticItemItemOutput,
                    parse_obj_as(
                        type_=StacPydanticItemItemOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def patch_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        request: PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StacPydanticItemItemOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        request : PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StacPydanticItemItemOutput]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}/items/{encode_path_param(item_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody,
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticItemItemOutput,
                    parse_obj_as(
                        type_=StacPydanticItemItemOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def create_collection(
        self,
        *,
        id: str,
        description: str,
        links: LinksInput,
        type: CollectionInputType,
        license: str,
        extent: Extent,
        stac_version: typing.Optional[str] = OMIT,
        stac_extensions: typing.Optional[typing.Sequence[str]] = OMIT,
        title: typing.Optional[str] = OMIT,
        assets: typing.Optional[typing.Dict[str, typing.Optional[Asset]]] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        providers: typing.Optional[typing.Sequence[Provider]] = OMIT,
        summaries: typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StacPydanticCollectionCollectionOutput]:
        """
        Endpoint.

        Parameters
        ----------
        id : str

        description : str

        links : LinksInput

        type : CollectionInputType

        license : str

        extent : Extent

        stac_version : typing.Optional[str]

        stac_extensions : typing.Optional[typing.Sequence[str]]

        title : typing.Optional[str]

        assets : typing.Optional[typing.Dict[str, typing.Optional[Asset]]]

        keywords : typing.Optional[typing.Sequence[str]]

        providers : typing.Optional[typing.Sequence[Provider]]

        summaries : typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StacPydanticCollectionCollectionOutput]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "catalog/collections",
            method="POST",
            json={
                "id": id,
                "description": description,
                "stac_version": stac_version,
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=LinksInput, direction="write"
                ),
                "stac_extensions": stac_extensions,
                "title": title,
                "type": type,
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[Asset]]],
                    direction="write",
                ),
                "license": license,
                "extent": convert_and_respect_annotation_metadata(object_=extent, annotation=Extent, direction="write"),
                "keywords": keywords,
                "providers": convert_and_respect_annotation_metadata(
                    object_=providers, annotation=typing.Optional[typing.Sequence[Provider]], direction="write"
                ),
                "summaries": convert_and_respect_annotation_metadata(
                    object_=summaries,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticCollectionCollectionOutput,
                    parse_obj_as(
                        type_=StacPydanticCollectionCollectionOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def update_collection(
        self,
        collection_id: str,
        *,
        id: str,
        description: str,
        links: LinksInput,
        type: CollectionInputType,
        license: str,
        extent: Extent,
        stac_version: typing.Optional[str] = OMIT,
        stac_extensions: typing.Optional[typing.Sequence[str]] = OMIT,
        title: typing.Optional[str] = OMIT,
        assets: typing.Optional[typing.Dict[str, typing.Optional[Asset]]] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        providers: typing.Optional[typing.Sequence[Provider]] = OMIT,
        summaries: typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StacPydanticCollectionCollectionOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        id : str

        description : str

        links : LinksInput

        type : CollectionInputType

        license : str

        extent : Extent

        stac_version : typing.Optional[str]

        stac_extensions : typing.Optional[typing.Sequence[str]]

        title : typing.Optional[str]

        assets : typing.Optional[typing.Dict[str, typing.Optional[Asset]]]

        keywords : typing.Optional[typing.Sequence[str]]

        providers : typing.Optional[typing.Sequence[Provider]]

        summaries : typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StacPydanticCollectionCollectionOutput]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}",
            method="PUT",
            json={
                "id": id,
                "description": description,
                "stac_version": stac_version,
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=LinksInput, direction="write"
                ),
                "stac_extensions": stac_extensions,
                "title": title,
                "type": type,
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[Asset]]],
                    direction="write",
                ),
                "license": license,
                "extent": convert_and_respect_annotation_metadata(object_=extent, annotation=Extent, direction="write"),
                "keywords": keywords,
                "providers": convert_and_respect_annotation_metadata(
                    object_=providers, annotation=typing.Optional[typing.Sequence[Provider]], direction="write"
                ),
                "summaries": convert_and_respect_annotation_metadata(
                    object_=summaries,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticCollectionCollectionOutput,
                    parse_obj_as(
                        type_=StacPydanticCollectionCollectionOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def delete_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StacPydanticCollectionCollectionOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StacPydanticCollectionCollectionOutput]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticCollectionCollectionOutput,
                    parse_obj_as(
                        type_=StacPydanticCollectionCollectionOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def patch_collection(
        self,
        collection_id: str,
        *,
        request: PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StacPydanticCollectionCollectionOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request : PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StacPydanticCollectionCollectionOutput]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody,
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticCollectionCollectionOutput,
                    parse_obj_as(
                        type_=StacPydanticCollectionCollectionOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def create_item(
        self,
        collection_id: str,
        *,
        request: CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StacPydanticItemItemOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request : CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StacPydanticItemItemOutput]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}/items",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody,
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticItemItemOutput,
                    parse_obj_as(
                        type_=StacPydanticItemItemOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawCatalogTransactionExtensionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def update_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        type: ItemInputType,
        properties: ItemProperties,
        id: str,
        assets: typing.Dict[str, Asset],
        links: LinksInput,
        bbox: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        geometry: typing.Optional[ItemInputGeometry] = OMIT,
        stac_version: typing.Optional[str] = OMIT,
        stac_extensions: typing.Optional[typing.Sequence[str]] = OMIT,
        collection: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StacPydanticItemItemOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        type : ItemInputType

        properties : ItemProperties

        id : str

        assets : typing.Dict[str, Asset]

        links : LinksInput

        bbox : typing.Optional[typing.Sequence[typing.Any]]

        geometry : typing.Optional[ItemInputGeometry]

        stac_version : typing.Optional[str]

        stac_extensions : typing.Optional[typing.Sequence[str]]

        collection : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StacPydanticItemItemOutput]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}/items/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "bbox": bbox,
                "type": type,
                "geometry": convert_and_respect_annotation_metadata(
                    object_=geometry, annotation=typing.Optional[ItemInputGeometry], direction="write"
                ),
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=ItemProperties, direction="write"
                ),
                "id": id,
                "stac_version": stac_version,
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets, annotation=typing.Dict[str, Asset], direction="write"
                ),
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=LinksInput, direction="write"
                ),
                "stac_extensions": stac_extensions,
                "collection": collection,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticItemItemOutput,
                    parse_obj_as(
                        type_=StacPydanticItemItemOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def delete_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StacPydanticItemItemOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StacPydanticItemItemOutput]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}/items/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticItemItemOutput,
                    parse_obj_as(
                        type_=StacPydanticItemItemOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def patch_item(
        self,
        collection_id: str,
        item_id: str,
        *,
        request: PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StacPydanticItemItemOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        request : PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StacPydanticItemItemOutput]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}/items/{encode_path_param(item_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody,
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticItemItemOutput,
                    parse_obj_as(
                        type_=StacPydanticItemItemOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def create_collection(
        self,
        *,
        id: str,
        description: str,
        links: LinksInput,
        type: CollectionInputType,
        license: str,
        extent: Extent,
        stac_version: typing.Optional[str] = OMIT,
        stac_extensions: typing.Optional[typing.Sequence[str]] = OMIT,
        title: typing.Optional[str] = OMIT,
        assets: typing.Optional[typing.Dict[str, typing.Optional[Asset]]] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        providers: typing.Optional[typing.Sequence[Provider]] = OMIT,
        summaries: typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StacPydanticCollectionCollectionOutput]:
        """
        Endpoint.

        Parameters
        ----------
        id : str

        description : str

        links : LinksInput

        type : CollectionInputType

        license : str

        extent : Extent

        stac_version : typing.Optional[str]

        stac_extensions : typing.Optional[typing.Sequence[str]]

        title : typing.Optional[str]

        assets : typing.Optional[typing.Dict[str, typing.Optional[Asset]]]

        keywords : typing.Optional[typing.Sequence[str]]

        providers : typing.Optional[typing.Sequence[Provider]]

        summaries : typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StacPydanticCollectionCollectionOutput]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "catalog/collections",
            method="POST",
            json={
                "id": id,
                "description": description,
                "stac_version": stac_version,
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=LinksInput, direction="write"
                ),
                "stac_extensions": stac_extensions,
                "title": title,
                "type": type,
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[Asset]]],
                    direction="write",
                ),
                "license": license,
                "extent": convert_and_respect_annotation_metadata(object_=extent, annotation=Extent, direction="write"),
                "keywords": keywords,
                "providers": convert_and_respect_annotation_metadata(
                    object_=providers, annotation=typing.Optional[typing.Sequence[Provider]], direction="write"
                ),
                "summaries": convert_and_respect_annotation_metadata(
                    object_=summaries,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticCollectionCollectionOutput,
                    parse_obj_as(
                        type_=StacPydanticCollectionCollectionOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def update_collection(
        self,
        collection_id: str,
        *,
        id: str,
        description: str,
        links: LinksInput,
        type: CollectionInputType,
        license: str,
        extent: Extent,
        stac_version: typing.Optional[str] = OMIT,
        stac_extensions: typing.Optional[typing.Sequence[str]] = OMIT,
        title: typing.Optional[str] = OMIT,
        assets: typing.Optional[typing.Dict[str, typing.Optional[Asset]]] = OMIT,
        keywords: typing.Optional[typing.Sequence[str]] = OMIT,
        providers: typing.Optional[typing.Sequence[Provider]] = OMIT,
        summaries: typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StacPydanticCollectionCollectionOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        id : str

        description : str

        links : LinksInput

        type : CollectionInputType

        license : str

        extent : Extent

        stac_version : typing.Optional[str]

        stac_extensions : typing.Optional[typing.Sequence[str]]

        title : typing.Optional[str]

        assets : typing.Optional[typing.Dict[str, typing.Optional[Asset]]]

        keywords : typing.Optional[typing.Sequence[str]]

        providers : typing.Optional[typing.Sequence[Provider]]

        summaries : typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StacPydanticCollectionCollectionOutput]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}",
            method="PUT",
            json={
                "id": id,
                "description": description,
                "stac_version": stac_version,
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=LinksInput, direction="write"
                ),
                "stac_extensions": stac_extensions,
                "title": title,
                "type": type,
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[Asset]]],
                    direction="write",
                ),
                "license": license,
                "extent": convert_and_respect_annotation_metadata(object_=extent, annotation=Extent, direction="write"),
                "keywords": keywords,
                "providers": convert_and_respect_annotation_metadata(
                    object_=providers, annotation=typing.Optional[typing.Sequence[Provider]], direction="write"
                ),
                "summaries": convert_and_respect_annotation_metadata(
                    object_=summaries,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[CollectionInputSummariesValue]]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticCollectionCollectionOutput,
                    parse_obj_as(
                        type_=StacPydanticCollectionCollectionOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def delete_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StacPydanticCollectionCollectionOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StacPydanticCollectionCollectionOutput]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticCollectionCollectionOutput,
                    parse_obj_as(
                        type_=StacPydanticCollectionCollectionOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def patch_collection(
        self,
        collection_id: str,
        *,
        request: PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StacPydanticCollectionCollectionOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request : PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StacPydanticCollectionCollectionOutput]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody,
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticCollectionCollectionOutput,
                    parse_obj_as(
                        type_=StacPydanticCollectionCollectionOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def create_item(
        self,
        collection_id: str,
        *,
        request: CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StacPydanticItemItemOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request : CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StacPydanticItemItemOutput]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}/items",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody,
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticItemItemOutput,
                    parse_obj_as(
                        type_=StacPydanticItemItemOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
