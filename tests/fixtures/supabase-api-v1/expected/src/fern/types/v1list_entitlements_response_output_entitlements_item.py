

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v1list_entitlements_response_output_entitlements_item_config import (
    V1ListEntitlementsResponseOutputEntitlementsItemConfig,
)
from .v1list_entitlements_response_output_entitlements_item_feature import (
    V1ListEntitlementsResponseOutputEntitlementsItemFeature,
)
from .v1list_entitlements_response_output_entitlements_item_type import (
    V1ListEntitlementsResponseOutputEntitlementsItemType,
)


class V1ListEntitlementsResponseOutputEntitlementsItem(UniversalBaseModel):
    feature: V1ListEntitlementsResponseOutputEntitlementsItemFeature
    has_access: typing_extensions.Annotated[bool, FieldMetadata(alias="hasAccess"), pydantic.Field(alias="hasAccess")]
    type: V1ListEntitlementsResponseOutputEntitlementsItemType
    config: V1ListEntitlementsResponseOutputEntitlementsItemConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
