import boto3

# Quick way to view all buckets

# Create an s3 client
s3 = boto3.client('s3')

# Call s3 to list current buckets
response = s3.list_buckets()
# Response returns a dictionary
# print(response)

buckets = [bucket['Name'] for bucket in response['Buckets']]
print(buckets)