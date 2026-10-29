

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .secondary_id_id import SecondaryIdId
from .semantics_base import SemanticsBase


class SemanticsSecondaryId(SemanticsBase):
    """
    Values are a secondaryId.
    """

    secondary_id: typing_extensions.Annotated[
        typing.Optional[SecondaryIdId], FieldMetadata(alias="secondaryId"), pydantic.Field(alias="secondaryId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
