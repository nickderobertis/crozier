

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_versions_signatures200response_signatures_item_field_mdp_action import (
    DocVersionsSignatures200ResponseSignaturesItemFieldMdpAction,
)


class DocVersionsSignatures200ResponseSignaturesItemFieldMdp(UniversalBaseModel):
    action: DocVersionsSignatures200ResponseSignaturesItemFieldMdpAction
    fields: typing.List[str]
    permission: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
