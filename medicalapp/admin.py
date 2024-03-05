from django.contrib import admin

# Register your models here.
from .models import Company,Medicine,Employeesalary,Billdetails,Customerrequest,Companyaccount,Companybank,Employeebank,Bill,Customer,Employee,Medicaldetails


admin.site.register(Company)
admin.site.register(Medicine)
admin.site.register(Medicaldetails)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(Employeesalary)
admin.site.register(Billdetails)
admin.site.register(Customerrequest)
admin.site.register(Companyaccount)
admin.site.register(Companybank)
admin.site.register(Employeebank)





