



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .attachment import Attachment
    from .items_result_of_project import ItemsResultOfProject
    from .items_result_of_project_group import ItemsResultOfProjectGroup
    from .items_result_of_project_membership import ItemsResultOfProjectMembership
    from .items_result_of_team import ItemsResultOfTeam
    from .items_result_of_team_membership import ItemsResultOfTeamMembership
    from .organization import Organization
    from .paged_result_of_organization import PagedResultOfOrganization
    from .paged_result_of_ticket import PagedResultOfTicket
    from .paged_result_of_ticket_comment import PagedResultOfTicketComment
    from .paged_result_of_ticket_event import PagedResultOfTicketEvent
    from .paged_result_of_ticket_status import PagedResultOfTicketStatus
    from .paged_result_of_user import PagedResultOfUser
    from .problem_details import ProblemDetails
    from .project import Project
    from .project_group import ProjectGroup
    from .project_membership import ProjectMembership
    from .sort_direction import SortDirection
    from .tag import Tag
    from .team import Team
    from .team_member import TeamMember
    from .team_membership import TeamMembership
    from .ticket import Ticket
    from .ticket_assignee_updated import TicketAssigneeUpdated
    from .ticket_comment import TicketComment
    from .ticket_comment_added import TicketCommentAdded
    from .ticket_created import TicketCreated
    from .ticket_description_updated import TicketDescriptionUpdated
    from .ticket_estimated_time_updated import TicketEstimatedTimeUpdated
    from .ticket_event import (
        TicketEvent,
        TicketEvent_TicketAssigneeUpdated,
        TicketEvent_TicketCommentAdded,
        TicketEvent_TicketCreated,
        TicketEvent_TicketDescriptionUpdated,
        TicketEvent_TicketEstimatedTimeUpdated,
        TicketEvent_TicketImpactUpdated,
        TicketEvent_TicketPriorityUpdated,
        TicketEvent_TicketProjectUpdated,
        TicketEvent_TicketRemainingTimeUpdated,
        TicketEvent_TicketStatusUpdated,
        TicketEvent_TicketSubjectUpdated,
        TicketEvent_TicketUrgencyUpdated,
    )
    from .ticket_impact import TicketImpact
    from .ticket_impact_updated import TicketImpactUpdated
    from .ticket_participant import TicketParticipant
    from .ticket_priority import TicketPriority
    from .ticket_priority_updated import TicketPriorityUpdated
    from .ticket_project_updated import TicketProjectUpdated
    from .ticket_remaining_time_updated import TicketRemainingTimeUpdated
    from .ticket_status import TicketStatus
    from .ticket_status_updated import TicketStatusUpdated
    from .ticket_subject_updated import TicketSubjectUpdated
    from .ticket_type import TicketType
    from .ticket_urgency import TicketUrgency
    from .ticket_urgency_updated import TicketUrgencyUpdated
    from .user import User
    from .user_info import UserInfo
