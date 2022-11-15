import arcgis
from Settings import PortalUrl,ProfileName
import datetime

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName,verify_cert=False)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

#Get GIS Server
print("Getting admin")
admin = gis.admin

print("Getting serverManager")
serverManager = admin.servers

print("getting hosting server")
gis_server = serverManager.get("HOSTING_SERVER")[0]

print("Getting report manager")
reportManager = gis_server.usage

reportname = "WorldCitiesLastWeek"


availableReports = gis_server.usage.list()
foundReports = [r for r in availableReports if r.properties.reportname == reportname]
if len(foundReports)>0:
    lastWeekReport = foundReports[0]
else:
    print("Report not found, creating it")
    queries =[{"resourceURIs": ["services/SampleWorldCities.MapServer"],
                "metrics": ["RequestCount"]}]
    since="LAST_WEEK"        
    
    lastWeekReport = reportManager.create(reportname, queries, since = since)


results = lastWeekReport.query()

resultDict = {}
counter =0
for timeSlice in results["report"]["time-slices"]:
    dt = datetime.datetime.fromtimestamp(timeSlice/1000)
    dtString = dt.strftime("%Y%m%d")
    
    if not dtString in resultDict:
        resultDict[dtString] = 0
    dataValue = results["report"]["report-data"][0][0]["data"][counter]
    resultDict[dtString] += dataValue

    counter +=1

print(f"Usage in the last {len(resultDict)} days")
for key in resultDict:
    print(f"{key} - {resultDict[key]}")




print("Script complete")