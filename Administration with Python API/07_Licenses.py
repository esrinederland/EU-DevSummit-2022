import arcgis
from Settings import PortalUrl,ProfileName

gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username))

newUser = gis.users.get("BerlinBear")

print("Update license type:")
newUser.update_license_type("Creator")

newRoleName = "DevSummit DemoRole"
print("Searching for role id")
for role in gis.users.roles.all():
    if role.name==newRoleName:
        roleId = role.role_id
        print("Updating role")
        newUser.update_role(roleId)
        break

print("Getting arcgis pro license manager")
pro_license = gis.admin.license.get('ArcGIS Pro')

print(pro_license.all())

print("Assigning a pro license to a user")
pro_license.assign(username='BerlinBear', entitlements='desktopBasicN')

print("Script complete")