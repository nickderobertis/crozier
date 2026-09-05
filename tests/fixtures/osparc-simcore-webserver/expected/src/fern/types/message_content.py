

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MessageContent(UniversalBaseModel):
    subject: str = pydantic.Field()
    """
    Email subject line (RFC 2822: max header line length)
    """

    body_html: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bodyHtml"), pydantic.Field(alias="bodyHtml")
    ] = None
    body_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bodyText"), pydantic.Field(alias="bodyText")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
