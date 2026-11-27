

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sequence_feature_custom_field import SequenceFeatureCustomField


class SequenceFeatureBase(UniversalBaseModel):
    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Hex color code used when displaying this feature in the UI.
    """

    custom_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[SequenceFeatureCustomField]],
        FieldMetadata(alias="customFields"),
        pydantic.Field(alias="customFields"),
    ] = None
    name: typing.Optional[str] = None
    notes: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
