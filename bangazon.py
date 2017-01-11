class Department:
	"""Parent class for all department
	Method: __init__, get_name, get_supervisor, meet
	"""

	def __init__(self, name, supervisor, employee_count):
		self.name = name
		self.supervisor = supervisor
		self.size = employee_count
		self.budget = 500

	


	def get_name(self):
		"""Returns the name of the department"""
		return self.name

	def get_supervisor(self):
		"""Returns the name of the supervisor"""
		return self.supervisor

	def get_budget(self):
		return self.budget

	def meet(self):
		print("Everyone meet in {}'s office ".format(self.supervisor))

	def __repr__(self):
		self.name




class Development(Department):
	"""softeware develpment department
	Methods: __init__, get_name, get_supervisor, meet
	"""
	def __init__(self, name, supervisor, employee_count):
		super().__init__(name, supervisor, employee_count)
		super().meet()

	def meet(self):
		""" this overrides the base meet() method completely"""
		print("Everyone meet in the server room")



class HumanResources(Department):
	"""Class for representing Human Resource department
	Methods: __init__, add_policy, get_policy, etc.
	"""
	def __init__(self, name, supervisor, employee_count):
		super().__init__(name, supervisor, employee_count)
		super().get_budget()
		self.policies = set()
		
		

	def add_policy(self, policy_name, policy_text):
		"""Adds a policy, as a tuple, to the set of policies

		Arguments:
			policy_name(string)
			policy_text(string)
		"""

		self.policies.add((policy_name, policy_text))
		""" this argument will go into the set as tuple , make sure to have extra ()"""


	def get_budget(self):

		self.budget = self.budget + 300
        
	def __repr__(self):
		self.name


class FrontOffice(Department):

	"""Class for represinting FrontOfiice department
	Methods: __init__, add_policy, get_policy, get_am_agent, get_pm_agent
	"""

	def __init__(self, name, supervisor, employee_count):
		super().__init__( name, supervisor, employee_count)
		super().get_budget()
		self.policies = set()
		self.am_agent  = set()
		self.pm_agent = set()


	def get_budget(self):
		self.budget = self.budget + 500

	def add_am_agent(self, agent_name):
		self.am_agent.add(agent_name)

	def add_pm_agent(self, agent_name):
		self.pm_agent.add(agent_name)


class EventServices(Department):

	def __init__(self, name, supervisor, employee_count):
		super().__init__(name, supervisor, employee_count)
		super().get_budget()
		self.admin_staff = set()
		self.event_sales_managers = set()

	def get_budget(self):
		self.budget = self.budget - 100


	def add_admin_staff(self, name, position, manager_name):
		self.admin_staff.add((name, position, manager_name))

	def add_event_sales_managers(self, name, years_employeed):
		self.event_sales_managers = set()


class CityGrill(Department):
	def __init__(self, name, supervisor,employee_count):
		super().__init__(name, supervisor, employee_count)
		super().get_budget()
		self.buser_staff = set()
		self.server_staff = set()

	def add_buser_staff(self, name, shift):
		self.buser_staff.add((name, pm))

	def get_budget(self):
		self.budget = self.budget +500


hr_department = HumanResources("HumanResources", "Millie Bisono", 5 )
print(hr_department.name)
print(hr_department.supervisor)
print(hr_department.size)
hr_department.get_budget()
print(hr_department.meet())


print(hr_department.budget)
# print(dir(hr_department))
hr_department.get_supervisor()
print(hr_department.get_supervisor())
hr_department.policies.add(("OASIS", "We abide by OASIS"))
print(hr_department.policies)




front_office = FrontOffice("Front Office", "Alex Sorogano", 45)
print(front_office.name)
front_office.add_am_agent("Halely Baley")
front_office.add_pm_agent("Kevin Baker")
print(front_office.am_agent)
print(front_office.pm_agent)
front_office.get_budget()
print(front_office.budget)


event_dept = EventServices("Event Services", "Joe Charlie", 12)
event_dept.add_admin_staff("Holly Polly", "Secretary", "Tom Hanks")
print(event_dept.admin_staff)
event_dept.get_budget()
print(event_dept.budget)

city_grill = CityGrill("City Grill", "Brett Williams", 80)
city_grill.buser_staff.add(("Bob Dylan", "pm"))
city_grill.get_budget()
print(city_grill.budget)
print(city_grill.buser_staff)

development = Development("Development", "Julia Kim_Chung", 8)
print(development.name)
development.meet()
print(development.meet())















