

###
import util.configurations as config

config = config.parser()
plotly_username=config['PLOTLY']['plotly_username']
plotly_apikey=config['PLOTLY']['plotly_apikey']
###

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASIC_HEATMAP_PATH = BASE_DIR+'/templates/heatmap.html'

try:
    import plotly
    import plotly.plotly as py
    import plotly.tools as tls
    import plotly.graph_objs as go
    from plotly import __version__
    from plotly.offline import plot
    import plotly.graph_objs as go
    print(__version__)
    plotly.tools.set_credentials_file(username=plotly_username, api_key=plotly_apikey)
except:
    print('Not installed plotly')

def genPlotlyHeatmap(matrix, x_label_list, y_label_list, path = None):
    import numpy as np
    if type(matrix) == type(np.ndarray):
        raise TypeError("matrix must be numpy ndarray")
    print(matrix.shape)
    if matrix.shape[0] != len(x_label_list) or matrix.shape[1] != len(x_label_list):
        raise ValueError("Wrong x_label_list or y_lable_list")
    fig = go.Heatmap(z=matrix, x=x_label_list, y=y_label_list)
    data=[fig]
    if path == None:
        _filename = BASIC_HEATMAP_PATH
    else:
        _filename = path
    plot(data, filename=_filename, auto_open=False)

if __name__ == "__main__":
    import numpy as np
    import TypoDataAnalyzer.CONST as const
    heatmapMat = np.load('../TypoDataAnalyzer/model/typoCondiProb_test.npy')
    #heatmapMat = np.load('../TypoDataAnalyzer/model/tmpResult.npy')
    genPlotlyHeatmap(heatmapMat, const.char_list, const.char_list)