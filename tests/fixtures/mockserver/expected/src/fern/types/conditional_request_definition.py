

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class ConditionalRequestDefinition(UniversalBaseModel):
    """
    conditional (if-then-else) request matcher: if the 'if' guard matches the request then the 'then' branch is required, otherwise the 'else' branch is required (when 'else' is omitted the expectation matches whenever the guard is false)
    """

    not_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    if_: typing_extensions.Annotated["RequestDefinition", FieldMetadata(alias="if"), pydantic.Field(alias="if")]
    then: typing.Optional["RequestDefinition"] = None
    else_: typing_extensions.Annotated[
        typing.Optional["RequestDefinition"], FieldMetadata(alias="else"), pydantic.Field(alias="else")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .request_definition import RequestDefinition

update_forward_refs(ConditionalRequestDefinition, RequestDefinition=RequestDefinition)
