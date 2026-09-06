

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute(UniversalBaseModel):
    """
    The definition of the content for submission
    """

    content_submission_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ContentSubmissionID"),
        pydantic.Field(
            alias="ContentSubmissionID", description="The ID of the content submission to which this attribute belongs."
        ),
    ] = None
    """
    The ID of the content submission to which this attribute belongs.
    """

    id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ID"),
        pydantic.Field(alias="ID", description="The ID of this attribute."),
    ] = None
    """
    The ID of this attribute.
    """

    name: typing_extensions.Annotated[
        str, FieldMetadata(alias="Name"), pydantic.Field(alias="Name", description="The name of this Attribute.")
    ]
    """
    The name of this Attribute.
    """

    value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Value"),
        pydantic.Field(alias="Value", description="The value of this Attribute"),
    ] = None
    """
    The value of this Attribute
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
