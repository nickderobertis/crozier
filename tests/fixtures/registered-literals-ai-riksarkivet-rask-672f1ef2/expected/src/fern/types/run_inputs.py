

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_input import RunInput


class RunInputs(UniversalBaseModel):
    """
    The inputs a run consumed, with their pinned versions — the reproducibility answer for one run.

    Governed like every other read: an input the caller can't ``can_get_metadata`` is dropped, so this
    can't enumerate datasets outside the caller's reach. For a training run this answers exactly *which
    feature versions produced this model*.
    """

    inputs: typing.Optional[typing.List[RunInput]] = None
    run_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
