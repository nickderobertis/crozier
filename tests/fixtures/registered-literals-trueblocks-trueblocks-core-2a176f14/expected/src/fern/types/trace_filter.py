

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TraceFilter(UniversalBaseModel):
    """
    used by chifra traces --filter option to query for traces
    """

    from_block: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="fromBlock"),
        pydantic.Field(alias="fromBlock", description="the first block to include in the queried list of traces."),
    ] = None
    """
    the first block to include in the queried list of traces.
    """

    to_block: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="toBlock"),
        pydantic.Field(alias="toBlock", description="the last block to include in the queried list of traces."),
    ] = None
    """
    the last block to include in the queried list of traces.
    """

    from_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fromAddress"),
        pydantic.Field(
            alias="fromAddress", description="if included, only traces `from` this address will be included."
        ),
    ] = None
    """
    if included, only traces `from` this address will be included.
    """

    to_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="toAddress"),
        pydantic.Field(alias="toAddress", description="if included, only traces `to` this address will be included."),
    ] = None
    """
    if included, only traces `to` this address will be included.
    """

    after: typing.Optional[int] = pydantic.Field(default=None)
    """
    only traces after this many traces are included.
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    only this many traces are included.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
