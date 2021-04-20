import base64
from io import BytesIO
import qrcode


def handler(event, context):
    data = 'https://www.youtube.com'
    img = qrcode.make(data)
    buff = BytesIO()
    img.save(buff, format='JPEG')
    img_b64encoded = base64.b64encode(buff.getvalue()).decode('utf-8')

    response = {
        'statusCode': 200,
        'headers': {
            'Content-Length': len(img_b64encoded),
            'Content-Type': 'image/jpg',
            'Content-Disposition': 'attachment;filename=qrcode.jpg'
        },
        'isBase64Encoded': True,
        'body': img_b64encoded
    }

    return response


if __name__ == "__main__":
    out = handler('', '')
    print(out)
