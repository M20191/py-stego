#Import modules
import argparse
from stegano import lsb
from base64 import b64encode

def cli() -> dict[str]:
	parser = argparse.ArgumentParser(prog='Py-Stego', description='Steganography text in images')
	parser.add_argument('-t','--text', help='Text to encode', required=False)
	parser.add_argument('-e','--encode', help='Image to encode data',required=False)
	parser.add_argument('-d','--decode', help='Image to decode data', required=False)
	
	return parser.parse_args()

def main():
	args = cli()
	
	if args.encode and args.encode.split(".")[-1] != "png":
		print("[+] Only PNG images")

	elif args.encode and args.text:
		encode = lsb.hide(args.encode,b64encode(args.text.encode('ascii')))
		encode.save(f"encode/{args.encode}_encoded.png")
		print(f"[+] File: {args.encode}, data has been encrypted")

	elif args.decode:
		print(lsb.reveal(args.decode))

if __name__ == '__main__':
	main()
