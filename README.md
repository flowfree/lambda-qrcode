lambda-qrcode
=============
AWS Lambda function for generating QR code images.

Build the Docker container
--------------------------

  docker build -t lambda-qrcode .

  docker run -p 9000:8080 lambda-qrcode

  curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"data":"https://www.google.com"}'
