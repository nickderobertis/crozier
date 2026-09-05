

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .compatible_service import CompatibleService


class Compatibility(UniversalBaseModel):
    can_update_to: typing_extensions.Annotated[
        CompatibleService,
        FieldMetadata(alias="canUpdateTo"),
        pydantic.Field(alias="canUpdateTo", description="Latest compatible service at this moment"),
    ]
    """
    Latest compatible service at this moment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
