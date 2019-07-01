class k8sApi:
	def __init__(self, ipAddr, Port=8080):
	    self.ipAddr = ipAddr
	    self.Port = Port
	    self.headers = {'Content-Type': 'application/json'}
	def listNamespaces(self, name=None):
	    if name:
		url = 'http://%s:%s/api/v1/namespaces/%s'%(self.ipAddr, self.Port, name)
	    else:
		url = 'http://%s:%s/api/v1/namespaces' %(self.ipAddr, self.Port)
	    print(url)
	    try:
		resp = requests.get(url)
	    except:
	        raise RequestError("Call k8s API %s Error!!" % url)
	    else:
		return resp.status_code, resp.json()

if __name__ == '__main__':
	x = k8sApi('192.168.1.125')
	print(x.listNamespaces())

