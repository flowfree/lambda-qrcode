lambda-qrcode
=============
AWS Lambda function for generating QR code images.

Build the Docker container
--------------------------

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

