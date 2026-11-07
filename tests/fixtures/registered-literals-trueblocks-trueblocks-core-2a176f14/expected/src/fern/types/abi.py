

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .function import Function


class Abi(UniversalBaseModel):
    """
    a human-readable representation of a Solidity smart contract
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address for the ABI
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    the filename of the ABI (likely the smart contract address)
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    the folder holding the abi file
    """

    file_size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="fileSize"),
        pydantic.Field(alias="fileSize", description="the size of this file on disc"),
    ] = None
    """
    the size of this file on disc
    """

    last_mod_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastModDate"),
        pydantic.Field(alias="lastModDate", description="the last update date of the file"),
    ] = None
    """
    the last update date of the file
    """

    is_known: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isKnown"),
        pydantic.Field(alias="isKnown", description="true if this is the ABI for a known smart contract or protocol"),
    ] = None
    """
    true if this is the ABI for a known smart contract or protocol
    """

    is_empty: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isEmpty"),
        pydantic.Field(
            alias="isEmpty", description="true if the ABI could not be found (and won't be looked for again)"
        ),
    ] = None
    """
    true if the ABI could not be found (and won't be looked for again)
    """

    n_functions: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nFunctions"),
        pydantic.Field(alias="nFunctions", description="if verbose, the number of functions in the ABI"),
    ] = None
    """
    if verbose, the number of functions in the ABI
    """

    n_events: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nEvents"),
        pydantic.Field(alias="nEvents", description="if verbose, the number of events in the ABI"),
    ] = None
    """
    if verbose, the number of events in the ABI
    """

    has_constructor: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasConstructor"),
        pydantic.Field(
            alias="hasConstructor", description="if verbose and the abi has a constructor, then `true`, else `false`"
        ),
    ] = None
    """
    if verbose and the abi has a constructor, then `true`, else `false`
    """

    has_fallback: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasFallback"),
        pydantic.Field(
            alias="hasFallback", description="if verbose and the abi has a fallback, then `true`, else `false`"
        ),
    ] = None
    """
    if verbose and the abi has a fallback, then `true`, else `false`
    """

    functions: typing.Optional[typing.List[Function]] = pydantic.Field(default=None)
    """
    the functions for this address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Abi)
