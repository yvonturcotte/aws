# Hautement inspiré de cet article : http://www.cloudberrylab.com/blog/how-to-save-up-to-50-on-your-non-production-ec2-instances-using-lambda-and-resource-tagging/

from __future__ import print_function

import boto3

def lambda_handler(event, context):

    ec2 = boto3.client("ec2", region_name="us-east-1")
    description = ec2.describe_instances()

    for instances in description["Reservations"]:
        for instance in instances["Instances"]:
            for tag in instance["Tags"]:
                if (tag["Key"] + tag["Value"]) == "autoshutdowntrue":
                    if instance["State"]["Name"] == "running":

                        print("Stopping : " + instance["InstanceId"])
                        ec2 = boto3.resource("ec2", region_name = "us-east-1")
                        instance = ec2.Instance(instance["InstanceId"])
                        instance.stop()

