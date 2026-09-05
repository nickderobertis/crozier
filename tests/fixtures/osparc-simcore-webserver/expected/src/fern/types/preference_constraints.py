

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .preference_constraints_ge import PreferenceConstraintsGe
from .preference_constraints_gt import PreferenceConstraintsGt
from .preference_constraints_le import PreferenceConstraintsLe
from .preference_constraints_lt import PreferenceConstraintsLt
from .preference_constraints_multiple_of import PreferenceConstraintsMultipleOf


class PreferenceConstraints(UniversalBaseModel):
    """
    Limits applying to a preference value, used by the frontend to render its widget.
    """

    ge: typing.Optional[PreferenceConstraintsGe] = None
    gt: typing.Optional[PreferenceConstraintsGt] = None
    le: typing.Optional[PreferenceConstraintsLe] = None
    lt: typing.Optional[PreferenceConstraintsLt] = None
    max_length: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxLength"), pydantic.Field(alias="maxLength")
    ] = None
    min_length: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minLength"), pydantic.Field(alias="minLength")
    ] = None
    multiple_of: typing_extensions.Annotated[
        typing.Optional[PreferenceConstraintsMultipleOf],
        FieldMetadata(alias="multipleOf"),
        pydantic.Field(alias="multipleOf"),
    ] = None
    pattern: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
