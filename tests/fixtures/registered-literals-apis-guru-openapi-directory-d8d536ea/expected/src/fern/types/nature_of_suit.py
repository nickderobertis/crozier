

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NatureOfSuit(UniversalBaseModel):
    """
    Nature Of Suit for a case.
    """

    code: int = pydantic.Field()
    """
    Nos Code from the source site which is extracted from the sourceText.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Code Name from the source site which is extracted from the sourceText.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    section: typing.Optional[str] = pydantic.Field(default=None)
    """
    Section of a nos code extracted from the sourceText.
    """

    source_text: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceText"),
        pydantic.Field(alias="sourceText", description="Source nos code data from the court site."),
    ] = None
    """
    Source nos code data from the court site.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
