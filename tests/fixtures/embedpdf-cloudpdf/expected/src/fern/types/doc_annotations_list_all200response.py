

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item import DocAnnotationsListAll200ResponsePagesItem


class DocAnnotationsListAll200Response(UniversalBaseModel):
    pages: typing.List[DocAnnotationsListAll200ResponsePagesItem]
    audit_head: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="auditHead"), pydantic.Field(alias="auditHead")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
