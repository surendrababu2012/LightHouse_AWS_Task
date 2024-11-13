from aws_cdk import App, Environment
from taskAPI_Stack import TaskApiStack

app = App()
TaskApiStack(app, "TaskApiStack",env=Environment(account="211125701790", region="us-east-1"))
app.synth()

