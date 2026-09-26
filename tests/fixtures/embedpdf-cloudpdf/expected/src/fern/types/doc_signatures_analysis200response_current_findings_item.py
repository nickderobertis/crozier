

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_analysis200response_current_findings_item_verdict import (
    DocSignaturesAnalysis200ResponseCurrentFindingsItemVerdict,
)


class DocSignaturesAnalysis200ResponseCurrentFindingsItem(UniversalBaseModel):
    rule: str
    verdict: DocSignaturesAnalysis200ResponseCurrentFindingsItemVerdict
    object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="objectNumber"), pydantic.Field(alias="objectNumber")
    ]
    edge: typing.Optional[str] = None
    detail: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
