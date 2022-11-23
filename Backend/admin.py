from django.contrib import admin

from .models import ModelsMachine, ModelsEngine, ModelsTransmission, ModelsDriveAxle, ModelsSteeringBridge, \
    ServiceCompany, Machine, TypeMaintenance, Maintenance, RecoveryMethod, FailureNode, Claims

admin.site.register(ModelsMachine)
admin.site.register(ModelsEngine)
admin.site.register(ModelsTransmission)
admin.site.register(ModelsDriveAxle)
admin.site.register(ModelsSteeringBridge)
admin.site.register(ServiceCompany)
admin.site.register(Machine)
admin.site.register(TypeMaintenance)
admin.site.register(Maintenance)
admin.site.register(RecoveryMethod)
admin.site.register(FailureNode)
admin.site.register(Claims)
