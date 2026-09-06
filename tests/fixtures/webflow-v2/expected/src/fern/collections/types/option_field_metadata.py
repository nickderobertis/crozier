

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .option_field_metadata_options_item import OptionFieldMetadataOptionsItem


class OptionFieldMetadata(UniversalBaseModel):
    """
    The metadata for the Option field.
    """

    options: typing.List[OptionFieldMetadataOptionsItem] = pydantic.Field()
    """
    The option values for the Option field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
