

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .schema_response_blocks_read_response_attributes_block_type import (
    SchemaResponseBlocksReadResponseAttributesBlockType,
)


class SchemaResponseBlocksReadResponseAttributes(UniversalBaseModel):
    """
    The attributes of the Registration Schema Block.
    """

    block_type: typing.Optional[SchemaResponseBlocksReadResponseAttributesBlockType] = pydantic.Field(default=None)
    """
    A string that represents the type of input that the schema will take and the UI element that appears to the user on the frontend.
    """

    display_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text that will accompany the UI element displayed on this Registration Schema Block.
    """

    example_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text that will accompany the UI element displayed on this Registration Schema Block.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    Integer beginning at zero that represents the order of Registration Schema Block in the Registration Schema.
    """

    registration_response_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    This string is the the block key for the Registration Schema Block's corresponding block on the Schema Response.
    """

    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Bool that represents if this field is required for creation of a Schema Response.
    """

    schema_block_group_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    This string indicates if a block is part of a block group, block groups may contain the different options dropdown menu or a group of inputs and display elements that are validated together.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
