

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_versions_analysis200response_basis_source import DocVersionsAnalysis200ResponseBasisSource
from .doc_versions_analysis200response_basis_version import DocVersionsAnalysis200ResponseBasisVersion


class DocVersionsAnalysis200ResponseBasis(UniversalBaseModel):
    version: DocVersionsAnalysis200ResponseBasisVersion
    edits_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="editsVersion"), pydantic.Field(alias="editsVersion")
    ]
    source: DocVersionsAnalysis200ResponseBasisSource

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
