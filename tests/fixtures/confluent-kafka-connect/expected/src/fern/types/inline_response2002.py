

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .inline_response2002type import InlineResponse2002Type


class InlineResponse2002(UniversalBaseModel):
    class_: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="class"),
        pydantic.Field(alias="class", description="The connector class name. E.g. BigQuerySink."),
    ]
    """
    The connector class name. E.g. BigQuerySink.
    """

    type: InlineResponse2002Type = pydantic.Field()
    """
    Type of connector, sink or source.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version string for the connector available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
