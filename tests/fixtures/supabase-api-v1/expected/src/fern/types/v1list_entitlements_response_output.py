

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1list_entitlements_response_output_entitlements_item import V1ListEntitlementsResponseOutputEntitlementsItem


class V1ListEntitlementsResponseOutput(UniversalBaseModel):
    entitlements: typing.List[V1ListEntitlementsResponseOutputEntitlementsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
