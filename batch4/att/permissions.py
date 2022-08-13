from rest_framework import permissions 

class MohitPermission(permissions.BasePermission):
	'''
	Global permission check for blocked IP
	''' 
	block_ip_list = ['192.168.132.1']
	def has_permission(self,request,view):
		ip_addr = request.META['REMOTE_ADDR']
		if ip_addr in self.block_ip_list:
			return False 
		else :
			return True

