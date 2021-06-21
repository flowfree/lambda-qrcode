lambda-qrcode
=============
AWS Lambda function for generating QR code images.

Build the Docker container on the local machine
-----------------------------------------------

1.  Download the code:

        git clone git@github.com:flowfree/lambda-qrcode.git

2.  Build the Docker container:

        cd lambda-qrcode
        docker build -t lambda-qrcode .

3.  Run the container and map the port:

        docker run -p 9000:8080 lambda-qrcode

4.  Make POST request to test the code:

        curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"data":"https://www.google.com"}'

    It will return JSON response like this:

        {
            'statusCode': 200,
            'headers': {
                'Content-Length': <length of the body>,
                'Content-Type': 'image/jpg',
                'Content-Disposition': 'attachment;filename=qrcode.jpg'
            },
            'isBase64Encoded': True,
            'body': <base64 encoded image data>
        }

Upload the Image to AWS ECR
---------------------------

        aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account number>.dkr.ecr.<region>.amazonaws.com

        aws ecr create-repository --repository-name lambda-qrcode --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE

        docker tag lambda-qrcode:latest <account number>.dkr.ecr.<region>.amazonaws.com/lambda-qrcode:latest

        docker push <account number>.dkr.ecr.<region>.amazonaws.com/lambda-qrcode:latest

