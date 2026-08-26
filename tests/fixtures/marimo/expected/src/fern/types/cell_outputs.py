

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cell_output import CellOutput


class CellOutputs(UniversalBaseModel):
    """
    Per-cell output snapshot delivered alongside the document snapshot.

        `output` carries the cell's last main (rich display) output;
        `console_outputs` carries the buffered stdout/stderr stream from
        its last execution.  Both are keyed by cell id; missing keys mean
        "no output captured" (the cell never ran, or produced nothing on
        that channel).
    """

    console_outputs: typing.Dict[str, typing.List[CellOutput]]
    output: typing.Dict[str, CellOutput]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
