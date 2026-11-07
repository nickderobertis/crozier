

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contextualized_term_code import ContextualizedTermCode


class ContextualizedTermCodeList(UniversalBaseModel):
    contextualized_term_codes: typing_extensions.Annotated[
        typing.Optional[typing.List[ContextualizedTermCode]],
        FieldMetadata(alias="contextualizedTermCodes"),
        pydantic.Field(alias="contextualizedTermCodes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
