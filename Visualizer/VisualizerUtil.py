from Visualizer.importPlotly import *


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

def genPlotly1DBarChart(labels, data, layout=None, path = None, width_size = 1):

    _width = [width_size for i in range(len(labels))]
    if len(labels) != len(data):
        raise ValueError("length of labels and length of data must be same")
    trace = go.Bar(x=labels, y=data, width=_width)
    data = [trace]
    if path == None:
        _filename = BASIC_BARCHART_PATH
    else:
        _filename = TEMPLATE_DIR+path
    if layout is not None:
        _layout = go.Layout(layout)
    else:
        _layout = go.Layout()

    plot(go.Figure(data=data, layout=_layout), filename=_filename, auto_open=False)


def genPlotlyDotPlot(X, Predicts, contour = None, _layout=None, _filename='', _colors=None, _markers=None):

    if len(_filename) == 0:
        raise ValueError('_filename must be filled')
    traces = []
    if contour is not None:

        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        x1 = [i for i in range(int(x1_min),int(x1_max))]
        x2 = [i for i in range(int(x2_min), int(x2_max))]
        traceContour = go.Contour(z=contour, opacity=0.4, autocontour=False,colorscale='Jet',
                                  x0=x1_min, y0=x2_min,
                                  #dx=1/100, dy=1/100
                                  dx=(x1_max-x1_min)/float(len(contour[:,0])), dy=(x2_max-x2_min)/float(len(contour[:,1]))
                                  )
        traces.append(traceContour)
    for idx, cl in enumerate(np.unique(Predicts)):
        trace = go.Scatter(
            x = X[Predicts == cl, 0],
            y = X[Predicts == cl, 1],
            mode = 'markers'

        )

        trace['name'] = "%d transformed feature" % idx
        if _colors is not None:
            trace['marker']['color'] = _colors[idx]

        if _markers is not None:
            trace['marker']['symbol'] = _markers[idx]

        traces.append(trace)

    plot(go.Figure(data=traces, layout=_layout), filename=_filename, auto_open=False)


    pass

def genPlotlyMultiLineChart(labels, datas, _layout=None, _filename='', width_size = 1, colors = None, names= None):
    if len(_filename) == 0:
        raise ValueError('_filename must be filled')
    if colors is not None:
        if len(datas) != len(colors):
            raise ValueError("lenght of data and color must be same or colors input as None")
    traces = []
    for i, data in enumerate(datas):
        trace = go.Scatter(
            x = labels,
            y = data,
            mode = 'lines',
        )
        if colors is not None:
            trace['line']['color']=colors[i]
        if names is not None:
            trace['name'] = names[i]
        traces.append(trace)

    plot(go.Figure(data=traces, layout=_layout), filename=_filename, auto_open=False)

def gen_params_prec_recall_curve(params, precs_all, precs_selected,
                              recalls_all, recalls_selected, F1Scores_all, F1Score_selected, _filename=BASIC_PREC_RECALL_PATH):
    fig = tls.make_subplots(rows=2, cols=2, specs=[[{}, {}],
                                               [{}, None], ],
                        subplot_titles=('Precision',
                                        'Recalls',
                                        'F1-Score',))

    trace_precs_all = go.Scatter(
        x=params, y=precs_all,
        mode = 'lines+markers',
        marker=dict(color="red",),
        name="All"
    )

    trace_precs_selected = go.Scatter(
        x=params, y=precs_selected,
        mode='lines+markers',
        marker=dict(color="blue", ),
        name="Selected"
    )

    trace_rec_all = go.Scatter(
        x=params, y=recalls_all,
        mode='lines+markers',
        marker=dict(color="red", ),
        name="All"
    )

    trace_rec_selected = go.Scatter(
        x=params, y=recalls_selected,
        mode='lines+markers',
        marker=dict(color="blue", ),
        name="Selected"
    )

    trace_f1_all = go.Scatter(
        x=params, y=F1Scores_all,
        mode='lines+markers',
        marker=dict(color="red", ),
        name="All"
    )

    trace_f1_selected = go.Scatter(
        x=params, y=F1Score_selected,
        mode='lines+markers',
        marker=dict(color="blue", ),
        name="Selected"
    )

    fig.append_trace(trace_precs_all, 1, 1)
    fig.append_trace(trace_precs_selected, 1, 1)
    fig.append_trace(trace_rec_all, 1, 2)
    fig.append_trace(trace_rec_selected, 1, 2)
    fig.append_trace(trace_f1_all, 2, 1)
    fig.append_trace(trace_f1_selected, 2, 1)

    fig['layout']['xaxis1'].update(title='threshold')
    fig['layout']['xaxis1'].update(title='threshold')
    fig['layout']['xaxis1'].update(title='threshold')

    plot(fig, filename=_filename, auto_open=False)

if __name__ == "__main__":
    import numpy as np
    import TypoDataAnalyzer.CONST as const
    heatmapMat = np.load('../TypoDataAnalyzer/model/typoCondiProb_test.npy')
    #heatmapMat = np.load('../TypoDataAnalyzer/model/tmpResult.npy')
    genPlotlyHeatmap(heatmapMat, const.char_list, const.char_list)