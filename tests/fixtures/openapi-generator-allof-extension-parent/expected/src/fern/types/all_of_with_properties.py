

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AllOfWithProperties(UniversalBaseModel):
    """
    parent object without x-parent extension
    """

    is_parent: typing_extensions.Annotated[bool, FieldMetadata(alias="isParent"), pydantic.Field(alias="isParent")]
    mum_or_dad: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
