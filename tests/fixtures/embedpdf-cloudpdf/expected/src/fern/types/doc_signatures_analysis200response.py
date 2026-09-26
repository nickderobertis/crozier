

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_analysis200response_basis import DocSignaturesAnalysis200ResponseBasis
from .doc_signatures_analysis200response_current import DocSignaturesAnalysis200ResponseCurrent
from .doc_signatures_analysis200response_later import DocSignaturesAnalysis200ResponseLater
from .doc_signatures_analysis200response_mode import DocSignaturesAnalysis200ResponseMode
from .doc_signatures_analysis200response_restrictions_item import DocSignaturesAnalysis200ResponseRestrictionsItem
from .doc_signatures_analysis200response_since import DocSignaturesAnalysis200ResponseSince
from .doc_signatures_analysis200response_until import DocSignaturesAnalysis200ResponseUntil
from .doc_signatures_analysis200response_verdict import DocSignaturesAnalysis200ResponseVerdict


class DocSignaturesAnalysis200Response(UniversalBaseModel):
    mode: DocSignaturesAnalysis200ResponseMode
    policy_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="policyVersion"), pydantic.Field(alias="policyVersion")
    ]
    basis: DocSignaturesAnalysis200ResponseBasis
    since: DocSignaturesAnalysis200ResponseSince
    until: DocSignaturesAnalysis200ResponseUntil
    restrictions: typing.List[DocSignaturesAnalysis200ResponseRestrictionsItem]
    current: DocSignaturesAnalysis200ResponseCurrent
    later: DocSignaturesAnalysis200ResponseLater
    verdict: DocSignaturesAnalysis200ResponseVerdict
    steps: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
