

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NamingStrategy(enum.StrEnum):
    """
    Specifies the behavior for automatically generated names when registering an entity.
    - NEW_IDS: Generate new registry IDs
    - IDS_FROM_NAMES: Generate registry IDs based on entity names
    - DELETE_NAMES: Generate new registry IDs and replace name with registry ID
    - SET_FROM_NAME_PARTS: Generate new registry IDs, rename according to name template, and keep old name as alias
    - REPLACE_NAMES_FROM_PARTS: Generate new registry IDs, and replace name according to name template
    - KEEP_NAMES: Keep existing entity names as registry IDs
    - REPLACE_ID_AND_NAME_FROM_PARTS: Generate registry IDs and names according to name template
    """

    NEW_IDS = "NEW_IDS"
    IDS_FROM_NAMES = "IDS_FROM_NAMES"
    DELETE_NAMES = "DELETE_NAMES"
    SET_FROM_NAME_PARTS = "SET_FROM_NAME_PARTS"
    REPLACE_NAMES_FROM_PARTS = "REPLACE_NAMES_FROM_PARTS"
    KEEP_NAMES = "KEEP_NAMES"
    REPLACE_ID_AND_NAME_FROM_PARTS = "REPLACE_ID_AND_NAME_FROM_PARTS"

    def visit(
        self,
        new_ids: typing.Callable[[], T_Result],
        ids_from_names: typing.Callable[[], T_Result],
        delete_names: typing.Callable[[], T_Result],
        set_from_name_parts: typing.Callable[[], T_Result],
        replace_names_from_parts: typing.Callable[[], T_Result],
        keep_names: typing.Callable[[], T_Result],
        replace_id_and_name_from_parts: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NamingStrategy.NEW_IDS:
            return new_ids()
        if self is NamingStrategy.IDS_FROM_NAMES:
            return ids_from_names()
        if self is NamingStrategy.DELETE_NAMES:
            return delete_names()
        if self is NamingStrategy.SET_FROM_NAME_PARTS:
            return set_from_name_parts()
        if self is NamingStrategy.REPLACE_NAMES_FROM_PARTS:
            return replace_names_from_parts()
        if self is NamingStrategy.KEEP_NAMES:
            return keep_names()
        if self is NamingStrategy.REPLACE_ID_AND_NAME_FROM_PARTS:
            return replace_id_and_name_from_parts()
