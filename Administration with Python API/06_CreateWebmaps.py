import arcgis
from Settings import PortalUrl,ProfileName

gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username))

#get featurelayer
layer = gis.content.get("cb563bfcd2ef4a009126872495f2b2d3").layers[0]

#get unique values
uniqueValues = layer.get_unique_values("gen_2") #gen_2 == "BUNDESLAND"

print(f"Found: {len(uniqueValues)} unique values")
for unique in uniqueValues:
    print(f"Creating webmap for {unique}")

    sql_expression = f"gen_2 = '{unique}'"

    wm = arcgis.mapping.WebMap()  # new web map

    wm.basemap = "dark-gray-vector"

    wm.add_layer(layer)  # add some layers

    wm.layers[0].layerDefinition.definitionExpression = sql_expression

    extent = layer.query(where=sql_expression,return_extent_only = True, out_sr=4326)

    # SAVE THE WEBMAP
    webmap_item_properties = {'title':f'DevSummits Created Webmap for {unique}',
                'snippet':'Map created using Python API',
                'tags':['automation', 'python', "DevSummit2022"],
                'extent': extent['extent']}

    print("Saving the webmap")
    new_wm_item = wm.save(webmap_item_properties, thumbnail=r'D:\Data\WebMap_Icon.jpg')
    print(f"Created item with id: {new_wm_item.id}")

print("Script complete")