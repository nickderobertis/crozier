

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_complete200response_signature_field_mdp_action import (
    DocSignaturesComplete200ResponseSignatureFieldMdpAction,
)


class DocSignaturesComplete200ResponseSignatureFieldMdp(UniversalBaseModel):
    action: DocSignaturesComplete200ResponseSignatureFieldMdpAction
    fields: typing.List[str]
    permission: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
