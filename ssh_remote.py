import pxssh
import argparse

class Client:
	def __init__(self, host, user, password):
		self.host=host
		self.user=user
		self.password=password
	def connect(self):
		try:
			s=pxssh.pxssh()
			s.login(self.host, self.user, self.password)
			return s
		except:
			print ("unable to connect ...") 
	def send_cmd(self, cmd):
		try:
			con=self.connect()
	        	con.sendline(cmd)
			con.prompt()
			return con.before 
		except:
			print ("host not rechable to pass cmd") 

if __name__ == "__main__":

	parser=argparse.ArgumentParser(prog='ssh.py',description='Run cmds remotely')
	parser.add_argument('ip',help='hostip')
	parser.add_argument('user',help='user')
	parser.add_argument('password',help='pass')
	parser.add_argument('dir',help='dirname')
	parser.add_argument('--test',help='test params')
	args=parser.parse_args()
	node=Client(args.ip, args.user, args.password)
print node.send_cmd(args.dir)

