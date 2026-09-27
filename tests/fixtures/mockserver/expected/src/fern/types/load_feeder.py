

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .load_feeder_format import LoadFeederFormat
from .load_feeder_strategy import LoadFeederStrategy


class LoadFeeder(UniversalBaseModel):
    """
    parameterized test data (a data feeder) for a load scenario: an inline dataset from which one row is selected per iteration and exposed to that iteration's templated request path, body and headers as $iteration.data.<column> (Velocity) / {{iteration.data.<column>}} (Mustache). The dataset is always inline (no external URL or file source). Supply EITHER rows (inline list of objects, the primary form) OR data + format (raw CSV/JSON parsed server-side); when both are given rows wins.
    """

    rows: typing.Optional[typing.List[typing.Dict[str, str]]] = pydantic.Field(default=None)
    """
    inline dataset: a list of column-name to value maps, one per row (the primary mechanism; round-trips with no parsing). Must be non-empty when used.
    """

    data: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional raw inline dataset parsed server-side into rows per format. CSV: first line is the header row (RFC 4180-ish — embedded commas, doubled quotes and newlines are handled). JSON: an array of flat objects. The raw text is preserved verbatim on round-trip (the derived rows are not re-serialized). Ignored when rows is set.
    """

    format: typing.Optional[LoadFeederFormat] = pydantic.Field(default=None)
    """
    the format of data (required when data is set)
    """

    strategy: typing.Optional[LoadFeederStrategy] = pydantic.Field(default=None)
    """
    how a row is chosen each iteration: CIRCULAR (default) cycles rows[globalIteration % size] and never exhausts; RANDOM picks a uniformly random row each iteration; SEQUENTIAL uses rows[globalIteration] once each in order and COMPLETES the run once the dataset is exhausted (data-driven replay-once).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
