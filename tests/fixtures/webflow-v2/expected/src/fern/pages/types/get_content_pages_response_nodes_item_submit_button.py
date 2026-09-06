

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetContentPagesResponseNodesItemSubmitButton(UniversalBaseModel):
    """
    Represents submit button elements within the DOM. It contains the text and waiting text of the button. Additional attributes can be associated with the text for styling or other purposes.
    """

    id: str = pydantic.Field()
    """
    Node UUID
    """

    value: str = pydantic.Field()
    """
    The text content of the submit button.
    """

    waiting_text: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="waitingText"),
        pydantic.Field(alias="waitingText", description="The text to show while the form is submitting."),
    ]
    """
    The text to show while the form is submitting.
    """

    attributes: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The custom attributes of the node
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
