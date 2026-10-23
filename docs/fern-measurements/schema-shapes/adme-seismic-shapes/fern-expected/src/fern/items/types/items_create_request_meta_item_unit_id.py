

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .items_create_request_meta_item_unit_id_kind import ItemsCreateRequestMetaItemUnitIdKind


class ItemsCreateRequestMetaItemUnitId(UniversalBaseModel):
    kind: ItemsCreateRequestMetaItemUnitIdKind
    unit_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="unitId"), pydantic.Field(alias="unitId")
    ] = None
    ref: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
