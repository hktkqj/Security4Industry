import rsa


pubkey, pirvkey = rsa.newkeys(1024)
anopubkey, anoprivkey = rsa.newkeys(1024)

signature = rsa.sign("Hello world".encode('utf8'),priv_key=pirvkey,hash_method='SHA-256')
print(signature)
signature1 = rsa.sign("Hello world".encode('utf8'),priv_key=anoprivkey,hash_method='SHA-256')

rsa.verify("Hello world".encode('utf8'),signature=signature1,pub_key=pubkey)
