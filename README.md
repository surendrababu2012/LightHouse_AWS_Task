
# Serverless CRUD API for Tasks

This project implements a serverless CRUD API for managing tasks using AWS CDK, Lambda, API Gateway, and DynamoDB. The API supports creating, reading, updating, and deleting tasks, each identified by a unique `taskId` and containing fields for `title`, `description`, and `status`.

---

## Solution Details

This solution satisfies the following requirements:

1. **CRUD Operations**: Provides API endpoints to create, read, update, and delete tasks.
2. **AWS CDK**: Defines all resources (DynamoDB table, Lambda functions, and API Gateway) using AWS CDK.
3. **API Gateway Integration**: Integrates Lambda functions with API Gateway, assigning appropriate HTTP methods (`POST`, `GET`, `PUT`, `DELETE`) to the endpoints.
4. **DynamoDB Access**: Lambda functions interact with DynamoDB using the AWS SDK for Python (`boto3`).

## Architecture

The architecture includes the following resources:

- **DynamoDB Table** (`TasksTable`): Stores tasks with attributes `taskId`, `title`, `description`, and `status`.
- **Lambda Functions**:
  - **Create Task** (`POST /tasks`): Creates a new task with auto-generated `taskId`.
  - **Get Task** (`GET /tasks/{taskId}`): Fetches a task by `taskId`.
  - **Update Task** (`PUT /tasks/{taskId}`): Updates task details.
  - **Delete Task** (`DELETE /tasks/{taskId}`): Deletes a task by `taskId`.
- **API Gateway**: Provides a RESTful API to expose the Lambda functions as HTTP endpoints.

## Deployment Instructions

### Prerequisites

- **AWS Account**: Ensure you have an AWS account and the necessary permissions to create resources.
- **AWS CLI**: Install and configure the AWS CLI. ([AWS CLI Installation Guide](https://aws.amazon.com/cli/))
- **AWS CDK**: Install the AWS CDK globally using Node.js.

```sh
  npm install -g aws-cdk
```

Python 3.8 or above: Required for Python-based Lambda functions.
Python dependencies: Install project-specific dependencies, typically defined in requirements.txt.

Step 1: Clone the Repository
Clone the repository to your local environment:

```sh
git clone https://github.com/surendrababu2012/LightHouse_AWS_Task

cd to/path
```

Step 2: Set Up a Python Virtual Environment
Create a virtual environment:

 ```sh
python3 -m venv .venv
Activate the virtual environment:
```

On macOS/Linux:

 ```sh
source .venv/bin/activate
```

On Windows:

 ```sh
 .venv\Scripts\activate
```

Step 3: Install Project Dependencies
Install the dependencies specified in requirements.txt:

```sh
pip install -r requirements.txt
```

Step 4: Configure AWS CLI
Set up your AWS CLI with your credentials:

```sh
aws configure
```

Enter your AWS Access Key ID, Secret Access Key, region, and output format.

Step 5: Bootstrap the CDK Environment
Bootstrap the environment. This step is only required once per account and region:

```sh
cdk bootstrap
```

This command prepares the environment by creating the necessary infrastructure for deploying CDK applications, such as an S3 bucket for storing assets.

Step 6: Set Environment Variables
Make sure the Lambda functions read the TABLE_NAME from environment variables if needed. These can be configured in the directory and has to be set in the AWS Lambda console after deployment.

Step 7: Synthesize the CDK Stack (Optional),
Run the following command to generate the CloudFormation template. This step is optional but helps confirm that the stack is correctly defined:

```sh
cdk synth
```

Step 8: Deploy the CDK Stack
Deploy the stack to AWS:

```sh
cdk deploy
```

Confirm the deployment by typing y when prompted.
CDK will output the API Gateway URL and other resource details upon successful deployment.

Step 9: Note the API Endpoint
After deployment, note the API Gateway endpoint URL provided in the output. You will use this URL to test the API.

API Endpoints
After deploying, you can access the following API endpoints:

Create Task (POST /tasks):

Request Body Example:
json

```sh
{
  "title": "Task 1",
  "description": "This is task 1",
  "status": "pending"
}
```

Response Example:

```sh
{
  "taskId": "generated-unique-id",
  "title": "Task 1",
  "description": "This is task 1",
  "status": "pending"
}
```

Get Task (GET /tasks/{taskId}):

```sh
{
  "taskId": "123",
  "title": "Task 1",
  "description": "This is task 1",
  "status": "in-progress"
}
```

Update Task (PUT /tasks/{taskId}):

```sh
{
  "title": "Updated Task 1",
  "description": "This task has been updated",
  "status": "completed"
}
```

Testing the API
You can test the API endpoints using Postman or cURL.

Example cURL Commands
Create Task:

```sh
curl -X POST https://your-api-id.execute-api.region.amazonaws.com/prod/tasks \
     -H "Content-Type: application/json" \
     -d '{"title": "New Task", "description": "A new task", "status": "pending"}'
```
