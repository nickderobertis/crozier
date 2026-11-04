

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .named_ref import NamedRef
from .predicate_dto import PredicateDto


class TransformResponse(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    type: typing.Optional[str] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    vaults: typing.Optional[typing.List[NamedRef]] = None
    config: typing.Optional[typing.Dict[str, typing.Any]] = None
    predicate: typing.Optional[PredicateDto] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
