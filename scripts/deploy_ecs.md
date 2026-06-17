# ECS Deploy

1. Build and push the image with `scripts/push_to_ecr.sh`.
2. Upload model artifacts to S3 or mount them into the image for a demo.
3. Register `infra/aws/ecs-task-definition.json`.
4. Create or update the ECS service with `infra/aws/ecs-service-example.json`.
5. Check CloudWatch logs for startup and request logs.
