

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .calculated_field import CalculatedField


class CalculatedFieldsPayload(UniversalBaseModel):
    """
    Payload for CALCULATED_FIELDS block type. Used for computed/calculated values.
    """

    calculated_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[CalculatedField]],
        FieldMetadata(alias="calculatedFields"),
        pydantic.Field(alias="calculatedFields"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
