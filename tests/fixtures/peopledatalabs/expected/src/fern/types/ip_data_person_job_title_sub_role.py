

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IpDataPersonJobTitleSubRole(enum.StrEnum):
    """
    A person's job title derived subrole. Each subrole maps to a role
    """

    ACCOUNTING = "accounting"
    ACCOUNTS = "accounts"
    BRAND_MARKETING = "brand_marketing"
    BROADCASTING = "broadcasting"
    BUSINESS_DEVELOPMENT = "business_development"
    COMPENSATION = "compensation"
    CONTENT_MARKETING = "content_marketing"
    CUSTOMER_SUCCESS = "customer_success"
    DATA = "data"
    DENTAL = "dental"
    DEVOPS = "devops"
    DOCTOR = "doctor"
    EDITORIAL = "editorial"
    EDUCATION_ADMINISTRATION = "education_administration"
    ELECTRICAL = "electrical"
    EMPLOYEE_DEVELOPMENT = "employee_development"
    EVENTS = "events"
    FITNESS = "fitness"
    GRAPHIC_DESIGN = "graphic_design"
    INFORMATION_TECHNOLOGY = "information_technology"
    INVESTMENT = "investment"
    JOURNALISM = "journalism"
    JUDICIAL = "judicial"
    LAWYER = "lawyer"
    LOGISTICS = "logistics"
    MECHANICAL = "mechanical"
    MEDIA_RELATIONS = "media_relations"
    NETWORK = "network"
    NURSING = "nursing"
    OFFICE_MANAGEMENT = "office_management"
    PARALEGAL = "paralegal"
    PIPELINE = "pipeline"
    PRODUCT = "product"
    PRODUCT_DESIGN = "product_design"
    PRODUCT_MARKETING = "product_marketing"
    PROFESSOR = "professor"
    PROJECT_ENGINEERING = "project_engineering"
    PROJECT_MANAGEMENT = "project_management"
    PROPERTY_MANAGEMENT = "property_management"
    QUALITY_ASSURANCE = "quality_assurance"
    REALTOR = "realtor"
    RECRUITING = "recruiting"
    RESEARCHER = "researcher"
    SECURITY = "security"
    SOFTWARE = "software"
    SUPPORT = "support"
    SYSTEMS = "systems"
    TAX = "tax"
    TEACHER = "teacher"
    THERAPY = "therapy"
    VIDEO = "video"
    WEB = "web"
    WEB_DESIGN = "web_design"
    WELLNESS = "wellness"
    WRITING = "writing"

    def visit(
        self,
        accounting: typing.Callable[[], T_Result],
        accounts: typing.Callable[[], T_Result],
        brand_marketing: typing.Callable[[], T_Result],
        broadcasting: typing.Callable[[], T_Result],
        business_development: typing.Callable[[], T_Result],
        compensation: typing.Callable[[], T_Result],
        content_marketing: typing.Callable[[], T_Result],
        customer_success: typing.Callable[[], T_Result],
        data: typing.Callable[[], T_Result],
        dental: typing.Callable[[], T_Result],
        devops: typing.Callable[[], T_Result],
        doctor: typing.Callable[[], T_Result],
        editorial: typing.Callable[[], T_Result],
        education_administration: typing.Callable[[], T_Result],
        electrical: typing.Callable[[], T_Result],
        employee_development: typing.Callable[[], T_Result],
        events: typing.Callable[[], T_Result],
        fitness: typing.Callable[[], T_Result],
        graphic_design: typing.Callable[[], T_Result],
        information_technology: typing.Callable[[], T_Result],
        investment: typing.Callable[[], T_Result],
        journalism: typing.Callable[[], T_Result],
        judicial: typing.Callable[[], T_Result],
        lawyer: typing.Callable[[], T_Result],
        logistics: typing.Callable[[], T_Result],
        mechanical: typing.Callable[[], T_Result],
        media_relations: typing.Callable[[], T_Result],
        network: typing.Callable[[], T_Result],
        nursing: typing.Callable[[], T_Result],
        office_management: typing.Callable[[], T_Result],
        paralegal: typing.Callable[[], T_Result],
        pipeline: typing.Callable[[], T_Result],
        product: typing.Callable[[], T_Result],
        product_design: typing.Callable[[], T_Result],
        product_marketing: typing.Callable[[], T_Result],
        professor: typing.Callable[[], T_Result],
        project_engineering: typing.Callable[[], T_Result],
        project_management: typing.Callable[[], T_Result],
        property_management: typing.Callable[[], T_Result],
        quality_assurance: typing.Callable[[], T_Result],
        realtor: typing.Callable[[], T_Result],
        recruiting: typing.Callable[[], T_Result],
        researcher: typing.Callable[[], T_Result],
        security: typing.Callable[[], T_Result],
        software: typing.Callable[[], T_Result],
        support: typing.Callable[[], T_Result],
        systems: typing.Callable[[], T_Result],
        tax: typing.Callable[[], T_Result],
        teacher: typing.Callable[[], T_Result],
        therapy: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
        web: typing.Callable[[], T_Result],
        web_design: typing.Callable[[], T_Result],
        wellness: typing.Callable[[], T_Result],
        writing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IpDataPersonJobTitleSubRole.ACCOUNTING:
            return accounting()
        if self is IpDataPersonJobTitleSubRole.ACCOUNTS:
            return accounts()
        if self is IpDataPersonJobTitleSubRole.BRAND_MARKETING:
            return brand_marketing()
        if self is IpDataPersonJobTitleSubRole.BROADCASTING:
            return broadcasting()
        if self is IpDataPersonJobTitleSubRole.BUSINESS_DEVELOPMENT:
            return business_development()
        if self is IpDataPersonJobTitleSubRole.COMPENSATION:
            return compensation()
        if self is IpDataPersonJobTitleSubRole.CONTENT_MARKETING:
            return content_marketing()
        if self is IpDataPersonJobTitleSubRole.CUSTOMER_SUCCESS:
            return customer_success()
        if self is IpDataPersonJobTitleSubRole.DATA:
            return data()
        if self is IpDataPersonJobTitleSubRole.DENTAL:
            return dental()
        if self is IpDataPersonJobTitleSubRole.DEVOPS:
            return devops()
        if self is IpDataPersonJobTitleSubRole.DOCTOR:
            return doctor()
        if self is IpDataPersonJobTitleSubRole.EDITORIAL:
            return editorial()
        if self is IpDataPersonJobTitleSubRole.EDUCATION_ADMINISTRATION:
            return education_administration()
        if self is IpDataPersonJobTitleSubRole.ELECTRICAL:
            return electrical()
        if self is IpDataPersonJobTitleSubRole.EMPLOYEE_DEVELOPMENT:
            return employee_development()
        if self is IpDataPersonJobTitleSubRole.EVENTS:
            return events()
        if self is IpDataPersonJobTitleSubRole.FITNESS:
            return fitness()
        if self is IpDataPersonJobTitleSubRole.GRAPHIC_DESIGN:
            return graphic_design()
        if self is IpDataPersonJobTitleSubRole.INFORMATION_TECHNOLOGY:
            return information_technology()
        if self is IpDataPersonJobTitleSubRole.INVESTMENT:
            return investment()
        if self is IpDataPersonJobTitleSubRole.JOURNALISM:
            return journalism()
        if self is IpDataPersonJobTitleSubRole.JUDICIAL:
            return judicial()
        if self is IpDataPersonJobTitleSubRole.LAWYER:
            return lawyer()
        if self is IpDataPersonJobTitleSubRole.LOGISTICS:
            return logistics()
        if self is IpDataPersonJobTitleSubRole.MECHANICAL:
            return mechanical()
        if self is IpDataPersonJobTitleSubRole.MEDIA_RELATIONS:
            return media_relations()
        if self is IpDataPersonJobTitleSubRole.NETWORK:
            return network()
        if self is IpDataPersonJobTitleSubRole.NURSING:
            return nursing()
        if self is IpDataPersonJobTitleSubRole.OFFICE_MANAGEMENT:
            return office_management()
        if self is IpDataPersonJobTitleSubRole.PARALEGAL:
            return paralegal()
        if self is IpDataPersonJobTitleSubRole.PIPELINE:
            return pipeline()
        if self is IpDataPersonJobTitleSubRole.PRODUCT:
            return product()
        if self is IpDataPersonJobTitleSubRole.PRODUCT_DESIGN:
            return product_design()
        if self is IpDataPersonJobTitleSubRole.PRODUCT_MARKETING:
            return product_marketing()
        if self is IpDataPersonJobTitleSubRole.PROFESSOR:
            return professor()
        if self is IpDataPersonJobTitleSubRole.PROJECT_ENGINEERING:
            return project_engineering()
        if self is IpDataPersonJobTitleSubRole.PROJECT_MANAGEMENT:
            return project_management()
        if self is IpDataPersonJobTitleSubRole.PROPERTY_MANAGEMENT:
            return property_management()
        if self is IpDataPersonJobTitleSubRole.QUALITY_ASSURANCE:
            return quality_assurance()
        if self is IpDataPersonJobTitleSubRole.REALTOR:
            return realtor()
        if self is IpDataPersonJobTitleSubRole.RECRUITING:
            return recruiting()
        if self is IpDataPersonJobTitleSubRole.RESEARCHER:
            return researcher()
        if self is IpDataPersonJobTitleSubRole.SECURITY:
            return security()
        if self is IpDataPersonJobTitleSubRole.SOFTWARE:
            return software()
        if self is IpDataPersonJobTitleSubRole.SUPPORT:
            return support()
        if self is IpDataPersonJobTitleSubRole.SYSTEMS:
            return systems()
        if self is IpDataPersonJobTitleSubRole.TAX:
            return tax()
        if self is IpDataPersonJobTitleSubRole.TEACHER:
            return teacher()
        if self is IpDataPersonJobTitleSubRole.THERAPY:
            return therapy()
        if self is IpDataPersonJobTitleSubRole.VIDEO:
            return video()
        if self is IpDataPersonJobTitleSubRole.WEB:
            return web()
        if self is IpDataPersonJobTitleSubRole.WEB_DESIGN:
            return web_design()
        if self is IpDataPersonJobTitleSubRole.WELLNESS:
            return wellness()
        if self is IpDataPersonJobTitleSubRole.WRITING:
            return writing()
