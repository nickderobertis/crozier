

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SolrResponseResponse(UniversalBaseModel):
    docs: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    max_score: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxScore"), pydantic.Field(alias="maxScore")
    ] = None
    num_found: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numFound"), pydantic.Field(alias="numFound")
    ] = None
    start: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
