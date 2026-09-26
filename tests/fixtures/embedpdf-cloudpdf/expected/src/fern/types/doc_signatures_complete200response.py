

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_complete200response_meta import DocSignaturesComplete200ResponseMeta
from .doc_signatures_complete200response_previous import DocSignaturesComplete200ResponsePrevious
from .doc_signatures_complete200response_protection import DocSignaturesComplete200ResponseProtection
from .doc_signatures_complete200response_signature import DocSignaturesComplete200ResponseSignature
from .doc_signatures_complete200response_status import DocSignaturesComplete200ResponseStatus
from .doc_signatures_complete200response_version import DocSignaturesComplete200ResponseVersion


class DocSignaturesComplete200Response(UniversalBaseModel):
    status: DocSignaturesComplete200ResponseStatus
    signature: DocSignaturesComplete200ResponseSignature
    version: DocSignaturesComplete200ResponseVersion
    previous: DocSignaturesComplete200ResponsePrevious
    protection: DocSignaturesComplete200ResponseProtection
    meta: DocSignaturesComplete200ResponseMeta

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
