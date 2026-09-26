

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_versions_analysis200response_basis import DocVersionsAnalysis200ResponseBasis
from .doc_versions_analysis200response_current import DocVersionsAnalysis200ResponseCurrent
from .doc_versions_analysis200response_later import DocVersionsAnalysis200ResponseLater
from .doc_versions_analysis200response_mode import DocVersionsAnalysis200ResponseMode
from .doc_versions_analysis200response_restrictions_item import DocVersionsAnalysis200ResponseRestrictionsItem
from .doc_versions_analysis200response_since import DocVersionsAnalysis200ResponseSince
from .doc_versions_analysis200response_until import DocVersionsAnalysis200ResponseUntil
from .doc_versions_analysis200response_verdict import DocVersionsAnalysis200ResponseVerdict


class DocVersionsAnalysis200Response(UniversalBaseModel):
    mode: DocVersionsAnalysis200ResponseMode
    policy_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="policyVersion"), pydantic.Field(alias="policyVersion")
    ]
    basis: DocVersionsAnalysis200ResponseBasis
    since: DocVersionsAnalysis200ResponseSince
    until: DocVersionsAnalysis200ResponseUntil
    restrictions: typing.List[DocVersionsAnalysis200ResponseRestrictionsItem]
    current: DocVersionsAnalysis200ResponseCurrent
    later: DocVersionsAnalysis200ResponseLater
    verdict: DocVersionsAnalysis200ResponseVerdict
    steps: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
