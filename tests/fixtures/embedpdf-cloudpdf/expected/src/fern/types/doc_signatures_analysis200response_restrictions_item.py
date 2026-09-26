

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_analysis200response_restrictions_item_source import (
    DocSignaturesAnalysis200ResponseRestrictionsItemSource,
)


class DocSignaturesAnalysis200ResponseRestrictionsItem(UniversalBaseModel):
    signature_index: typing_extensions.Annotated[
        int, FieldMetadata(alias="signatureIndex"), pydantic.Field(alias="signatureIndex")
    ]
    revision_index: typing_extensions.Annotated[
        int, FieldMetadata(alias="revisionIndex"), pydantic.Field(alias="revisionIndex")
    ]
    source: DocSignaturesAnalysis200ResponseRestrictionsItemSource
    own: bool
    permission: typing.Optional[float] = None
    fields: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
