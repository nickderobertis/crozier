

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .conditional_action_payload_calculate import ConditionalActionPayloadCalculate
from .conditional_action_payload_jump_to_page import ConditionalActionPayloadJumpToPage


class ConditionalActionPayload(UniversalBaseModel):
    """
    Action details executed when conditions match.
    """

    jump_to_page: typing_extensions.Annotated[
        typing.Optional[ConditionalActionPayloadJumpToPage],
        FieldMetadata(alias="jumpToPage"),
        pydantic.Field(alias="jumpToPage", description="Target page number or page UUID to jump to."),
    ] = None
    """
    Target page number or page UUID to jump to.
    """

    show_blocks: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="showBlocks"),
        pydantic.Field(alias="showBlocks", description="Block UUIDs to show when condition matches."),
    ] = None
    """
    Block UUIDs to show when condition matches.
    """

    hide_blocks: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="hideBlocks"),
        pydantic.Field(alias="hideBlocks", description="Block UUIDs to hide when condition matches."),
    ] = None
    """
    Block UUIDs to hide when condition matches.
    """

    require_answer: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requireAnswer"),
        pydantic.Field(alias="requireAnswer", description="Block UUID to mark as required when condition matches."),
    ] = None
    """
    Block UUID to mark as required when condition matches.
    """

    calculate: typing.Optional[ConditionalActionPayloadCalculate] = pydantic.Field(default=None)
    """
    Calculation to apply when condition matches.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
