

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .preference_constraints import PreferenceConstraints


class Preference(UniversalBaseModel):
    default_value: typing_extensions.Annotated[
        typing.Any, FieldMetadata(alias="defaultValue"), pydantic.Field(alias="defaultValue")
    ]
    value: typing.Any
    constraints: typing.Optional[PreferenceConstraints] = pydantic.Field(default=None)
    """
    null when the value is unconstrained
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
