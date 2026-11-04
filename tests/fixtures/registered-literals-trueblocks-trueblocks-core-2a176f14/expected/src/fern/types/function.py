

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class Function(UniversalBaseModel):
    """
    a human-readable representation of a Solidity function call or event
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    the name of the interface
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    the type of the interface, either 'event' or 'function'
    """

    signature: typing.Optional[str] = pydantic.Field(default=None)
    """
    the canonical signature of the interface
    """

    encoding: typing.Optional[str] = pydantic.Field(default=None)
    """
    the signature encoded with keccak
    """

    inputs: typing.Optional[typing.List["Parameter"]] = pydantic.Field(default=None)
    """
    the input parameters to the function, if any
    """

    outputs: typing.Optional[typing.List["Parameter"]] = pydantic.Field(default=None)
    """
    the output parameters to the function, if any
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .parameter import Parameter

update_forward_refs(Function, Parameter=Parameter)
