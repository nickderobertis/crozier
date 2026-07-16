

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_progression import DestinyDestinyProgression
from .destiny_destiny_talent_node import DestinyDestinyTalentNode


class DestinyEntitiesItemsDestinyItemTalentGridComponent(UniversalBaseModel):
    """
    Well, we're here in Destiny 2, and Talent Grids are unfortunately still around.
    The good news is that they're pretty much only being used for certain base information on items and for Builds/Subclasses. The bad news is that they still suck. If you really want this information, grab this component.
    An important note is that talent grids are defined as such:
    A Grid has 1:M Nodes, which has 1:M Steps.
    Any given node can only have a single step active at one time, which represents the actual visual contents and effects of the Node (for instance, if you see a "Super Cool Bonus" node, the actual icon and text for the node is coming from the current Step of that node).
    Nodes can be grouped into exclusivity sets *and* as of D2, exclusivity groups (which are collections of exclusivity sets that affect each other).
    See DestinyTalentGridDefinition for more information. Brace yourself, the water's cold out there in the deep end.
    """

    grid_progression: typing_extensions.Annotated[
        typing.Optional[DestinyDestinyProgression],
        FieldMetadata(alias="gridProgression"),
        pydantic.Field(
            alias="gridProgression",
            description="If the item has a progression, it will be detailed here. A progression means that the item can gain experience. Thresholds of experience are what determines whether and when a talent node can be activated.",
        ),
    ] = None
    """
    If the item has a progression, it will be detailed here. A progression means that the item can gain experience. Thresholds of experience are what determines whether and when a talent node can be activated.
    """

    is_grid_complete: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isGridComplete"),
        pydantic.Field(
            alias="isGridComplete",
            description="Indicates whether the talent grid on this item is completed, and thus whether it should have a gold border around it.\r\nOnly will be true if the item actually *has* a talent grid, and only then if it is completed (i.e. every exclusive set has an activated node, and every non-exclusive set node has been activated)",
        ),
    ] = None
    """
    Indicates whether the talent grid on this item is completed, and thus whether it should have a gold border around it.
    Only will be true if the item actually *has* a talent grid, and only then if it is completed (i.e. every exclusive set has an activated node, and every non-exclusive set node has been activated)
    """

    nodes: typing.Optional[typing.List[DestinyDestinyTalentNode]] = pydantic.Field(default=None)
    """
    Detailed information about the individual nodes in the talent grid.
    A node represents a single visual "pip" in the talent grid or Build detail view, though each node may have multiple "steps" which indicate the actual bonuses and visual representation of that node.
    """

    talent_grid_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="talentGridHash"),
        pydantic.Field(
            alias="talentGridHash",
            description="Most items don't have useful talent grids anymore, but Builds in particular still do.\r\nYou can use this hash to lookup the DestinyTalentGridDefinition attached to this item, which will be crucial for understanding the node values on the item.",
        ),
    ] = None
    """
    Most items don't have useful talent grids anymore, but Builds in particular still do.
    You can use this hash to lookup the DestinyTalentGridDefinition attached to this item, which will be crucial for understanding the node values on the item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
