

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ..core.serialization import FieldMetadata
from .concept_additional_infos_item import ConceptAdditionalInfosItem
from .connector import Connector
from .labeled import Labeled
from .universal_select import UniversalSelect


class Concept(Labeled):
    """
    Describes a collection of filters and aggregations from multiple source tables. If `children` is set, events of the connectors will be matched according to conditions defined in the children. Each event may only map to a single child. The structure of the children describes a directed tree: Querying for a non-leaf node, always includes its sub-tree.
    Using multiple connectors allows funneling of different source tables into a single tree.
    """

    tables: typing.Optional[typing.List[Connector]] = None
    children: typing.Optional[typing.List["ConceptTreeChild"]] = pydantic.Field(default=None)
    """
    The children describing the tree to structure events onto. May be empty, if the concept only defines filters and selects.
    """

    selects: typing.Optional[typing.List[UniversalSelect]] = pydantic.Field(default=None)
    """
    Selects able to be applied to all events, irrespective of source table.
    """

    default_exclude_from_time_aggregation: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="defaultExcludeFromTimeAggregation"),
        pydantic.Field(
            alias="defaultExcludeFromTimeAggregation",
            description="If true, excludeFromTimeAggregation will be set to true by default for the users.",
        ),
    ] = None
    """
    If true, excludeFromTimeAggregation will be set to true by default for the users.
    """

    hidden: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, the concept is not visible in the API or the frontend.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A textual description of the concept. May include markdown text.
    """

    additional_infos: typing_extensions.Annotated[
        typing.Optional[typing.List[ConceptAdditionalInfosItem]],
        FieldMetadata(alias="additionalInfos"),
        pydantic.Field(
            alias="additionalInfos",
            description="A list of key value pairs of additional information. Displayed to the user in a side pane. May contain markdown text.",
        ),
    ] = None
    """
    A list of key value pairs of additional information. Displayed to the user in a side pane. May contain markdown text.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .concept_tree_child import ConceptTreeChild

update_forward_refs(Concept, ConceptTreeChild=ConceptTreeChild)
