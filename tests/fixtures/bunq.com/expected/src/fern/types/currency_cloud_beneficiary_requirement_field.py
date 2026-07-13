

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CurrencyCloudBeneficiaryRequirementField(UniversalBaseModel):
    input_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of data to input. Determines the keyboard to display.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    The label to display for the field.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the field.
    """

    validation_expression: typing.Optional[str] = pydantic.Field(default=None)
    """
    The expression to validate field input.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
