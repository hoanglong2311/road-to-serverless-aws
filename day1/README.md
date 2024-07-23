# 30 Days of AWS Serverless Challenge - Day 1

## Unveiling the Serverless Paradigm

Welcome to Day 1 of the 30 Days of AWS Serverless Challenge! Today, we'll dive into the fundamentals of serverless computing and set up our AWS environment.

### Contents

1. [Theory](#theory)
2. [Practice](#practice)
3. [Mini Project](#mini-project)
4. [Research](#research)
5. [Additional Resources](#additional-resources)

### Theory

In this section, we'll explore:

#### The concept of serverless computing
Serverless computing is a cloud computing execution model where the cloud provider dynamically manages the allocation and provisioning of servers. A serverless application runs in stateless compute containers that are event-triggered, ephemeral (may last for one invocation), and fully managed by the cloud provider.

#### Comparison between serverless and traditional architectures
- Traditional: You provision and manage servers, worry about uptime, and pay for idle capacity.
- Serverless: No server management, auto-scaling, pay-per-execution model.

#### Key benefits of serverless
1. Reduced operational costs
2. Automatic scaling
3. Faster time to market
4. Increased focus on business logic

#### Potential drawbacks and considerations
1. Cold starts
2. Vendor lock-in
3. Limited execution duration
4. Debugging complexity

### Practice

Get hands-on with AWS:

1. Set up your AWS account (if you haven't already)
   - Navigate to aws.amazon.com and click "Create an AWS Account"
   - Follow the prompts to create your account

2. Install and configure the AWS CLI
   - Download the AWS CLI from the official AWS website
   - Run `aws configure` in your terminal and input your AWS credentials

3. Navigate the AWS Management Console
   - Familiarize yourself with the dashboard
   - Locate key services like Lambda, API Gateway, and CloudFormation

4. Understand key AWS concepts:
   - Regions: Geographical areas where AWS has data centers
   - Availability Zones: Isolated locations within regions for high availability
   - AWS Free Tier: Services and usage limits available at no cost for new accounts

### Mini Project

Deploy a "Hello World" Lambda function with a twist:

1. Create a Lambda function that retrieves data from an external API
   - Use Python or Node.js as the runtime
   - Implement error handling and logging

2. Use a random quote API to fetch and display quote
   - Get API free
   - Fetch data random quote

3. Trigger the function and observe the dynamic results
   - Use the AWS CLI to invoke the function
   - Review CloudWatch logs for function execution details

### Additional Resources

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- [AWS Free Tier](https://aws.amazon.com/free/)
- [OpenWeatherMap API](https://openweathermap.org/api) (suggested for the mini project)
- [Serverless Architecture Explained](https://martinfowler.com/articles/serverless.html) by Martin Fowler
- [AWS Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)

### Next Steps

- Complete the tasks outlined above
- Document your learnings and any challenges faced
- Prepare questions for areas you'd like to explore further
- Get ready for Day 2 of the challenge!

Happy learning, and enjoy your journey into the world of serverless computing!