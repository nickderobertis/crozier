

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .probe_run_id import ProbeRunId
from .store_probe_check import StoreProbeCheck


class StoreProbeResponse(UniversalBaseModel):
    """
    The results of one store contract probe, in order.
    """

    checks: typing.List[StoreProbeCheck] = pydantic.Field()
    """
    The check results, in the order that the checks ran.
    """

    run_id: ProbeRunId = pydantic.Field()
    """
    The ID of this probe run. The server generates the ID and writes the probe's temporary
    objects under it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
