cocuruto = QgsProject.instance().mapLayersByName('Cocuruto')[0]
peaks = QgsProject.instance().mapLayersByName('peak_points')[0]

polylines = [polyline.geometry().asPolyline() for polyline in cocuruto.getFeatures()]
print(polylines)
contains = {}

for index, contour in enumerate(polylines):
    closed_contour = QgsGeometry.fromPolygonXY([contour])
    print(closed_contour)
#    for spot in peaks.getFeatures():
#        point_geom = spot.geometry()
#        print(point_geom)
#        
#        if closed_contour.contains(point_geom):
#            print('contains')
#            break
#            contains[index] = point_geom
            
#print(contains)