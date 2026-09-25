

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .basic_program import BasicProgram


class ChargeScheduleProgram(BasicProgram):
    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines whether this program is enabled or not.
    """

    slot: typing.Optional[int] = pydantic.Field(default=None)
    """
    This program number. Can only be used ONE time in the same charging program list.
    """

    end: typing.Optional[str] = pydantic.Field(default=None)
    """
    The program relative (to 00:00) end time formatted using the duration format based on [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) with the schema: P[n]Y[n]M[n]DT[n]H[n]M[n]S
    
    _example_: 
    
    * PT14H30M means 14H and 30Min
    """

    charge_until_full: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="chargeUntilFull"),
        pydantic.Field(
            alias="chargeUntilFull", description="If this program is tagged as chargin until battery is full."
        ),
    ] = None
    """
    If this program is tagged as chargin until battery is full.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
