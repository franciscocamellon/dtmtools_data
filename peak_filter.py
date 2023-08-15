filtered_layer = QgsProject.instance().mapLayersByName('Filtered contour')[0]
peak_layer = QgsVectorLayer("LineString?crs=EPSG:4326", "Cocuruto", "memory")
provider = peak_layer.dataProvider()

polylines = [polyline.geometry().asMultiPolyline()[0] for polyline in filtered_layer.getFeatures()]
first_vertex = [polyline.geometry().asMultiPolyline()[0][0] for polyline in filtered_layer.getFeatures()]
first_vertex_set = set(first_vertex)
#print('first_vertex_set: ',first_vertex_set)

my_lines = []

for index, polyline in enumerate(polylines):
    closed_contour = QgsGeometry.fromPolygonXY([polyline])
    is_valid = True
    
    for vertex in first_vertex_set:
        if closed_contour.contains(vertex) and vertex != polyline[0]:
            is_valid = False
            break
            
    if is_valid:
        feat = QgsFeature()
        feat.setGeometry(QgsGeometry.fromPolylineXY(polyline))
        my_lines.append(feat)

provider.addFeatures(my_lines)
##
### Add the layer to the map canvas
QgsProject.instance().addMapLayer(peak_layer) 