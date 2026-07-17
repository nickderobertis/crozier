

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .parameter_constraint_in import ParameterConstraintIn


class ParameterConstraint(UniversalBaseModel):
    """
    Companion object for Operation that may be used to express constraints on request parameters
    """

    in_: typing_extensions.Annotated[
        typing.Optional[ParameterConstraintIn],
        FieldMetadata(alias="in"),
        pydantic.Field(alias="in", description="Parameter location"),
    ] = None
    """
    Parameter location
    """

    must_match_regexp: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mustMatchRegexp"),
        pydantic.Field(alias="mustMatchRegexp", description="Whether it's a regular expression matching constraint"),
    ] = None
    """
    Whether it's a regular expression matching constraint
    """

    name: str = pydantic.Field()
    """
    Parameter name
    """

    recopy: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether it's a recopy constraint
    """

    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether it's a required constraint
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
