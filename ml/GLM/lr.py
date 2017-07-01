""" Linear regression for multiple features """
__author__="Aakash"
from ..numc import *
class LR():
	def fit(self,X,Y):
		if checkfit(X,Y):
			if not isinstance(X,np.ndarray):self.a=np.array(X)
			else:self.a=X
			inst=nx(self.a)
			self.feat=inst.add_col(col_no=0,val=1)
			self.target=Y
			self.theta=np.zeros(self.feat.shape[1])
			self.m=self.a.shape[0]
	def hyp(self,it=None):
		"""returns the hypothesis equation of a pirticular feature"""
		return self.theta.dot(self.feat[it])				
	def cost(self):
		"""computes the cost"""
		sum=0
		for i in range(self.m):
			res=(self.hyp(it=i)-self.target[i])**2
			sum+=res
		return (1/2*(self.m))*(sum)	
	#def gd(self,rate=0.001,loops=700):
	def gd(self,rate=0.01,loops=1000):
		"""gradient descent"""
		for k in range(loops):
			for i in range(len(self.theta)):
				ts=0
				for j in range(self.m):
					res=(self.hyp(it=j)-self.target[j])*self.feat[j][i]
					ts+=res
				self.theta[i]-=rate*(1/(self.m))*(ts)
				#self.theta[i]-=rate*(ts)
			t=self.cost()
		#return self.theta
	def predict(self,x):
		"""predicting the values"""
		self.gd()
		#return x.dot(self.theta[1:])
		return x.dot(self.theta[1:])+self.theta[0]
	@property
	def intercept_coef(self):
		return "intercept:{} coef:{}".format(self.theta[0],self.theta[1:])
		
def checkfit(X,Y):
	if len(X)!=len(Y):
		raise ValueError("The length of the features vector and target vector does not match")
	elif len(X.shape)!=2:
			raise ValueError("all the values in the feature vector do not have same dimensions")
	else:return True
def normalize(X):
	"""	This function normalizes the feature values:
		new_x=(x-min(x))/(max(x)-min(x))"""
	mi=np.min(X,axis=0)
	ma=np.max(X,axis=0)
	r=np.full(X.shape,np.inf)
	for i in range(len(X)):
		q=(X[i]-mi)/(ma-mi)
		r[i]=q
	return r
def check_labels(y):
	"""creates one-hot vector for the target variables
	for example,if a training set consists of multiple classes y=(0,1,2...n)
	one-hot vector for y(0)=[1,0,0,..n],y(2)=[0,0,1,0,..n]"""
	no_=y.shape[0]
	class_set=set(y)
	temp=np.full([no_,len(class_set)],0.0)
	for i in range(len(y)):
		temp[i][y[i]]=1
	return temp
				
			
		
		
