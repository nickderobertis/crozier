

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .crane_operators_value import CraneOperatorsValue
from .crane_scopes_value import CraneScopesValue


class Crane(UniversalBaseModel):
    operators: typing.Optional[typing.Dict[str, CraneOperatorsValue]] = pydantic.Field(default=None)
    """
    Operators on shift, keyed by badge number.
    """

    inspections: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Inspection notes, keyed by date, declared without a type.
    """

    tags: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = None
    scopes: typing.Optional[typing.Dict[str, CraneScopesValue]] = None
    loads_by_hook: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="loadsByHook"),
        pydantic.Field(alias="loadsByHook"),
    ] = None
    counters: typing.Optional[typing.Dict[str, int]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
