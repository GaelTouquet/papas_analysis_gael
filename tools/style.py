from cpyroot.tools.style import Style as sty

class Style(sty):

    def __init__(self, label,
                 markerStyle = 8,
                 markerColor = 1,
                 markerSize = 1,
                 lineStyle = 1,
                 lineColor = 1,
                 lineWidth = 2,
                 fillColor = None,
                 fillStyle = 1001 ):
        self.label = label
        super(Style, self).__init__(markerStyle,
                                    markerColor,
                                    markerSize,
                                    lineStyle,
                                    lineColor,
                                    lineWidth,
                                    fillColor,
                                    fillStyle)


papas_style = Style('papas',
                    markerStyle = 2,
                    markerColor = 2,
                    markerSize = 1,
                    lineStyle = 1,
                    lineColor = 2,
                    lineWidth = 2,
                    fillColor = 0,
                    fillStyle = 0 )
                    

cms_style = Style('cms',
                  markerStyle = 3,
                  markerColor = 4,
                  markerSize = 1,
                  lineStyle = 1,
                  lineColor = 4,
                  lineWidth = 2,
                  fillColor = 0,
                  fillStyle = 0 )

cms_style2 = Style('cms2',
                  markerStyle = 3,
                  markerColor = 3,
                  markerSize = 1,
                  lineStyle = 1,
                  lineColor = 3,
                  lineWidth = 2,
                  fillColor = 0,
                  fillStyle = 0 )
