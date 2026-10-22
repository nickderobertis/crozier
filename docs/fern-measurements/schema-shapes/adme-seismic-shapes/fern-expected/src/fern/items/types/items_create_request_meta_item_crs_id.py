

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .items_create_request_meta_item_crs_id_kind import ItemsCreateRequestMetaItemCrsIdKind


class ItemsCreateRequestMetaItemCrsId(UniversalBaseModel):
    kind: ItemsCreateRequestMetaItemCrsIdKind
    crs_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="crsId"), pydantic.Field(alias="crsId")
    ] = None
    ref: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
