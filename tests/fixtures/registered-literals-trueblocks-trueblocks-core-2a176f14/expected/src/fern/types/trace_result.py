

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TraceResult(UniversalBaseModel):
    """
    trace result data as returned from the RPC (with slight enhancements)
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    address of new contract, if any
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    if this trace is creating a new smart contract, the byte code of that contract
    """

    gas_used: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="gasUsed"),
        pydantic.Field(alias="gasUsed", description="the amount of gas used by this trace"),
    ] = None
    """
    the amount of gas used by this trace
    """

    output: typing.Optional[str] = pydantic.Field(default=None)
    """
    the result of the call of this trace
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
