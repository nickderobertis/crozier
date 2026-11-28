

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntryLinkType(enum.StrEnum):
    """
    The type of resource being linked. For hyperlinks: 'link'. For linked Benchling resources, one of: 'user', 'request', 'entry', 'stage_entry', 'protocol', 'workflow', 'custom_entity', 'aa_sequence', 'dna_sequence', 'batch', 'box', 'container', 'location', 'plate', 'sql_dashboard'; and (for legacy support) 'insights_dashboard', 'folder'.
    """

    LINK = "link"
    USER = "user"
    REQUEST = "request"
    ENTRY = "entry"
    STAGE_ENTRY = "stage_entry"
    PROTOCOL = "protocol"
    WORKFLOW = "workflow"
    CUSTOM_ENTITY = "custom_entity"
    AA_SEQUENCE = "aa_sequence"
    DNA_SEQUENCE = "dna_sequence"
    BATCH = "batch"
    BOX = "box"
    CONTAINER = "container"
    LOCATION = "location"
    PLATE = "plate"
    INSIGHTS_DASHBOARD = "insights_dashboard"
    FOLDER = "folder"
    SQL_DASHBOARD = "sql_dashboard"

    def visit(
        self,
        link: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        request: typing.Callable[[], T_Result],
        entry: typing.Callable[[], T_Result],
        stage_entry: typing.Callable[[], T_Result],
        protocol: typing.Callable[[], T_Result],
        workflow: typing.Callable[[], T_Result],
        custom_entity: typing.Callable[[], T_Result],
        aa_sequence: typing.Callable[[], T_Result],
        dna_sequence: typing.Callable[[], T_Result],
        batch: typing.Callable[[], T_Result],
        box: typing.Callable[[], T_Result],
        container: typing.Callable[[], T_Result],
        location: typing.Callable[[], T_Result],
        plate: typing.Callable[[], T_Result],
        insights_dashboard: typing.Callable[[], T_Result],
        folder: typing.Callable[[], T_Result],
        sql_dashboard: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntryLinkType.LINK:
            return link()
        if self is EntryLinkType.USER:
            return user()
        if self is EntryLinkType.REQUEST:
            return request()
        if self is EntryLinkType.ENTRY:
            return entry()
        if self is EntryLinkType.STAGE_ENTRY:
            return stage_entry()
        if self is EntryLinkType.PROTOCOL:
            return protocol()
        if self is EntryLinkType.WORKFLOW:
            return workflow()
        if self is EntryLinkType.CUSTOM_ENTITY:
            return custom_entity()
        if self is EntryLinkType.AA_SEQUENCE:
            return aa_sequence()
        if self is EntryLinkType.DNA_SEQUENCE:
            return dna_sequence()
        if self is EntryLinkType.BATCH:
            return batch()
        if self is EntryLinkType.BOX:
            return box()
        if self is EntryLinkType.CONTAINER:
            return container()
        if self is EntryLinkType.LOCATION:
            return location()
        if self is EntryLinkType.PLATE:
            return plate()
        if self is EntryLinkType.INSIGHTS_DASHBOARD:
            return insights_dashboard()
        if self is EntryLinkType.FOLDER:
            return folder()
        if self is EntryLinkType.SQL_DASHBOARD:
            return sql_dashboard()
