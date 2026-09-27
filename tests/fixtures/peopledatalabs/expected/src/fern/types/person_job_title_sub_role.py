

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PersonJobTitleSubRole(enum.StrEnum):
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
        if self is PersonJobTitleSubRole.ACCOUNTING:
            return accounting()
        if self is PersonJobTitleSubRole.ACCOUNTS:
            return accounts()
        if self is PersonJobTitleSubRole.BRAND_MARKETING:
            return brand_marketing()
        if self is PersonJobTitleSubRole.BROADCASTING:
            return broadcasting()
        if self is PersonJobTitleSubRole.BUSINESS_DEVELOPMENT:
            return business_development()
        if self is PersonJobTitleSubRole.COMPENSATION:
            return compensation()
        if self is PersonJobTitleSubRole.CONTENT_MARKETING:
            return content_marketing()
        if self is PersonJobTitleSubRole.CUSTOMER_SUCCESS:
            return customer_success()
        if self is PersonJobTitleSubRole.DATA:
            return data()
        if self is PersonJobTitleSubRole.DENTAL:
            return dental()
        if self is PersonJobTitleSubRole.DEVOPS:
            return devops()
        if self is PersonJobTitleSubRole.DOCTOR:
            return doctor()
        if self is PersonJobTitleSubRole.EDITORIAL:
            return editorial()
        if self is PersonJobTitleSubRole.EDUCATION_ADMINISTRATION:
            return education_administration()
        if self is PersonJobTitleSubRole.ELECTRICAL:
            return electrical()
        if self is PersonJobTitleSubRole.EMPLOYEE_DEVELOPMENT:
            return employee_development()
        if self is PersonJobTitleSubRole.EVENTS:
            return events()
        if self is PersonJobTitleSubRole.FITNESS:
            return fitness()
        if self is PersonJobTitleSubRole.GRAPHIC_DESIGN:
            return graphic_design()
        if self is PersonJobTitleSubRole.INFORMATION_TECHNOLOGY:
            return information_technology()
        if self is PersonJobTitleSubRole.INVESTMENT:
            return investment()
        if self is PersonJobTitleSubRole.JOURNALISM:
            return journalism()
        if self is PersonJobTitleSubRole.JUDICIAL:
            return judicial()
        if self is PersonJobTitleSubRole.LAWYER:
            return lawyer()
        if self is PersonJobTitleSubRole.LOGISTICS:
            return logistics()
        if self is PersonJobTitleSubRole.MECHANICAL:
            return mechanical()
        if self is PersonJobTitleSubRole.MEDIA_RELATIONS:
            return media_relations()
        if self is PersonJobTitleSubRole.NETWORK:
            return network()
        if self is PersonJobTitleSubRole.NURSING:
            return nursing()
        if self is PersonJobTitleSubRole.OFFICE_MANAGEMENT:
            return office_management()
        if self is PersonJobTitleSubRole.PARALEGAL:
            return paralegal()
        if self is PersonJobTitleSubRole.PIPELINE:
            return pipeline()
        if self is PersonJobTitleSubRole.PRODUCT:
            return product()
        if self is PersonJobTitleSubRole.PRODUCT_DESIGN:
            return product_design()
        if self is PersonJobTitleSubRole.PRODUCT_MARKETING:
            return product_marketing()
        if self is PersonJobTitleSubRole.PROFESSOR:
            return professor()
        if self is PersonJobTitleSubRole.PROJECT_ENGINEERING:
            return project_engineering()
        if self is PersonJobTitleSubRole.PROJECT_MANAGEMENT:
            return project_management()
        if self is PersonJobTitleSubRole.PROPERTY_MANAGEMENT:
            return property_management()
        if self is PersonJobTitleSubRole.QUALITY_ASSURANCE:
            return quality_assurance()
        if self is PersonJobTitleSubRole.REALTOR:
            return realtor()
        if self is PersonJobTitleSubRole.RECRUITING:
            return recruiting()
        if self is PersonJobTitleSubRole.RESEARCHER:
            return researcher()
        if self is PersonJobTitleSubRole.SECURITY:
            return security()
        if self is PersonJobTitleSubRole.SOFTWARE:
            return software()
        if self is PersonJobTitleSubRole.SUPPORT:
            return support()
        if self is PersonJobTitleSubRole.SYSTEMS:
            return systems()
        if self is PersonJobTitleSubRole.TAX:
            return tax()
        if self is PersonJobTitleSubRole.TEACHER:
            return teacher()
        if self is PersonJobTitleSubRole.THERAPY:
            return therapy()
        if self is PersonJobTitleSubRole.VIDEO:
            return video()
        if self is PersonJobTitleSubRole.WEB:
            return web()
        if self is PersonJobTitleSubRole.WEB_DESIGN:
            return web_design()
        if self is PersonJobTitleSubRole.WELLNESS:
            return wellness()
        if self is PersonJobTitleSubRole.WRITING:
            return writing()
