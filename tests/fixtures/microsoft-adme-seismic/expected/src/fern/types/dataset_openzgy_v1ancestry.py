

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DatasetOpenzgyV1Ancestry(UniversalBaseModel):
    """
    A list of entity IDs in the data ecosystem, which act as legal parents to the current entity. This structure is included by the SystemProperties "ancestry", which is part of all OSDU records. Not extensible.
    """

    parents: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of none, one or many entity references in the data ecosystem, which identify the source of data in the legal sense. In contract to other relationships, the source record version is required. Example: the 'parents' will be queried when e.g. the subscription of source data services is terminated; access to the derivatives is also terminated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
