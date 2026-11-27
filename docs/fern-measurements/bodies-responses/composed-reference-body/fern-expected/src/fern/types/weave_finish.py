

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .weave_finish_delivery import WeaveFinishDelivery


class WeaveFinish(UniversalBaseModel):
    """
    Where a started weave is filed.
    """

    shelf_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="shelfId"), pydantic.Field(alias="shelfId", description="The shelf the cloth goes to.")
    ]
    """
    The shelf the cloth goes to.
    """

    label: str = pydantic.Field()
    """
    The cloth's label.
    """

    delivery: WeaveFinishDelivery

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
