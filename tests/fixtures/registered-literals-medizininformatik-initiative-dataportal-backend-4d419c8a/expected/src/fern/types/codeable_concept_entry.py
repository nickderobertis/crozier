

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .display_entry import DisplayEntry
from .term_code import TermCode


class CodeableConceptEntry(UniversalBaseModel):
    id: typing.Optional[str] = None
    term_code: typing_extensions.Annotated[
        typing.Optional[TermCode], FieldMetadata(alias="termCode"), pydantic.Field(alias="termCode")
    ] = None
    display: typing.Optional[DisplayEntry] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
