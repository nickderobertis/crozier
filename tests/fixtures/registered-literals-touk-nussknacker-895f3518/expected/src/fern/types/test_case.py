

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .map_node_id_enricher_mock import MapNodeIdEnricherMock
from .map_node_id_list_assertion import MapNodeIdListAssertion


class TestCase(UniversalBaseModel):
    id: str
    name: str
    inputs: str
    mocks: MapNodeIdEnricherMock
    assertions: MapNodeIdListAssertion

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
