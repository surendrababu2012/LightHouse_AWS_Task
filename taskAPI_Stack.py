from aws_cdk import Stack, RemovalPolicy
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigateway as apigateway
from constructs import Construct


class TaskApiStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define DynamoDB table
        self.tasks_table = dynamodb.Table(
            self, "TasksTable",
            partition_key=dynamodb.Attribute(name="taskId", type=dynamodb.AttributeType.STRING),
            removal_policy=RemovalPolicy.DESTROY
        )

        # Lambda functions
        create_task_lambda = _lambda.Function(
            self, "CreateTaskFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="create_task.lambda_handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={"TABLE_NAME": self.tasks_table.table_name}
        )

        get_task_lambda = _lambda.Function(
            self, "GetTaskFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="get_task.lambda_handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={"TABLE_NAME": self.tasks_table.table_name}
        )

        update_task_lambda = _lambda.Function(
            self, "UpdateTaskFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="update_task.lambda_handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={"TABLE_NAME": self.tasks_table.table_name}
        )

        delete_task_lambda = _lambda.Function(
            self, "DeleteTaskFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="delete_task.lambda_handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={"TABLE_NAME": self.tasks_table.table_name}
        )

        # Grant Lambda functions permission to access DynamoDB table
        self.tasks_table.grant_read_write_data(create_task_lambda)
        self.tasks_table.grant_read_write_data(get_task_lambda)
        self.tasks_table.grant_read_write_data(update_task_lambda)
        self.tasks_table.grant_read_write_data(delete_task_lambda)

        # Set up API Gateway
        api = apigateway.RestApi(self, "TasksApi")

        # POST /tasks
        tasks_resource = api.root.add_resource("tasks")
        tasks_resource.add_method("POST", apigateway.LambdaIntegration(create_task_lambda))

        # GET, PUT, DELETE /tasks/{taskId}
        task_resource = tasks_resource.add_resource("{taskId}")
        task_resource.add_method("GET", apigateway.LambdaIntegration(get_task_lambda))
        task_resource.add_method("PUT", apigateway.LambdaIntegration(update_task_lambda))
        task_resource.add_method("DELETE", apigateway.LambdaIntegration(delete_task_lambda))
