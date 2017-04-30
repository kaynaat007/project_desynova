import base64

from Crypto.Cipher import AES

from .constants import valid_aes_key_sizes


def encode(target_string, password=None):
    """
    :param target_string: The string to be encoded
    :param password: The password to encrypt the string
    :return: encodes a string using AES
    """
    function = encode.__name__
    try:
        if not target_string:
            raise Exception(function, 'The string to be encoded must be provided')
        if not password:
            return target_string
        # we will work with utf-8 encoding
        target_string = target_string.encode('utf-8')
        obj = AES.new(password.encode('utf-8'), AES.MODE_CFB, 'This is an IV456')
        return base64.b64encode(obj.encrypt(target_string))
    except Exception as e:
        raise Exception(function, e.args or e.message)


def decode(cipher_string, password=None):
    """
    :param cipher_string: The string to be decoded
    :param password: The password to unlock the string
    :return: returns the decoded string if password was correct
    """
    function = decode.__name__
    try:
        cipher_string = base64.b64decode(cipher_string)
        obj = AES.new(password.encode('utf-8'), AES.MODE_CFB, 'This is an IV456')
        return obj.decrypt(cipher_string).strip()
    except Exception as e:
        raise Exception(function, e.args or e.message)


def check_key_size_bytes(key):
    """
    returns False if key size is not in valid key sizes of AES
    :param key:
    :return:
    """
    function = check_key_size_bytes.__name__
    try:
        return len(key.encode('utf-8')) in valid_aes_key_sizes
    except Exception as e:
        raise Exception(function, e.args or e.message)


