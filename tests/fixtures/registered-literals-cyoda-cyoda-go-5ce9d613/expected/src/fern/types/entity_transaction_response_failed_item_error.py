

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EntityTransactionResponseFailedItemError(UniversalBaseModel):
    code: str
    message: str
    item_index: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="itemIndex"),
        pydantic.Field(alias="itemIndex", description="Per-chunk-relative item index."),
    ]
    """
    Per-chunk-relative item index.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
