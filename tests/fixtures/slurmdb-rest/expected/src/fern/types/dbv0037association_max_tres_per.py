

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037association_max_tres_per_job_item import Dbv0037AssociationMaxTresPerJobItem
from .dbv0037association_max_tres_per_node_item import Dbv0037AssociationMaxTresPerNodeItem


class Dbv0037AssociationMaxTresPer(UniversalBaseModel):
    """
    Max TRES per settings
    """

    job: typing.Optional[typing.List[Dbv0037AssociationMaxTresPerJobItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    node: typing.Optional[typing.List[Dbv0037AssociationMaxTresPerNodeItem]] = pydantic.Field(default=None)
    """
    TRES list of attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
