

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class RegistrationSchemaReadResponseAttributes(UniversalBaseModel):
    """
    The attributes of the Registration Schema.
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Bool that represents whether the Registration Schema is active.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the Registration Schema
    """

    schema_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="schema"),
        pydantic.Field(
            alias="schema",
            description="This dictionary is the raw schema that originally defined the Registration Schema object and it's blocks.",
        ),
    ] = None
    """
    This dictionary is the raw schema that originally defined the Registration Schema object and it's blocks.
    """

    schema_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of this Registration Schema
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
