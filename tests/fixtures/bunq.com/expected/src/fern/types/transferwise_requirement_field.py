

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transferwise_requirement_field_group import TransferwiseRequirementFieldGroup


class TransferwiseRequirementField(UniversalBaseModel):
    group: typing.Optional[TransferwiseRequirementFieldGroup] = pydantic.Field(default=None)
    """
    The field group.
    """

    key: str = pydantic.Field()
    """
    The name of the required field.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The descriptive label of the field.
    """

    value: str = pydantic.Field()
    """
    The value of the required field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