_dynamic_imports: typing.Dict[str, str] = {
    "Attachment": ".attachment",
    "ItemsResultOfProject": ".items_result_of_project",
    "ItemsResultOfProjectGroup": ".items_result_of_project_group",
    "ItemsResultOfProjectMembership": ".items_result_of_project_membership",
    "ItemsResultOfTeam": ".items_result_of_team",
    "ItemsResultOfTeamMembership": ".items_result_of_team_membership",
    "Organization": ".organization",
    "PagedResultOfOrganization": ".paged_result_of_organization",
    "PagedResultOfTicket": ".paged_result_of_ticket",
    "PagedResultOfTicketComment": ".paged_result_of_ticket_comment",
    "PagedResultOfTicketEvent": ".paged_result_of_ticket_event",
    "PagedResultOfTicketStatus": ".paged_result_of_ticket_status",
    "PagedResultOfUser": ".paged_result_of_user",
    "ProblemDetails": ".problem_details",
    "Project": ".project",
    "ProjectGroup": ".project_group",
    "ProjectMembership": ".project_membership",
    "SortDirection": ".sort_direction",
    "Tag": ".tag",
    "Team": ".team",
    "TeamMember": ".team_member",
    "TeamMembership": ".team_membership",
    "Ticket": ".ticket",
    "TicketAssigneeUpdated": ".ticket_assignee_updated",
    "TicketComment": ".ticket_comment",
    "TicketCommentAdded": ".ticket_comment_added",
    "TicketCreated": ".ticket_created",
    "TicketDescriptionUpdated": ".ticket_description_updated",
    "TicketEstimatedTimeUpdated": ".ticket_estimated_time_updated",
    "TicketEvent": ".ticket_event",
    "TicketEvent_TicketAssigneeUpdated": ".ticket_event",
    "TicketEvent_TicketCommentAdded": ".ticket_event",
    "TicketEvent_TicketCreated": ".ticket_event",
    "TicketEvent_TicketDescriptionUpdated": ".ticket_event",
    "TicketEvent_TicketEstimatedTimeUpdated": ".ticket_event",
    "TicketEvent_TicketImpactUpdated": ".ticket_event",
    "TicketEvent_TicketPriorityUpdated": ".ticket_event",
    "TicketEvent_TicketProjectUpdated": ".ticket_event",
    "TicketEvent_TicketRemainingTimeUpdated": ".ticket_event",
    "TicketEvent_TicketStatusUpdated": ".ticket_event",
    "TicketEvent_TicketSubjectUpdated": ".ticket_event",
    "TicketEvent_TicketUrgencyUpdated": ".ticket_event",
    "TicketImpact": ".ticket_impact",
    "TicketImpactUpdated": ".ticket_impact_updated",
    "TicketParticipant": ".ticket_participant",
    "TicketPriority": ".ticket_priority",
    "TicketPriorityUpdated": ".ticket_priority_updated",
    "TicketProjectUpdated": ".ticket_project_updated",
    "TicketRemainingTimeUpdated": ".ticket_remaining_time_updated",
    "TicketStatus": ".ticket_status",
    "TicketStatusUpdated": ".ticket_status_updated",
    "TicketSubjectUpdated": ".ticket_subject_updated",
    "TicketType": ".ticket_type",
    "TicketUrgency": ".ticket_urgency",
    "TicketUrgencyUpdated": ".ticket_urgency_updated",
    "User": ".user",
    "UserInfo": ".user_info",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "Attachment",
    "ItemsResultOfProject",
    "ItemsResultOfProjectGroup",
    "ItemsResultOfProjectMembership",
    "ItemsResultOfTeam",
    "ItemsResultOfTeamMembership",
    "Organization",
    "PagedResultOfOrganization",
    "PagedResultOfTicket",
    "PagedResultOfTicketComment",
    "PagedResultOfTicketEvent",
    "PagedResultOfTicketStatus",
    "PagedResultOfUser",
    "ProblemDetails",
    "Project",
    "ProjectGroup",
    "ProjectMembership",
    "SortDirection",
    "Tag",
    "Team",
    "TeamMember",
    "TeamMembership",
    "Ticket",
    "TicketAssigneeUpdated",
    "TicketComment",
    "TicketCommentAdded",
    "TicketCreated",
    "TicketDescriptionUpdated",
    "TicketEstimatedTimeUpdated",
    "TicketEvent",
    "TicketEvent_TicketAssigneeUpdated",
    "TicketEvent_TicketCommentAdded",
    "TicketEvent_TicketCreated",
    "TicketEvent_TicketDescriptionUpdated",
    "TicketEvent_TicketEstimatedTimeUpdated",
    "TicketEvent_TicketImpactUpdated",
    "TicketEvent_TicketPriorityUpdated",
    "TicketEvent_TicketProjectUpdated",
    "TicketEvent_TicketRemainingTimeUpdated",
    "TicketEvent_TicketStatusUpdated",
    "TicketEvent_TicketSubjectUpdated",
    "TicketEvent_TicketUrgencyUpdated",
    "TicketImpact",
    "TicketImpactUpdated",
    "TicketParticipant",
    "TicketPriority",
    "TicketPriorityUpdated",
    "TicketProjectUpdated",
    "TicketRemainingTimeUpdated",
    "TicketStatus",
    "TicketStatusUpdated",
    "TicketSubjectUpdated",
    "TicketType",
    "TicketUrgency",
    "TicketUrgencyUpdated",
    "User",
    "UserInfo",
]
