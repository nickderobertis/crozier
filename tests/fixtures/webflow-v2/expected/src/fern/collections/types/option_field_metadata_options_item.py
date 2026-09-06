

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OptionFieldMetadataOptionsItem(UniversalBaseModel):
    """
    A single option value for the Option field.
    """

    name: str = pydantic.Field()
    """
    The name of the option
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the option
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
