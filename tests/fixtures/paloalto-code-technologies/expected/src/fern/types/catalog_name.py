

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogName(enum.StrEnum):
    GITHUB = "Github"
    GITLAB = "Gitlab"
    BITBUCKET = "Bitbucket"
    AZURE_REPOS = "Azure Repos"
    CODE_COMMIT = "CodeCommit"
    JENKINS = "Jenkins"
    TEAM_CITY = "TeamCity"
    TRAVIS_CI = "Travis CI"
    GIT_HUB_ACTIONS = "GitHub Actions"
    GIT_LAB_CI_CD = "GitLab CI/CD"
    BITBUCKET_PIPELINES = "Bitbucket Pipelines"
    CODE_FRESH = "CodeFresh"
    CIRCLE_CI = "CircleCI"
    ARGO_CD = "Argo CD"
    CONCOURSE_CI = "Concourse CI"
    BUILD_KITE = "BuildKite"
    AWS_CODE_BUILD = "AWS CodeBuild"
    AWS_CODE_DEPLOY = "AWS CodeDeploy"
    AWS_CODE_PIPELINE = "AWS CodePipeline"
    DRONE = "Drone"
    J_FROG_ARTIFACTORY = "JFrog Artifactory"
    AWS_ECR = "AWS ECR"
    NEXUS = "Nexus"
    DOCKER_HUB = "Docker Hub"
    GIT_HUB_REGISTRY = "GitHub Registry"
    AWS_EC2 = "AWS EC2"
    AWS_EKS = "AWS EKS"
    AWS_ECS = "AWS ECS"
    AWS_LAMBDA = "AWS Lambda"
    AWS_APP_MESH = "AWS App Mesh"
    AWS_API_GATEWAY = "AWS API Gateway"
    AWS_ELASTIC_LOAD_BALANCING = "AWS Elastic Load Balancing"
    AZURE_VIRTUAL_MACHINES = "Azure Virtual Machines"
    AZURE_FUNCTIONS = "Azure Functions"
    AZURE_AKS = "Azure AKS"
    AZURE_CONTAINER_INSTANCES = "Azure Container Instances"
    AZURE_SERVICE_FABRIC = "Azure Service Fabric"
    GOOGLE_KUBERNETES_ENGINE = "Google Kubernetes Engine"
    GOOGLE_COMPUTE_ENGINE = "Google Compute Engine"
    GOOGLE_CONTAINER_REGISTRY = "Google Container Registry"
    CHROMATIC = "Chromatic"
    ENV0 = "env0"
    FIRE_FLY = "FireFly"
    TESTIM = "Testim"
    UNITY = "Unity"
    JFROG_XRAY = "JfrogXray"
    BUDDY_WORKS = "Buddy.Works"
    SNOWFLAKE = "Snowflake"
    DATABRICKS = "databricks"
    HEROKU = "Heroku"
    NETLIFY = "Netlify"
    PAGER_DUTY = "PagerDuty"
    NGROK = "Ngrok"
    GOOGLE_PLAY = "Google Play"
    FIRE_BASE = "FireBase"
    NPM = "npm"
    GRAFANA = "Grafana"
    AWS_DYNAMO_DB = "AWS DynamoDB"
    GOOGLE_CLOUD_FUNCTIONS = "Google Cloud Functions"
    GOOGLE_CLOUD_BUILD = "Google Cloud Build"
    AZURE_PIPELINES = "Azure Pipelines"
    AWS_CODE_ARTIFACT = "AWS CodeArtifact"
    AWS_STS = "AWS STS"
    AWS_SQS = "AWS SQS"
    AWS_SNS = "AWS SNS"
    AWS_S3 = "AWS S3"
    HASHI_CORP_CONSUL = "HashiCorp Consul"
    DATADOG = "Datadog"
    SENTRY = "SENTRY"
    BAMBOO = "Bamboo"
    TERRAFORM_CLOUD = "Terraform Cloud"
    NX_CLOUD = "Nx Cloud"
    DEPLOY_HQ = "DeployHQ"
    CLOUDFLARE = "Cloudflare"
    ALLURE_TEST_OPS = "Allure TestOps"
    BITRISE = "Bitrise"
    SKAFFOLD = "Skaffold"
    GOOGLE_CLOUD_RUN = "Google Cloud Run"
    CODECOV = "Codecov"
    CHECKOV = "Checkov"
    CYPRESS = "Cypress"
    SNYK = "Snyk"
    HELM = "Helm"
    SALESFORCE = "Salesforce"
    NGINX = "Nginx"
    BANDIT = "Bandit"
    VELOCITY = "Velocity"
    COVERAGE_PY = "CoveragePy"
    HASHI_CORP_VAULT = "HashiCorpVault"
    ZAPIER = "Zapier"
    ANSIBLE = "Ansible"
    YOR = "Yor"
    SEMGREP = "Semgrep"
    TRIVY_ACTION = "TrivyAction"
    SLACK = "Slack"
    GIT_LEAKS = "GitLeaks"
    AZURE_ARTIFACTS_FEED = "Azure Artifacts Feed"
    ADOBE_CLOUD_MANAGER = "Adobe Cloud Manager"
    ADOBE_CLOUD_PACKAGE_MANAGER = "Adobe Cloud Package Manager"

    def visit(
        self,
        github: typing.Callable[[], T_Result],
        gitlab: typing.Callable[[], T_Result],
        bitbucket: typing.Callable[[], T_Result],
        azure_repos: typing.Callable[[], T_Result],
        code_commit: typing.Callable[[], T_Result],
        jenkins: typing.Callable[[], T_Result],
        team_city: typing.Callable[[], T_Result],
        travis_ci: typing.Callable[[], T_Result],
        git_hub_actions: typing.Callable[[], T_Result],
        git_lab_ci_cd: typing.Callable[[], T_Result],
        bitbucket_pipelines: typing.Callable[[], T_Result],
        code_fresh: typing.Callable[[], T_Result],
        circle_ci: typing.Callable[[], T_Result],
        argo_cd: typing.Callable[[], T_Result],
        concourse_ci: typing.Callable[[], T_Result],
        build_kite: typing.Callable[[], T_Result],
        aws_code_build: typing.Callable[[], T_Result],
        aws_code_deploy: typing.Callable[[], T_Result],
        aws_code_pipeline: typing.Callable[[], T_Result],
        drone: typing.Callable[[], T_Result],
        j_frog_artifactory: typing.Callable[[], T_Result],
        aws_ecr: typing.Callable[[], T_Result],
        nexus: typing.Callable[[], T_Result],
        docker_hub: typing.Callable[[], T_Result],
        git_hub_registry: typing.Callable[[], T_Result],
        aws_ec2: typing.Callable[[], T_Result],
        aws_eks: typing.Callable[[], T_Result],
        aws_ecs: typing.Callable[[], T_Result],
        aws_lambda: typing.Callable[[], T_Result],
        aws_app_mesh: typing.Callable[[], T_Result],
        aws_api_gateway: typing.Callable[[], T_Result],
        aws_elastic_load_balancing: typing.Callable[[], T_Result],
        azure_virtual_machines: typing.Callable[[], T_Result],
        azure_functions: typing.Callable[[], T_Result],
        azure_aks: typing.Callable[[], T_Result],
        azure_container_instances: typing.Callable[[], T_Result],
        azure_service_fabric: typing.Callable[[], T_Result],
        google_kubernetes_engine: typing.Callable[[], T_Result],
        google_compute_engine: typing.Callable[[], T_Result],
        google_container_registry: typing.Callable[[], T_Result],
        chromatic: typing.Callable[[], T_Result],
        env0: typing.Callable[[], T_Result],
        fire_fly: typing.Callable[[], T_Result],
        testim: typing.Callable[[], T_Result],
        unity: typing.Callable[[], T_Result],
        jfrog_xray: typing.Callable[[], T_Result],
        buddy_works: typing.Callable[[], T_Result],
        snowflake: typing.Callable[[], T_Result],
        databricks: typing.Callable[[], T_Result],
        heroku: typing.Callable[[], T_Result],
        netlify: typing.Callable[[], T_Result],
        pager_duty: typing.Callable[[], T_Result],
        ngrok: typing.Callable[[], T_Result],
        google_play: typing.Callable[[], T_Result],
        fire_base: typing.Callable[[], T_Result],
        npm: typing.Callable[[], T_Result],
        grafana: typing.Callable[[], T_Result],
        aws_dynamo_db: typing.Callable[[], T_Result],
        google_cloud_functions: typing.Callable[[], T_Result],
        google_cloud_build: typing.Callable[[], T_Result],
        azure_pipelines: typing.Callable[[], T_Result],
        aws_code_artifact: typing.Callable[[], T_Result],
        aws_sts: typing.Callable[[], T_Result],
        aws_sqs: typing.Callable[[], T_Result],
        aws_sns: typing.Callable[[], T_Result],
        aws_s3: typing.Callable[[], T_Result],
        hashi_corp_consul: typing.Callable[[], T_Result],
        datadog: typing.Callable[[], T_Result],
        sentry: typing.Callable[[], T_Result],
        bamboo: typing.Callable[[], T_Result],
        terraform_cloud: typing.Callable[[], T_Result],
        nx_cloud: typing.Callable[[], T_Result],
        deploy_hq: typing.Callable[[], T_Result],
        cloudflare: typing.Callable[[], T_Result],
        allure_test_ops: typing.Callable[[], T_Result],
        bitrise: typing.Callable[[], T_Result],
        skaffold: typing.Callable[[], T_Result],
        google_cloud_run: typing.Callable[[], T_Result],
        codecov: typing.Callable[[], T_Result],
        checkov: typing.Callable[[], T_Result],
        cypress: typing.Callable[[], T_Result],
        snyk: typing.Callable[[], T_Result],
        helm: typing.Callable[[], T_Result],
        salesforce: typing.Callable[[], T_Result],
        nginx: typing.Callable[[], T_Result],
        bandit: typing.Callable[[], T_Result],
        velocity: typing.Callable[[], T_Result],
        coverage_py: typing.Callable[[], T_Result],
        hashi_corp_vault: typing.Callable[[], T_Result],
        zapier: typing.Callable[[], T_Result],
        ansible: typing.Callable[[], T_Result],
        yor: typing.Callable[[], T_Result],
        semgrep: typing.Callable[[], T_Result],
        trivy_action: typing.Callable[[], T_Result],
        slack: typing.Callable[[], T_Result],
        git_leaks: typing.Callable[[], T_Result],
        azure_artifacts_feed: typing.Callable[[], T_Result],
        adobe_cloud_manager: typing.Callable[[], T_Result],
        adobe_cloud_package_manager: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatalogName.GITHUB:
            return github()
        if self is CatalogName.GITLAB:
            return gitlab()
        if self is CatalogName.BITBUCKET:
            return bitbucket()
        if self is CatalogName.AZURE_REPOS:
            return azure_repos()
        if self is CatalogName.CODE_COMMIT:
            return code_commit()
        if self is CatalogName.JENKINS:
            return jenkins()
        if self is CatalogName.TEAM_CITY:
            return team_city()
        if self is CatalogName.TRAVIS_CI:
            return travis_ci()
        if self is CatalogName.GIT_HUB_ACTIONS:
            return git_hub_actions()
        if self is CatalogName.GIT_LAB_CI_CD:
            return git_lab_ci_cd()
        if self is CatalogName.BITBUCKET_PIPELINES:
            return bitbucket_pipelines()
        if self is CatalogName.CODE_FRESH:
            return code_fresh()
        if self is CatalogName.CIRCLE_CI:
            return circle_ci()
        if self is CatalogName.ARGO_CD:
            return argo_cd()
        if self is CatalogName.CONCOURSE_CI:
            return concourse_ci()
        if self is CatalogName.BUILD_KITE:
            return build_kite()
        if self is CatalogName.AWS_CODE_BUILD:
            return aws_code_build()
        if self is CatalogName.AWS_CODE_DEPLOY:
            return aws_code_deploy()
        if self is CatalogName.AWS_CODE_PIPELINE:
            return aws_code_pipeline()
        if self is CatalogName.DRONE:
            return drone()
        if self is CatalogName.J_FROG_ARTIFACTORY:
            return j_frog_artifactory()
        if self is CatalogName.AWS_ECR:
            return aws_ecr()
        if self is CatalogName.NEXUS:
            return nexus()
        if self is CatalogName.DOCKER_HUB:
            return docker_hub()
        if self is CatalogName.GIT_HUB_REGISTRY:
            return git_hub_registry()
        if self is CatalogName.AWS_EC2:
            return aws_ec2()
        if self is CatalogName.AWS_EKS:
            return aws_eks()
        if self is CatalogName.AWS_ECS:
            return aws_ecs()
        if self is CatalogName.AWS_LAMBDA:
            return aws_lambda()
        if self is CatalogName.AWS_APP_MESH:
            return aws_app_mesh()
        if self is CatalogName.AWS_API_GATEWAY:
            return aws_api_gateway()
        if self is CatalogName.AWS_ELASTIC_LOAD_BALANCING:
            return aws_elastic_load_balancing()
        if self is CatalogName.AZURE_VIRTUAL_MACHINES:
            return azure_virtual_machines()
        if self is CatalogName.AZURE_FUNCTIONS:
            return azure_functions()
        if self is CatalogName.AZURE_AKS:
            return azure_aks()
        if self is CatalogName.AZURE_CONTAINER_INSTANCES:
            return azure_container_instances()
        if self is CatalogName.AZURE_SERVICE_FABRIC:
            return azure_service_fabric()
        if self is CatalogName.GOOGLE_KUBERNETES_ENGINE:
            return google_kubernetes_engine()
        if self is CatalogName.GOOGLE_COMPUTE_ENGINE:
            return google_compute_engine()
        if self is CatalogName.GOOGLE_CONTAINER_REGISTRY:
            return google_container_registry()
        if self is CatalogName.CHROMATIC:
            return chromatic()
        if self is CatalogName.ENV0:
            return env0()
        if self is CatalogName.FIRE_FLY:
            return fire_fly()
        if self is CatalogName.TESTIM:
            return testim()
        if self is CatalogName.UNITY:
            return unity()
        if self is CatalogName.JFROG_XRAY:
            return jfrog_xray()
        if self is CatalogName.BUDDY_WORKS:
            return buddy_works()
        if self is CatalogName.SNOWFLAKE:
            return snowflake()
        if self is CatalogName.DATABRICKS:
            return databricks()
        if self is CatalogName.HEROKU:
            return heroku()
        if self is CatalogName.NETLIFY:
            return netlify()
        if self is CatalogName.PAGER_DUTY:
            return pager_duty()
        if self is CatalogName.NGROK:
            return ngrok()
        if self is CatalogName.GOOGLE_PLAY:
            return google_play()
        if self is CatalogName.FIRE_BASE:
            return fire_base()
        if self is CatalogName.NPM:
            return npm()
        if self is CatalogName.GRAFANA:
            return grafana()
        if self is CatalogName.AWS_DYNAMO_DB:
            return aws_dynamo_db()
        if self is CatalogName.GOOGLE_CLOUD_FUNCTIONS:
            return google_cloud_functions()
        if self is CatalogName.GOOGLE_CLOUD_BUILD:
            return google_cloud_build()
        if self is CatalogName.AZURE_PIPELINES:
            return azure_pipelines()
        if self is CatalogName.AWS_CODE_ARTIFACT:
            return aws_code_artifact()
        if self is CatalogName.AWS_STS:
            return aws_sts()
        if self is CatalogName.AWS_SQS:
            return aws_sqs()
        if self is CatalogName.AWS_SNS:
            return aws_sns()
        if self is CatalogName.AWS_S3:
            return aws_s3()
        if self is CatalogName.HASHI_CORP_CONSUL:
            return hashi_corp_consul()
        if self is CatalogName.DATADOG:
            return datadog()
        if self is CatalogName.SENTRY:
            return sentry()
        if self is CatalogName.BAMBOO:
            return bamboo()
        if self is CatalogName.TERRAFORM_CLOUD:
            return terraform_cloud()
        if self is CatalogName.NX_CLOUD:
            return nx_cloud()
        if self is CatalogName.DEPLOY_HQ:
            return deploy_hq()
        if self is CatalogName.CLOUDFLARE:
            return cloudflare()
        if self is CatalogName.ALLURE_TEST_OPS:
            return allure_test_ops()
        if self is CatalogName.BITRISE:
            return bitrise()
        if self is CatalogName.SKAFFOLD:
            return skaffold()
        if self is CatalogName.GOOGLE_CLOUD_RUN:
            return google_cloud_run()
        if self is CatalogName.CODECOV:
            return codecov()
        if self is CatalogName.CHECKOV:
            return checkov()
        if self is CatalogName.CYPRESS:
            return cypress()
        if self is CatalogName.SNYK:
            return snyk()
        if self is CatalogName.HELM:
            return helm()
        if self is CatalogName.SALESFORCE:
            return salesforce()
        if self is CatalogName.NGINX:
            return nginx()
        if self is CatalogName.BANDIT:
            return bandit()
        if self is CatalogName.VELOCITY:
            return velocity()
        if self is CatalogName.COVERAGE_PY:
            return coverage_py()
        if self is CatalogName.HASHI_CORP_VAULT:
            return hashi_corp_vault()
        if self is CatalogName.ZAPIER:
            return zapier()
        if self is CatalogName.ANSIBLE:
            return ansible()
        if self is CatalogName.YOR:
            return yor()
        if self is CatalogName.SEMGREP:
            return semgrep()
        if self is CatalogName.TRIVY_ACTION:
            return trivy_action()
        if self is CatalogName.SLACK:
            return slack()
        if self is CatalogName.GIT_LEAKS:
            return git_leaks()
        if self is CatalogName.AZURE_ARTIFACTS_FEED:
            return azure_artifacts_feed()
        if self is CatalogName.ADOBE_CLOUD_MANAGER:
            return adobe_cloud_manager()
        if self is CatalogName.ADOBE_CLOUD_PACKAGE_MANAGER:
            return adobe_cloud_package_manager()
