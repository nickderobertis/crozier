

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class Parameter(UniversalBaseModel):
    """
    an input or output parameter to a Solidity function or event
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    the type of this parameter
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    the name of this parameter
    """

    str_default: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="strDefault"),
        pydantic.Field(alias="strDefault", description="the default value of this parameter, if any"),
    ] = None
    """
    the default value of this parameter, if any
    """

    indexed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    `true` if this parameter is indexed
    """

    internal_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="internalType"),
        pydantic.Field(alias="internalType", description="for composite types, the internal type of the parameter"),
    ] = None
    """
    for composite types, the internal type of the parameter
    """

    components: typing.Optional[typing.List["Parameter"]] = pydantic.Field(default=None)
    """
    for composite types, the parameters making up the composite
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Parameter)
