

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .documents_documents_item import DocumentsDocumentsItem
from .documents_order import DocumentsOrder
from .documents_sort_by import DocumentsSortBy


class Documents(UniversalBaseModel):
    consent_id: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="consentId"), pydantic.Field(alias="consentId")
    ] = None
    documents: typing.List[DocumentsDocumentsItem]
    next_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextToken"), pydantic.Field(alias="nextToken")
    ] = None
    dataset_id: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="datasetId"), pydantic.Field(alias="datasetId")
    ] = None
    sort_by: typing_extensions.Annotated[
        typing.Optional[DocumentsSortBy], FieldMetadata(alias="sortBy"), pydantic.Field(alias="sortBy")
    ] = None
    order: typing.Optional[DocumentsOrder] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Documents)
