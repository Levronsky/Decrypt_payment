from base64 import b64decode


base64_encoded = 'c2hvcElkOjEyMzQuc2NpZDo0MzIxLmN1c3RvbWVyTnVtYmVyOmFiYzAwMC5zaG9wQXJ0aWNsZUlkOjU2Nzg5MC5wYXltZW50VHlwZTpBQy5vcmRlck51bWJlcjphYmMxMTExMTExLmN1c3ROYW1lOkpvaG4gRG9lLmN1c3RBZGRyOtCc0L7RgdC60LLQsCwg0LAv0Y8gMTAwLm9yZGVyRGV0YWlsczrQodGH0LDRgdGC0YzQtSDQtNC70Y8g0LLRgdC10YUsINCyINC/0LDQutC10YLQuNC60LDRhSwg0YDQvtGB0YHRi9C/0YzRjg=='


def main():
    decrypted_payment = decrypt_payment(base64_encoded)
    print(decrypted_payment)


def decrypt_payment(base64_encoded):
    """Decrypt payment information."""
    base64_decoded = b64decode(base64_encoded)
    payment_decoded = base64_decoded.decode('utf-8')
    payment_chunks = payment_decoded.split('.')
    payment_chunks_list = [
        chunk.split(':') for chunk in payment_chunks
        ]
    decrypted_payment = dict(payment_chunks_list)
    for key, value in decrypted_payment.items():
        if value.isnumeric():
            decrypted_payment[key] = int(value)
    return decrypted_payment


if __name__ == '__main__':
    main()
