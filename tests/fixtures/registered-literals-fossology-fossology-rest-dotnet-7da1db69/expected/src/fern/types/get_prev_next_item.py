

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetPrevNextItem(UniversalBaseModel):
    prev_item_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="prevItemId"),
        pydantic.Field(alias="prevItemId", description="Previous item Id"),
    ] = None
    """
    Previous item Id
    """

    next_item_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nextItemId"),
        pydantic.Field(alias="nextItemId", description="Next item Id"),
    ] = None
    """
    Next item Id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
