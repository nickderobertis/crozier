

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContextDescription(UniversalBaseModel):
    human_readable: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="human-readable"),
        pydantic.Field(
            alias="human-readable",
            description="The description of data collected in this context. Should describe the purpose of processing. Should use the languages in the request Accept-Language header or a language preference expressed by the data subject earlier.",
        ),
    ] = None
    """
    The description of data collected in this context. Should describe the purpose of processing. Should use the languages in the request Accept-Language header or a language preference expressed by the data subject earlier.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
